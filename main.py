import json
import random
from threading import Thread
import asyncio
from random import choices
import discord
from discord import *
from discord.ext import commands



def get_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config



config = get_config('config.json')
token = config.get('bot_token')
guild_id_config = config.get('guild_id')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# error handling for wrong commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found, use !commands for info")

    
# sends error message to a channel
SERVER_ID = config.get("guild.id")
CHANNEL_ID = config.get("channel_id")
@bot.event
async def on_error(event, *args, **kwargs):
    error_message = f"An error occurred in {event}: {args[0]}"
    print(error_message)

    # If the error is related to getting a channel, handle it
    if "get_channel" in error_message:
        # Handle the error here
        pass

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your custom status'))
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.event
async def on_message(message):

    #log dms the bot recives in a specific channel

    if isinstance(message.channel, discord.DMChannel) and message.author != bot.user:
        guild = bot.get_guild(guild_id_config)  # replace with guild id
        channel = discord.utils.get(guild.text_channels, name='name')  # replace with channel name
        await channel.send(f'DM from: {message.author.name} id {message.author.id}\nContent: {message.content}')

    await bot.process_commands(message)

# calculate (utility)
@bot.command()
async def calculate(ctx):
    help_message = """To use the calculator, enter a equation, then the bot will solve it and send it to you. example: `5 + 3`
    
    note:
    `+ = plus`
    `- = minus`
    `/ = divide`
    `* = multiply`
    """                           
    await ctx.send(help_message)

    try:
        msg = await bot.wait_for("message", check=lambda message: message.author == ctx.author, timeout=60)
        equation = msg.content
        if not equation.startswith('!calculate'):
            equation = '!calculate ' + equation
        equation = equation[len('!calculate '):]

        valid_characters = set("0123456789+-*/() ")
        if not all(char in valid_characters for char in equation):
            await ctx.send("Invalid characters in the expression.")
            return

        result = eval(equation)
        await ctx.send(f'Result: {result}')
    except asyncio.TimeoutError:
        await ctx.send("Calculation request timed out. Please try again.")


# poll (utility)
@bot.command()
async def poll(ctx, duration, question):
    if not duration.isdigit():
        await ctx.send("Invalid duration, please provide a valid number of seconds")
        return

    duration = int(duration)
    
    if duration <= 0:
        await ctx.send("Duration must be a positive number of seconds")
        return

    embed = discord.Embed(
        title="Vote with '✅' for Yes, or '❌' for No",
        description=question,
        color=discord.Colour(842593)
    )

    embed.set_footer(text="Untitled Poll Bot v1.0")
    embed.set_author(name="Poll", icon_url="https://cdn-icons-png.flaticon.com/512/32/32175.png")

    poll_message = await ctx.send(embed=embed)

    for emoji in ('✅', '❌'):
        await poll_message.add_reaction(emoji)

    await asyncio.sleep(duration)
    await ctx.send("The poll has ended")

# ping (utility)
@bot.command()
async def ping(ctx):
    bot_latency = round(bot.latency * 1000)

# kick (moderation)
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} has been kicked.')
    else:
        await ctx.send("You don't have permission to kick members.")

# ban (moderation)
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} has been banned.')
    else:
        await ctx.send("You don't have permission to ban members.")

# clear (moderation)
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


# coinflip (fun)
@bot.command()
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f"The coin landed on {result}!")

# diceroll (fun)
@bot.command()
async def diceroll(ctx):
    roll = random.randint(1, 6)
    await ctx.send(f"The dice rolled a {roll}!")

# random number (fun)
@bot.command()
async def randomnumber(ctx, min_value=1, max_value=100):
    result = random.randint(min_value, max_value)
    await ctx.send(f"Your random number is {result}!")

# magic8ball (fun)
@bot.command()
async def magic8ball(ctx, *, question):
    responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.",
                 "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.",
                 "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                 "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

    response = random.choice(responses)
    await ctx.send(f"Question: {question}\nAnswer: {response}")

# joke (fun)
@bot.command()
async def joke(ctx):
    jokes = [
    "add jokes here", "seperated by a comma"
   ]
    await ctx.send(random.choice(jokes))

# riddle (fun)
@bot.command()
async def riddle(ctx):
    riddles = [
  {"q": "add riddles here question in q ", "a": "and answer in a"},
    ]
    riddle = random.choice(riddles)
    await ctx.send(f"Riddle: {riddle['q']}\nAnswer: {riddle['a']}")

# fortune (fun)
@bot.command()
async def fortune(ctx):
    fortunes = [
      "Add fortunes here",
      "seperated by a comma",
    ]
    await ctx.send(random.choice(fortunes) )


# set slowmode on a channel (utility) (made by zaynedrift)
@bot.command()
async def slowmode(ctx, duration: int):
   if ctx.author.guild_permissions.manage_channels:
    await ctx.channel.edit(slowmode_delay=duration)
    await ctx.send(f"Slowmode has been set to {duration} seconds in this channel")

# remove slowmode (utility)
# remove slowmode from a channel (made by zaynedrift)
@bot.command()
async def noslowmode(ctx):
   if ctx.author.guild_permissions.manage_channels:
    await ctx.channel.edit(slowmode_delay=0)
    await ctx.send("Slowmode has been removed from this channel!")


@bot.command()
async def help(ctx):
    # Create an embed
    embed = discord.Embed(
        title="Available Commands",
        description="Use these commands to interact with the bot!",
        color=discord.Color.blue()
    )

    # Add fields for each category of commands
    embed.add_field(name="Moderation", value="- `!kick [member] [reason]`: Kick a member from the server.\n- `!ban [member] [reason]`: Ban a member from the server.\n- `!clear [amount]`: Clear a specified number of messages.", inline=False)
    embed.add_field(name="Utility", value="- `!ping`: Check the latency of the bot.\n- `!slowmode` [slowmode seconds]: Set slowmode.\n- `!noslowmode`: Turn off slowmode.", inline=False)

**Utility:**
- `!ping`: Check the latency of the bot.
- `!slowmode` [slowmode seconds]: Set slowmode.
- `!noslowmode`: Turn off slowmode.
- `!calculate`: answers a simple math equation.
- `!poll:` creates a poll


    embed.add_field(name="Fun", value="- `!coinflip`: Simulate a coin flip.\n- `!diceroll [sides]`: Simulate a dice roll with a specified number of sides.\n- `!randomnumber [min] [max]`: Generate a random number within a specified range.\n- `!magic8ball [question]`: Ask the magic 8 ball a question.\n- `!joke`: Get a random joke.\n- `!riddle`: Get a random riddle.\n- `!fortune`: Get a fortune cookie message.", inline=False)

    embed.add_field(name="Games", value="- `!trivia`: Play the Trivia Quiz Game. (Currently broken)\n- `!wouldyourather`: Play the 'Would You Rather' Game.\n- `!numbergame [min] [max]`: Play the 'Guess the Number' Game.\n- `!wordgame`: Play the 'Guess the Word' Game.\n- `!rps [choice]`: Play Rock, Paper, Scissors with the bot.", inline=False)

    embed.add_field(name="Game Info", value="- `!gameinfo`: Display more information about the available games.", inline=False)

    # Send the embed
    await ctx.send(embed=embed)



# wordgame (game)
with open("words.txt") as file:
    word_list = [line.strip() for line in file]

# Select 10 words randomly
selected_words = random.sample(word_list, 10)


selected_words = []

@bot.command()
async def wordgame(ctx):
    word_to_guess = random.choice(selected_words)
    guessed_word = ["_"] * len(word_to_guess)
    tries = 0
    max_tries = 6
    revealed_letters = []  # List to track already revealed letters

    await ctx.send("Welcome to the Word Guessing Game! I've selected a random word. Try to guess one letter at a time.")
    await ctx.send(f"{' '.join(guessed_word)}")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    while "_" in guessed_word and tries < max_tries:
        await ctx.send("Enter a letter:")
        try:
            guess = await bot.wait_for("message", check=check, timeout=30)
            guess = guess.content.lower()

            if len(guess) == 1 and guess.isalpha() and guess not in revealed_letters:
                if guess in word_to_guess:
                    for i in range(len(word_to_guess)):
                        if word_to_guess[i] == guess:
                            guessed_word[i] = guess
                    await ctx.send(f"{' '.join(guessed_word)}")
                else:
                    tries += 1
                    await ctx.send(f"Wrong guess! You have {max_tries - tries} tries left.")

                    # Check if it's time to reveal a letter
                    if tries % 2 == 0:
                        unrevealed_letters = [letter for letter in word_to_guess if letter not in revealed_letters]
                        if unrevealed_letters:
                            letter_to_reveal = random.choice(unrevealed_letters)
                            guessed_word[word_to_guess.index(letter_to_reveal)] = letter_to_reveal
                            revealed_letters.append(letter_to_reveal)
                            await ctx.send(f"Revealing letter: {letter_to_reveal}")
            else:
                await ctx.send("Please enter a single letter that hasn't been guessed before.")

        except asyncio.TimeoutError:
            await ctx.send("Time's up! The game is over.")
            break

    if "_" not in guessed_word:
        await ctx.send("Congratulations! You guessed the word.")
    else:
        await ctx.send(f"Sorry, you're out of tries. The word was '{word_to_guess}'.")

# would you rather (game)
@bot.command()
async def wouldyourather(ctx):
    await ctx.send("Welcome to the 'Would You Rather' Game!")
    
    questions = [
        "add would you rather questions here", 
        "seperated by commas",
    ]
    
    random.shuffle(questions)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    for i, question in enumerate(questions):
        await ctx.send(f"Question {i + 1}: {question}\nType '1' for the first option or '2' for the second option.")
        try:
            response = await bot.wait_for("message", check=check, timeout=30)
            response_text = response.content
            if response_text == "1":
                await ctx.send("You chose the first option.")
            elif response_text == "2":
                await ctx.send("You chose the second option.")
            else:
                await ctx.send("Please type '1' or '2' for your choice.")

        except asyncio.TimeoutError:
            await ctx.send("Time's up! The game is over.")
            break
 

#rock paper scissors (game)
@bot.command()
async def rps(ctx, user_choice: str):
    if user_choice not in choices:
        await ctx.send("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
        return

    bot_choice = random.choice(choices)

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and bot_choice == "scissors") or
        (user_choice == "paper" and bot_choice == "rock") or
        (user_choice == "scissors" and bot_choice == "paper")
    ):
        result = f"You win! You chose {user_choice} and I chose {bot_choice}."
    else:
        result = f"I win! You chose {user_choice} and I chose {bot_choice}."

    await ctx.send(f"You chose {user_choice}.")
    await ctx.send(f"I chose {bot_choice}.")
    await ctx.send(result)
                    
           
# guess the number (game)
@bot.command()
async def numbergame(ctx):
    number_to_guess = random.randint(1, 100)
    tries = 0

    await ctx.send("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100. Try to guess it!")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    while True:
        await ctx.send("Enter your guess:")
        try:
            guess = await bot.wait_for("message", check=check, timeout=30)
            guess = int(guess.content)
            tries += 1

            if guess < number_to_guess:
                await ctx.send("Too low! Try a higher number.")
            elif guess > number_to_guess:
                await ctx.send("Too high! Try a lower number.")
            else:
                await ctx.send(f"Congratulations! You guessed the number ({number_to_guess}) in {tries} tries.")
                break

        except asyncio.TimeoutError:
            await ctx.send("Time's up! The game is over.")
            break
        except ValueError:
            await ctx.send("Please enter a valid number.")

# trivia (game)
trivia_questions = []    

# CONTRIBUTOR NOTE
# rivia, is completly broken now, i wasn't able to get it to work, so it's just commented out, i don't have the original trivua_questions.txt file

# with open('trivia_questions.txt', 'r') as file:
#     lines = file.read().split('\n\n')
#     for line in lines:
#         question_lines = line.strip().split('\n')
#         question = question_lines[0]
#         options = question_lines[1].split(', ')
#         correct = question_lines[2]
#         trivia_questions.append({"question": question, "options": options, "correct": correct})

# trivia questions will be in a seperate file called "trivia_questions.txt"

# @bot.command()
# async def trivia(ctx):
#     await ctx.send("Welcome to the Trivia Quiz Game!")

#     random.shuffle(trivia_questions)

#     score = 0

#     def check(msg):
#         return msg.author == ctx.author and msg.channel == ctx.channel

#     for i, question in enumerate(trivia_questions):
#         await ctx.send(f"Question {i + 1}: {question['question']}\nOptions: {', '.join(question['options'])}")
#         try:
#             response = await bot.wait_for("message", check=check, timeout=30)
#             response_text = response.content
#             if response_text.lower() == question["correct"].lower():
#                 await ctx.send("Correct!")
#                 score += 1
#             else:
#                 await ctx.send(f"Sorry, the correct answer is {question['correct']}.")

#         except asyncio.TimeoutError:
#             await ctx.send("Time's up! The game is over.")
#             break

#     await ctx.send(f"You scored {score}/{len(trivia_questions)} in the Trivia Quiz Game!")

bot.run(token) #replace with your bot token