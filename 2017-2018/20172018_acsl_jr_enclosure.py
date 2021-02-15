def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
for i in range(5):
    solutions = []
    equation = input("Enter the equation: ").replace(" ","")
    for i in range(len(equation)):
        if equation[i] == "(" or equation[i] == ")":
            index = i
    if equation[index] == "(":
        for i in range(index, len(equation)):
            if isint(equation[i]) == True:
                solutions.append(i+2)
        print(solutions[1:len(solutions)])
    if equation[index] == ")":
        for i in range(0, index):
            if isint(equation[i]) == True:
                solutions.append(i+1)
        print(solutions[0:len(solutions) - 1])
