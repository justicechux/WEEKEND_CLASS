# write a program that will print out tripple the value of all integers from 0 to 10

for i in range(11):
    if i %2 == 0: 
        print(i*3)
    elif i %2 == 1:
        print(i*2)


le = [i*3 for i in range(11) if i%2 ==0]