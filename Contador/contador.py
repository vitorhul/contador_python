#criar um contador que va do numero escrito pelo usuario, até 100.

#pedir ao user que digite um numero
try:

    numero=(input('digite um numero: '))
    numero_int=int(numero)
    end=(input('digite onde você quer que o contador pare:'))
    end=int(end)
    end=end+1
    #criar um contador que acrescente mais um numero até o 100
    def contador():
        for num in range( numero_int,(end)):
            print(num)
            
            
            
    
    if end < numero_int:
        print('infelizmente não sera possivel essa operação')  

    elif numero_int>=1 and end<=101:
        contador()    
        
    else:
        print('tente novamente e digite um numero menor que 100')
        

except:
    print('digite um valor valido')
    

