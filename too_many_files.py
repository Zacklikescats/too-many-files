import os
import subprocess

num_files = int(input("How many files do you want to create:\n> "))

content = input("What do you want in the files:\n> ")

for i in range(1, num_files + 1):
    filename = f"file{i}.txt"
    with open(filename, "w") as f:
        f.write(content)

print(f"{num_files} files created successfully!")
