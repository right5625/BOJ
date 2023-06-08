D = int(input())
E = int(input())
W = int(input())
A = max((D - 100) * 0.25, 0) + E * 0.15 + W * 0.2
B = max((D - 250) * 0.45, 0) + E * 0.35 + W * 0.25
print(f'Plan A costs {A:.2f}\nPlan B costs {B:.2f}')
if A == B:
    print('Plan A and B are the same price.')
else:
    print(f'Plan A is cheapest.' if A < B else 'Plan B is cheapest.')