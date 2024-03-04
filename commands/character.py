import discord
from discord import app_commands
from replit import db

from assets.leaf_data import leaf_data


class Character(app_commands.Group):

  @app_commands.command(name='stats', description='view your character stats')
  async def stats(self, ctx: discord.Interaction):
    if (str(ctx.user.id) in db.keys()):
      user = db[str(ctx.user.id)]
      user_stats = discord.Embed(color=discord.Color.green())
      user_stats.set_author(name=f"{ctx.user.name}'s Stats:",
                            icon_url=ctx.user.avatar.url)
      user_stats.add_field(
          name='Leaf',
          value=
          f"{leaf_data[user['leaf']['type']]['name']} | Level {user['leaf']['level']}",
          inline=False)
      user_stats.add_field(name='Coin',
                           value=f"{user['coins']} coins",
                           inline=True)
      user_stats.add_field(name='Rank', value=user['start-point'], inline=True)
      await ctx.response.send_message(embed=user_stats)
    else:
      await ctx.response.send_message(
          'Your account has not been initalized yet.\n"/acc init" to initalize your account~ :D'
      )


async def setup(client):
  client.tree.add_command(
      Character(name='char', description='character commands'))
