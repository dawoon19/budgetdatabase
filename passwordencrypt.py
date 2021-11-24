import math as m
def encrypt(username, password):
    if len(username) ==0 or len(password)==0:
        return ''
    final_encryption=''
    user_temp = list(username)
    loop = 0
    index = 0
    while len(user_temp)>0 and loop<len(user_temp):
        if index>=len(user_temp):
            index = 0
        if index%2==0:
            try:
                int(user_temp[index])
            except:
                user_temp[index] = str(ord(user_temp[index].upper())-len(user_temp))
        else:
            try:
                int(user_temp[index])
            except:
                user_temp[index] = str(ord(user_temp[index].lower())-len(user_temp))
        loop +=1
        index+=(m.floor(loop/2)+m.floor(len(user_temp)/2))

    pass_temp = list(password)

    loop = 0
    index = 0
    while len(pass_temp)>0 and loop<len(pass_temp):
        if index>=len(pass_temp):
            index = 0
        if index%2==0:
            try:
                int(pass_temp[index])
                pass_temp[index] = str(chr(pass_temp[index]+len(pass_temp)))
            except:
                try:
                    pass_temp[index] = str(ord(pass_temp[index].upper())-len(pass_temp))
                except:
                    pass_temp[index]=str(loop+index)
        else:
            try:
                int(user_temp[index])
                pass_temp[index] = str(chr(pass_temp[index]+m.floor(len(pass_temp)/2)))
            except:
                try:
                    pass_temp[index] = str(ord(pass_temp[index].lower())-len(pass_temp))
                except:
                    pass_temp[index]=str(loop+index)
        loop +=1
        index+=(m.floor(loop/2)+m.floor(len(pass_temp)/2))

    user_index = 0
    pass_index = 0
    loop = 0
    while pass_index<len(pass_temp) and user_index<len(user_temp):
        if m.floor(len(pass_temp)/2)==0:
            final_encryption+=str(loop)
        elif m.floor(loop%(m.floor(len(pass_temp)/2)))==0:
            final_encryption+=user_temp[user_index]
        else:
            final_encryption+=pass_temp[pass_index]
        user_index+=1
        pass_index+=1
        loop+=1
    

    final_encryption = final_encryption+encrypt(username[1:], password[1:])
    if len(final_encryption)>20:
        final_encryption = final_encryption[0:20]

    return final_encryption

    
