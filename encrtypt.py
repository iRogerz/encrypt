abc='abcdefghijklmnopqrstuvwxyz'
encrypt_dict = {}
front3 = abc[:3]
end3 = abc[3:]
subText = end3+front3
encrypt_dict = dict(zip(abc,subText))
print('dict\n',encrypt_dict)

msgText = input('please input message:')
cipher = []
for i in msgText:
    v = encrypt_dict[i]
    cipher.append(v)
    cipherText = ''.join(cipher)

print('原本輸入\n',msgText)
print('加密後\n',cipherText)

