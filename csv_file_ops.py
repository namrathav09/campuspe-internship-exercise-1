# READ FILE
import csv
# with open ("Book2.csv") as file:
#     for line in file:
#         data = line.strip().split(",")

#         print("Dear",data[1],", Your UserID is",data[0])

#WRITE FILE

# with open ("student.csv","w") as file:
#     file.write("name,age,grade\n")
#     file.write("Nams,22,A\n")
#     file.write("Jerome,23,B\n")


# students=[
#     ["name","age","grade"],
#     ["Nams p",22,"A"],
#     ["sandhya p",22,"B"]
# ]
# with open ("new_student.csv","w",newline='')as file:
#     writer=csv.writer(file)
#     writer.writerows(students)

with open("new_student.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)





