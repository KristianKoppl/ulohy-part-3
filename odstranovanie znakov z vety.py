from random import *
s = input('Zadaj text: ')
novy = ''


for i in range(len(s)):
    ktory = randrange(len(s))
    print('Odstraňujem znak', s[ktory])
    novy = novy+s[ktory]
    print('Zatiaľ som vytvoril:', novy)
    s = s[:ktory]+s[ktory+1:]
    print('Ešte zostali tieto znaky:', s)
print('Zamiešané slovo:', novy)







#29 doplnil som do premmenej input
#30 pridal som randrange aby to bolo náhodné
