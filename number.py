def extractNumbersWithLoop(num):
    while num>0:
        lastdigit=num%10
        print(lastdigit)
        num=num//10


value=extractNumbersWithLoop(21323)

print(f"Result :{value}")