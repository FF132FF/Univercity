import reading_writing_train_log as rw


requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = rw.read_log(requested_file)
save_file = str(input("Enter the name of the file you want to write the data: "))

try:
    rw.save_log(save_file, requested_file)
except FileNotFoundError:
    print("такого файла не существует")
finally:
    print("===========")


