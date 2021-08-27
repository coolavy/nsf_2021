import os
from posixpath import dirname

file_path = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\practice\\code_session_2\\words.txt"

opening_file = open(file_path, "r")

contents = []

for line in opening_file:
    line = line.strip()
    contents.append(line + "\n")

contents.sort()

dir_name = os.path.dirname(file_path)
sorted_file_path = os.path.join(dir_name, "sorted_words.txt")

writing_file = open(sorted_file_path, "w")

writing_file.writelines(contents)


writing_file.flush()
writing_file.close()