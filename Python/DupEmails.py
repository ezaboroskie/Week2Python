with open("emails.txt") as file:
   emails=file.read()

print(emails)

duplicate_emails=emails.split(',')
print(duplicate_emails)

duplicate_free_emails =[]

for email in duplicate_emails:
    email=email.strip() #removes empty space
    if email not in duplicate_emails:
        duplicate_free_emails.append(email)

with open("duplicate_free_emails.txt" , "w") as file:
    for email in duplicate_free_emails:
        file.write(email)
        file.write("\n")