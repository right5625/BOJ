import string

leftKey = ['q', 'w', 'e', 'r', 't', 'y', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
left = right = 0
for i in input():
    if i == ' ':
        if left > right:
            right += 1
        else:
            left += 1
    else:
        if i.lower() in leftKey:
            left += 1
        else:
            right += 1
        if i in string.ascii_uppercase:
            if left > right:
                right += 1
            else:
                left += 1
print(left, right)