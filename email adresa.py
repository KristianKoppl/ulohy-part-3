email = input('zadajte platnu email adresu: ')




def adresy():
    server=''
    user=''
    domena1=''
    domena2=''
    domena3=''
    for i in range(len(email)):
        if email[i]=='@':
            ns=email[:i]
            user=ns

        if email[i]=='@':
            ns=email[i+1:]
            server=ns
            
        if email[i]=='@':
            ns=email[i+21:]
            domena1=ns
            
        if email[i]=='@':
            ns=email[i+6:i+20]
            domena2=ns

        if email[i]=='@':
            ns=email[i+1:i+5]
            domena3=ns
            
    
    print('email: '+ email)
    print('TLD: '+ email)
    print('Server: '+server)
    print('User: '+user)
    print('Domény:.......')
    print('Doména 1. úrovne je: '+domena1)
    print('Doména 2. úrovne je: '+ domena2)
    print('Doména 3. úrovne je: '+ domena3)


adresy()
