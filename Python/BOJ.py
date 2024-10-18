for _ in range(int(input())):
    w = input()
    print(f"The number of vowels in {w} is {sum([w.count(i) for i in 'aeiou'])}.")
