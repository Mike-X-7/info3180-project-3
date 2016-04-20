import smtplib

def sendemail(toname,toemail,fromsubject,msg):
    fromname = 'Wishlist' 
    fromemail  = 'likemike303@gmail.com'
    message = """From: {} <{}>\nTo: {} <{}>\nSubject: {}\n\n{}"""
    
    messagetosend = message.format(
                                 fromname,
                                 fromemail,
                                 toname,
                                 toemail,
                                 fromsubject,
                                 msg)
    
    # Use your own credentials (if needed)
    username = 'likemike303@gmail.com'
    password = '   '
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromemail, toemail, messagetosend)
    server.quit()
    return