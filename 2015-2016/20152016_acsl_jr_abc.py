def is_int(v):
    try:
        int(v)
        return True
    except ValueError:
        return False

def generate_possible():
    possibilities = []
    possible_rows = [["A","B","C"],["A","C","B"],["B","A","C"],["B","C","A"],["C","A","B"],["C","B","A"]]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                p = [possible_rows[i],possible_rows[j],possible_rows[k]]
                possibilities.append(p)
    return possibilities


def validate_puzzle(puzzle):
    valid = True
    for i in range(3):
        if puzzle[0][i] == puzzle[1][i] or puzzle[1][i] == puzzle[2][i] or puzzle[0][i] == puzzle[2][i]:
            valid = False
    return valid

def check_puzzle(unsolved, brute):
    valid = True
    for i in range(3):
        for j in range(3):
            if unsolved[i][j] == "":
                pass
            else:
                if unsolved[i][j] != str(brute[i][j]):
                    valid = False

    return valid

def solve_puzzle(puzzle):
    p = generate_possible()
    valid = []
    for i in range(len(p)):
        if validate_puzzle(p[i]) == True:
            valid.append(p[i])

    for i in range(len(valid)):
        if check_puzzle(puzzle,valid[i]) == True:
            return valid[i]



def main():
    for i in range(5):
        sudoku_arr = ["", "", "", "", "", "", "", "", ""]
        sudoku = [["","",""],["","",""],["","",""]]

        position_input = input("Enter locations: ").split(", ")

        current = []

        for i in range(1,len(position_input)):
            if is_int(position_input[i]):
                current.append(int(position_input[i]))
            else:
                for j in range(len(current)):
                    sudoku_arr[current[j] - 1] = position_input[i]
                del current[:]

        for i in range(9):
            sudoku[i//3][i%3] = sudoku_arr[i]

        output = ""
        solved = solve_puzzle(sudoku)

        for i in range(3):
            for j in range(3):
                output += solved[i][j]

        print(output)

if __name__ == "__main__":
    main()

"""
SAMPLE INPUT:          | SAMPLE OUTPUT:
1. 3, 1, A, 3, C, 8, A | 1. ABCBCACAB
2. 3, 1, A, 6, C, 8, B | 2. ACBBACCBA
3. 3, 1, B, 6, B, 9, C | 3. BCACABABC
4. 2, 1, C, 5, B       | 4. CABABCBCA
5. 2, 3, B, 7, A       | 5. CABBCAABC
"""
