import random
from threading import Thread

import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your custom status'))
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

    # command to log dms the bot recives in a specific channel
    if isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
        guild = bot.get_guild(guild id) # replace with guild id
        channel = discord.utils.get(guild.text_channels, name='name')# replace with channel name
        await channel.send(f'DM from: {message.author.name} id {message.author.id}\nContent: {message.content}')

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)


@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')
    else:
        await ctx.send("You don't have permission to kick members.")


@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')
    else:
        await ctx.send("You don't have permission to ban members.")


@bot.command()
async def clear(ctx, amount=5):
    if ctx.author.guild_permissions.manage_messages:
        if amount > 100:
            await ctx.send("You can only clear up to 100 messages at a time.")
        else:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f'{amount} messages cleared.')
    else:
        await ctx.send("You don't have permission to clear messages.")



@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"The coin landed on {result}!")


@bot.command()
async def diceroll(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f"The dice rolled a {roll}!")


@bot.command()
async def randomnumber(ctx, min_value=1, max_value=100):
    result = random.randint(min_value, max_value)
    await ctx.send(f"Your random number is {result}!")


@bot.command()
async def magic8ball(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
                 "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                 "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    response = random.choice(responses)
    await ctx.send(f"Question: {question}\nAnswer: {response}")


@bot.command()
async def joke(ctx):
    jokes = [
    "add jokes here", "seperated by a comma"
   ]
    await ctx.send(random.choice(jokes))


@bot.command()
async def riddle(ctx):
    riddles = [
  {"q": "add riddles here question in q ", "a": "and answer in a"},
    ]
    riddle = random.choice(riddles)
    await ctx.send(f"Riddle: {riddle['q']}\nAnswer: {riddle['a']}")


@bot.command()
async def fortune(ctx):
    fortunes = [
      "Add fortunes here",
      "seperated by a comma",
    ]
    await ctx.send(random.choice(fortunes) )




@bot.command()
async def commands(ctx):
    commands = """
   commands:

   
   **moderation**
   !kick: Kick a member from the server
   !ban: Ban a member from the server
   !clear: Clear a specified number of messages

   
   **utility**
   !ping: Check the latency of the bot
   !commands: Display the list of available commands


   **fun**
   !coinflip: Simulate a coin flip
   !diceroll: Simulate a dice roll
   !randomnumber: Generate a random number between 1 and 100
   !magic8ball: Ask the magic 8 ball a question 
   !fortune: Display a fortune cookie
   !joke: random joke
   !riddle: a riddle
   
   """
    await ctx.send(commands)


bot.run("your bot token") #replace with your bot token