input_file_name = "01_input.txt"

# Opening file
input_file = open(input_file_name, 'r')
row_count = 0

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    #print("Line{}: {}".format(row_count, line.strip()))
print("Rows number: " + str(row_count))
