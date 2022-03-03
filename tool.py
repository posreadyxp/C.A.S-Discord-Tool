from requests import get
from os import rename, system, name
from json import load
import time
import messages
import tools.crash
import tools.info
import tools.spam
import tools.tokens
import tools.webhook


def cls():
    return system("cls") if name == "nt" else system("clear")


def update():
    rename("metadata.json", "metadata_old.json")
    with get(
        "https://raw.githubusercontent.com/posreadyxp/C.A.S-Discord-Tool/tool/metadata.json"
    ) as d:
        with open("metadata.json", "wb") as f:
            f.write(d.content)
    rename("tool.py", "tool_old.py")
    with get(
        "https://raw.githubusercontent.com/posreadyxp/C.A.S-Discord-Tool/tool/tool.py"
    ) as d:
        with open("tool.py", "wb") as f:
            f.write(d.content)
    exit()


# Check Update----------------------------------------------+

updateStatus = ""
updateSoft = ""
currentVersion = ""
dataProject = get(
    "https://raw.githubusercontent.com/posreadyxp/C.A.S-Discord-Tool/tool/metadata.json"
)
version1 = dataProject.json()["Version"]
config = open("metadata.json", "r")
config = load(config)
currentVersion = config["Version"]
if currentVersion < version1:
    a = str(input("New update in tool. Do you like update tool now? (yes/no): "))
    if a == "yes":
        update()
    else:
        updateStatus = "Update the utility using item 18"
        updateSoft = True
else:
    updateStatus = "The utility does not need updating"
    updateSoft = False

# Text, Settings, Info----------------------------------------------+


# Interaction----------------------------------------------+

if __name__ == "__main__":
    while True:
        cls()
        print(messages.start)
        try:
            select = str(input("\nSelect: "))
            if select == "1":
                info = tools.info.Info()
                info.grabInfo()
            elif select == "2":
                token = tools.tokens.TokensTool()
                token.tokenAnnihilation(messages.icon, messages.dMdefaultText)
                # tokenAnnihilation(icon, dMdefaultText)
            elif select == "3":
                webhook = tools.webhook.WebhookTool()
                webhook.Webhook_tool(
                    messages.defaultMessage, 
                    messages.icons, 
                    messages.nameHooks,
                    messages.jsonHook, 
                    messages.statuses
                )
                # Webhook_tool(defaultMessage, icons, nameHooks, jsonHook, statuses)
            elif select == "4":
                token = tools.tokens.TokensTool()
                token.validToken(token=None, for_nuker=False)
                # validToken(token=None, for_nuker=False)
            elif select == "5":
                token = tools.tokens.TokensTool()
                token.joinToken()
                # joinToken()
            elif select == "6":
                token = tools.tokens.TokensTool()
                token.glitch(messages.statusName)
                # glitch(statusName)
            elif select == "7":
                token = tools.tokens.TokensTool()
                token.add()
                # add()
            elif select == "8":
                # leaver()
                token = tools.tokens.TokensTool()
                token.leaver()
            elif select == "9":
                token = tools.spam.Spam()
                token.spam(messages.defaultMessage, messages.defaultMessage2)
                # spam(defaultMessage, defaultMessage2)
            elif select == "10":
                token = tools.tokens.TokensTool()
                token.ownTrans()
                # ovnTrans()
            elif select == "11":
                spam = tools.spam.Spam()
                spam.dmSpam(messages.defaultMessage3)
                # dmSpam(defaultMessage3)
            elif select == "12":
                crash = tools.crash.Crash()
                crash.crash(
                    messages.jsonHook, 
                    messages.defaultMessage, 
                    messages.nameHooks, 
                    messages.icons, 
                    messages.icon, 
                    messages.statuses
                )
                # crash(jsonHook, defaultMessage, nameHooks, icons, icon, statuses)
            elif select == "13":
                card = tools.tokens.TokensTool()
                card.cardGrab(messages.cc_digits)
                # cardGrab(cc_digits)
            elif select == "14":
                anim = tools.tokens.TokensTool()
                anim.animator()
                # animator()
            elif select == "15":
                st = tools.webhook.WebhookTool()
                st.scriptGen()
                # scriptGen()
            elif select == "16":
                nuker = tools.tokens.TokensTool()
                nuker.nuker()
                # nuker()
            elif select == "17":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpsEN)
                elif select == "2":
                    print(messages.helpsRU)
                else:
                    print("\nInvalid option.")
                nextCode = input("\nPress key to continue.")
            elif select == "18":
                print("\nGoodbye!")
                time.sleep(2)
                if updateSoft:
                    update()
                else:
                    exit()
            else:
                print("\nInvalid option.")
                nextCode = input("\nPress key to continue.")
        except KeyboardInterrupt:
            print("\nUse Item 18.")
            time.sleep(3)
