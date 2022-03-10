new_text=""
msg=input("Enter word : ")
d=input("Enter distance : ")
d=int(d)
if d>0:
    for c in msg:
        cipher_text = ord(c) + d
        if cipher_text > ord('z') or ( cipher_text < ord('a') and cipher_text > ord('Z') ):
            cipher_text -= 26
        new_text += (chr(cipher_text))


else :
    for c in msg:
        cipher_text = ord(c) + d
        if cipher_text < ord('a') and cipher_text > ord('Z'):
            cipher_text += 26
        elif cipher_text < ord('A'):
            cipher_text += 26
        new_text += (chr(cipher_text))

print(new_text)