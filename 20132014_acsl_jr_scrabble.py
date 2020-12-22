letter_map = [[3,9,15,21,27,33,39],[5,10,20,25,30,35,40],[7,14,28],[8,16,24,32]]
point_values = [["A","E"],["D","R"],["B","M"],["V","Y"],["J","X"]]
lengths = [7,7,3,4]

word_sum = 0
word_arr = (input("Enter the word: ")).split(",")
score_map = []

for i in range(4):
    for j in range(5):
        if point_values[j][0] == word_arr[i] or point_values[j][1] == word_arr[i]:
            if j == 4:
                word_sum += 8
                score_map.append(8)
            else:
                word_sum += (j+1)
                score_map.append(j+1)

#print(score_map)




for i in range(5):
    sum = word_sum
    multiplier = 1
    start_num = int(input("Enter a starting number: "))
    nums = []
    nums.append(start_num)
    nums.append(start_num+1)
    nums.append(start_num+2)
    nums.append(start_num+3)
    for j in range(4):
        for k in range(4):
            for l in range(len(letter_map[k])):
                if letter_map[k][l] == nums[j]:
                    if k == 0:
                        sum += score_map[j]
                    if k == 1:
                        sum += (score_map[j]*2)
                    if k == 2:
                        multiplier *= 2
                    if k == 3:
                        multiplier *= 3

    print(sum*multiplier)
                    

        


            
