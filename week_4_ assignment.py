#opening a new file
file = open("nyanjui.txt", "r")
print(file.read())

#writing on a new file
newfile = open("sawa.txt", "w")
newfile.write("saw sawa")

file_name = input("Enter the file name:")

try:
    file = open("file_name",)
    print(file.read())
except FileNotFoundError:
    print("File does not exist in our database")
finally:
    print("thank you for your understanding")