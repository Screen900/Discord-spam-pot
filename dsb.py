import requests
import time
import sys
import pyfiglet
from colorama import init, Fore, Back
import os

# تهيئة colorama للعمل على جميع الأنظمة
init(autoreset=True)

# مسح الشاشة قبل بدء البرنامج
os.system("clear")  # لمسح الشاشة في Termux أو أي بيئة طرفية

# وضع التوكن الخاص بك هنا
token = "MTMxNTg3ODE2NTgwOTMzNjM2MA.GmXiiP.3JT1z7EFtpehARHWqIVOUqeuaDsuBVvww1d4ao"

# دالة للتحقق من المدخلات الصحيحة
def get_valid_number():
    while True:
        try:
            value = input(Fore.GREEN + "Please enter a number: ")
            number = int(value)
            return number
        except ValueError:
            print(Fore.RED + "Error: Invalid input. Please enter a valid number.")

# دالة لإرسال الرسائل إلى الروم أو المستخدم
def send_messages_to_channel(channel_url, message, count):
    try:
        parts = channel_url.split("/")
        channel_id = parts[-1]
    except IndexError:
        print(Fore.RED + "Invalid URL format. Please enter a valid channel URL.")
        return

    api_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": message
    }

    for i in range(count):
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"✔️ Message {i+1} sent successfully!")
        else:
            print(Fore.RED + f"❌ Failed to send message {i+1}: {response.status_code}, {response.text}")
        time.sleep(0.3)

# دالة لإرسال الرسائل إلى المستخدم
def send_messages_to_user(user_id, message, count):
    api_url = f"https://discord.com/api/v9/users/{user_id}/messages"
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": message
    }

    for i in range(count):
        response = requests.post(api_url, headers=headers, json=payload)
        if response.status_code == 200:
            print(Fore.GREEN + f"✔️ Message {i+1} sent successfully!")
        else:
            print(Fore.RED + f"❌ Failed to send message {i+1}: {response.status_code}, {response.text}")
        time.sleep(0.3)

# عرض الخيارات للمستخدم
def main():
    # عرض العنوان باستخدام pyfiglet
    title = pyfiglet.figlet_format("DSB", font="slant")
    print(Fore.YELLOW + title)
    print(Fore.YELLOW + "by Screen\n")
    
    print(Fore.CYAN + "-"*50)
    print(Fore.YELLOW + "Welcome to the Message Spammer Tool! Choose an option to proceed.\n")
    
    print(Fore.GREEN + """
    [1] Spam a number of messages to a user
    [2] Spam messages to a channel
    """)

    choice = input(Fore.GREEN + "Please choose an option (1 or 2): ")

    print(Fore.CYAN + "-"*50)

    if choice == '1':
        user_id = input(Fore.GREEN + "Enter the User ID to send messages to: ")
        message = input(Fore.GREEN + "Enter the message to send: ")
        count = get_valid_number()
        send_messages_to_user(user_id, message, count)

    elif choice == '2':
        channel_url = input(Fore.GREEN + "Enter the channel URL: ")
        message = input(Fore.GREEN + "Enter the message to send: ")
        count = get_valid_number()
        send_messages_to_channel(channel_url, message, count)

    else:
        print(Fore.RED + "❌ Invalid choice. Please choose option 1 or 2.")
        sys.exit()

if __name__ == "__main__":
    main()
