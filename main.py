#-----Galerie Discord ----#

from pyexpat.errors import messages

import discord

from discord.ext import commands

#-----Préfixe et Description du Bot ----#

bot = commands.Bot(command_prefix = "!", description = "Bot Created by Tom.#9710 \n  French Bot \n Regarde la version 1.0.0")

#-----Message BOT Machine----#

@bot.event

async def on_ready():

    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('la Version 1.0.0 by FTC'))
    
    print("Ready !")

#-----Commandes Public----#

@bot.command()

async def botinfo(ctx):

    await ctx.send("Mon créateur est Tom.#9710 \nMa date de création est le 30/03/22")

    

@bot.command()

async def bonjour(ctx):

    await ctx.send("Bonjour comment vas-tu?")

    

@bot.command()

async def serveurinfo(ctx):

    server = ctx.guild

    numberOfTextChannels = len(server.text_channels)

    numberOfVoiceChannels = len(server.voice_channels)

    serverDescription = server.description

    numberOfPerson = server.member_count

    serverName = server.name

    message = f"Le serveur **{serverName}** à *{numberOfPerson}* membres. \nDescription du serveur est {serverDescription} \nCe serveur possède {numberOfTextChannels} salons textuels et {numberOfVoiceChannels} salons vocaux"

    await ctx.send(message)

    

@bot.command()

async def liens(ctx):

    await ctx.send("Voici quelques liens utiles \nPour m'inviter dans ton serveur: https://discord.com/api/oauth2/authorize?client_id=953699601788063774&permissions=8&scope=bot")

 

 #-----Commandes Administration----#

@bot.command()

async def clear(ctx, nombre : int):

    messages = await ctx.channel.history(limit = nombre + 1).flatten()

    for message in messages:

     await message.delete()

     

@bot.command()

async def kick(ctx, user : discord.User, *reason):

    reason = " ".join(reason)

    await ctx.guild.kick(user, reason = reason)

    await ctx.send(f"{user} à été kick du serveur")

    embed = discord.Embed(title = "Exclusion", description = "Un membre du Staff à kick un membre du serveur!", color=0xfa8072)

    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

    embed.add_field(name = "Membre Kick", value = user.name, inline = True)

    embed.add_field(name = "Raison", value = reason, inline = True)

    embed.add_field(name = "Staff", value = ctx.author.name, inline = True) 

    embed.set_footer(text = "Rapport de Sanction Staff")

    

    await ctx.send(embed = embed)

    

@bot.command()

@commands.has_permissions(ban_members = True)

async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):

    await ctx.guild.ban(user, reason = reason)

    embed = discord.Embed(title = "**Banissements**", description = "Un membre du Staff à Banni un membre du serveur!", color=0xfa8072)

    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

    embed.add_field(name = "Membre Banni", value = user.name, inline = True)

    embed.add_field(name = "Raison", value = reason, inline = True)

    embed.add_field(name = "Staff", value = ctx.author.name, inline = True) 

    embed.set_footer(text = "Rapport de Sanction Staff")

    

    await ctx.send(embed = embed)

    

@bot.command()

async def unban(ctx, user, *reason):

    reason = " ".join(reason)

    userName, userId = user.split("#")

    bannedUsers = await ctx.guild.bans()

    for i in bannedUsers:

        if i.user.name == userName and i.user.discriminator == userId:

            await ctx.guild.unban(i.user, reason = reason)

            await ctx.send(f"{user} à bien été unban")

            return

    #utilisateur non trouvée

    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des banissements")

    

    #-----Vérification----#

 

def isOwner(ctx):

    return ctx.message.author.id == 643097416555560966

     

@bot.command()

@commands.check(isOwner)

async def owner(ctx):

    await ctx.send("Cette commande peut seulement être effectués par le propriétaire du bot")

        

 #-----TOKEN BOT----#

bot.run("OTUzNjk5NjAxNzg4MDYzNzc0.YjIX9w.HAufPFUe2eabYK87mTffgNxJzTA")
