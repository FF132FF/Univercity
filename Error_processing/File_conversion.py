def read_file(requested_file):
    content = open(requested_file, "r+")
    returned_file = content.read().splitlines()
    return returned_file

def file_conversion(requested_file):
    returned_file = read_file(requested_file)
    returned_file = list(map(int, returned_file))
    del returned_file[0]
    return returned_file
