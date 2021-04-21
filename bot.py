import discord
import asyncio
from discord.ext import commands
from prsaw import RandomStuff
import os
import json

client = commands.Bot(command_prefix = "^")
client.remove_command("help")
rs = RandomStuff(async_mode = True)

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="DISCORD.py | ^help \ ^h")) 
  print("SOFAN IS READY")

@client.group(invoke_without_command=True, aliases=['h'])
async def help(ctx):
    em = discord.Embed(title= "Help",  description="PREFIX=`^`", color=0xffff)

    em.add_field(name="<a:hype:794886288909926420>|General Commands", value="`info / io`-To get the information of the bot \n `version / v`=To get the version of the bot", inline=False)

    em.add_field(name=":tools:| Moderation", value="`ban / b` *user*-To ban a user \n `kick / k` *user*=To kick a member \n `purge / pg` *amount*=To delete a amount of numbers", inline=False)

    em.add_field(name="<:happyblake:783325011288915979>| Fun", value="`ping / p`-To get your network's ms/ping \n `snipe / sp`=If someone deletes a message u can type this command to see the message \n `coinflip / cf`-To do coin flip", inline=False)

    em.add_field(name=":eyes: | Emojis", value="`pepelaugh`=<a:L_B:801774547144671232> \n `hi`=<a:W_:797404718376157184> \n `false`=<a:tickred:791845423769845760> \n `true`=<a:yes:791844956746678312> \n `SUS`=<a:S_:801989445779849247><a:U_:801989177646383144><a:S_:801989445779849247>")

    em.add_field(name=":gear: | On devlopment", value="`change_prefix` \n `unban`", inline=False)

    em.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    
    await ctx.send(embed=em)
    
# @bot.event
# async def on_message(message):
#   if bot.user == message.author:
#     return
  
#   if message.channel.id == 834252222501224489:
#     responce = await rs.get_ai_response(message.content)
#     await message.reply(response)
  
#   await bot.process_commands(message)

snipe_message_content = None
snipe_message_author = None

@client.event
async def on_message_delete(message):
  global snipe_message_content
  global snipe_message_author

  snipe_message_content = message.content
  snipe_message_author = message.author.name
  await asyncio.sleep(60)
  snipe_message_author = None
  snipe_message_content = None

@client.command(aliases=['sp'])
async def snipe(message):
  if snipe_message_content==None:
    await message.channel.send("Nothing to snipe!")
  else:
      embed = discord.Embed(description=f"{snipe_message_content}")
      embed.set_footer(text=f"Requested by {message.author.name}#{message.author.discriminator}")
      embed.set_author(name=f"Sniped the message deleted by : {snipe_message_author}")
      await message.channel.send(embed=embed)
      return

# client.sniped_messages = {}

# @client.event
# async def on_message_delete(message):
#     client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
    # contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    # embed = discord.Embed(description = contents, color =0xffff, timestamp=time)
    # embed.set_author(name=f'{author.name}#{author.discriminator}', icon_url=author.avatar_url)
    # embed.set_footer(text=f'Deleted in #{channel_name}')

    # await ctx.channel.send(embed=embed)

  # @client.command()
  # async def snipe(message):
  #   if snipe_message_content==None:
  #     await message.channel.send("Nothing to snipe!")
  #   else:
  #     embedhi = discord.Embed(description=f"{snipe_message_content}")
  #     embedhi.set_footer(text=f"Requested By{message.author.name}#{message.author.discriminator}")
  #     embedhi.set_author(name = f"Sniped The Message Deleted By : {snipe_message_author}")
  #     await message.channel.send(embed=embedhi)
  #     return


@client.command(aliases=['io'])
async def info(ctx):

    myEmbed2 = discord.Embed(title="INFO", description="Hey, Guys, My name is `Sofan` and I developed this bot. It is not good since it is my first time coding \n Thank You <a:C_v:796981227223253032>", color=0xffff)

    myEmbed2.add_field(name=":stars:| Contributors", value="Sick#7475 \n MaybeUman#4352", inline=False)

    myEmbed2.add_field(name="Made BY", value="SofanGaming#0704", inline=False)
    
    myEmbed2.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

    await ctx.send(embed=myEmbed2)

@client.command(aliases=['v'])
async def version(ctx):

    myEmbed = discord.Embed(title="Current Version", description="The Current Version is `1.0` ", color=0xffff)
     
    myEmbed.add_field(name="`1.0`", value="Added Some New Commands Type `>help` To Get The Command List", inline=False)
    
    myEmbed.add_field(name="Date Released:",   value="April 16, 2021", inline=False)

    myEmbed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    # myEmbed=set_footer(text=LOL)
    # myEmbed=set_author(name="Sofan")

    await ctx.send(embed=myEmbed)

# @client.command()
# @commands.has_permissions(administrator = True)
# async def kick(ctx, member : discord.Member, *, reason=None):
#   await member.kick(reason=reason)
#   await ctx.send(f'(member)was kicked!')

# @client.command()
# @commands.has_permissions(administrator = True)
# async def ban(ctx, member : discord.Member, *, reason=None):
#   await member.ban(reason=reason)
#   await ctx.send(f'Banned {member.mention}')

# @client.command()
# @commands.has_permissions(administrator = True)
# async def unban(ctx, *, member):
#   banned_users = await ctx.guild.bans()
#   member_name, member_discriminator = member.spilt('#')

#   for ban_entry in banned_users:
#     user = ban_entry.user

#     if (user.name, user.discriminator) == (member_name, member_discriminator):
#       await ctx.guild.unban(user)
#       await ctx.send(f'Unbanned {user.mention}')
#       return

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member, *, reason = "No reason was provided"):
  await member.send("You have been kicked from SofanGaming server, Because:"+reason)
  await ctx.send(member.mention + "has been banned because:"+reason)
  await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "No reason was provided"):
  await member.send("You have been Banned from SofanGaming server, Because:"+reason)
  await ctx.send(member.mention + "has been banned because: "+reason)
  await member.ban(reason=reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.spilt('#')

  for banned_entry in banned_users:
    user = banned_entry.user

    if(user.name, user.discriminator)==(member_name,member_disc):

      await ctx.guild.unban(user)
      await ctx.send(member_name +" has been unbanned!")
      return

  await ctx.send(member+" was not found")

@client.command()
async def hello(ctx):

  em2 = discord.Embed(title="HI", color=0xffff)

  await ctx.send(embed=em2)

  # @client.command()
  # async def ping(ctx):
  #   await ctx.send("PONG!!!")

@client.command(aliases=['pg'])
@commands.has_permissions(administrator=True)
async def purge(ctx, amount):
  await ctx.message.delete()
  await ctx.channel.purge(limit=int(amount))
  message_to_delete = await ctx.send(f'{amount} messages have been deleted!')
  await asyncio.sleep(1)
  await message_to_delete.delete()
  
@client.command(aliases=['p'])
async def ping(ctx):

    em = discord.Embed(title="PONG!", description=f"{round(client.latency * 1000)}ms", color=0xffff)

    em.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

    await ctx.send(embed=em)

@client.command()
async def pepelaugh(ctx):
  await ctx.send("<a:L_B:801774547144671232>")

@client.command()
async def hi(ctx):
  await ctx.send("<a:W_:797404718376157184>")

@client.command()
async def false(ctx):
  await ctx.send("<a:tickred:791845423769845760>")

@client.command()
async def true(ctx):
  await ctx.send("<a:yes:791844956746678312>")

@client.command()
async def SUS(lol):
  await lol.send("<a:S_:801989445779849247><a:U_:801989177646383144><a:S_:801989445779849247>")

@client.command()
async def op(sickissick):
  await sickissick.send("op")
  
@client.command(aliases=["cf"])
async def coinflip(ctx):
  choices = ["HEADS","TAILS"]
  rancoin = random.choice(choices)
  await ctx.send(rancoin)

  

  # @client.group(invoke_without_command=True)
  # async def help(ctx):
  #   em = discord.Embed(title= "Help",  description="PREFIX=`^`", color=0xffff)

  #   em.add_field(name="Commands", value="`^info`-To get the information of the bot \n `^ping`-To get your network's ms/ping", inline=False)


  #   await ctx.send(embed=em)

client.run('NjQyMzYzODE0MzY0NTc3ODA3.XcV16w.VYJ5n5v1vMid1fNa6E-NVJ02KAQ')

#un if needed

# def get_prefix(client,message):

#   with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#     return prefixes[str(message.guild.id)]

# client = commands.Bot(command_prefix=get_prefix)

# @client.event
# async def on_guild_join(guild):

#   with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#   prefixes[str(guild.id)] ="^"

#   with open("prefixes.json", "w") as f:
#     json.dump(prefixes,f)

# client.remove_command("help")

# @client.command()
# @commands.has_permissions(administrator = True)
# async def change_prefix(ctx, prefix):

#   with open("prefixes.json", "r") as f:
#     prefixes = json.load(f)

#   prefixes[str(guild.id)] = prefix

#   with open("prefixes.json", "w") as f:
#     json.dump(prefixes,f)

#   await ctx.send(f"The prefix was change to{prefix}")

# @client.event
# async def on_message(msg):

#     try:
#       if msg.mentions[0] == client.user:

#           with open("prefixes.json", "r") as f:
#             prefixes = json.load(f)

#           pre = prefixes[str(msg.guild.id)]

#           await msg.channel.send(f"My prefix for this server is {pre}")

#     except:
#       pass

#     await client.process_commands(msg)

# un if needed

# client.run(ok.env.token)

#   await client.change_presence(activity=discord.Game(name="^info-To Get The Info Of The Bot"))

#   await client.change_presence(activity=discord.Game(name="^ping-To Get ms(ping)"))


# async def ch_pr():
#   await client.wait_until_ready()

#   statuses = ["^info-To Get The Info Of The Bot", "^ping-To Get ms(ping)"]

#   while not client.is_closed():

#     statuses = random.choice(statuses)

#     await client.change_presence(activity=discord.Game(name=status))

#     await asyncio.sleep(10)
# client.loop.create_task(ch_pr())
# client.run()

  # @client.command()
  # async def help(ctx):

  #   myEmbed3 = discord.Embed(title="SOFAN HELP",description="My prefix for command is ^", color=0xffff)

  #   myEmbed3.add_field(name="Commands", description="^info-To get The Information of the bot \n >version To Get The Upadtes Or Which Version The Bot Is Currently On \n Thank You :giftik:", inline=False)

  #   await ctx.send(embed=myEmbed3)

  # @client.command()
  # async def god(ctx):

  #   me = discord.Embed(title="HELP", description="PREFIX=*", color=0xffff)

  #   me.add_field(name=commands, description="^info-To Get Information ^version-To Get The Updates Or Which Vrsion The Bot Is On", inline=False)

  #   await ctx.send(embed=me)pp