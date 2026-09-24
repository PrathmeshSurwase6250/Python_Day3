# Reverse a string without slicing.
def revString(str):
    string = ''
    for i in range (len(str)-1,-1 , -1):
        string += str[i]
    return string
# Check whether a string is palindrome.
def revPalString(str):
    string = ''
    for i in range (len(str)-1,-1 , -1):
        string += str[i]
    return string
    
        
# Count vowels.
def revString(str):
    count = 0 
    for i in range (len(str)):
        if (str[i] == 'a' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'e'):
            count += 1 
    return count

# Count consonants.
def consonatString(str):
    count = 0 
    for i in range (len(str)):
        if (str[i] != 'a' or str[i] != 'i' or str[i] != 'o' or str[i] != 'u' or str[i] != 'e'):
            count += 1 
    return count

# Count digits in a string.
def digitString(str):
    count = 0 
    for i in range (len(str)):
        if (str[i].isdigit()):
            count += 1 
    return count
# Count spaces.
def CountSpaces(str):
    count = 0 
    for i in range (len(str)):
        if (str[i]==' '):
            count += 1 
    return count
# Count words.
def CountWords(str):
    count = 0 
    for i in range (len(str)):
        if (str[i] !=' '):
            count += 1 
    return count

# Find the length without using len().

def len(str):
    count = 0 
    for i in str :
        count += 1 
    return count 

# Convert lowercase to uppercase without .upper().

def lowertoUpper(str):
    newStr = ''
    for i in str :
        if 'a' <= i <= 'z':
            newStr += chr(ord(i)-32)
        else :
            newStr += i
    return newStr
    
# Remove spaces from a string.

def removeSpace(str):
    count = 0 
    for i in str :
        if i != '':
            count += str[i]
    return count 

# Find frequency of every character.

def frequency(str):
    dictonary = {}
    for i in str :
        if i in dictonary :
            dictonary[i] +=  1 
        else :
            dictonary = 1
    return dictonary

# Find the first non-repeating character.

def nonRepeat(str):
    dictonary = {}
    for i in str :
        if i in dictonary :
            dictonary[i] +=  1 
        else :  
            dictonary = 1
    for key , value in  dictonary.items() :
        if (value == 1) :
            print(key)
    
# Find duplicate characters.

def duplicateChar (str):
    dictonary = {}
    for i in str :
            if i in dictonary :
                dictonary[i] +=  1 
            else :  
                dictonary = 1
    for key , value in  dictonary.items() :
            if (value >= 2) :
                print(key)
                

# Find the longest word in a sentence.
def  longestWord(sentence):
    words = sentence.split()
    longestWord = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# Find the shortest word.
def  longestWord(sentence):
    words = sentence.split()
    longestWord = words[0]
    for word in words:
        if len(word) < len(longest):
            longest = word

    return longest
# Capitalize every word.

# Replace vowels with *.
def vowelsReplace(str):
    words = ''
    for i in range (len(str)):
        if (str[i] == 'a' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u' or str[i] == 'e'):
            words += '*'
        else:
            words += i
    return words
# Check whether a string contains only digits.
def onlyDigits(str) :
    return str.isdigit()
# Check whether a string contains only alphabets.
def onlyAlpha(str):
    return str.isalpha

# Extract numbers from a string.
def extractNum(str):
    num = ''
    for i in str :
        if i.isdigit():
            num +=i
    return num
# Extract email addresses from a string.
def extractEmail(str):
    words = str.split()
    email = []
    for word in words :
        if  '@' in word :
            email.append(word)
    return email
        
