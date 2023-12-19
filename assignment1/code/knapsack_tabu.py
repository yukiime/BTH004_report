import torch
from typing import Tuple
from TestDataGenerator import TestDataNeighbour

# function: to find the situation where items placed in which knapsack or not 
# matrix: current item's situation matrix in snapsacks
def find_placedKnapsacks(matrix):
    placedKnapsacks = [0] * matrix.size(1)
    for i in range(matrix.size(0)):
        for j in range(matrix.size(1)):
            if matrix[i][j] == 1:
                placedKnapsacks[j] = i + 1
    return placedKnapsacks

# function: use tabo search algorithm to find the overall maximum value and item placement 
# TABOLIST_LEN: The length of tabo list,store placedKnapsacks
# startSolution_matrix: current item's situation matrix in snapsacks
# KNAPSACK_NUMBER: number of knapsacks
# knapsacks_tensor: knapsacks capacity tensor
# ITEM_NUMBER: number of items
# items_matrix: items values and weights matrix
def taboSearch_knapsack(TABOLIST_LEN:list,startSolution_matrix:torch.Tensor,KNAPSACK_NUMBER:int,knapsacks_tensor:torch.Tensor,ITEM_NUMBER:int,items_matrix:torch.Tensor)->Tuple[int,torch.Tensor]:
    if KNAPSACK_NUMBER == knapsacks_tensor.size()[0] == startSolution_matrix.size()[0] and ITEM_NUMBER == items_matrix.size()[1] == startSolution_matrix.size()[1]  :
        Z_valueSum = torch.mm(startSolution_matrix, items_matrix.t())[:, 0].sum()
        placedKnapsacks = find_placedKnapsacks(startSolution_matrix)
        tabo_list = []
        noBiggerNeighbor_flag = False
        nextSolution_matrix = startSolution_matrix.clone() 
        nextSolution_placedKnapsacks = placedKnapsacks.copy()
        neighbour_valueSum_max = Z_valueSum.clone()

        # find solution which has maximum value sum
        while noBiggerNeighbor_flag == False:
            noBiggerNeighbor_flag = True
            nowSolution_matrix = nextSolution_matrix.clone()
            nowSolution_placedKnapsacks = nextSolution_placedKnapsacks.copy()
            nowSolution_valueSum = neighbour_valueSum_max.clone()
            if len(tabo_list) == TABOLIST_LEN:
                tabo_list.pop(0)
            tabo_list.append(nowSolution_placedKnapsacks)

            # calculate the value sum of neighbours
            if not torch.cuda.is_available():
                raise RuntimeError("cuda not available when calculate the value sum of neighbours")
            neighbour_valueSum_max = torch.tensor(0.0).to('cuda')
            for j in range(ITEM_NUMBER):
                for i in range(KNAPSACK_NUMBER):

                    # item j is not put into any knapsack
                    if nowSolution_placedKnapsacks[j] == 0:

                        # current weight of knapsack i 
                        weight_knapsackI = torch.matmul(nowSolution_matrix[i], items_matrix[1])
                        capacity_knapsackI = knapsacks_tensor[i]
                        value_itemJ = items_matrix[0][j]
                        weight_itemJ = items_matrix[1][j]

                        # put item j into knapsack i
                        if weight_knapsackI + weight_itemJ <= capacity_knapsackI:
                            neighbour_valueSum = nowSolution_valueSum + value_itemJ

                            # get the maximum value sum of neighbours
                            if neighbour_valueSum > neighbour_valueSum_max:
                                neighbour_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                neighbour_placedKnapsacks[j] = i+1 

                                #  check if it is in tabo list
                                if neighbour_placedKnapsacks not in tabo_list:
                                    nextSolution_matrix = nowSolution_matrix.clone()
                                    nextSolution_matrix[i][j] = 1.0
                                    nextSolution_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                    nextSolution_placedKnapsacks[j] = i+1                                
                                    neighbour_valueSum_max = neighbour_valueSum
                        else:
                            # move item jj from knapsack i into knapsack ii
                            for jj in range(ITEM_NUMBER):
                                if nowSolution_matrix[i][jj] == 1.0 and (weight_knapsackI + weight_itemJ - items_matrix[1][jj]) <= capacity_knapsackI:
                                    for ii in range(KNAPSACK_NUMBER):

                                        # current weight of knapsack ii 
                                        weight_knapsackII = torch.matmul(nowSolution_matrix[ii], items_matrix[1])
                                        capacity_knapsackII = knapsacks_tensor[ii]
                                        weight_itemJJ = items_matrix[1][jj]
                                        
                                        # put item jj into knapsack ii
                                        if weight_knapsackII + weight_itemJJ < capacity_knapsackII:
                                            neighbour_valueSum = nowSolution_valueSum + value_itemJ

                                            # get the maximum value sum of neighbours
                                            if neighbour_valueSum > neighbour_valueSum_max:
                                                neighbour_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                                neighbour_placedKnapsacks[j] = i+1
                                                neighbour_placedKnapsacks[jj] = ii+1    
                                                if neighbour_placedKnapsacks not in tabo_list:
                                                    nextSolution_matrix = nowSolution_matrix.clone()
                                                    nextSolution_matrix[i][j] = 1.0
                                                    nextSolution_matrix[i][jj] = 0.0
                                                    nextSolution_matrix[ii][jj] = 1.0
                                                    nextSolution_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                                    nextSolution_placedKnapsacks[j] = i+1
                                                    nextSolution_placedKnapsacks[jj] = ii+1                                                
                                                    neighbour_valueSum_max = neighbour_valueSum
                                        else:
                                            # move item jjj from knapsack ii out
                                            for jjj in range(ITEM_NUMBER):
                                                if nowSolution_matrix[ii][jjj] == 1.0 and (weight_knapsackII + weight_itemJJ - items_matrix[1][jjj]) <= capacity_knapsackII :
                                                    neighbour_valueSum = nowSolution_valueSum + value_itemJ - items_matrix[0][jjj]
                                                    
                                                    # get the maximum value sum of neighbours
                                                    if neighbour_valueSum > neighbour_valueSum_max:
                                                        neighbour_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                                        neighbour_placedKnapsacks[j] = i+1
                                                        neighbour_placedKnapsacks[jj] = ii+1    
                                                        if neighbour_placedKnapsacks not in tabo_list:
                                                            nextSolution_matrix = nowSolution_matrix.clone()
                                                            nextSolution_matrix[i][j] = 1.0
                                                            nextSolution_matrix[i][jj] = 0.0
                                                            nextSolution_matrix[ii][jj] = 1.0
                                                            nextSolution_matrix[ii][jjj] = 0.0
                                                            nextSolution_placedKnapsacks = nowSolution_placedKnapsacks.copy()
                                                            nextSolution_placedKnapsacks[j] = i+1
                                                            nextSolution_placedKnapsacks[jj] = ii+1
                                                            nextSolution_placedKnapsacks[jjj] = 0                                                        
                                                            neighbour_valueSum_max = neighbour_valueSum
            
            # next step
            if neighbour_valueSum_max > nowSolution_valueSum:
                noBiggerNeighbor_flag = False                                  

        # return neighbour_valueSum_max,nextSolution_matrix
        return nowSolution_valueSum,nowSolution_matrix

    else:
        print(f"KNAPSACK_NUMBER = {KNAPSACK_NUMBER},\nknapsacks_tensor = {knapsacks_tensor.size()[0]},\nstartSolution_matrix.size()[0] = {startSolution_matrix.size()[0]}")
        print(f"ITEM_NUMBER = {ITEM_NUMBER},\nitems_matrix.size()[1] = {items_matrix.size()[1]},\nstartSolution_matrix.size()[1] = {startSolution_matrix.size()[1]}")
        raise RuntimeError("knapsack or item quantity is wrong")

def main():
    # target
    Z_valueSum = 0

    # test
    print("------test data------")
    test_data_generator = TestDataNeighbour()
    startSolution_matrix,KNAPSACK_NUMBER,knapsacks_tensor,ITEM_NUMBER,items_matrix = test_data_generator.creat_testData1()
    for i in range(KNAPSACK_NUMBER):
        print(f"Knapsack {i+1}: capacity = {knapsacks_tensor[i]}")
    for i in range(ITEM_NUMBER):
        print(f"Item {i+1}: value = {items_matrix[0][i]}, weight = {items_matrix[1][i]}")
    print("------solution------")
    TABOLIST_LEN = ITEM_NUMBER*ITEM_NUMBER*KNAPSACK_NUMBER
    Z_valueSum,solution = taboSearch_knapsack(TABOLIST_LEN,startSolution_matrix,KNAPSACK_NUMBER,knapsacks_tensor,ITEM_NUMBER,items_matrix)
    # print(f"Solution:\n{solution}")
    solution_knapsacks = torch.mm(solution, items_matrix.t())
    for i in range(KNAPSACK_NUMBER):
        items_knapsackI = []
        for j in range(ITEM_NUMBER):
            if solution[i][j] != 0.0 :
                items_knapsackI.append(j+1)
        print(f"Knapsack {i+1}: value = {solution_knapsacks[i][0]}  Residual capacity = {knapsacks_tensor[i]-solution_knapsacks[i][1]}   Items = {items_knapsackI}")

    print(f"Z = {Z_valueSum.item()}")
if __name__ == "__main__":
    main()
