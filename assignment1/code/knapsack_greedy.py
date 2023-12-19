from TestDataGenerator import TestDataGreedy

# class: items to put in snapsack
# sequenceNo: serial number of the item
# value: value of item
# weight: weight of item
# benefit: value per weight unit of item
class Item:
    def __init__(self, sequenceNo, value, weight):
        self.sequenceNo = sequenceNo  
        self.value = value  
        self.weight = weight  
        self.benefit = value / weight if weight != 0 else 0  

    def __str__(self):
        return f"Item {self.sequenceNo}: Value = {self.value}  Weight = {self.weight}  Value per Weight = {self.benefit:.2f}"

# class: knapsack which get in items
# sequenceNo: serial number of the knapsack
# capacity: capacity of knapsack 
# residualCapacity: Residual capacity of knapsack 
# items: items to put in the knapsack
class Knapsack:
    def __init__(self, sequenceNo, capacity):
        self.sequenceNo = sequenceNo  
        self.capacity = capacity  
        self.residualCapacity = self.capacity
        self.items = []  

    def __str__(self):
        return f"Knapsack {self.sequenceNo}: Capacity = {self.capacity}  Residual capacity = {self.residualCapacity}  Items = {self.items}"

    # function: put the item putted in the knapsack
    def put_itemIn(self,item):
        self.residualCapacity = self.residualCapacity - item.weight
        self.items.append(item.sequenceNo)

# funciton: sort items_list based on Value per Weight
def sort_itemBenefit(items_list):
    items_list.sort(key=lambda x: x.benefit, reverse=True)
    return items_list

# funciton: sort knapsacks_list based on residualCapacity
def sort_knapsackResidualCapacity(knapsacks_list):
    knapsacks_list.sort(key=lambda knapsack: knapsack.residualCapacity)
    return knapsacks_list

# function: use a greedy algorithm to find the overall maximum value and item placement
# KNAPSACK_NUMBER: number of knapsacks
# knapsacks_list: knapsacks list
# ITEM_NUMBER: number of items
# items_list: items list
def greedy_knapsack(KNAPSACK_NUMBER,knapsacks_list,ITEM_NUMBER,items_list):
    Z_valueSum = 0

    if KNAPSACK_NUMBER != len(knapsacks_list) and ITEM_NUMBER != len(items_list):
        print("knapsack or item quantity is wrong")
        return None
    else:
        sort_itemBenefit(items_list)
        for item in items_list:
            sort_knapsackResidualCapacity(knapsacks_list)
            for knapsack in knapsacks_list:
                if item.weight <= knapsack.residualCapacity:
                    knapsack.put_itemIn(item)
                    Z_valueSum = Z_valueSum + item.value
                    break
        
        return Z_valueSum

# function: receive test data and instantiate it
def creat_testData():
    KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list = TestDataGreedy.creat_testData1()

    # create knapsacks
    knapsacks_list = []
    for i in range(KNAPSACK_NUMBER):
        knapsack = Knapsack(i + 1, knapsacks_capacity_list[i])
        knapsacks_list.append(knapsack)

    # create items
    items_list = []
    for i in range(ITEM_NUMBER):
        item = Item(i + 1, item_value_list[i], item_weight_list[i])
        items_list.append(item)

    return KNAPSACK_NUMBER, knapsacks_list, ITEM_NUMBER, items_list

def main():
    # target
    Z_valueSum = 0

    # test
    print("------test data------")
    KNAPSACK_NUMBER,knapsacks_list,ITEM_NUMBER,items_list = creat_testData()
    for knapsack in knapsacks_list:
        print(knapsack)
    for item in items_list:
        print(item)

    print("------result------")
    Z_valueSum = greedy_knapsack(KNAPSACK_NUMBER,knapsacks_list,ITEM_NUMBER,items_list)
    knapsacks_list.sort(key=lambda knapsack: knapsack.sequenceNo)
    for knapsack in knapsacks_list:
        print(knapsack)

    print(f"Z = {Z_valueSum}")

if __name__ == "__main__":
    main()
