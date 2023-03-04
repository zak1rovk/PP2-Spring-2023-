source_file_path = "/path/to/source_file.txt"
destination_file_path = "/path/to/destination_file.txt"
with open(source_file_path, "r") as source_file:
    with open(destination_file_path, "w") as destination_file:
        for line in source_file:
            destination_file.write(line)
