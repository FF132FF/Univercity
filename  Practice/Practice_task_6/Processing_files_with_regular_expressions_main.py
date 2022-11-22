import Reading_writing_train_log as rw

requested_file: str = str(input("Enter the name of the file to read and return data: "))
returned_file: str = rw.read_log(requested_file)
save_file: str = str(input("Enter the name of the file you want to write the data: "))
