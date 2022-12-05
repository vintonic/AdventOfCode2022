# https://adventofcode.com/2022/day/3

from os import path
file_path = path.abspath(__file__) # full path of your script
dir_path = path.dirname(file_path) # full path of the directory of your script

input_file_name = "01_input.txt"
#input_file_name = "01_input_easy.txt"

input_file_path = path.join(dir_path,input_file_name) # absolute file path

# Opening file
input_file = open(input_file_path, 'r')
row_count = 0

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    #print("Line{}: {}".format(row_count, line.strip()))
print("Rows number: " + str(row_count))
