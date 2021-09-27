a = int(input('geef het eerste hele getal '))
b = int(input('geef het tweede hele getal '))

if a > b:
    max = a
    print (" a is het grootste getal: " +  str(max)  ) 

elif a < b:
    min = a 
    print ("a is het kleinste getal " + str(min) )

else:
    print ("a en b zijn even groot ")
    