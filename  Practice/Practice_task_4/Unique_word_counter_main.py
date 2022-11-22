from Unique_word_counter import Read_Save_Files as rsf

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = str(input("Enter the name of the file you want to write the data: "))

print(rsf.read_file(requested_file))
rsf.save_file(returned_file, requested_file)