# 23627. driip
s = input()
if len(s) >= len('driip') and s[-len('driip'):] == 'driip':
    print('cute')
else:
    print('not cute')
