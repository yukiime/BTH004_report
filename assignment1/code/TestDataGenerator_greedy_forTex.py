import random

# class: create test data for greedy
class TestDataGreedy:
    # function: create test data 1
    @staticmethod
    def creat_testData1():
        # create knapsack
        KNAPSACK_NUMBER = 2
        knapsacks_capacity_list = [7,8]

        # create items
        ITEM_NUMBER = 6
        item_value_list = [1.5, 3.0, 4.0, 2.5, 5.0, 7.5]
        item_weight_list = [5, 4, 2, 3, 5, 5]
        
        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list

    # function: create test data 2
    @staticmethod
    def creat_testData2():
        # create knapsack
        KNAPSACK_NUMBER = 4
        knapsacks_capacity_list = [12, 11, 8, 7]

        # create items
        ITEM_NUMBER = 10
        item_value_list = [8, 30, 12, 5, 6, 11, 2, 2, 1, 12]
        item_weight_list = [4, 10, 7, 3, 4, 9, 8, 10, 9, 11]
        
        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list
    
    @staticmethod
    def creat_testData3():
        # create knapsack
        KNAPSACK_NUMBER = 4
        knapsacks_capacity_list = [10,2,1,6]

        # create items
        ITEM_NUMBER = 6
        item_value_list = [3,4,5,5,2,3]
        item_weight_list = [4,5,6,7,1,3]
        
        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list
    
    @staticmethod
    def creat_testData4():
        # create knapsack
        KNAPSACK_NUMBER = 5
        knapsacks_capacity_list = [2,6,8,17,7]

        # create items
        ITEM_NUMBER = 9
        item_value_list = [8,25,6,34,11,42,10,33,15]
        item_weight_list = [5,1,6,9,2,3,8,4,5]
        
        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list
    
    @staticmethod
    def creat_testData5():
        # create knapsack
        KNAPSACK_NUMBER = 5
        knapsacks_capacity_list = [10, 7, 8, 15,16]

        # create items
        ITEM_NUMBER = 18
        item_value_list = [5, 6, 8, 2, 4, 9, 7, 3, 1, 6, 5, 10, 3, 7, 4, 8, 6, 5]
        item_weight_list = [4, 5, 7, 2, 3, 8, 6, 2, 1, 5, 4, 9, 2, 6, 3, 7, 5, 4]
        
        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list
    
    # function: create test data with random values
    def creat_testDataRandom(KNAPSACK_NUMBER,ITEM_NUMBER,RANDOM_WEIGHT_BASE,RANDOM_VALUE_BASE):
        RANDOM_WEIGHT_BASE_HALF = RANDOM_WEIGHT_BASE//2
        RANDOM_WEIGHT_BASE_2TIMES = RANDOM_WEIGHT_BASE*2
        RANDOM_WEIGHT_BASE_3TIMES = RANDOM_WEIGHT_BASE*3
        RANDOM_VALUE_BASE_3TIMES = RANDOM_VALUE_BASE*3
        # create knapsacks
        knapsacks_capacity_list = []
        for i in range(1, KNAPSACK_NUMBER + 1):
            capacity = random.randint(RANDOM_WEIGHT_BASE, RANDOM_WEIGHT_BASE_3TIMES) 
            knapsacks_capacity_list.append(capacity)

        # create items
        item_value_list = []
        item_weight_list = []
        for i in range(1, ITEM_NUMBER + 1):
            value = random.randint(RANDOM_VALUE_BASE, RANDOM_VALUE_BASE_3TIMES) 
            weight = random.randint(RANDOM_WEIGHT_BASE_HALF, RANDOM_WEIGHT_BASE_2TIMES)  
            item_value_list.append(value)
            item_weight_list.append(weight)

        return KNAPSACK_NUMBER,knapsacks_capacity_list,ITEM_NUMBER,item_value_list,item_weight_list
