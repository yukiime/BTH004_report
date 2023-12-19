import time
from mergeSort import merge_sort
from bubbleSort import bubble_sort

def testIntBubbleSort(fileName):
    # Measure initialization time
    start_time = time.process_time()
    
    # Read data from file
    with open(fileName, 'r') as file:
        data = [int(line.strip()) for line in file]
    # Measure sorting time
    sorting_start_time = time.process_time()
    bubble_sort(data)
    sorting_end_time = time.process_time()

    initialization_time = sorting_start_time - start_time
    sorting_time = sorting_end_time - sorting_start_time
    print(f"Initialization Time: {initialization_time} seconds")
    print(f"Sorting Time: {sorting_time} seconds")

def testIntMergeSort(fileName):
    # Measure initialization time
    start_time = time.process_time()
    
    # Read data from file
    with open(fileName, 'r') as file:
        data = [int(line.strip()) for line in file]
    # Measure sorting time
    sorting_start_time = time.process_time()
    merge_sort(data)
    sorting_end_time = time.process_time()

    initialization_time = sorting_start_time - start_time
    sorting_time = sorting_end_time - sorting_start_time
    print(f"Initialization Time: {initialization_time} seconds")
    print(f"Sorting Time: {sorting_time} seconds")

def testFloatBubbleSort(fileName):
    # Measure initialization time
    start_time = time.process_time()
    
    # Read data from file
    with open(fileName, 'r') as file:
        data = [float(line.strip()) for line in file]
    # Measure sorting time
    sorting_start_time = time.process_time()
    bubble_sort(data)
    sorting_end_time = time.process_time()

    initialization_time = sorting_start_time - start_time
    sorting_time = sorting_end_time - sorting_start_time
    print(f"Initialization Time: {initialization_time} seconds")
    print(f"Sorting Time: {sorting_time} seconds")

def testFloatMergeSort(fileName):
    # Measure initialization time
    start_time = time.process_time()
    
    # Read data from file
    with open(fileName, 'r') as file:
        data = [float(line.strip()) for line in file]
    # Measure sorting time
    sorting_start_time = time.process_time()
    merge_sort(data)
    sorting_end_time = time.process_time()

    initialization_time = sorting_start_time - start_time
    sorting_time = sorting_end_time - sorting_start_time
    print(f"Initialization Time: {initialization_time} seconds")
    print(f"Sorting Time: {sorting_time} seconds")

if __name__ == "__main__":
    # for power in range(1, 6):  # Compare up to 10^5
    #     file_name = f'assignment2/TestData/dataInt_10^{power}.txt'
    #     print(f"-------------Comparison for type of Int 10^{power}-------------")
    #     print("Bubble Sort:")
    #     testIntBubbleSort(file_name)
    #     print("Merge Sort:")
    #     testIntMergeSort(file_name)
    #     print()
    for power in range(1, 6):  # Compare up to 10^5
        file_name = f'assignment2/TestData/dataFloat_10^{power}.txt'
        print(f"-------------Comparison for type of Float 10^{power}-------------")
        print("Bubble Sort:")
        testFloatBubbleSort(file_name)
        print("Merge Sort:")
        testFloatMergeSort(file_name)
        print()

