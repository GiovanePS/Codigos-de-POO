msgCodificada = input().split(' ')
msgDecodificada = msg = ''

for txt in msgCodificada:
    msg = txt[-1:-len(txt):-2]
    msgDecodificada += msg[::-1]
    msgDecodificada += ' '

print(msgDecodificada.strip())