import re

for _ in range(int(input())):
    print(re.sub(r'(?<!^)([A-Z])', r'_\1', input()).lower())