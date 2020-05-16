import discord 
import data_stocks as ds
import stock_data_india as sdi

# id  710894873254821899
# token  NzEwODk0ODczMjU0ODIxODk5.Xr7Hbg.ID55xw36W8xB2eUulHdwvzmCE5M
# 67648

# https://discordapp.com/oauth2/authorize?client_id=710894873254821899&scope=bot&permissions=67648

#print(discord.__version__)  # check to make sure at least once you're on the right version!

token =  'NzEwODk0ODczMjU0ODIxODk5.Xr7Hbg.ID55xw36W8xB2eUulHdwvzmCE5M' # I've opted to just save my token to a text file. 

client = discord.Client()  # starts the discord client.


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.


@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    try:
        if "!greet" in message.content.lower():
            await message.channel.send('Sup cunt!')
        elif "!diss" in message.content.lower():
            await message.channel.send('Fuck off bitch')
        elif "!madhen" in message.content.lower():
            await message.channel.send('B L A C K  L I V E S  M A T T E R.')
        elif "!quit" in message.content.lower():
            await client.close()
        elif "!stockpindia" in message.content.lower():
            st = message.content.split(' ')[1]
            await message.channel.send(str(sdi.get_price_ind(st)))        
        elif "!stockp" in message.content.lower():
            st = message.content.split(' ')[1]
            await message.channel.send(str(ds.get_price(st)))
        elif "!topgain" in message.content.lower():
            st = message.content.split(' ')[1]
            await message.channel.send(str(sdi.get_topgain(st)))
        elif "!toploss" in message.content.lower():
            st = message.content.split(' ')[1]
            await message.channel.send(str(sdi.get_toploss(st)))
        
    except Exception as e:
        print(e)
        await message.channel.send('Type the code properly dumbfuck') 


client.run(token)  # recall my token was saved!

