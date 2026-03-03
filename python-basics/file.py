# file=open("test.txt","r")
# content=file.read()
# print(content)
# file.close()
# with open("test.txt","r") as file:
#     lines=file.readline()
#     for line in lines:
#         print(line.strip())

# with open("output.txt","w")as file:
#     file.write("Hello world\n")
#     file.write("This is a new file\n")
# with open("output.txt","a")as file:
#     file.write("Hello world\n")
#     file.write("This is a new file\n")


try:
    with open("students_new.csv","r") as file:
        content=file.read():
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("You don't have permission to access this file")
except SyntaxError:
    print("There is a  error in your syntax")
except Exception as e:
    print(f"An Error Occured:{e}")
