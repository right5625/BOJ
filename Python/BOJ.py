for i in range(1, 10):
    print('? A', i, flush = True)
    if int(input()):
        for j in range(1, 10):
            print('? B', j, flush = True)
            if int(input()):
                break
        print('!', i + j)
        break