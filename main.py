from operator import iconcat
from types import new_class
import discord
from discord import *
from discord.ext import commands
import json
import os
import random
import asyncio
import urllib.parse, urllib.request, re
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import bot


from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.flags import Intents
from discord.raw_models import RawBulkMessageDeleteEvent

TOKEN = "ODM5NTQxNjMwNTk1MjM1ODYx.YJLKEg.HgDZIKPKq_CJr47I8OPSr9316cA"

client = commands.Bot(command_prefix= "*", intents=discord.Intents.all())


server = "🌴┃Polish Dynamo Chill™"


images = [
    'https://cdn.discordapp.com/attachments/876858512444096548/877517456929873930/meme1.jpg',
    'https://cdn.discordapp.com/attachments/876858512444096548/877517476391432192/meme2.jpg',
    'https://cdn.discordapp.com/attachments/876858512444096548/877517501611773962/meme3.jpg',
    'https://cdn.discordapp.com/attachments/876858512444096548/877518020224892938/meme4.png',
    'https://cdn.discordapp.com/attachments/876858512444096548/877518141519978506/meme5.jpg',
    'https://cdn.discordapp.com/attachments/876858512444096548/877518156254552074/meme6.jpg'
]




@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('*help'))
    print('Zalogowano do bota')


@client.event
async def on_raw_reaction_add(payload):

    if payload.member.bot:
        pass

    else:

        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await client.get_guild(payload.guild_id).get_member(payload.user_id).add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):

    if payload.member:
        pass

    else:

        with open('reactrole.json') as react_file:

            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name and x['message_id'] == payload.message_id:
                    role = discord.utils.get(client.get_guild(payload.guild_id).roles, id=x['role_id'])

                    await client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        m1 = discord.Embed(title = "Error", description = "❌ You are not permisions to this command ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        m1 = discord.Embed(title = "Error", description = "❌ Invalid command argument ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.message.delete()
    elif isinstance(error, commands.CommandNotFound):
        m1 = discord.Embed(title = "Error", description = "❌ Command not found ❌", colour = discord.Colour.red())
        await ctx.send(embed=m1)
        await ctx.message.delete()


@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def  clear(ctx, amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member, *,reason):
    
        em=discord.Embed(title="🔨 Kicked 🔨", description = f"You have been Kicked from {server}", colour=discord.Colour.red())
        em.add_field(name="Reason", value=f"{reason}", inline=False)
        await member.send(embed=em)
    
    
        em=discord.Embed(title="✅", description = "The user has been kicked", colour=discord.Colour.green())
        em.add_field(name="Reason", value=f"{reason}", inline=False)
        await ctx.send(embed=em)

        await member.kick(reason=reason)


@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member, *,reason):
    
        em=discord.Embed(title="🔨 Banned 🔨", description = f"You have been Banned from {server}", colour=discord.Colour.red())
        em.add_field(name="Reason", value=f"{reason}", inline=False)
        await member.send(embed=em)
    
    
        em=discord.Embed(title="Success", description = "The user has been banned", colour=discord.Colour.green())
        em.add_field(name="Reason", value=f"{reason}", inline=False)
        await ctx.send(embed=em)

        await member.ban(reason=reason)


@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, member : discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')


    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name, member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +" has been unbanned!")
            return

        await ctx.send("was not found")
 
@client.command(aliases=['m'])
@commands.has_permissions(mute_members = True)
async def mute(ctx,member : discord.Member, *,reason):
    muted_role = ctx.guild.get_role(877206980907905034)

    em=discord.Embed(title="🔇Muted🔇", description = "You have been Muted from Bluppy Support Server", colour=discord.Colour.red())
    em.add_field(name="Reason", value=f"{reason}", inline=False)
    await member.send(embed=em)

    em=discord.Embed(title="✅Succesfully✅", description = f"{member.mention} is muted!", colour=discord.Colour.green())
    em.add_field(name="Reason", value=f"{reason}", inline=False)
    await ctx.send(embed=em)

    for role in member.roles:
        if str(role) != "@everyone":                    
            role = discord.utils.get(ctx.guild.roles, id = role.id)
            await member.remove_roles(role)
    await member.add_roles(muted_role)

@client.command(aliases=['ks'])
@commands.has_permissions(send_messages = True)
async def kiss(ctx, member):

    image = 'https://cdn.discordapp.com/attachments/876858512444096548/877884436056772608/free-kiss-anime.jpg'

    await ctx.send("Kiss 💋!")
    await ctx.send(image)
    

@client.command(aliases=['h'])
@commands.has_permissions(send_messages = True)
async def hello(ctx):
    em=discord.Embed(title="Hi👋", description = "```I am new discord bot.```", colour=discord.Colour.orange())
    em.add_field(name="About Me", value="Bot Prefix: ```*```", inline=True)
    await ctx.send(embed=em)



@client.group(invoke_without_command=True)
@commands.has_permissions(send_messages=True)
async def user(ctx, member : discord.Member):
    embed =  discord.Embed(title = "Title", description =  "This is a Description", colour = discord.Colour.green())
    embed.add_field(name = "ID", value = member.id,  inline = True)
    embed.add_field(name = "Top Role", value = member.top_role,  inline = True)
    embed.set_author(name = member.display_name, icon_url = member.avatar_url)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_image(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)


@client.command()
async def emoji(ctx):
    await ctx.send("🔥")

@client.command()
async def dm(ctx, member = discord.Member):
    try:
        await member.send("XD")
    except:
            await ctx.send("The member has their DM's closed")


@client.command()
async def ping(ctx):
    em=discord.Embed(colour=discord.Colour.blue())
    em.add_field(name="Ping", value=(f"{round(client.latency*1000)} ms"), inline=True)
    await ctx.send(embed=em)


@client.command()
@commands.has_permissions(manage_messages=True)
async def reactrole(ctx, emoji, role: discord.Role, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)


        new_react_role = {
            'role_name':role.name,
            'role_id':role.id,
            'emoji':emoji,
            'message_id':msg.id
        }

        data.append(new_react_role)


    with open ('reactrole.json','w') as j:
        json.dump(data, j, indent=4)


@client.command()
async def meme(ctx):
    embed = discord.Embed(colour = discord.Colour.red())

    random_link = random.choice(images)

    embed.set_image(url = random_link)
 
    await ctx.send(embed = embed)

@client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Command List", colour = discord.Colour.blue())
    em.add_field(name="⚙ Moderation", value=("ban, mute, clear, kick, reactrole, unban"), inline=False)
    em.add_field(name="🎯 Information", value=("ping, user, hello"), inline=False)
    em.add_field(name="✨4Fun", value=("meme, kiss, emoji"), inline=False)

    await ctx.send(embed=em)
    
client.run(TOKEN)