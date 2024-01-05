from datetime import date

Y, M, D = map(int, input().split('-'))
d = date(Y, M, D)
if date(Y, 3, 21) <= d <= date(Y, 4, 19):
    print('Aries')
if date(Y, 4, 20) <= d <= date(Y, 5, 20):
    print('Taurus')
if date(Y, 5, 21) <= d <= date(Y, 6, 20):
    print('Gemini')
if date(Y, 6, 21) <= d <= date(Y, 7, 22):
    print('Cancer')
if date(Y, 7, 23) <= d <= date(Y, 8, 22):
    print('Leo')
if date(Y, 8, 23) <= d <= date(Y, 9, 22):
    print('Virgo')
if date(Y, 9, 23) <= d <= date(Y, 10, 22):
    print('Libra')
if date(Y, 10, 23) <= d <= date(Y, 11, 22):
    print('Scorpio')
if date(Y, 11, 23) <= d <= date(Y, 12, 21):
    print('Sagittarius')
if date(Y, 12, 22) <= d or date(Y, 1, 19) >= d:
    print('Capricorn')
if date(Y, 1, 20) <= d <= date(Y, 2, 18):
    print('Aquarius')
if date(Y, 2, 19) <= d <= date(Y, 3, 20):
    print('Pisces')