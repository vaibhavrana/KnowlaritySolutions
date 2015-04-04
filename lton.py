
def decodestr(inputString):

    strVal=0

    for c in list(inputString):
            strVal += decodechar(c)         
            print "Current chracter: " + c + " value: " + str(decodechar(c))
            
    print "Decoded value: " + str(strVal)

def decodechar(c):

    charVal=0

    if c == 'A':
            charVal = charVal + 1
    else:
            charVal += 2*(decodechar(chr(ord(c)-1))) + (ord(c) - 64)

    return charVal




def decodenum(num):
    
    result =''

    char = 'Z'

    rem=num
 
    
             
    while rem>0:


        rem = rem%decodechar(char)
               

        if rem<num and rem>=0:
            result+=char

    
        char = chr(ord(char)-1)

        
    print result
        




    
