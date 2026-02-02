def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_ceaser(string,key):
    output=""
    for i in string:
        original_ascii=ord(i)
        final_ascii=original_ascii+key
        if (65<=original_ascii<=90 and final_ascii>90) or (97<=original_ascii<=122 and final_ascii>122):
            final_ascii-=26
        output+=chr(final_ascii)
    return output

def encrypt_vernan(string,key):
    return ''.join(chr(ord(s)^ord(k)) for s,k in zip(string,key))

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_ceaser(string,key):
    output=""
    for i in string:
        original_ascii=ord(i)
        final_ascii=original_ascii-key+64
        if (65<=original_ascii<=90 and final_ascii<65) or (97<=original_ascii<=122 and final_ascii<97):
                final_ascii+=26
        output+=chr(final_ascii)
    return output

def decrypt_vigenere(msg, key):
    decrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

while True:
    encrypt=bool(input("Enter True for encryption, False for decryption: "))
    if encrypt:
        txt=input("Enter text to encrypt: ")
    else:
        txt=input("Enter message to decrypt: ")
    choice=0
    while choice<1 or choice>3:
        print("Enter a number to choose the cipher used")
        print("1) Ceaser")
        print("2) Vernan")
        print("3) Vigenere")
        choice=int(input("Enter choice: "))
    if choice==1:
        key=int(input("Enter key: "))
        if encrypt:
            res=encrypt_ceaser(txt,key)
        else:
            res=decrypt_ceaser(txt,key)
    elif choice==2:
        key=""
        while len(key)!=len(txt):
            key=input("Enter key (must be same length as input text): ")
        res=encrypt_vernan(txt,key)
    else:
        key=""
        while len(key)<len(txt):
            key=input("Enter key (must be at least as long as input text): ")
        if encrypt:
            res=encrypt_vigenere(txt,key)
        else:
            res=decrypt_vigenere(txt,key)
    print(res)
    print()
