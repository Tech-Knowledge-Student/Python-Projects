import string
import random

pass_len = 8

'''
choice_list = []
password = ""

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punct = string.punctuation

for each in (lower+upper+digits+punct) :
  choice_list.append(each)

password = "".join([random.choice(choice_list) for i in range(pass_len)])

#for i in range(pass_len) :
  #char = random.choice(choice_list)
  password += char

print("Your Password: ", password)
'''

password = ""

letters = string.ascii_letters
digits = string.digits
punct = string.punctuation

choice_string = letters + digits + punct

password = "".join([random.choice(choice_string) for i in range(pass_len)])

#for i in range(pass_len) :
  #password += random.choice(choice_string)

print("Password : ", password)