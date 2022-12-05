input_file_name = "01_input.txt"
#input_file_name = "01_input_easy.txt"

# Opening file
input_file = open(input_file_name, 'r')
row_count = 0


max_capacities_list = [0, 0, 0]
lower_max_capacity = 0
total_sum_of_max_capacities = 0
curr_capacity = 0

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    if(line.strip().isnumeric()):
        curr_capacity = curr_capacity + int(line)
    else:
        if(curr_capacity > lower_max_capacity):

            count = 0
            for max_capacity_item in max_capacities_list:
                if(max_capacity_item == lower_max_capacity):
                    total_sum_of_max_capacities = total_sum_of_max_capacities - max_capacities_list[count] + curr_capacity
                    max_capacities_list[count] = curr_capacity
                    lower_max_capacity = curr_capacity
                    break
                count += 1

            for max_capacity_item in max_capacities_list:
                if(max_capacity_item < lower_max_capacity):
                    lower_max_capacity = max_capacity_item

        curr_capacity = 0


if(curr_capacity > lower_max_capacity):

            count = 0
            for max_capacity_item in max_capacities_list:
                if(max_capacity_item == lower_max_capacity):
                    total_sum_of_max_capacities = total_sum_of_max_capacities - max_capacities_list[count] + curr_capacity
                    max_capacities_list[count] = curr_capacity
                    lower_max_capacity = curr_capacity
                    break
                count += 1

            for max_capacity_item in max_capacities_list:
                if(max_capacity_item < lower_max_capacity):
                    lower_max_capacity = max_capacity_item


print("Rows number: " + str(row_count))
print("total_sum_of_max_capacities: " + str(total_sum_of_max_capacities))

for max_capacity_item in max_capacities_list:
    print(max_capacity_item)





