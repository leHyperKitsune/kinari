
# thingies from pip or watever
import discord
import random

# thingies from here
import thingy
import meme
from general import kon, hi, hru, gm, ga, ge, gn, ty, np, kinari
from support import sad
from random_tools import coin, d20, dice, fortune, le8ball, truth
from emotion import compliment

# thx discord for making this hecc hard
intent = discord.Intents.default()
intent.members = True
intent.message_content = True

client = discord.Client(intents=intent)


@client.event
async def on_ready():
    print(f"🌾 kon! me aka {client.user} is on the server, kon!")


@client.event
# le join message, kon!
async def on_member_join(member: discord.Member):
    channel = client.get_channel(thingy.bubble_welcome)

    if channel.guild != member.guild:
        return

    join_output = [
      f"kon! welcome {member.mention} to the hyper bubble! everyone say hi to them, kon!",
      f"kon! {member.mention} has crashed to the bubble! come and say hi, kon!"
    ]
    await channel.send(random.choice(join_output))


@client.event
# on leave message, kon!
async def on_member_remove(member: discord.Member):
    channel = client.get_channel(thingy.bubble_welcome)

    if channel.guild != member.guild:
        return

    leave_output = [
      f"kon! {member.mention} has figured out the way out the bubble! safe travels, kon!",
      f"kon! me might have accidentally popped {member.mention} out of the bubble, hecc!"
    ]
    await channel.send(random.choice(leave_output))

# me gonna make this a daily kon! thingy so kinari can yip every midnight, kon!


@client.event
# yes this is for kinari's brain me gonna make konmand thingies, kon!
async def on_message(message: discord.Message):

    kinari_input = message.content.lower()

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    guild = str(message.guild)

    print(f'🌾 {username} said: "{user_message}" in {guild}: {channel}, kon!')

    if message.author == client.user or message.author.bot:
        return

    # general thingies ----------------------------------
    if any(word in kinari_input for word in tuple(kon.input)):
        await message.channel.send(random.choice(kon.output))
        return

    if any(word in kinari_input for word in tuple(hi.input)):
        await message.channel.send(random.choice(hi.output))
        return

    if any(word in kinari_input for word in tuple(hru.input)):
        await message.channel.send(random.choice(hru.output))
        return

    if any(word in kinari_input for word in tuple(gm.input)):
        await message.channel.send(random.choice(gm.output))
        return

    if any(word in kinari_input for word in tuple(ga.input)):
        await message.channel.send(random.choice(ga.output))
        return

    if any(word in kinari_input for word in tuple(ge.input)):
        await message.channel.send(random.choice(ge.output))
        return

    if any(word in kinari_input for word in tuple(gn.input)):
        await message.channel.send(random.choice(gn.output))
        return

    if any(word in kinari_input for word in tuple(ty.input)):
        await message.channel.send(random.choice(np.output))
        return

    if kinari_input == "kinari" or kinari_input == "きなり" or kinari_input == "キナリ":
        await message.channel.send(random.choice(kinari.output))
        return
    # support thingies -------------------------------
    if any(word in kinari_input for word in tuple(sad.input)):
        await message.channel.send(random.choice(sad.output))
        return

    # random tools -----------------------------------
    if any(word in kinari_input for word in tuple(coin.input)):
        await message.channel.send(random.choice(coin.output))
        return

    if any(word in kinari_input for word in tuple(d20.input)):
        await message.channel.send(random.choice(d20.output))
        return

    if any(word in kinari_input for word in tuple(dice.input)):
        await message.channel.send(random.choice(dice.output))
        return

    if any(word in kinari_input for word in tuple(fortune.input)):
        await message.channel.send(random.choice(fortune.output))
        return

    if any(word in kinari_input for word in tuple(le8ball.input)):
        await message.channel.send(random.choice(le8ball.output))
        return

    if any(word in kinari_input for word in tuple(truth.input)):
        await message.channel.send(random.choice(truth.output))
        return

    # emotional thingies ----------------------------------------
    if any(word in kinari_input for word in tuple(compliment.input1)):
        await message.channel.send(random.choice(ty.output))
        return

    # meme thingies ----------------------------------------------
    if any(word in kinari_input for word in meme.input_cute):
        await message.channel.send(meme.cute())
        return

    if any(word in kinari_input for word in meme.input_who_cute):
        await message.channel.send(meme.who_cute(message))
        return

    if any(word in kinari_input for word in meme.input_fortnite):
        await message.channel.send(meme.fortnite())
        return

    if any(word in kinari_input for word in meme.input_who_small):
        await message.channel.send(meme.who_small(message))
        return

    if any(word in kinari_input for word in meme.input_incredible):
        await message.channel.send(meme.incredible())
        return


token = thingy.kinari_token
client.run(token)
