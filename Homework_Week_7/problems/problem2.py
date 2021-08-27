import random

# problem 2
file_path1 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file1.txt"
file_path2 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file2.txt"


n = int(input("How many lines do you want?: "))


options = [file_path1, file_path2]

selected_filepath = random.choice(options)

opening_file = open(selected_filepath, "r")
file_contents = []
for line in opening_file:
    line = line.strip()
    file_contents.append(line)
opening_file.close()

trimmed_contents = file_contents[-n:]

for x in trimmed_contents:
    print(x)