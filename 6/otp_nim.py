import math, random

# Function to generate OTP
def generateOTP():
    # Declare a string variable
    string = 'Akbar Rahmadani 2141762150'
    
    OTP = ""
    length = len(string)
    
    for i in range(6):
        OTP += string[math.floor(random.random() * length)]
    
    return OTP

# Driver code
if __name__ == "__main__":
    print("OTP of length 6:", generateOTP())
