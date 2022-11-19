from random import *

aktualny_rok=2022
meno = input('Ako sa voláš?')
print('Ahoj '+meno+' rád Ťa spoznávam :)')
roknarodenia = input(meno+', v ktorom roku si sa narodil?')
meno2 = choice(('Alena', 'Barbora', 'Eva', 'Sofia'))
print('Á spomínam si, v roku '+roknarodenia+' sa narodila aj '+meno2)
print(roknarodenia)
c= aktualny_rok - int(roknarodenia)
print(c)
kdebivas=input('Kde bivas ?')
print(kdebivas+',to mi pride blizko,mozem ta prist navstivit ?')


