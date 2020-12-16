
list = open("input.txt").readlines()
    
for line in list:
    output1 = int(line)
    for line in list:
        output2=int(line)
        for line in list:
            output3=int(line)
            answer = (output1+output2+output3)
            if answer == 2020:
                print(answer) 
                print(output1)
                print(output2)
                print(output3)
                print(output1*output2*output3)



#for x in list:
    #for y in list:
            #answer = (x*y)
            #print (print)
