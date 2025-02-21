

#returns on a scale of 1 - 5 how strong the password is, 1 weakest, 5 strongest
def check_password(password):
    common_passwords = ["password", "123456", "qwerty","abc123"] # Could access database of most common passwords
    if password in common_passwords:
        return 1
    strength = 1
    #makes sure password has at least 8 characters
    if len(password) > 7:
        strength +=1

    #checks for uppercase letters
    if password.lower() is not password:
        strength += 1
    
    #checks for number
    for c in password:
        if c.isdigit():
            strength +=1
            break

    #checks for special characters
    symbols = "!@#$%^&*(){}[]?"
    for c in password:
        if c in symbols:
            strength += 1
            break
    
    return strength
    
password = input("enter a password to be analyzed!")

print(f"your password: {password} is on a scale of 1-5 (5 is strongest) at a strength of: " + check_password(password))
