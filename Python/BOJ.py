N = int(input())
for i in range(N, 1, -1):
    print(f'{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down and pass it around, {i - 1} ' + ('bottle' if i - 1 == 1 else 'bottles') + ' of beer on the wall.\n')
print(f'1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {N} ' + ('bottle' if N == 1 else 'bottles') + ' of beer on the wall.')