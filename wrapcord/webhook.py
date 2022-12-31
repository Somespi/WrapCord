import requests
import json 
class Webhook:
    def __init__(self, webhook_url: str):
        webhook_url = webhook_url.replace(" ", "")
        if webhook_url.startswith("https://discord.com/api/webhooks/"):
            self.token = webhook_url
        else:
            raise ValueError("Looks like webhook_url is not a valid webhook URL")
    def send_message(self, content=None, username=None, avatar_url: str = None, tts: bool = False, files=None, embeds=None, allowed_mentions=None):
        dataSend: dict = {}
        if content is None and files is None and embeds is None:
            raise ValueError("Cannot send an empty message.")
        else:
            datas: tuple = [content, username,avatar_url, tts, embeds, allowed_mentions]
            dats: list = ["content", "username", "avatar_url","tts", "embeds", "allowed_mentions"]
            for i in datas:
                index = datas.index(i)
                if i is not None:
                    dataSend[f"{dats[index]}"] = i
            if files is not None:
                return requests.post(self.token, {"payload_json": json.dumps(dataSend)}, files=files)
            else:
                return requests.post(self.token, json.dumps(dataSend), headers={"Content-Type": "application/json"})

