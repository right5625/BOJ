print('Unlocked' if ''.join(list(map(str, sorted(list(map(int, input())))))) in ['123', '456', '789', '147', '258', '369', '058'] else 'Locked')