
list = open("input.txt").readlines()
finalcount = 0
for line in list:
    count=0
    formatted = line.split(' ')
    rule = formatted[0]
    letter = formatted[1].strip(":")
    password = formatted[2].strip()
    
    print('your rule is '+ rule +' ya dingus' + 'wow your password is '+password+"!")
    formatrule = rule.split('-')
    
    rulemin=int(formatrule[0])
    rulemax=int(formatrule[1])
    print ('did you use '+letter +"?")
    for i in password:
        if i ==letter:
            count = count + 1
    print ("the letter " + letter + " is used " + str(count) +" times in " + password +"!" )    
    if count >= rulemin and count <= rulemax:
        print("you have a good password")
        finalcount=finalcount + 1
print(finalcount)
