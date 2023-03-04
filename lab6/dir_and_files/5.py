file_path = "/path/to/file.txt"
my_list = ["item1", "item2", "item3"]
with open(file_path, "w") as file:
    for item in my_list:
        file.write(item + "\n")
