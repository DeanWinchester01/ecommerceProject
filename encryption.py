import random
import math

key = {
    'a': 'R',
    'b': 'S',
    'c': 'T', 
    'd': 'U', 
    'e': 'V', 
    'f': 'W', 
    'g': 'X', 
    'h': 'Y', 
    'i': 'Z', 
    'j': 'a', 
    'k': 'b', 
    'l': 'c', 
    'm': 'd', 
    'n': 'e', 
    'o': 'f', 
    'p': 'g', 
    'q': 'h', 
    'r': 'i', 
    's': 'j', 
    't': 'k', 
    'u': 'l', 
    'v': 'm', 
    'w': 'n', 
    'x': 'o', 
    'y': 'p', 
    'z': 'q', 
    'A': 'r', 
    'B': 's', 
    'C': 't', 
    'D': 'u', 
    'E': 'v', 
    'F': 'w', 
    'G': 'x', 
    'H': 'y', 
    'I': 'z', 
    'J': '0', 
    'K': '1', 
    'L': '2', 
    'M': '3', 
    'N': '4', 
    'O': '5', 
    'P': '6', 
    'Q': '7', 
    'R': '8', 
    'S': '9', 
    'T': 'á', 
    'U': 'é', 
    'V': 'í', 
    'W': 'ó', 
    'X': 'ú', 
    'Y': 'ü', 
    'Z': 'ñ'}
secondKey = {
    'a': 'c',
    'b': 'k',
    'c': 'm',
    'd': 'e',
    'e': 'x',
    'f': 'b',
    'g': 't',
    'h': 'r',
    'i': 'n',
    'j': 'p',
    'k': 'o',
    'l': 'u',
    'm': 'a',
    'n': 'w',
    'o': 'v',
    'p': 'z',
    'q': 's',
    'r': 'y',
    's': 'g',
    't': 'd',
    'u': 'l',
    'v': 'i',
    'w': 'h',
    'x': 'q',
    'y': 'j',
    'z': 'f',
    '1': 'C',
    '2': 'J',
    '3': 'G',
    '4': 'T',
    '5': 'Q',
    '6': 'B',
    '7': 'R',
    '8': 'M',
    '9': 'X',
    '0': 'O'
}

def GetCorrectLetter(letter, key):
    defaultChar = '_'
    for entry in key:
        if key[entry] == letter:
            return entry
    
    return defaultChar

def Decrypt(message, key) :
    decrypted = ""
    for letter in message:
        correctLetter = GetCorrectLetter(letter, key)
        if correctLetter == '_':
            decrypted += letter
        else:
            decrypted += GetCorrectLetter(letter, key)
    
    return decrypted

def reverse(word):
    newWord = ""
    even = ""
    uneven = ""

    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            uneven += word[i]
    
    newWord = even + uneven
    return newWord

def unmix(word):
    newWord = ""
    uneven = ""
    even = ""

    for i in range(len(word)):
        if len(word) % 2 == 0 :
            if i < len(word) / 2:
                even += word[i]
            else:
                uneven += word[i]
        else:
            if i <= len(word) / 2:
                even += word[i]
            else:
                uneven += word[i]

    i = 0
    evenTurn = True
    while len(newWord) < len(word):
        if evenTurn:
            newWord += even[i]
            evenTurn = False
        else :
            newWord += uneven[i]
            evenTurn = True
            i += 1

    return newWord

def Translate(password, key):
    newPass = ""
    for letter in password:
        if key.get(letter):
            newPass += key[letter]
        else:
            newPass += letter

    return newPass

def GetRandomNum(lower, upper):
    number = random.randrange(lower, upper)
    return number

def RemoveGarbage(message):
    messageFound = math.floor(math.sqrt(len(message)))
    actualMessage = message[messageFound:messageFound+messageFound]
    return actualMessage

def GetRandomChar(randomNum):
    i = 0
    for entry in secondKey:
        if i == randomNum:
            return entry
        i += 1

def AddGarbage(message):
    newMessage = ""
    amountOfGarbage = pow(len(message), 2)

    for i in range(amountOfGarbage):
        num = GetRandomNum(0, len(secondKey))

        if i == len(message) :
            newMessage += message
            chosenChar = GetRandomChar(num)
            newMessage += chosenChar
        else:
            chosenChar = GetRandomChar(num)
            newMessage += chosenChar

    return newMessage

def EncryptMessage(message):
    if len(message) < 2:
        message = "Message too short to decrypt"
    else:
        for i in range(3): 
            message = reverse(message)
            message = Translate(message, secondKey)
        

        message = Translate(message, secondKey)
        message = reverse(message)
        message = Translate(message, secondKey)
        message = AddGarbage(message)

    return message

def DecryptMessage(message):
    decrypted = ""
    if len(message) < 2:
        decrypted = "Message too short to decrypt"
    else:
        decrypted = RemoveGarbage(message)
        decrypted = Decrypt(decrypted, secondKey)
        decrypted = unmix(decrypted)
        decrypted = Decrypt(decrypted, secondKey)

        for i in range(3):
            decrypted = unmix(decrypted)
            decrypted = Decrypt(decrypted, secondKey)

    return decrypted