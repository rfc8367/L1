def mail_hider():
    user_string = str(input('Enter E-Mail Address:' ))
    hider = user_string[:3] + '**@**' + user_string[-5:]
    return hider

print(mail_hider())