from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items): 
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name :- ")
        p = Path(name)

        if p.exists():
            print("File already exists!")
        else:
            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        
    except Exception as err:
        print(f"An error occurred: {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read :- ")
        p = Path(name)
    
        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
            print("\n📖 File Content:\n", data)
            print("Read successfully")
        else:
            print("❌ The file does not exist")
    except Exception as err:
        print(f"An error occurred: {err}")
        
def updatefile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to update :- ")
        p = Path(name)   # ✅ fixed

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for appending some content in your file")
            
            res = int(input("Tell your response :- "))
            
            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
                print("✅ File renamed successfully")
            
            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write in this file :- ")
                    fs.write(data)
                print("✅ File overwritten successfully")
                    
            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append in this file :- ")
                    fs.write(" " + data)
                print("✅ Data appended successfully")
        else:
            print("❌ File does not exist")
    except Exception as err:
        print(f"An error occurred: {err}")
        
def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete :- ")
        p = Path(name)   # ✅ fixed
        
        if p.exists() and p.is_file():
            os.remove(p)
            print("🗑 File removed successfully")
        else:
            print("❌ No such file exists")
    except Exception as err:
        print(f"An error occurred: {err}")
        
        
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("Please tell your response:- "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("❌ Invalid choice")
