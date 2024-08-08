pink = int(input())
green = int(input())
red = int(input())
orange = int(input())
cost = int(input())
combination = 0
minTicket = float('inf')
for p in range(cost // pink + 1):
    for g in range(cost // green + 1):
        for r in range(cost // red + 1):
            for o in range(cost // orange + 1):
                if pink * p + green * g + red * r + orange * o == cost:
                    print(f'# of PINK is {p} # of GREEN is {g} # of RED is {r} # of ORANGE is {o}')
                    combination += 1
                    minTicket = min(minTicket, p + g + r + o)
print(f'Total combinations is {combination}.\nMinimum number of tickets to print is {minTicket}.')