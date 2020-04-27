from flask_bcrypt import Bcrypt

bycrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bycrypt.generate_password_hash(password=password)

print(hashed_password)

check = bycrypt.check_password_hash(hashed_password,"supersecretsdfspassword")
print(check)
