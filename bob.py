body=f"Hi, {name}, thank you for shopping with Cafe George. Enjoy your order!" # your message body goes here
subject="Your order from Cafe George" # your subject goes here
recipients=[email] # list of your recipients
smtpObj = smtplib.SMTP('smtp.office365.com', 587) # object init
smtpObj.ehlo() # handshake
smtpObj.starttls() # encryption
smtpObj.login('cafe_george@outlook.com', "Messaging1") # also outlook login details
smtpObj.sendmail('cafe_george@outlook.com', recipients, f"Subject: {subject}\n\n{body}") # create & send the email
smtpObj.quit() # terminate session
