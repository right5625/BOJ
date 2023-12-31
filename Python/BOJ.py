from string import ascii_lowercase

for i in list(zip(*[ascii_lowercase[ascii_lowercase.find(i):] + ascii_lowercase[:ascii_lowercase.find(i)] for i in input()])):
    try:
        print({'northlondo' : 'NLCS', 'branksomeh' : 'BHA', 'koreainter' : 'KIS', 'stjohnsbur' : 'SJA'}[''.join(i)])
        break
    except:
        pass