import discord
from discord import app_commands

from assets.cmd import cmds


class About(app_commands.Group):

  @app_commands.command(name='bot', description='about this bot')
  async def bot(self, ctx: discord.Interaction):
    await ctx.response.send_message(
        'Hello!\nI am Leaf Upgrade Simulator Bot.\nI am a bot that hosts a simple game of Leaf Upgrade Simulator.\nI was developed by @hys_13 and @snu_08!\nTo learn how to play the game, please use "/about howto"~ :D'
    )

  @app_commands.command(name='howto', description='how to play the game')
  async def howto(self, ctx: discord.Interaction):
    await ctx.response.send_message(
        'This is a really simple game.\nYour goal is to earn as much coins as possible, which can be obtained by selling your leaf.\nThe value of the leaf increases as you upgrade them.\nTo learn about the commands, please use "/about cmds"~ :D'
    )

  @app_commands.command(name='cmds', description='list of commands')
  async def cmds(self, ctx: discord.Interaction):
    await ctx.response.send_message("\n".join(cmds))

  @app_commands.command(name='src', description='link to source code')
  async def src(self, ctx: discord.Interaction):
    src_embed = discord.Embed(
        color=discord.Color.dark_purple(),
        url="https://github.com/hysk13/leaf-upgrade-sim",
        title="Source Code",
        description="Source code to the {Leaf Upgrade Simulator} on GitHub")
    await ctx.response.send_message(embed=src_embed)


async def setup(client):
  client.tree.add_command(About(name="about", description="about commands"))
