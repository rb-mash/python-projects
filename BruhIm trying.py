from cProfile import run


print("Hey I'm here to help convert the floor from EU to weird US version")


nam=input('Insert Passcode- ')
if nam==('Farai'):
    print('-Welcome', nam,'!!')
    print('-Allow me to help you convert the floor to US Version')

    inp = input('-What is the Europe Floor? ')
    usf = int(inp) + 1
    print ('The US floor for', inp, 'is', usf)

else:
    print('Sorry Bruh, Try Again') 

