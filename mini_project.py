a = float (input("Enter a no. a: ")) 
b = float (input("Enter a no. b: ")) 
x =  input ("Choose an operator (sum, sub , multi, modulus,power, div)")
sum = a+b
sub = a-b
power = a**b
modulus = a%b
div= a/b
multi= a*b

if  x == "sum":
    print ("sum= ", sum)
elif x == "sub":
    print ("substraction= ", sub)
elif x == "power":
    print ("power= ", power)
elif x == "modulus":
    print ("remainder= ", modulus)
elif x == "div":
    print ("a/b= ", div)
elif x == "multi":
    print ("multiplication ", multi)
else : print("the entered operator is incorrect")    

