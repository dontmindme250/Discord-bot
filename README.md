# Basic discord bot

A simple and basic discord bot with moderation, utility, and fun commands. \
Most of the code written by [@dontmindme250](https://github.com/dontmindme250)

# Table of Contents

- [Installation](#installation)
- [Permissions needed](#permissions-needed)
- [Commands](#commands)
	- [Moderation](#moderation)
	- [Utility](#utility)
	- [Fun](#fun)
	- [Games](#games)
- [Extra](#extra)
	- [More statuses](#more-statuses)
	- [Log commands](#log-commands)

## Installation

1. Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications) and get a bot token.
2. Replace `BOT_TOKEN_HERE` in the last line of the config.json with your bot token.

```json
"bot_token": "BOT_TOKEN_HERE",
```

# Permissions needed

- Send messages
- manage messages
- View channels
- Manage channels
- Read message history
- Kick members
- Ban members

or just give it admin

# Commands

### Moderation:
`!kick [member] [reason]`: Kick a member from the server. \
`!ban [member] [reason]`: Ban a member from the server. \
`!clear [amount]`: Clear a specified number of messages.

### Utility
`!ping`: Check the latency of the bot. \
`!slowmode [slowmode seconds]`: Set slowmode. \
`!noslowmode`: Turn off slowmode.

### Fun
`!coinflip`: Simulate a coin flip. \
`!diceroll [amount of sides]`: Simulate a dice roll with a specified number of sides. \
`!randomnumber [minimum] [maximum]`: Generate a random number within a specified range. \
`!magic8ball [question]`: Ask the magic 8 ball a question. \
`!joke`: Get a random joke. \
`!riddle`: Get a random riddle. \
`!fortune`: Get a fortune cookie message.

### Games:
`!trivia`: Play the Trivia Quiz Game. \
`!wouldyourather`: Play the 'Would You Rather' Game. \
`!numbergame [minimum] [maximum]`: Play the 'Guess the Number' Game. \
`!wordgame`: Play the 'Guess the Word' Game. \
`!rps [choice]`: Play Rock, Paper, Scissors with the bot. \
`!gameinfo`: Display more information about the available games.

## extra

### more statuses
change the bots status types with the code in `different_statuses.py`

### log commands
add a simple logging function to the bot, add the code in `log_commands.py` into the main 
file