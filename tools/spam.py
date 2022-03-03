# from messages import (
    # exitMenu, 
    # spamessagesenu,
    # modeMenu,
    # statuses,
    # menu,
    # helpSpamEN,
    # helpSpamRU,
    # dmSpamessagesenu,
    # helpdmSpamessagesEN,
    # helpdmSpamessagesRU
    # )
from threading import Thread
import messages
from datetime import datetime
from requests import get, post

class Spam:
    def __init__(self) -> None:
        """
        Initialization
        """
        pass

    def m_spam(self, channels, tokenSH, messages1, messages2, errorLog):
        for channelID in channels:
            for token in tokenSH:
                req = post(
                    f"https://discord.com/api/v9/channels/{channelID}/messages",
                    json={"content": messages1},
                    headers={"Authorization": token},
                )
                if req.status_code in messages.statuses:
                    req = post(
                        f"https://discord.com/api/v9/channels/{channelID}/messages",
                        json={"content": messages2},
                        headers={"Authorization": token},
                    )
                    if req.status_code not in messages.statuses:
                        errorLog.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                        )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )

    def spam(self, defaultMessage, defaultMessage2):
        sessionName = "Server spam"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.spamMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                channelID = input("\nChannel ID: ")
                print(messages.modeMenu)
                mode = input("\nSelect: ")
                if mode == "1":
                    messages1 = input("\nMessage [1]: ")
                    messages2 = input("\nMessage [2]: ")
                else:
                    messages1 = defaultMessage
                    messages2 = defaultMessage2
                print("\nSpam started.")
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                    while True:
                        # data = any(tokens)
                        if any(tokens):
                            for x in tokens:
                                token = x.rstrip()
                                req = post(
                                    f"https://discord.com/api/v9/channels/{channelID}/messages",
                                    json={"content": messages1},
                                    headers={"Authorization": token},
                                )
                                if req.status_code in messages.statuses:
                                    req = post(
                                        f"https://discord.com/api/v9/channels/{channelID}/messages",
                                        json={"content": messages2},
                                        headers={"Authorization": token},
                                    )
                                    if req.status_code not in messages.statuses:
                                        errorLog.write(
                                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                        )
                                else:
                                    errorLog.write(
                                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                    )
                        else:
                            print("\nNo tokens.")
            elif select == "2":
                serverID = input("\nServer ID: ")
                print(messages.modeMenu)
                mode = input("\nSelect: ")
                if mode == "1":
                    messages1 = input("\nMessage [1]: ")
                    messages2 = input("\nMessage [2]: ")
                else:
                    messages1 = defaultMessage
                    messages2 = defaultMessage2
                print("\nSpam started.")
                channels = []
                tokenSH = []
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                    for x in tokens:
                        token = x.rstrip()
                        tokenSH.append(token)
                    # data1 = any(tokenSH)
                    if any(tokenSH):
                        request = get(
                            f"https://discord.com/api/v9/guilds/{serverID}/channels",
                            headers={"Authorization": tokenSH[0]},
                        )
                        if request.status_code == 200:
                            for channel in request.json():
                                if channel["type"] == 0:
                                    channels.append(channel["id"])
                        else:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                            )
                        # data2 = any(channels)
                        if any(channels):
                            while True:
                                for _ in len(tokenSH):
                                    my_thread = Thread(target=self.m_spam, args=(channels, tokenSH, messages1, messages2, errorLog,))
                                    my_thread.start()
            elif select == "3":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpSpamEN)
                elif select == "2":
                    print(messages.helpSpamRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nIvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def dmSpam(self, defaultMessage3):
        sessionName = "DM spam"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.dmSpamMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                data = {}
                userId = input("\nUser ID: ")
                payload = {"recipient_id": userId}
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                    # data2 = any(tokens)
                    if any(tokens):
                        for x in tokens:
                            token = x.rstrip()
                            req = post(
                                "https://canary.discord.com/api/v8/users/@me/channels",
                                headers={"Authorization": token},
                                json=payload,
                            )
                            if req.status_code in messages.statuses:
                                dm = req.json()
                                data[token] = dm["id"]
                            else:
                                errorLog.write(
                                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                )
                print(messages.modeMenu)
                mode = input("\nSelect: ")
                if mode == "1":
                    message = input("\nMessage: ")
                else:
                    message = defaultMessage3
                dmPayload = {"content": message, "tts": False}
                print("\nSpam started.")
                while True:
                    for token, dmId in data.items():
                        req = post(
                            f"https://canary.discord.com/api/v8/channels/{dmId}/messages",
                            headers={"Authorization": token},
                            json=dmPayload,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "2":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpdmSpamessagesEN)
                elif select == "2":
                    print(messages.helpdmSpamessagesRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

