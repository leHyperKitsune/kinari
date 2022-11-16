import discord
import random


def who_cute(message: discord.Message):
    member_list = message.guild.members
    lucky_winner: discord.Member

    while True:
        lucky_winner = random.choice(member_list)

        if lucky_winner.bot:
            continue

        else:
            break

    return random.choice(kdictout_who_cute).format(name=lucky_winner.name)


kdictin_who_cute = [
    "kinari kdictin who_cute",
    "kinari whos cute", "kinari who's cute", "kinari who cute", "kinari who the cute",
    "kinari, whos cute", "kinari, who's cute", "kinari, who cute", "kinari, who the cute",
    "whos cute kinari", "who's cute kinari", "who cute kinari", "who the cute floof kinari",
    "whos cute, kinari", "who's cute, kinari", "who cute, kinari", "who the cute floof, kinari"
]


kdictout_who_cute = [
    "u are, kon! <:thingy:1036519788106743808>", "it u, kon! <:thingy:1036519788106743808>",
    "{name} is, kon! <:thingy:1036519788106743808>", "it {name}, kon! <:thingy:1036519788106743808>"
]
