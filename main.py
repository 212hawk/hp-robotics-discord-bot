import discord
import replit
import random
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

replit.clear()
@client.event
async def on_ready():
  print("ready")



#hud for person
@client.event
async def on_member_join(member):
  print(f"{member} has joined!")

#latency
@client.command()
async def ping(ctx):
  await ctx.send(f"pong! \nIt took me {round(client.latency*1000)} ms to respond!")

@client.command(aliases=["8ball-add"])
async def add_command(ctx,*,response):
  responses=open("8ball-responses.txt","w")
  responses.write(response)
  await ctx.send(f"response {response} added")
  responses.close()

@client.command(aliases=['8ball'])
async def eightBall(ctx,*,question):
  responses=open("8ball-responses.txt","r").readlines()
  #list of all responses from wikapedia
  await ctx.send(f"question: {question} \nanswer: {random.choice(responses)}")

client.run('NjY5NjgxNTU1ODAyNjg1NDQx.XijgSQ.5ujJiqorhD9qHb6eZjoZ9k5bDzc')