file_path = "/path/to/file.txt"
with open(file_path, "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
    print("Number of lines in file:", num_lines)
