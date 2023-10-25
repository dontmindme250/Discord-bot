# Heyo This is Zayne! I made this code and gave it to my bud dontmindme to use. 
# check my profile (Zaynedrift) and join my discord server from there because dontmindme said no advertising >:c

# this is a basic logging fuction made by Zaynedrift
# it sends a log to a channel specified by its name

@bot.event
async def on_member_ban(guild, user):
    log_channel = discord.utils.get(guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'{user.name} was banned.')

@bot.event
async def on_member_unban(guild, user):
    log_channel = discord.utils.get(guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'{user.id} ({user.name}) was Unbanned.')

@bot.event
async def on_message_delete(message):
    log_channel = discord.utils.get(message.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Message by {message.author.name} deleted: {message.content}')

@bot.event
async def on_message_edit(before, after):
    if before.content != after.content:
        log_channel = discord.utils.get(before.guild.text_channels, name='log-channel')
        if log_channel:
            await log_channel.send(f'Message by {before.author.name} edited: \nBefore: {before.content}\nAfter: {after.content}')

@bot.event
async def on_member_join(member):
    log_channel = discord.utils.get(member.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'{member.name} joined the server.')

@bot.event
async def on_member_remove(member):
    log_channel = discord.utils.get(member.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'{member.name} left the server.')

@bot.event
async def on_guild_update(before, after):
    # You can add more specific logging for server updates here
    log_channel = discord.utils.get(after.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send('Server settings updated.')

@bot.event
async def on_guild_channel_create(channel):
    log_channel = discord.utils.get(channel.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Channel created: {channel.name}')

@bot.event
async def on_guild_channel_delete(channel):
    log_channel = discord.utils.get(channel.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Channel deleted: {channel.name}')

@bot.event
async def on_guild_role_create(role):
    log_channel = discord.utils.get(role.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Role created: {role.name}')

@bot.event
async def on_guild_role_update(before, after):
    # You can add more specific logging for role updates here
    log_channel = discord.utils.get(after.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Role settings updated for the role: {role.name}')

@bot.event
async def on_guild_role_delete(role):
    log_channel = discord.utils.get(role.guild.text_channels, name='log-channel')
    if log_channel:
        await log_channel.send(f'Role deleted: {role.name}')

# change the string "log-channel" to your logging channel name
# and it will log actions to that channel
# note: as of now the logs are in normal messages, not embeds and are not very detailed.
