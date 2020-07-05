from telethon.sync import TelegramClient
from telethon.sessions import StringSession

print("""Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details""")

API_KEY = input("1124443")
API_HASH = input("4a5038cc4c4ef047eb78ba1bbf4495f4")

with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
    print("Here is your userbot srting, copy it to a safe place !!")
    print("")
    print(client.session.save())
    print("")
    print("")
    print("Enjoy your userbot !!")
