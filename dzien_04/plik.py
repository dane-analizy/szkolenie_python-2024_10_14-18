def load_file(file_name, enc="utf-8"):
    file = [line.strip("\n") for line in open(file_name, "r", encoding=enc).readlines()]
    return file
