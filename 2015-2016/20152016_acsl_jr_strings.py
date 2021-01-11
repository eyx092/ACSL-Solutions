string = input("Enter the string: ")
for i in range(5):
    r = input("Enter the ranges: ")
    arr_r = r.split(",")
    start = int(arr_r[0])
    length = int(arr_r[1])
    if start < 0:
        start = len(string)+start
    if length == 0:
        length = len(string)-start
    out = ""
    #print(start)
    #print(length)
    if length < 0:
        length = len(string)+length
        out = string[start:length]
    else:
        while length != 0:
            out += string[start]
            start += 1
            length -= 1
        length = len(string)
    
    
    print(out)
