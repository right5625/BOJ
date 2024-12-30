for i in range(int(input())):
    S = input()
    print(f'Case #{i + 1}: {S} is ruled by {'nobody' if S[-1].lower() == 'y' else ('a queen' if S[-1].lower() in 'aeiou' else 'a king')}.')