import os
def part1(file) :
    d=0
    for line in file :
        stripped_line = line.strip()
        values = stripped_line.split()
        column1.append(int(values[0]))
        column2.append(int(values[1]))
    column1.sort()
    column2.sort()
    for i in range(len(column1)):
        d = d + abs(int(column1[i])  - int(column2[i]))
    return d

def part2(col1, col2) :
    similarity_score = 0
    for elem in col1 :
        occurences = elem * col2.count(elem)
        similarity_score = similarity_score + occurences
    return similarity_score

values = []
column1 = []
column2= []

print("Working directory is : ", os.getcwd())
with open("PuzzleInput.txt", 'r') as file : 
    distance = part1(file)
    print("The distance is : ", distance)
    similarity_score = part2(column1, column2)
    print("The similarity score is : ", similarity_score)


