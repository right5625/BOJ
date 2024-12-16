S = input()
for k, v in {'socail': 'digital humanities', 'history': 'digital humanities', 'language': 'digital humanities', 'literacy': 'digital humanities', 'bigdata': 'public bigdata', 'public': 'public bigdata', 'society': 'public bigdata'}.items():
    if k in S:
        print(v)
        break