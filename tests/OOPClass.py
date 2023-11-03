'''
    constructor name should be __init__ in python
    self keyword is mandatory for calling variables name into method
    instance variable & class variable have whole different purpose
    "new" keyword is not required when you create object in Python
'''
class Calculator:
    num = 100

    # def __init__(self):
    #     print("Default constructor is called")

    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b

    def sum2numbers(self):
        # return self.first_num + self.second_num + self.num  # self co the dung tat ca
        return self.first_num + self.second_num + Calculator.num # class name chi dung cho class variable

    def get_date(self):
        self.num = Calculator.num + 1
        print("call get_data() method")


obj = Calculator(2, 3)
obj.get_date()
print(obj.num)
