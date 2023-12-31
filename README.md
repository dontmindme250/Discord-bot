# Basic discord bot
A simple and basic discord bot with moderation, utility, and fun commands. \
Most of the code written by [@dontmindme250](https://github.com/dontmindme250)

## Installation
1. Create a new application in the [Discord Developer Portal](https://discord.com/developers/applications) and get a bot token.

3. Replace `"your bot token"` in the last line of the script with your bot token.

```python
bot.run("your bot token")
```

# Permissions needed
- Send messages
- View channels
- Manage channels
- Read message history
- Kick members
- Ban members

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
