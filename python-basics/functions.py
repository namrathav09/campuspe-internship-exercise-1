# def iamgroot():
#     print("I am Groot")
# for i in range(0,10):
#     iamgroot()

#functions with argments/parameters and return types
#functions with no arguments and only return types
#function with arguments/parameters and no return types
#functions with no argument and no types

# def greet_someone(name):
#     print(f"Hello ,{name}!")
#     print("Welcome to my python script!")
# name=input("Please enter your name to continue:")
# greet_someone(name)

# def sum(a,b):
#     result=a+b
#     print(f"Sum of {a} + {b} = ",result)
# a=int(input("Please enter the value A :"))
# b=int(input("Please enter the value B :"))
# sum(a,b)

# def sum(*args):
#     result=0
#     for i in args:
#         result=result+i
#     return result
# a=int(input("Please enter the value A :"))
# b=int(input("Please enter the value B :"))
# c=int(input("Please enter the value C :"))
# print("Sum is  ",sum(a,b,c))


def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
display_info(name="Namratha",age=22,sex="Female",married="false")