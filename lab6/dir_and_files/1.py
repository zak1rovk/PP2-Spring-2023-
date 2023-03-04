import os
path = "/path/to/directory"

print("Directories:")
for dir in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir)):
        print(dir)

print("\nFiles:")
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        print(file)

print("\nAll directories and files:")
for root, dirs, files in os.walk(path):
    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))
