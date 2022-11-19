url1 = input('zadajte platnu url adresu: ')



def url():
    a=''
    b=''
    c=''

    g=''

    
    for i in range(len(url1)):
        

       
            
        if url1[i]==':':
            ns=url1[:i]
            a=ns

        if url1[i]==':':
            ns=url1[i+23:i+26]
            b=ns

        if url1[i]==':':
            ns=url1[i+3:i+26]
            c=ns

   
            

        
            
        
                
    

    print('url adresa: '+url1)

    print('a): '+ a)
    print('b): ' + b)
    print('c): ' + c)
    
    


   


          
url()
