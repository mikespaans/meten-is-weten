a = int(input('geef het eerste hele getal '))
b = int(input('geef het tweede hele getal '))

if a > b:
    max = a
    min = b
    print (" a is het grootste getal: " +  str(max)  ) 
    print ("het minimum is " + str(min))
    print (" het maximum is " + str(max))

elif a < b:
    min = a 
    max = b
    print ("a is het kleinste getal " + str(min) )
    print (" het minimum is " + str(min))
    print (" het maximum is " + str(max))
else:
    print ("a en b zijn even groot ")
    max = a
    min = b
    print (" het minimum is " + str(min))
    print ("het maximum is " + str(max))