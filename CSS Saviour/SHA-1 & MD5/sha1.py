# Python 3 code to demonstrate the 
# working of SHA1 
  
import hashlib
  
# Input string
message = input("Enter the message: ")

# converting to byte
message = message.encode()

# encoding GeeksforGeeks using md5 hash function 
result = hashlib.sha1(message)

# printing the equivalent byte value.
print("\nThe byte equivalent of hash is : ", end ="")
print(result.digest())

# printing the equivalent hex value.
print("\nThe hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())