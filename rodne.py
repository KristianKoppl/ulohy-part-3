rodnec = input('zadajte platne rodne cislo: ')



def rodne():
    a=''
    b=''
    c=''

    g=''

    s=''
    d=''
    m=''
    k=''
    for i in range(len(rodnec)):
        

       
            
        if rodnec[i]=='/':
            ns=rodnec[:i-4]
            a=ns

        if rodnec[i]=='/':
            ns=rodnec[i-4:i-2]
            b=ns

        if rodnec[i]=='/':
            ns=rodnec[i-2:i]
            c=ns

    if rodnec[0] or rodnec[0] <3:
        g='Muž'
    if rodnec[0] or rodnec[0] >5:
        g ='Žena'
            

        if rodnec[i]=='/':
            ns=rodnec[i+1:]
            s=ns
                
        if rodnec[i]=='/':
            ns=rodnec[i+21:]
            d=ns
                
        if rodnec[i]=='/':
            ns=rodnec[i+6:i+20]
            m=ns

        if rodnec[i]=='/':
            ns=rodnec[i+1:i+5]
            k=ns
            
        
                
    

    print('rodne cislo: '+rodnec)

    print('datum narodenia: ' +c+'.'+b+'.'+a)

    print('vase pohlavie: ' + g)
    print(rodnec[2]+rodnec[3])
    


   


          
rodne()
