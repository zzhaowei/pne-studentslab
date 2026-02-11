def maximum(tem):
    i = 0
    highest = tem[0]
    while i < len(tem):
        if tem[i] > highest:
            highest = tem[i]
            i += 1
        else:
            i += 1
    return highest

def minimum(tem):
    i = 0
    lowest = tem[0]
    while i < len(tem):
        if tem[i] < lowest:
            lowest = tem[i]
            i += 1
        else:
            i += 1
    return lowest

def average(tem):
    sum = 0
    num = len(tem)
    for i in range(0 , len(tem)):
        sum += tem[i]
    return round(sum / num, 1)

def above_17(tem):
    num = 0
    for i in range(0, len(tem)):
        if tem[i] > 17:
            num += 1
    return num

temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
temperatures_sorted = sorted(temperatures)
print("\n\n\nWednesday:" , temperatures[2])
print("Max:" , maximum(temperatures))
print("Min:" , minimum(temperatures))
print("Average:" , average(temperatures))
print("Days above 17:" , above_17(temperatures))
print("Sorted:" , temperatures_sorted)