
list = open("input.txt").readlines()
finalcount = 0
for line in list:
    count=0
    formatted = line.split(' ')
    rule = formatted[0]
    letter = formatted[1].strip(":")
    password = formatted[2].strip()
    
    #print('your rule is '+ rule +' ya dingus' + ' wow your password is '+password+"!")
    formatrule = rule.split('-')
    
    spot1=int(formatrule[0])
    spot2=int(formatrule[1])
    
    #print ('did you use '+letter +"?")
    #for i in password:
#        if i ==letter:
#            count = count + 1
    #if count > 1 :
        #print ("yah goofed!")
        #print ("the letter " + letter + " is used " + str(count) +" times in " + password +"!" )

    ##if count == 1:
    print('your rule is '+ rule +' ya dingus' + ' wow your password is '+password+"!")
    print ('did you use '+letter +"?")

    if letter == password[spot1-1] or letter == password[spot2-1] :
        print("hit")
        print ("is "  +password[spot1-1] + "   " + password[spot2-1] )
        if letter == password[spot1-1] is letter == password[spot2-1] :
            print("you have an bad password")
            print (password[spot1-1] + "  is  " + password[spot2-1] )
        else:
            print (password[spot1-1] + "  is not " + password[spot2-1] )
            finalcount=finalcount + 1

print(finalcount)
