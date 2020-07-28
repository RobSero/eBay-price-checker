import smtplib


connection = smtplib.SMTP('smtp.outlook.com', 587)

print(type(connection))

connection.ehlo()

connection.starttls()

print(connection.login('spreadsheetpriceproject@outlook.com', 'testemailsending2020'))

message = """
Subject: SMTP e-mail test

This is a test e-mail message.
"""

connection.sendmail('spreadsheetpriceproject@outlook.com', 'abcd.efvnwosivncd@outlook.com', message )

connection.quit()