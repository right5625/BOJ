for _ in range(int(input())):
    n, s, b, c = input().split()
    if int(s.split("/")[0]) >= 2010 or int(b.split("/")[0]) >= 1991:
        print(n, "eligible")
    elif int(c) > 40:
        print(n, "ineligible")
    else:
        print(n, "coach petitions")
