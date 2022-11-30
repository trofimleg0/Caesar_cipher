# text encryption function    
def encryption(shift):
    with open('encryption.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        encrypted_letters = ''
        
        while shift > 26:
            shift -= 26
        
        for char in text:
            if char.isalpha():
                if char.isupper():
                    char = chr(ord(char) + shift)
                    if char < chr(65) or char > chr(90):
                        char = chr(ord(char) - 26)
                else:
                    char = chr(ord(char) + shift)
                    if char < chr(97) or char > chr(122):
                        char = chr(ord(char) - 26)
            encrypted_letters += char
    return encrypted_letters

# text decryption function    
def decryption(shift):
    with open('decryption.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        decrypted_letters = ''
        
        while shift > 26:
            shift -= 26
        
        for char in text:
            if char.isalpha():
                if char.isupper():
                    char = chr(ord(char) - shift)
                    if char < chr(65) or char > chr(90):
                        char = chr(ord(char) + 26)
                else:
                    char = chr(ord(char) - shift)
                    if char < chr(97) or char > chr(122):
                        char = chr(ord(char) + 26)
            decrypted_letters += char
    return decrypted_letters
    
cypher = input('Choose encryption or decryption. Select e/d: ').lower()
while cypher != 'e' and cypher != 'd':
    cypher = input('Choose "e" or "d": ')

shift = input('Select the number of shifts: ')
while not shift.isdigit():
    shift = input('Print the number: ')
    
if cypher == 'e':
    print(encryption(int(shift)))
else:
    print(decryption(int(shift)))