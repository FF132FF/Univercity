from Error_processing import File_conversion as fc

requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = fc.read_file(requested_file)
converted_file = fc.file_conversion(requested_file)
print(returned_file, "\n", converted_file)



