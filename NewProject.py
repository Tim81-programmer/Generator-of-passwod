import secrets
import string
example=input("Напиши вигадиний пароль щоб я міг тобі допомогти його покращити або зробити більш захищеним:")
characters=string.ascii_lowercase + string.digits
if any(char.isupper() for char in example):
    characters += string.ascii_uppercase
if any(not char.isalnum() for char in example):
    characters += string.punctuation
lenght=max(16,len(example))
password ="" 
for i in range(lenght):
    password += secrets.choice(characters)
print("Ось твій надійний пароль:", password)




