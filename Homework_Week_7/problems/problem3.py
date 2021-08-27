# Creating 2 filepaths.
file_path5 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file5.txt"
file_path6 = "C:\\Users\\avyan\\python\\nsf_2021\\Homework_Week_7\\problems\\file6.txt"

# Opening the files.
opening_file5 = open(file_path5, "r")
opening_file6 = open(file_path6, "w")

# Taking the contents of file5 and putting then into file6.
for line in opening_file5:
    if len(line) <= 50:
        opening_file6.write(line)
    else:
        ## split the line and write
        index = 0
        line = line.strip()
        while index < len(line):
            result = line[index : index + 50]
            opening_file6.write(result + "\n")
            index = index + 50
              
opening_file6.flush()
opening_file6.close()