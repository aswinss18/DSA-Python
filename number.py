def extractNumbersWithLoop(num):
    while num>0:
        lastdigit=num%10       
        print(lastdigit)
        num=num//10

def extractNumbersAndPrintNumberPattern(num):
    while num>0:
        lastdigit=num%10
        for i in range (0,lastdigit):
            print(lastdigit)     
        num=num//10



value=extractNumbersAndPrintNumberPattern(24)

print(f"Result :{value}")