import random
import math

key = {}
secondKey = {
    '@':'.',
    '.':'@',
    '1': 'h',
    '2': 't',
    '3': 'e',
    '4': 'u',
    '5': 'c',
    '6': 'b',
    '7': 'k',
    '8': 'x',
    '9': 'q',
    '0': 'j',
    'A': 'a',
    'B': 'y',
    'C': 'n',
    'D': 'r',
    'E': 'f',
    'F': 'z',
    'G': 'm',
    'H': 'w',
    'I': 'v',
    'J': 'p',
    'K': 's',
    'L': 'd',
    'M': 'l',
    'N': 'i',
    'O': 'g',
    'P': 'o',
    'Q': 'j',
    'R': 'c',
    'S': 'e',
    'T': 'q',
    'U': 'x',
    'V': 'k',
    'W': 't',
    'X': 'h',
    'Y': 'b',
    'Z': 'a',
    'a': '4',
    'b': '8',
    'c': '3',
    'd': '1',
    'e': '6',
    'f': '9',
    'g': '0',
    'h': '2',
    'i': '5',
    'j': '7',
    'k': 'l',
    'l': 'w',
    'm': 'p',
    'n': 'v',
    'o': 'm',
    'p': 'j',
    'q': 't',
    'r': 'f',
    's': 'n',
    't': 'r',
    'u': 'y',
    'v': 'e',
    'w': 'c',
    'x': 'd',
    'y': 'a',
    'z': 'g',
}



firstKey = "RSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789áéíóúüñß"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

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
    '''int a = 1;
    int b = 1;
    int length = message.length() * -1;
    int discriminant = b * b - 4 * a * length;
    int x1 = (-b + sqrt(discriminant)) / (2 * a);
    string actualMessage = message.substr(x1, x1);
    '''
    actualMessage = message[messageFound:messageFound+messageFound]
    #print(message)
    return actualMessage

def AddGarbage(message):
    newMessage = ""
    amountOfGarbage = pow(len(message), 2)

    for i in range(amountOfGarbage):
        if i == len(message) :
            newMessage += message
            chosenChar = firstKey[GetRandomNum(0, len(firstKey))]
            newMessage += chosenChar
        else:
            chosenChar = firstKey[GetRandomNum(0, len(firstKey))]
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
        message = Translate(message, key)
        message = AddGarbage(message)

    return message

def DecryptMessage(message):
    decrypted = ""
    if len(message) < 2:
        decrypted = "Message too short to decrypt"
    else:
        decrypted = RemoveGarbage(message)
        #print(decrypted)
        decrypted = Decrypt(decrypted, key)
        #print(decrypted)
        decrypted = unmix(decrypted)
        #print(decrypted)
        decrypted = Decrypt(decrypted, secondKey)
        #print(decrypted)

        for i in range(3):
            decrypted = unmix(decrypted)
            #print(decrypted)
            decrypted = Decrypt(decrypted, secondKey)
            #print(decrypted)

    return decrypted


for i in range(len(alphabet)):
    #entry = {alphabet[i]: firstKey[i]}
    key[alphabet[i]] = firstKey[i]