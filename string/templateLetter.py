# it type of syntax and for letter 
letter = '''Dear <|NAME|>,
greeting from ABC conding house . I am happy to tell 
you about to you about your selectons 
you are selected !
Have a great day ahead!
Thank and regards ,
Bill
Date: <|DATE|>'''
name = input("Enter your name:\n")
date = input("Enter Date :\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)