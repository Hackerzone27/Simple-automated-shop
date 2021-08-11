sum1 = 0

x = input("Welcome to our candy shop, what's your name: ")

op = input("Would you like to buy something? (y/n): ")
if op=="n" or op=="N":
    print("Thanks for visiting, have a good day.")
elif op == "y" or op == "Y":

    print("""

    1. Dairy milk small          $10        dmsm
    2. Kitkat                    $15        kk
    3. Dairy milk silk           $50        dms
    4. Snikers                   $10        sk
    5. 5 Star                    $10        st
    6. Chressmello               $25        cmo
    7. Oreo chocolate            $75        oc
    8. Munch                     $10        mc
    9. Snakers                   $5         snk""")

    op2 = input ("What all would u like to buy? (enter the item code): ")

    opt = op2.split()

    if "dmsm" in opt:
        sum1 += 10
        
    if "kk" in opt:
        sum1 += 15
        
    if "dms" in opt:
        sum1 += 50
        
    if "sk" in opt:
        sum1 += 10
        
    if "st" in opt:
        sum1 += 10
        
    if "cmo" in opt:
        sum1 += 25
        
    if "oc" in opt:
        sum1 += 75
        
    if "mc" in opt:
        sum1 += 10
        
    if "snk" in opt:
        sum1 += 5
        
    print (f"Hey {x}, your total is ${sum1}")
    money = input("Would u like to provide cash or online? (c/o): ")
    if money.upper() == "C":
        cash = input("How much money did u give? ")
        if int(cash) > int(sum1):
            sum2 = int(cash) - int(sum1)
            print (f"Here's your change ${sum2}.")
            print ("Have a good day.")
        elif int(cash) == int(sum1):
            print ("Thank u for coming have a good day.")
        else:
            print("""Here's your money back
            Pls provide appropriate cash.""")
    elif money.upper() == "O":
        print ("this service is not yet available")
    else:
        print ("invalid input")
else:

    print ("invalid option try again")
