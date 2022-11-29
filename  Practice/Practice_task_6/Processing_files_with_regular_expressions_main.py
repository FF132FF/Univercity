import Reading_writing_train_log

requested_file: str = str(input("Enter the name of the file to read and return data: "))
save_file: str = str(input("Enter the name of the file you want to write the data: "))
print(Reading_writing_train_log.formatting_and_save_log(requested_file, save_file))

# train_log.txt changed_train_log.txt названия файлов для проверки работы
