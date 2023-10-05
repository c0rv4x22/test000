import os

# Read the value of the secret named 'SECRET_123'
my_secret = os.environ['SECRET_123']

# Use the value of the secret in your code
print(my_secret)
