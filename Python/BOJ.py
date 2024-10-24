res = [0] * 8
for i in input():
    if i in "1QAZ":
        res[0] += 1
    elif i in "2WSX":
        res[1] += 1
    elif i in "3EDC":
        res[2] += 1
    elif i in "4RFV5TGB":
        res[3] += 1
    elif i in "6YHN7UJM":
        res[4] += 1
    elif i in "8IK,":
        res[5] += 1
    elif i in "9OL.":
        res[6] += 1
    else:
        res[7] += 1
print(*res, sep="\n")
