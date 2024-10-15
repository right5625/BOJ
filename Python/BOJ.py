import string

while True:
    if input() == "ENDOFINPUT":
        break
    for i in input():
        (
            print(chr(ord(i) + 21) if ord(i) < 70 else chr(ord(i) - 5), end="")
            if i in string.ascii_uppercase
            else print(i, end="")
        )
    print()
    input()
