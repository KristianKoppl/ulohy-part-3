veta1 = input('zadaj vetu')

for i in range(len(veta1)):
    if veta1[i] == '?':
        print('oznamovacia')
    if veta1[i] == '.':
        print('opitovaciu')
    if veta1[i] == '!':
        print('rozkazovacia')

              
print(veta1)

