student_list = []

def student_add(name):
    student_list.append(name)

def save_file(name):
    try:
        f = open("rollcall.txt", "a")
        f.write(name + "\n")
        f.close()
    except Exception:
        ("Could not save file")


def read_file():
    try:
        f = open("rollcall.txt", "r")
        for name in f.readlines():
            student_add(name)
        f.close()
    except Exception:
        print("Cloud not read file")


answer = input("Do you want to add to the list? (yes/no): ")

try:
    if answer == "yes":
        name = input("Please add a new student to the roll: ")
        #student_add(name) the below line adds the name to the file, instead of this line adding it to the dictionary.
        save_file(name)
        read_file()
        print(student_list)
    elif answer == "no":
        print("Thank you.")
        
except Exception:
    print("Broke! Sorry")

# Try Catch not printing on false input



