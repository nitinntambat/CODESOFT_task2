import random
import string

print("====== PASSWORD GENERATOR ======")

# Step 1: Ask user for desired password length
length = int(input("Enter desired password length: "))

# Step 2: Ask user for password complexity
print("\nSelect password complexity:")
print("1. Easy (letters only)")
print("2. Medium (letters + digits)")
print("3. Strong (letters + digits + symbols)")

complexity = input("Enter your choice (1/2/3): ")

# Step 3: Define character sets based on complexity
if complexity == '1':
    characters = string.ascii_letters  # Only uppercase & lowercase letters
elif complexity == '2':
    characters = string.ascii_letters + string.digits  # Letters + digits
elif complexity == '3':
    characters = string.ascii_letters + string.digits + string.punctuation  # Letters + digits + symbols
else:
    print("Invalid choice! Defaulting to Strong password.")
    characters = string.ascii_letters + string.digits + string.punctuation

# Step 4: Generate random password
password = ''.join(random.choices(characters, k=length))

# Step 5: Display the generated password
print("\nGenerated Password:")
print(password)

print("\n====== KEEP IT SAFE! ======")
