import random

def generate(size):
    password=""
    for i in range(size):
        password+=chr(random.randint(21,122))
    return password

print(generate(5))
print(generate(16))

