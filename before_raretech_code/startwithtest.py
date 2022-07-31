list12 = ['jiji', 'jiji']
tuple12 = ('tu', 'hih')

#print(type(list12[1]))
if list12[0].startswith('ji'):
    print('ok')
tu = list12[1]
if tu.startswith('ji'):
    print('ok2')


if tuple12[0].startswith('tu'):
    print('ok3')
yu = tuple12[1]
if yu.startswith('hi'):
    print('ok3')
a = 'ji'
if a.startswith('j'):
    print('lastok')

print(dir(a))