import math
import random

# Function to generate OTP
def generateOTP():
    # Declare a digits variable which stores all digits
    digits = "0123456789"
    OTP = ""

    # Length of OTP can be changed by changing the range value
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    
    return OTP

# Driver code
if __name__ == "__main__":
    print("OTP of 4 digits:", generateOTP())
