# these are different types of custom status messages
# ex: streaming, listening and playing

# note: non of these have been tested yet 
# if one if these do not work please create a issue


# online status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.online)
    
    
# idle status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.idle)
    

# do not disturb status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.dnd)
    
    
# invisible status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.invisible)
    
# listening to spotify status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Listening to Spotify Status"))


# streaming on twitch status (no need for actual stream url)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Streaming(name="Streaming Status", url="your_stream_url"))


# competing status
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="Competing Status"))
    

# custom status (will show as online)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    await bot.change_presence(activity=discord.Game(name="Custom Status"))
    

# to change the status types just change this bit of code to the status you would like to have
# (the code is in main.py)
@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your custom status'))
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    
# make sure the change the status content before running the bot.