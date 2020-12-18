line1in = input("Set variables: ")
arrline1 = line1in.split(", ")
milage = int(arrline1[0])
price = float(arrline1[1])
average_speed = int(arrline1[2])
citiesdist = [450, 140, 120, 320, 250, 80]
citieslookup = ["A", "B", "C", "D", "E", "F", "G"]

for i in range(5):
    dist = 0
    cities = input("Enter the two cities: ")
    citiesarr = cities.split(", ")
    startcity = citiesarr[0]
    endcity = citiesarr[1]
    for i in range(len(citieslookup)):
        if startcity == citieslookup[i]:
            startlookupcity = i
    for i in range(len(citieslookup)):
        if endcity == citieslookup[i]:
            endlookupcity = i
    for i in range(startlookupcity, endlookupcity):
        dist += citiesdist[i]
    time = round(int(dist)/int(average_speed)*60)
    hrtime = time // 60
    mintime = time % 60
    if hrtime < 10:
        hrtime = "0"+str(hrtime)
    if mintime < 10:
        mintime = "0"+str(mintime)
    formatted_time = str(hrtime)+":"+str(mintime)
    gallons = round(dist)/round(milage)
    gas_price = float(gallons*price)
    gas_price = round(gas_price, 2)
    gas_price = "$"+str(gas_price)
    if len(gas_price) == 5:
        gas_price += "0"
    if len(gas_price) == 4:
        gas_price += "00"
    print((dist),", ",(formatted_time),", ",(gas_price),sep="")
