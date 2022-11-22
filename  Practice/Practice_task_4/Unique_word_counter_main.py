import Read_Save_Files

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = str(input("Enter the name of the file you want to write the data: "))

print(Read_Save_Files.read_file(requested_file))
Read_Save_Files.save_file(returned_file, requested_file)