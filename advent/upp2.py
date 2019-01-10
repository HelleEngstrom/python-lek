def getArea(present):
    present = present.split('x')
    for i in range(0, 3):
        present[i] = int(present[i])
    
    areas = [present[0]*present[1], present[0]*present[2], present[1]*present[2]]
    totalArea = 2*sum(areas)
    return totalArea
    
def getShortestCurcumference(present):
    present = present.split('x')
    for i in range(0, 3):
        present[i] = int(present[i])
    circumferences = [present[0] + present[1], present[0] + present[2], present[1] + present[2]]
    return 2*min(circumferences)

with open("upp2input.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

area = 0

for line in content:
    area += getArea(line)
    area += getShortestCurcumference(line)
print(area)



