# -------------------------------------------------
# IMPORTS
# -------------------------------------------------
import ceasar as cs

# -------------------------------------------------
# CREATIVE CONSOLE STYLES
# -------------------------------------------------

# FOREGROUND (text) colour escape codes
k = "\033[30m"  # black
r = "\033[31m"  # red
g = "\033[32m"  # green
y = "\033[33m"  # yellow
b = "\033[34m"  # blue
p = "\033[35m"  # purple
c = "\033[36m"  # cyan
w = "\033[37m"  # white
reset = "\033[0m"  # reset text back to normal

# BACKGROUND colour escape codes
kb = "\033[40m"  # black
rb = "\033[41m"  # red
gb = "\033[42m"  # green
yb = "\033[43m"  # yellow
bb = "\033[44m"  # blue
pb = "\033[45m"  # purple
cb = "\033[46m"  # cyan
wb = "\033[47m"  # white

# escape codes for styles
bold = "\033[1m"
faint = "\033[2m"
underline = "\033[4m"
invert = "\033[7m"
reset = "\033[0m"  # reset text back to normal

# ===========================================================
# 🕵️ CHECKPOINT 9 PROJECT - SECRET AGENT CIPHER
# ===========================================================


# -------------------------------------------------
# PART A - TESTING A FUNCTION THAT SHIFTS LETTERS
# -------------------------------------------------

new_letter= cs.shift_letter("D",26)
print(new_letter)
# -------------------------------------------------
# PART B - ENCODING AND DECODING FUNCTIONS
# -------------------------------------------------

# get a string of all the upper case letters
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode(message, key):
    encrypted_message = ""
    message = message.upper()
    for i in message:
        if i in LETTERS:
            new_letter = cs.shift_letter(i,key)
        else:
            new_letter= i
        encrypted_message= encrypted_message + new_letter
       
    # 🧑‍💻 YOUR CODE HERE
    print(f"\nYour encrypted message is:{g}{encrypted_message}{reset}")


def decode(message, key):
    decrypted_message =""
    message= message.upper()
    for i in message:
        if i in LETTERS:
            decoded_letter= cs.shift_letter(i,-key)
        else:
            decoded_letter=i
        decrypted_message= decrypted_message+decoded_letter
    # 🧑‍💻 YOUR CODE HERE
    print(f"\nYour decrypted message is:{g}{decrypted_message.lower()}{reset}")

heading = r"""
 ________  _______   ________  ________  _______  _________        
|\   ____\|\  ___ \ |\   ____\|\   __  \|\  ___ \|\___   ___\      
\ \  \___|\ \   __/|\ \  \___|\ \  \|\  \ \   __/\|___ \  \_|      
 \ \_____  \ \  \_|/_\ \  \    \ \   _  _\ \  \_|/__  \ \  \       
  \|____|\  \ \  \_|\ \ \  \____\ \  \\  \\ \  \_|\ \  \ \  \      
    ____\_\  \ \_______\ \_______\ \__\\ _\\ \_______\  \ \__\     
   |\_________\|_______|\|_______|\|__|\|__|\|_______|   \|__|     
   \|_________|                                                    


 ________  ________  _______   ________   _________  ________      
|\   __  \|\   ____\|\  ___ \ |\   ___  \|\___   ___\\   ____\     
\ \  \|\  \ \  \___|\ \   __/|\ \  \\ \  \|___ \  \_\ \  \___|_    
 \ \   __  \ \  \  __\ \  \_|/_\ \  \\ \  \   \ \  \ \ \_____  \   
  \ \  \ \  \ \  \|\  \ \  \_|\ \ \  \\ \  \   \ \  \ \|____|\  \  
   \ \__\ \__\ \_______\ \_______\ \__\\ \__\   \ \__\  ____\_\  \ 
    \|__|\|__|\|_______|\|_______|\|__| \|__|    \|__| |\_________\
                                                       \|_________|
"""

def call_encode():
    print("\nType in the message you would want to encode.")
    encode_message = input("🤖Message:")
    print("\nChoose a secret key (an integer) to use to encode your message.")
    encode_key = int(input("🔑Key:"))
    encode(encode_message,encode_key)
    
def call_decode():
    print("\nType in the message you would want to Decode.")
    decode_message= input("🤖Message:")
    print("\nChoose a secret key (an integer) to use to DECODE your message.")
    decode_key= int(input("🔑Key:"))
    decode(decode_message,decode_key)



    
print(f"{g}{bold}{heading}{reset}")
print("Hello! Welcome to Secret Agents!\nThis is a python program which allows you to decode and encode your own messages!\nThis program works similar to the Caesar Cipher!\n\n  ")
print("-----------OPTIONS:----------\t\n\n🔒 1 to encode a message\n🔓 2 to decode a message\n🔏 q to quit\n\n----------------------------")
user_choice = input("\nEnter your choice here:")
if user_choice == "1":
    call_encode()
elif user_choice =="2":
    call_decode()
elif user_choice.lower()=="q":
    print("Thanks for visiting! See you next time!")
else:
    print("Invalid Input....\nThis program has stop running due to security issues...")


#  TEST CASE




# -------------------------------------------------
# 🚀 PART C - BONUS FEATURES
# -------------------------------------------------
