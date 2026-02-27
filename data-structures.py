#Lists
students=["Namratha","Manjunath","Kavya","Sneha","Kali"]
numbers=[1,2,3,4,4,5]
mixed=[1,"Namratha",34.5,True]
# print(students)
# students[1]="Arun"
# students.remove("Sneha")
# print(students)
# print(students[1:4])
# print(students[-1])
# print(students[::2])
# students.pop()
# print(students)
#Length
# print("Length of students array is Length of students array is",len(students))
# #sum,min,max
# print("Sum of all numbers in Numbers list is",sum(numbers))
# print("Min number in the number list is",min(numbers))
# print("Max number in the number list is",max(numbers))

# #count
# print("Total number of occurence of number 4 is",numbers.count(4))
# print("index of manjunath",students.index("Manjunath"))
# print("summ of numbers list is:",sum(numbers))
# #sort
# print(numbers.sort)
# students.sort()
# print(students)
# numbers.reverse()
# print(numbers)
# print("Savithri" in students)
# for name in students:
#     print(name)
# print(range(len(students)))
# for i in range(len(students)):
#     print(f"{i}:{students[i]}")
# print(enumerate(students))
# for k,v in enumerate(students):
#     print(f"{k}:{v}")


#List automation
squares=[]

for i in range(1,6):
    squares.append(i**2)
print(squares)


squares = [i**2 for i in range(1,6)]
print(squares)

#Tuples
#Dictionaries
#Sets