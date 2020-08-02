import requests

token = "1382780262:AAHE2aUDgqERju0V1GQhNdLcTj5FYZISDJA"
API_link = f"https://api.telegram.org/bot{token}/"

updates = requests.get(API_link+"getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text = message["text"]

send_message = requests.get(API_link+f"sendMessage?chat_id={chat_id}&text=Sen bylai dedin {text}.")

print(send_message.json())