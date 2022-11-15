import discord
import random


def koutput(message: discord.Message):
    member_list = message.guild.members
    lucky_winner: discord.Member

    while True:
        lucky_winner = random.choice(member_list)

        if lucky_winner.bot:
            continue

        else:
            break

    return random.choice(koutput_list).format(name=lucky_winner.mention)


kinput = [
    "kinari kdictin who_cute",
    "kinari whos cute", "kinari who's cute", "kinari who cute", "kinari who the cute",
    "kinari, whos cute", "kinari, who's cute", "kinari, who cute", "kinari, who the cute",
    "whos cute kinari", "who's cute kinari", "who cute kinari", "who the cute floof kinari",
    "whos cute, kinari", "who's cute, kinari", "who cute, kinari", "who the cute floof, kinari"
]


koutput_list = [
    "u are, kon!", "it u, kon!", "u",
    "{name} is, kon!", "it {name}, kon!"
]
