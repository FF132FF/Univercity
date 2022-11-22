def Get_Word():
    words = open('Dictionary.txt')
    Dictionary = words.read().split()
    Dictionary = [i.lower() for i in Dictionary]

    return Dictionary

def Fix_a_Rec(Current_Record):
    new_Record = open("Record.txt", mode ='r+')
    max_Record = int(new_Record.read())

    if Current_Record > max_Record:
        max_Record = Current_Record

    new_Record.seek(0)
    new_Record.write(str(max_Record))

    return("Current record: ", Current_Record, "Max record: ", max_Record)