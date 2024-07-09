from application import Message
import pandas as pd

Message.acess_browser()
Message.login_gmail()

date = pd.read_csv('table.csv') # Data table path

for line in date.index:
    name = date.loc[line, "Name"]
    gmail = date.loc[line, "Gmail"]
    subject = date.loc[line, "Subject"] # If the user wants to put the same subject for all contacts, this line of code should be replaced by this:
    #subject = "Email Subject"
    body = date.loc[line, "Body"] #If the user wants to put the same text for all contacts, you should replace this line of code with this:
    #body = """Email Text"""
    Message.creating_gmail(name, gmail, subject, body)

Message.end_submission()
print("Program Finished")
