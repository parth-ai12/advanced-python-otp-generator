import random
import time
import pyperclip
from colorama import Fore, Style

print(Fore.GREEN + "🔐 Advanced OTP Generator")
print(Style.RESET_ALL)

length = int(input("Enter OTP length (4 or 6): "))

if length not in [4, 6]:
    print(Fore.RED + "❌ Please enter only 4 or 6")
    print(Style.RESET_ALL)
    exit()

otp = ""

for i in range(length):
    otp += str(random.randint(0, 9))

pyperclip.copy(otp)

print(Fore.CYAN + "Your OTP is:", otp)
print(Fore.YELLOW + "📋 OTP copied to clipboard!")
print(Style.RESET_ALL)

print("⏳ OTP will expire in 10 seconds...")

for i in range(10, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)

print("\n" + Fore.RED + "⚠️ OTP Expired!")
print(Style.RESET_ALL)