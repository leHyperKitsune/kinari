
import random
import emotes


def motivate():

    kdictout_motivate = [
        "me gonna give u cuddles, kon! {snuggle}",
        "dont give up, me gotchu! {cuddle}",
        "dont feel down. me believe in u, kon! {excite}",
        "dont be afraid! me is here, kon! {excite}",
        "u super floofy, kon! {giggle}",
        "if u were a fox me will cuddle u, kon! {excite}"
    ]

    return random.choice(kdictout_motivate).format(snuggle=emotes.snuggle,
                                                   cuddle=emotes.cuddle,
                                                   excite=emotes.excite,
                                                   giggle=emotes.giggle)
