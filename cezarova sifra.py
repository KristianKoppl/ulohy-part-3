#Cézarova_šifra
vstup = input('Zadaj text:')
p = input('Zadaj počet zašifloraví:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+int(p)) 
    if znak == 'z':
        novyznak = 'a'
    sifra = sifra+novyznak
print(sifra)




#25 chr(ord(znak)+1) ::: tu sa zmení namiesto +1 lubovolné čislo do + aby sa šifrovalo
#26 to is´te ako 25 úloha len sa dá - pred ćislo teda -1 
#27 chr(ord(znak)-2) buď sa tam dá +2 alebo +3 či -1
#28 dál som input kde som len po zadaní ak dal kladné alebo záporné tak sa dalo podla toho aké som dal znamienko ++ je + +- je -
