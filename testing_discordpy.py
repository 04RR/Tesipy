import discord 
import data_stocks as ds
import stock_data_india as sdi


token =  'YOUR TOKEN'  

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

