from fbchat import Client
from fbchat.models import *

message_count = 0
script = []
script2 = []

with open("movie.txt", "r") as movie:
    for line in movie:
        script.append(line.strip().split(" "))
for line in script:
    for x in line:
        script2.append(x)

client = Client("username", "password!")
users = client.fetchAllUsers()
thread_type = ThreadType.USER
thread_id = []
for user in users:
    if user.name == "users name you want to send message to":
        thread_id.append(user.uid)
for _ in range(len(script2)-1):
    client.send(Message(text=f'{script2[message_count]}'), thread_id=int(thread_id[0]), thread_type=thread_type)
    message_count += 1
client.logout()



