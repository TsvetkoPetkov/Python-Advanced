def eat_cookie(presents_left, good_kids):  
    for x_and_y in directions.values():
        r = santa_position[0] + x_and_y[0]  
        c = santa_position[1] + x_and_y[1] 

        if matrix[r][c].isalpha():  
            if matrix[r][c] == 'V':  
                good_kids += 1 

            matrix[r][c] = '-' 
            presents_left -= 1 

        if not presents_left:  
            break  

    return presents_left, good_kids  


number_of_presents = int(input())  
size = int(input()) 

matrix = [] 
santa_position = []  

total_nice_kids = 0 
nice_kids_visited = 0

directions = { 
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size): 
    line = input().split() 

    matrix.append(line) 

    if 'S' in line: 
        santa_position = [row, line.index('S')]  
        matrix[row][santa_position[1]] = '-' 

    total_nice_kids += line.count('V')  

command = input()  

while command != "Christmas morning": 
    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1],
    ]  

    house = matrix[santa_position[0]][santa_position[1]]  

    if house == 'V': 
        nice_kids_visited += 1  
        number_of_presents -= 1  
    elif house == 'C':
        number_of_presents, nice_kids_visited = eat_cookie(number_of_presents, nice_kids_visited) 

    matrix[santa_position[0]][santa_position[1]] = '-' 

    if not number_of_presents or nice_kids_visited == total_nice_kids:
        break 

    command = input() 

matrix[santa_position[0]][santa_position[1]] = 'S'

if not number_of_presents and nice_kids_visited < total_nice_kids:  
    print('Santa ran out of presents!') 

print(*[' '.join(line) for line in matrix], sep='\n') 

if total_nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.') 
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')
