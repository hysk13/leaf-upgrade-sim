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

  @app_commands.command(name='compare',
                        description='compare with another player')
  @app_commands.describe(target='who to compare to')
  async def compare(self, ctx: discord.Interaction, target: discord.Member):
    if (str(ctx.user.id) in db.keys() and str(target.id) in db.keys()):
      user = db[str(ctx.user.id)]
      targ = db[str(target.id)]
      compare_embed = discord.Embed(color=discord.Color.purple())
      compare_embed.set_author(name=f"{ctx.user.name} vs. {target.name}",
                               icon_url=ctx.user.avatar.url)
      compare_embed.add_field(name='Leaf Comparison', inline=False)
      compare_embed.add_field(
          name=f"{ctx.user.name}'s Leaf",
          value=
          f"{leaf_data[user['leaf']['type']]} | Level {user['leaf']['level']}",
          inline=True)
      compare_embed.add_field(
          name=f"{targ.name}'s Leaf",
          value=
          f"{leaf_data[targ['leaf']['type']]} | Level {targ['leaf']['level']}",
          inline=True)
      compare_embed.add_field(name='Coin Comparison', inline=False)
      compare_embed.add_field(name=f"{ctx.user.name}'s Coin",
                              value=f"{user['coins']} coins",
                              inline=True)
      compare_embed.add_fied(name=f"{targ.name}'s Coin",
                             value=f"{targ['coins']} coins",
                             inline=True)
      compare_embed.add_field(name='Rank Comparison', inline=False)
      compare_embed.add_field(name=f"{ctx.user.name}'s Rank",
                              value=f"{user['start-point']}",
                              inline=True)
      compare_embed.add_field(name=f"{targ.name}'s Rank",
                              value=f"{targ['start-point']}",
                              inline=True)
      await ctx.response.send_message(embed=compare_embed)
    else:
      await ctx.response.send_message(
          f'Either/both of you and {target.name} do not have their account initialized\n"/acc init" to initialize your accounts~ :D'
      )


async def setup(client):
  client.tree.add_command(
      Character(name='char', description='character commands'))
