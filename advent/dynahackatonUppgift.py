
    
def main():
    with open("uppgiftsinput.txt") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
    
    matrix = []
    
    for i in range(0,1000):
        matrix.append([])
        for j in range(0,1000):
            matrix[i].append(0)

    for instruction in content:
        matrix = assignment(instruction, matrix)
        
    lightsLitCount = 0
    for i in range(0,1000):
        for j in range(0,1000):
            lightsLitCount += matrix[i][j]
                
    print(lightsLitCount)

def assignment(input, matrix):
    
    input = input.split(" ")
    if input[0] == "turn":
        start = input[2]
        end = input[4]
    
    elif input[0] == "toggle":
        start = input[1]
        end = input[3]
    
    startX = start.split(",")[0]
    startY = start.split(",")[1]
    
    endX = end.split(",")[0]
    endY = end.split(",")[1]
    
    for i in range(int(startX), int(endX)+1):
        for j in range(int(startY), int(endY)+1):
            list = matrix[j]
            if input[0] == 'toggle':
                list[i] += 2
            elif input[1] == "on":
                try:
                    list[i] += 1
                except Exception as e:
                    print('error in on, i, j: ', e, i, j)
            elif input[1] == "off":
                try:
                    if list[i] > 0:
                        list[i] -= 1
                except Exception as e:
                    print('error in of, i, j: ', e, i, j)

                

    return matrix
    
if __name__ == '__main__' : 
    main()