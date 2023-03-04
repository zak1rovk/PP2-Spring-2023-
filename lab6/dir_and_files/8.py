import os
path = "/path/to/file.txt"
if os.access(path, os.W_OK):
    if os.path.exists(path):
        os.remove(path)
        print("File deleted.")
    else:
        print("Path does not exist.")
else:
    print("Path is not writable.")
