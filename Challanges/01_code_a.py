input_file_name = "01_input.txt"

# Opening file
input_file = open(input_file_name, 'r')
row_count = 0

max_sum = 0
curr_sum = 0

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    if(line.strip().isnumeric()):
        curr_sum = curr_sum + int(line)
    else:
        if(curr_sum > max_sum):
            max_sum = curr_sum
        curr_sum = 0
    '''
    print("Line{}: {}".format(row_count, line.strip()), end = '')
    print("  CurrSum: " + str(curr_sum), end = '')
    print("  MaxSum: " + str(max_sum), end = '')
    print("")
    '''
if(curr_sum > max_sum):
            max_sum = curr_sum
print("Rows number: " + str(row_count))
print("Max sum: " + str(max_sum))
