#string - non-primitive data type
#   sequence of data put tiogether
#sequence - combination or collection of info
# type o data struct
# list, typle, dictionary, array, array list
#
name = "billy"
password = "123456"
#string = "" or ''
# but for every quote uneed an end 

output = f"welcome, {name}!"
#{} inject variables
stuff = f"here is 2+2={2+2"
print(output,stuff)

'''
in other words 
 " string value + mathvalue = error
 f"var {}" converts data types
 '''
 print(f"")

 #escape characters
 #\n -enter
 #\t-tab button
 #\s-spacebar
 #\"-quote button

print(2+2)
#print(2+"2") #WONT work
print("="*50)#string mTH, RETURNS 50 = SIGNS
#stringObject.method() or object.method()
domain = email[10:]#portion
print(domain)
domain = email[email.index("@"):]#grabs first occurence of chr var.index(chr)+1):
print(domain[0:domain.index(".")])
'''
stringObject[:#] this grabs from beginning to value 
stringObject[#:] this grabs from value to end
stringObject[#:3] grab from value and 3 more chr
'''

