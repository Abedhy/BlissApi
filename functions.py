import random
# random is used to generate numbers and make random selections 
def generate_random_digits(length=6):
# ''.join() it concatinates the random string to a single string
    digits = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return str(digits)


import re

def check_phone_number(phone_number):
    pattern = r'^\+254\d{9}$'
    # ^ it asserts the start of the string
    # \+254 it matches the literal string +254
    # \d{9} matches exactly 9 digits
    # $ it shows the end of the string
    if re.match(pattern, phone_number):
        print("phone_number is correct")
        return True
    else:
        print("phone number is incorrect format")
        return False

# check password validity
import re
def check_password(password):
    if len(password) < 8:
        return ("password must be 8 characters")
    elif not re.search("[A-Z]", password ):
        return ("Password must have 1 uppercase")
    elif not re.search("[a-z]", password):
        return ("Password must have 1 lowercase")
    elif not re.search("[0-9]", password):
        return ("password must contain atleast a number")
    elif not re.search("[_@$]", password):
        return ("password must contain atleast a special character")
    else:
        return True
# check_password(input("Enter your password"))
    

# sending an sms 
import africastalking
africastalking.initialize(
username="joe2022",
api_key="aab3047eb9ccfb3973f928d4ebdead9e60beb936b4d2838f7725c9cc165f0c8a"
)
sms = africastalking.SMS
def send_sms(phone, message):
    recepients= [phone]
    sender = "AFRICASTALKING"
    try:
        response = sms.send(message, recepients)
        return (response)
    except:
        return ("An error occured")

send_sms("+254757821060", "Thank you for registering Bliss hospital")
    
# hash password
import bcrypt
#bcrypt is a module for hashing and checking password 
# it is very secure
def hash_password(password):
    #we encode password into bytes
    #it is neccesary beecause bcrypt library works well with byte data
    bytes = password.encode("utf-8")
    #print(bytes)
    #using a unique salt for each user password ensures even if two users have same password,
    #their hashed password will be different i.e
    salt = bcrypt.gensalt()
    #print(salt)
    hash = bcrypt.hashpw(bytes, salt)
    #print(hash.decode())
    return hash.decode()
#hash_password(input("Enter your password:"))

#function to verify password
#$2b$12$XQncdTYXm7lX3Re9t9kc/OgoWlaf0FLWDVfzXoimIwYZ7Jiqam8G6
# def hash_verify(password, hashed_password):
#     bytes = password.encode("utf-8")
#     result =bcrypt.checkpw(bytes, hashed_password.decode("utf-8"))
#     #print(result)
#     return result
def hash_verify(password, hashed_password):
    # Ensure password is bytes
    if isinstance(password, str):
        password = password.encode('utf-8')
    
    # Ensure hashed_password is bytes
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode('utf-8')

    result = bcrypt.checkpw(password, hashed_password)
    return result
# hash_verify("1234", '$2b$12$XQncdTYXm7lX3Re9t9kc/OgoWlaf0FLWDVfzXoimIwYZ7Jiqam8G6')

#encrypting data
#denmark
#we import fernet class
# the module is used for encryption and decryption
from cryptography.fernet import Fernet
def gen_key():
    #function to generate a new encryption KeyboardInterrupt
    key = Fernet.generate_key()
    #print(key)
    with open("key.key","wb") as key_file:
        key_file.write(key)
        #with open - it opens a new file if it exists
        #creates a new file if it doesnt exist
        #wb= write binnary ensures the file is properly closed after writing on it

#gen_key()


# Assighnment
# 1 function to laod key
def load_key():
    return open("key.key", "rb").read()
# load_key()

#encrypt data
def encrypt(data):
    #load the key first and put in a variable
    key = load_key()
    #print(key)
    f = Fernet(key)
    #print(f)
    #this f becomes an object for encryption
    encrypt_data = f.encrypt(data.encode())
    # print(encrypt_data.decode())
    return (encrypt_data.decode())


# encrypt(input("enter your data:"))
 
 #decrypt data
#def decrypt(encrypted_data):
    #load the key
    #key = load_key
    # f object
    #f=Fernet(key)
    #decrypt_data = f.decrypt(encrypted_data.encode())
def decrypt(encrypted_data):
    # Load the key
    key = load_key()
    # Initialize Fernet with the loaded key
    f = Fernet(key)
    # Decrypt the data
    decrypted_data = f.decrypt(encrypted_data.encode())
    # Return the decrypted data as a string
    #return decrypted_data.decode()
    #print(decrypted_data)
    return decrypt_data.decode()
#decrypt("gAAAAABmi8vt6B-6mJGdpFnoYWwKsHYkI6W3ucX16dO0DdVIfzyFG9eIm7au39j1DBF8RDsay04uumdHgnaMLZHTJthWVcmFtA==")






import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

def stk_push(phone, amount, invoice_no):
    # GENERATING THE ACCESS TOKEN
    # create an account on safaricom daraja, here you are provided with below Credentials (Consumer Key and Secret Key)
    # For testing Purposes we use MODCOM Credentials
    consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
    consumer_secret = "amFbAoUByPV2rM5A"

    # Pass Consumer and Secret Key to Mpesa URL
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials" # AUTH URL
    data = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret)).json()

    # We get access token from data above - To be used Later
    access_token = data['access_token']

    # GETTING THE PASSWORD
    timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    business_short_code = "174379"
    # Combine the above 3 variables into single variable called "dats"
    data = business_short_code + passkey + timestamp
    # We encode data into base64(ASCII)
    encoded = base64.b64encode(data.encode())
    # Decode with utf-8
    # This might be useful if you need to pass this string as a parameter in an API request
    # Its a requirement by Safaricom to be in UTF-8(web)
    password = encoded.decode('utf-8')
    print(password)

    # BODY OR PAYLOAD
    payload = {
    "BusinessShortCode": "174379",
    "Password": "{}".format(password),
    "Timestamp": "{}".format(timestamp),
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount, # use 1 when testing
    "PartyA": phone, # change to your number
    "PartyB": "174379",
    "PhoneNumber": phone,
    "CallBackURL": "https://modcom.co.ke/job/confirmation.php",
    "AccountReference": "account",
    "TransactionDesc": "account"
    }

    # POPULATING THE HTTP HEADER
    # Headers carry the access token and content type
    # JSON is the format of data
    headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
    }

    # SPECIFY SAFARICOM URL
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" # C2B URL

    # Finally, using requests, we post payload and headers to above url
    # Below code will automatically send a SIM TOOLKIT(stk) push to your phone

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
