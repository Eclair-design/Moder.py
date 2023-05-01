import discord
from discord import Option
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord.utils import get
import random
import asyncio
import embed_builder
import os
from discord import ChannelType
import time
import Moder

async def flood(ctx, member: discord.Member, content):
    channel = await member.create_dm()
    nmsg = 0
    while nmsg < 10:
        try:
            await channel.send(content)
            await ctx.send("Successful")
        except:
            await ctx.send("Error")
        nmsg += 1