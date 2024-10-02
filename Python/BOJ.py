month = {
    i: j
    for i, j in zip(
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        range(1, 13),
    )
}
while True:
    d, m = input().split()
    d = int(d)
    if d == 0:
        break
    if month[m] == 8 and d == 4:
        print("Happy birthday")
    elif month[m] == 2 and d == 29:
        print("Unlucky")
    else:
        print("Yes" if month[m] < 8 or (month[m] == 8 and d < 4) else "No")
