import Reading_writing_train_log
import re

requested_file: str = str(input("Enter the name of the file to read and return data: "))
returned_file: str = Reading_writing_train_log.read_log(requested_file)
save_file: str = str(input("Enter the name of the file you want to write the data: "))
timing: str = re.compile(r'в (\d+:\d+:\d+)')
print(type(timing))