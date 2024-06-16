import random
import string

def password_generator(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")
   
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    punctuation=string.punctuation
    
    password=[
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    
    characters=lowercase+uppercase+digits+punctuation
    password+=[random.choice(characters) for _ in range(length - 4)]
    
    random.shuffle(password)
    
    return ''.join(password)

password_length=int(input("Enter the length:"))
print("Generated password:",password_generator(password_length))

