import discord
from fonksiyonlar import *
from dsb import rakam,islem


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptik.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    if message.content.startswith('$komutlar'):
        await message.channel.send("merhaba, emoji,parola,oyun gibi aktiviteler gerçekleştirebilirsin. Sana nasıl yatdımcı olabilirim ? (unutma her komutun başına $ işareti koymalısın !)")
    elif message.content.startswith('$merhaba'):
        await message.channel.send("merhaba, $komutlar yazarak neler yapabileceğini öğrenebilirsin")
    elif message.content.startswith('$emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith('$parola'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$oyun'):
        await message.channel.send(yazi_tura())  
    elif message.content.startswith('$rakam'):
        await message.channel.send(rakam)
    elif message.content.startswith('$islem'):
        await message.channel.send(islem)

    else:
        await message.channel.send('Bu komutu anlamadım')

client.run("09f8334d0889d4f2228a70bc0f37bd26c55e4994da30e7979b5e2a00e057d8ef")
