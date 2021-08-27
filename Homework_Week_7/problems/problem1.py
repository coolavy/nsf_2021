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
number_of_lines = 5

create_file(file_path2, 2, number_of_lines)

file_path3 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file3.txt"

opening_file = open(file_path1, "r")
reading_file1 = opening_file.read()
opening_file.close

opening_file = open(file_path2, "r")
reading_file2 = opening_file.read()
opening_file.close()

opening_file = open(file_path3, "w")
opening_file.write(reading_file1)
opening_file.write("-" * 20)
opening_file.write(reading_file2)
opening_file.flush()
opening_file.close()