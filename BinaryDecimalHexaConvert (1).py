#Abigail Lowe
#Decimal-binary, Binary-Decimal, Decimal-Hexadecimal conversion program
#COSC 101
ans=True
while ans:
    print("""
    1.Decimal to Binary Conversion
    2.Binary to Decimal Conversion
    3.Decimal to Hexadecimal Conversion
    4.Exit/Quit [ends program] 
    """)
    ans=input("Select desired conversion: ")

    if ans=="1": #converts decimal to binary
        print("\n Decimal to Binary Conversion selected.")
        n=int(input('Enter decimal value to be converted: '))
        x=n
        k=[]
        while (n>0):
            a=int(float(n%2))
            k.append(a)
            n=(n-a)/2
        k.append(0)
        string=""
        for j in k[::-1]:
            string=string+str(j)
        print('%d in binary is %s'%(x, string))
        
    elif ans=="2": #converts binary to decimal
        print("\n Binary to Decimal Conversion selected.")
        binary = input('Enter binary value to be converted: ')
        decimal = 0
        for digit in binary:
            decimal = decimal*2 + int(digit)
        print (binary, "in decimal is", decimal)

    elif ans=="3": #converting decimal to hexadecimal
        print("Decimal to Hexadecimal conversion was selected.") 
        n=int(input("Enter decimal to be converted: "))
        def DectoHex(n):
            if n <= 16:
                return n
            elif n>16:          
                if n%16 == 10:
                    x = 'A'
                elif n%16 == 11:
                    x = 'B'
                elif n%16 == 12:
                    x = 'C'
                elif n%16 == 13:
                    x = 'D'
                elif n%16 == 14:
                    x ='E' 
                elif n%16 == 15:
                    x = 'F'
                else:
                    x = n%16            
                print ('%n in binary is %x')     
                n = n/16        
                print (n)
  

    elif ans=="4": #exit/quit
        print("\n Goodbye") 
        ans = None

    elif ans !="": #not a valid choice on menu
        print("\n Not Valid Choice, Try again")

                    
        
