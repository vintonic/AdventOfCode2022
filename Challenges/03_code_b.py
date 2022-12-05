# https://adventofcode.com/2022/day/3

from os import path
file_path = path.abspath(__file__) # full path of your script
dir_path = path.dirname(file_path) # full path of the directory of your script

input_file_name = "03_input.txt"
#input_file_name = "03_input_easy.txt"

input_file_path = path.join(dir_path,input_file_name) # absolute file path

# Opening file
input_file = open(input_file_path, 'r')
row_count = 0

total_priorities_found = 0

first_bag = []
second_bag = []
third_bag = []

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    #print("Line{}: {}".format(row_count, line.strip()))

    bag = []
    for item in line[:len(line)-1]:
        value = ord(item)
        if(value >= 65 and value <= 90):
            #letters from A to Z (values 65 to 90 need to be 27 to 52)
            value = value - 38
        else:
            #letters from a to z (values 97 to 122 need to be 1 to 26)
            value = value - 96
        bag.append(value)

    #print(bag)

    bag.sort()
    
    if(len(first_bag) == 0):
        first_bag = bag
    elif(len(second_bag) == 0):
        second_bag = bag
    else:
        third_bag = bag  


        for index, item in enumerate(first_bag):
            while(len(second_bag)>0 and first_bag[index]>second_bag[0]):
                second_bag.pop(0)

            while(len(third_bag)>0 and first_bag[index]>third_bag[0]):
                third_bag.pop(0)
            
            while(len(third_bag)>0 and second_bag[0]>third_bag[0]):
                third_bag.pop(0)
            
            while(len(second_bag)>0 and third_bag[0]>second_bag[0]):
                second_bag.pop(0)

            if(first_bag[index] == second_bag[0] == third_bag[0]):
                total_priorities_found = total_priorities_found + first_bag[index]
                print("Found at {}: {}".format(index, first_bag[index]))
                break
        
        first_bag = []
        second_bag = []
        third_bag = []


print("total_priorities_found: {}".format(total_priorities_found))

print("Rows number: " + str(row_count))
