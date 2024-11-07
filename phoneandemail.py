import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 #user name
    @
    [a-zA-Z]+
    \.
    [a-z]{2,}                 
    )''',re.VERBOSE)

# This is also working
# emailRegex = re.compile(r'''(
#     (\w{1,})+                         #email-name
#     (\@)+                             #at the rate
#     (\w{1,})+                         #company
#     (\.)
#     (\w{2,3})                         #domain
#     )''',re.VERBOSE)

# a = (emailRegex.findall('This is my email id test123@gmail.com, and this is my another email id nowHere@yahoo.in'))
# print(a)

text = pyperclip.paste().strip()


if not text:
    print("Clipboard is empty. Please copy some text with phone numbers or email addresses.")
else:
    # Find matches in the clipboard text
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups)

    # Display or copy matches to clipboard
    if matches:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')