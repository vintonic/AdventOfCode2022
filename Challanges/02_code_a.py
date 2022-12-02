input_file_name = "02_input.txt"
# input_file_name = "02_input_easy.txt"

# Opening file
input_file = open(input_file_name, 'r')
row_count = 0
points_count = 0

# Reading file
print("Starting reading the file " + input_file_name)
for line in input_file:
    row_count += 1
    #print("Line{} Len={}: {}".format(row_count, len(line), line.strip()))
    if(len(line)>2):
        opponent_move = line[0]
        my_move = line[2]
        if(my_move == 'X'):
            #X is rock
            points_count = points_count + 1
            if(opponent_move == 'A'):
                #A is rock
                points_count = points_count + 3
            elif(opponent_move == 'C'):
                #C is scissor
                points_count = points_count + 6
        if(my_move == 'Y'):
            #Y is paper
            points_count = points_count + 2
            if(opponent_move == 'B'):
                #B is paper
                points_count = points_count + 3
            elif(opponent_move == 'A'):
                #A is rock
                points_count = points_count + 6
        if(my_move == 'Z'):
            #Z is scissor
            points_count = points_count + 3
            if(opponent_move == 'C'):
                #C is scissor
                points_count = points_count + 3
            elif(opponent_move == 'B'):
                #B is paper
                points_count = points_count + 6
            
    
print("Rows number: " + str(row_count))

print("points_count: " + str(points_count))
