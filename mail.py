import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
jojo= 'codingbird1@gmail.com'
ko= '1qazZXCV'
from_add =jojo
bob= ['codingbird2018@gmail.com', 'S0410330@gmail.com']  
Subject = "Hi"
contents = "poiuytrewqlkjhgfdsamnbvcxz"
mail = MIMEMultipart()
mail['From'] =jojo
mail['To'] = ', '.join(bob)
mail['Subject'] = Subject
mail.attach(MIMEText(contents))  
smtpserver = smtplib.SMTP_SSL("smtp.gmail.com", 465)
smtpserver.ehlo()
smtpserver.login(jojo,ko)
smtpserver.sendmail(jojo, bob, mail.as_string())
smtpserver.quit()


#