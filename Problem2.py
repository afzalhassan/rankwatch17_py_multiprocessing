#Problem 2
#Using Multiprocessing library of python send parallel emails to users using
#smtp services like mailgun. Your Script should be able to read emails, subject and message
# from a csv file.

# Hello mam there is a trouble in installing multiprocessing library
# That's why I didn't use multiprocessing else code is working. I am still working on it.



import csv                           # csv is comma separated values I read the data from csv so I import it
import smtplib                       # smtp is a simple mail transporting protocol library wch is used for transporting the mail.
from email.mime.text import MIMEText      #MIMEText class is used to create mime object of major type text.
from email.mime.multipart import MIMEMultipart  # MIMEMultipart is an intermediate baseclass for MIME that are multipart.

SENDER_MAIL = "abcdefghij@gmail.com"        #email-id of sender 
SENDER_PASSWORD = "xxxxxxxxxxxxxx"               #Password of sender

with open('file.csv') as csv_file:                  # opening the file.csv and assign the data in csv_file
    
    csv_reader = csv.reader(csv_file,delimiter=',') #csv_file is in string so I convert it into list for getting the value of each index and it separated by comma
    
    next(csv_reader)                          # because first line contain the heading part so I move to the next line
    
    smtp = smtplib.SMTP('smtp.gmail.com')     # every mail server has their own server I am using gmail. so I used ('mtp.gmail.com') 
    
    smtp.starttls()                         # SMTP connection in TLS (Transport Layer Security) mode. All smtp commands that follow will be encrypted.
    
    smtp.login(SENDER_MAIL, SENDER_PASSWORD)  # smtp.login is used for login from the sender account
    # before executing this u enable your IMAP and less secure app on otherwise login will through error 
    
    
    for row in csv_reader:            # from csv_reader I take row by row data
        
        email, subject, msg = row     # In each row their is specific name , subject and message and it assign sequentially
        
        detail = MIMEMultipart()      # MIMEMultipart contain multipart so all the detail will merge in multipart
        
        detail['From'] = SENDER_MAIL  # 'From' consist sender email address
        
        detail['To'] = email        # 'email' consist where are you sending the email
        
        detail['Subject'] = subject   # 'Subject' is used for adding subject
        
        detail.attach(MIMEText(msg,"plain")) # message is a plain text so it is attach as attach(MIMEText(msg,"plain")) 
        
        text = detail.as_string()  # return entire message as string
        
        #print("send e-mail to: {}".format(email))   
        #print("Subject : {}".format(subject))
        #print("E-mail content:")
        #print(msg)
        
        smtp.sendmail(SENDER_MAIL, email, text)  # sendmail consist argument of sender_mail, reciever_mail, and message 
    
    smtp.quit()  # quit the smtp server
print('finished')