# problem 1
def create_file(file_path, file_index, number_of_lines):
    opening_file = open(file_path, "w")
    for x in range(0, number_of_lines):
        opening_file.write(f"File {file_index}: Line {x + 1}")
        opening_file.write("\n")
    opening_file.flush()
    opening_file.close()

file_path1 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file1.txt"
create_file(file_path1, 1, 7)

file_path2 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file2.txt"
create_file(file_path2, 2, 5)

file_path3 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file3.txt"

opening_file1 = open(file_path1, "r")
opening_file2 = open(file_path2, "r")
opening_file3 = open(file_path3, "w")


while True:
    
    # Reading from file1.
    line1 = opening_file1.readline()
    if line1:
        opening_file3.write(line1)
    # Reading from file2.
    line2 = opening_file2.readline()
    if line2:
        opening_file3.write(line2)
    # Breaking the loop when there is nothing to read.    
    if line1 == "" and line2 == "":
        break

opening_file1.close()
opening_file2.close()
opening_file3.close()