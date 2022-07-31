"""
untest = 'Wklv lv wrr orqj! Vr, L grq\'w zdqw wr ghfubsw lw pdqxdoob!!'

after_word = []

for untext_word in untest:
    if untext_word in ['!', ',', '\'',' ']:
        after_word.append(untext_word)
    else:
        encrypt_untext_word = chr(ord(untext_word)+3)
        after_word.append(encrypt_untext_word)

print(''.join(after_word))
"""

test = 'f'
test2 = 'd'
print((ord(test)-3))
print(chr(94))