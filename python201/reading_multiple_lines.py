with open('emails.txt', 'r') as emails:
    emails = emails.readlines() #returns an array of items asked for

for email in emails:
    if "kanchan" in email: #will fetch the email with same keyword 
        print(email.rstrip()) #will print matched email trimming all whitespaces on the right side

for email in emails: 
    if "gmail" in email: #will fetch all gmail domain emails
        print(email.rstrip())


