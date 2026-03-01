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
# squares=[]

# for i in range(1,6):
#     squares.append(i**2)
# print(squares)


# squares = [i**2 for i in range(1,6)]
# print(squares)

#Tuples
coordinates=(10,20)
person=("kavya",25,"Chitradurga")
#print(person[2])

name,age,district=person
print(f"I am {name},from {district}. I am {age} years old")
#Dictionaries
mathClass={}
student={
    "name":"Dennis",
    "age":22,
    "grade":"A",
    "Courses":["Math","Science","Social Sciece"]

    }
# print(student["name"])
# print(student.get("phone","User's Phone number doesn't exist"))
student["phone"] =9880898980
student["age"]=36
# print(student)  
# student.pop("grade")
# print(student)
# for key in student:
# print(f"{key}:{student[key]}")

# Sets
empty_set=set()
numbers=[1,2,3,3,3,3,3,4,4,4,4,5]
unique_numbers=set(numbers)
print(numbers)
print(unique_numbers)
unique_numbers.add(88888)
print(unique_numbers)
unique_numbers.remove(88888)
print(unique_numbers)
unique_numbers.remove(88)#gives error if number not exist
unique_numbers.discard(88)#doesnot give error een though the number not present

