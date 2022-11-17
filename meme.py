
import discord
import random
import emotes


def cute():

    kdictout_cute = [
        "no u, kon! {giggle}",
        "hecc! {ded}",
        "yes and u, kon! {giggle}",
        "me know u are but wat is me, kon? {think}",
        "kek! {lul}"
    ]

    return random.choice(kdictout_cute).format(giggle=emotes.giggle,
                                               ded=emotes.ded,
                                               think=emotes.think,
                                               lul=emotes.lul)


def who_cute(message: discord.Message):

    member_list = message.guild.members
    lucky_winner: discord.Member

    kdictout_who_cute = [
        "u are, kon! {emote}",
        "it u, kon! {emote}",
        "{name} is, kon! {emote}",
        "it {name}, kon! {emote}"
    ]

    while True:
        lucky_winner = random.choice(member_list)

        if lucky_winner.bot:
            continue

        else:
            break

    return random.choice(kdictout_who_cute).format(name=lucky_winner.name,
                                                   emote=emotes.giggle)


def who_small(message: discord.Message):

    member_list = message.guild.members
    lucky_winner: discord.Member

    kdictout_who_cute = [
        "u are, kon! {emote}",
        "it u, kon! {emote}",
        "{name} is, kon! {emote}",
        "it {name}, kon! {emote}",
        "it jazzy, shikaboom! {emote}",
        "u is smol, kon! {emote}"
    ]

    while True:
        lucky_winner = random.choice(member_list)

        if lucky_winner.bot:
            continue

        else:
            break

    return random.choice(kdictout_who_cute).format(name=lucky_winner.name,
                                                   emote=emotes.giggle)


def fortnite():

    kdictout_fortnite = [
        "battle pass {giggle}",
        "battle pass, yea sethie made me say this hecc {ded}",
        "hecc {ded}"
    ]

    return random.choice(kdictout_fortnite).format(giggle=emotes.giggle,
                                                   ded=emotes.ded)


def incredible():

    kdictout_incredible = [
        "https://tenor.com/view/honestly-quite-incredible-drinking-water-underwater-cool-gif-22285702",
        "https://tenor.com/view/honestly-quite-incredible-gif-26151631",
        "https://tenor.com/view/honestly-quite-incredible-shy-guy-mario-falling-honestly-gif-24911137",
        "https://tenor.com/view/floppa-honestly-honestly-quite-incredible-funnyh-cat-gif-26367558",
        "https://tenor.com/view/honestly-quite-incredible-frog-incredible-fascinating-gif-23673132",
        "https://tenor.com/view/honestly-quite-incredible-honestly-bird-funny-bird-gif-25631927",
        "https://tenor.com/view/agree-gif-26233397"
    ]

    return random.choice(kdictout_incredible)


kdictin = [
    [
        "kinari meme cute",
        "kinari ure cute", "kinari, ure cute",
        "kinari u are cute", "kinari, u are cute",
        "kinari u r cute", "kinari, u r cute",
        "ure cute kinari", "ure cute, kinari",
        "u are cute kinari", "u are cute, kinari",
        "u r cute kinari", "u r cute, kinari"
    ],
    [
        "kinari meme who_cute",
        "kinari whos cute", "kinari who's cute", "kinari who cute", "kinari who the cute",
        "kinari, whos cute", "kinari, who's cute", "kinari, who cute", "kinari, who the cute",
        "whos cute kinari", "who's cute kinari", "who cute kinari", "who the cute floof kinari",
        "whos cute, kinari", "who's cute, kinari", "who cute, kinari", "who the cute floof, kinari"
    ],
    [
        "kinari meme jazzy",
        "kinari who is small", "kinari, who is small",
        "kinari who small", "kinari, who small",
        "kinari who is smol", "kinari, who is smol",
        "kinari who smol", "kinari, who smol",
        "who is smol", "who smol",
        "who is small", "who small"
    ],
    [
        "kinari meme fortnite",
        "fortnite"
    ],
    [
        "kinari meme incredible",
        "honestly quite incredible", "hoenstly, quite incredible"
    ]
]

input_cute, input_who_cute, input_who_small, input_fortnite, input_incredible = kdictin
