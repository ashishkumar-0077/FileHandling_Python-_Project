from pathlib import Path
import os
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i+1} : {items}')



def createfile():
    try:
        readfileandfolder()
        name = input('Please tell me your file name:-')
        p = Path(name)
        if not p.exists() :
            with open(p, "w") as fs:
                data = input("What you want to write this file:-")
                fs.write(data)
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("File already exists.")
    except Exception as err:
        print(f" An occured Error: {err}")


def readfile():
    try:
       readfileandfolder()
       name = input("Which file you want to read:-")
       p = Path(name)
       if p.exists() and p.is_file():
             with open(p, "r") as fs:
              data = fs.read()
             print("File Readed Successfully")
       else:
            print("File not found or inaccessible.")

    except Exception as err:
        print(f"An occured Error: {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update:-")
        p = Path(name)
        if p.exists() and p.is_file():


            print("Press 1 for changing the name of file")
            print("Press 2 for overwrting  the data of file")
            print("Press 3 for appending some content in file")


            res = int(input("Enter the response:-"))
            if res == 1:
                name2 = input("Enter the new name of file:-")
                p2 = Path(name2)
                p.rename(p2)
                print("File name changed successfully")


            if res == 2:
                with open(p, "w") as fs:
                    data = input("What you want to write this file:-")
                    fs.write(data)
                print("File overwritten successfully")

            if res == 3:
                with open(p, "a") as fs:
                    data = input("What you want to append in this file:-")
                    fs.write(" " + data)


            with open(p, "a") as fs:
                data = input("What you want to write this file:-")
                fs.write(data)
            print("File Updated Successfully")
        else:
            print("File not found or inaccessible.")
    except Exception as err:
        print(f"An occured Error: {err}")





def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete:-")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File deleted successfully.")
        else:
            print("File not found or inaccessible.")
    except Exception as err:
        print(f"An occured Error: {err}")





print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for delete a file")

check = int(input("Enter the response:-"))

if check ==1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()