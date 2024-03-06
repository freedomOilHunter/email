import smtplib
body=f"eat" # your message body goes here
subject="Your order from Cafe George" # your subject goes here
recipients=["21gbower@kes.net"] # list of your recipients
smtpObj = smtplib.SMTP('smtp.office365.com', 587) # object init
smtpObj.ehlo() # handshake
smtpObj.starttls() # encryption
smtpObj.sendmail('21rhall@kes.net', recipients, f"Subject: {subject}\n\n{body}") # create & send the email
smtpObj.quit() # terminate session
