try:
    number=int(input("Enter a number: "))
    result=100/number
    print(result)
except ValueError:
    print("This is not a number , please enter a valid number!")
except  ZeroDivisionError:
    print("Zero can not divite any number, please enter a valid number")
except Exception as e:
    print(f"An error occured: {e}")
# def validate_age(age):
#     if age<0:
#         raise ValueError("Age cannot be negative")
#     if age > 200:
#         raise ValueError("Invalid Age")
#     return age
# try:
#     validate_age(-10)
# except ValueError as e:
#     print(e)