# Simple Discord Bot - README

## Introduction

This repository contains the source code for a simple Discord bot created using the Discord.py library. The bot provides a handful of commands for basic moderation, utility, and fun interactions within your server.

## Features

- **Moderation**: Kick and ban members, and clear messages from text channels.

- **Utility**: Check the bot's latency, learn about the bot's creator, and view available commands.

- **Fun**: Enjoy coin flipping, dice rolling, random number generation, and magic 8-ball responses. Additionally, the bot can tell jokes, riddles, and even provide fortune cookie messages.

## Installation and Configuration


1. Create a Discord bot on the [Discord Developer Portal](https://discord.com/developers/applications) and get your bot token.

2. Replace `"your bot token"` in the last line of the script with your bot token.

```python
bot.run("your bot token")
```

7. Modify other parts of the code with your own settings and responses as needed.

## Usage

Run the bot with the following command:

```bash
python bot.py
```

## Available Commands

The bot offers the following commands:

### Moderation

- `!kick <@user> [reason]`: Kick a member from the server.
- `!ban <@user> [reason]`: Ban a member from the server.
- `!clear [amount]`: Clear a specified number of messages.

### Utility

- `!ping`: Check the latency of the bot.
- `!bot_creator`: Display information about the bot.
- `!commands`: Display the list of available commands.

### Fun

- `!coinflip`: Simulate a coin flip.
- `!diceroll`: Simulate a dice roll.
- `!randomnumber [min_value] [max_value]`: Generate a random number.
- `!magic8ball <question>`: Ask the magic 8 ball a question.
- `!joke`: Get a random joke.
- `!riddle`: Get a random riddle.
- `!fortune`: Display a fortune cookie message.

------

Enjoy using this simple Discord bot for your server!
