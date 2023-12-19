import random

class TestDataGenerator:
    @staticmethod
    def createDataInt(n, filename):
        data = [random.randint(1, 100000) for _ in range(n)]
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
    @staticmethod
    def createDataFloat(n, filename):
        data = [random.uniform(1.0, 1000.0) for _ in range(n)]
        # data = [n * random.random() for _ in range(n)]
        with open(filename, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')

if __name__ == "__main__":
    # int
    TestDataGenerator.createDataInt(10**1, 'assignment2\TestData\dataInt_10^1.txt')
    # TestDataGenerator.createDataInt(10**2, 'assignment2\TestData\dataInt_10^2.txt')
    # TestDataGenerator.createDataInt(10**3, 'assignment2\TestData\dataInt_10^3.txt')
    # TestDataGenerator.createDataInt(10**4, 'assignment2\TestData\dataInt_10^4.txt')
    # TestDataGenerator.createDataInt(10**5, 'assignment2\TestData\dataInt_10^5.txt')
    # TestDataGenerator.createDataInt(10**6, 'assignment2\TestData\dataInt_10^6.txt')
    # TestDataGenerator.createDataInt(10**7, 'assignment2\TestData\dataInt_10^7.txt')
    # TestDataGenerator.createDataInt(10**8, 'assignment2\TestData\dataInt_10^8.txt')
    
    # float
    # TestDataGenerator.createDataFloat(10**1, 'assignment2\TestData\dataFloat_10^1.txt')
    # TestDataGenerator.createDataFloat(10**2, 'assignment2\TestData\dataFloat_10^2.txt')
    # TestDataGenerator.createDataFloat(10**3, 'assignment2\TestData\dataFloat_10^3.txt')
    # TestDataGenerator.createDataFloat(10**4, 'assignment2\TestData\dataFloat_10^4.txt')
    # TestDataGenerator.createDataFloat(10**5, 'assignment2\TestData\dataFloat_10^5.txt')
    # TestDataGenerator.createDataFloat(10**6, 'assignment2\TestData\dataFloat_10^6.txt')
    # TestDataGenerator.createDataFloat(10**7, 'assignment2\TestData\dataFloat_10^7.txt')
    # TestDataGenerator.createDataFloat(10**8, 'assignment2\TestData\dataFloat_10^8.txt')
