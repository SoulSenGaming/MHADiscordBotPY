import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random 

bot = commands.Bot(command_prefix='mha!')
token = 'NDQyODU2OTc5MTMyODQxOTg0.DdE6Nw.Bfyo-xa-oiq1jELJF7nyzD0Cx74'
quoteOpen = open("quotes.txt", "a")
quoteRead = open("quotes.txt", "r")

@bot.event
async def on_ready():
  print ("MHA Discord Bot Has Been Enabled, Remember Go Beyond, PLUS ULTRAA!")
  print ("Logged In As: " + bot.user.name)
  print ("User ID: " + bot.user.id)
  
@bot.command(pass_context=True)
async def about(ctx):
  await bot.say("About MHA Bot")
  await bot.say("Author: Deku 2.0")
  await bot.say("Based On The Anime: My Hero Academia")
  await bot.say("I DO NOT OWN THIS FRANCHISE")
  
@bot.command(pass_context=True)
async def quote(ctx):
  await bot.say (quoteRead.readlines())

@bot.command(pass_context=True)
async def addquote(ctx, arg):
  await bot.say("Quote Successfully Added: {}".format(arg))
  quoteOpen.write("{}\n".format(arg))
  quoteOpen.close()
  
  

  
bot.run(token)
