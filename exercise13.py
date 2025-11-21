from functools import reduce

class NUmber:
    def __init__(self, numbers):
        self.numbers = numbers

    def get(self):
        return self.numbers
    
    def change_original_values(self, function=lambda x: x):
        new_numbers = list(map(function, self.numbers))
        return new_numbers
    
    def filter_values(self, filter_function=lambda x: x):
        filtered_numbers = list(filter(filter_function, self.numbers))
        return filtered_numbers
    
    def commound_the_numbers(self, reduce_function=lambda compound, d: compound + d):
        compounded_value = reduce(reduce_function, self.numbers)
        return compounded_value
    
    def sort(self):
        sorted_numbers = sorted(self.numbers)
        return sorted_numbers
    

if __name__ == "__main__":
    numbers=[2, 5, 1, 66, 22, 11, 10]
    num = NUmber(numbers)

    print("original numbers:", num.get())

    lambda_function1 = lambda x: x * 2
    print("new values:",  num.change_original_values(function=lambda_function1))
    lambda_function2 = lambda x: x % 2 == 0
    print("filtered values:", num.filter_values(filter_function=lambda_function2))
    lambda_function3 = lambda a, b: a + b
    print("commounded value:", num.commound_the_numbers(reduce_function=lambda_function3))
    print("sorted values:", num.sort())



