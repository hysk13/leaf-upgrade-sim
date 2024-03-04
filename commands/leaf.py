import discord, random
from discord import app_commands
from replit import db

from assets.leaf_data import leaf_data


def UpdateLeafStats(userid, user):
  user['leaf']['worth'] = leaf_data[
      user['leaf']['type']]['worth-per-level'] * user['leaf']['level']
  db[userid] = user


class Leaf(app_commands.Group):

  @app_commands.command(name='view', description='view your leaf stats')
  async def view(self, ctx: discord.Interaction):
    if (str(ctx.user.id) in db.keys()):
      user = db[str(ctx.user.id)]
      leaf_stats = discord.Embed(color=discord.Color.blue())
      leaf_stats.set_author(name=f"{ctx.user.name}'s Leaf:",
                            icon_url=ctx.user.avatar.url)
      leaf_stats.add_field(
          name='Leaf Description',
          value=leaf_data[user['leaf']['type']]['description'],
          inline=False)
      leaf_stats.add_field(name='Leaf Level',
                           value=f"{user['leaf']['level']}  ",
                           inline=True)
      leaf_stats.add_field(name='Leaf Worth',
                           value=f"{user['leaf']['worth']} coins")
      await ctx.response.send_message(embed=leaf_stats)
    else:
      await ctx.response.send_message(
          'Your account has not been initialized yet.\n"/acc init" to initialize your account~ :D'
      )

  @app_commands.command(name='peek',
                        description="view someone else's leaf stats")
  @app_commands.describe(target='who to peek at')
  async def peek(self, ctx: discord.Interaction, target: discord.Member):
    if (str(target.id) in db.keys()):
      user = db[str(target.id)]
      leaf_stats = discord.Embed(color=discord.Color.blue())
      leaf_stats.set_author(name=f"{ctx.user.name}'s Leaf:",
                            icon_url=ctx.user.avatar.url)
      leaf_stats.add_field(
          name='Leaf Description',
          value=leaf_data[user['leaf']['type']]['description'],
          inline=False)
      leaf_stats.add_field(name='Leaf Level',
                           value=user['leaf']['level'],
                           inline=True)
      leaf_stats.add_field(name='Leaf Worth',
                           value=f"{user['leaf']['worth']} coins")
      await ctx.response.send_message(embed=leaf_stats)
    else:
      await ctx.response.send_message(
          'Selected user does not have an initialized account~ :D')

  @app_commands.command(name='upgrade', description="upgrade your leaf")
  async def upgrade(self, ctx: discord.Interaction, sure: bool):
    try:
      if (str(ctx.user.id) in db.keys()):
        user = db[str(ctx.user.id)]
        if (sure):
          if ((user['leaf']['level'] > 0
               and random.randint(0, user['leaf']['level'] + 1) == 1)
              or (user['leaf']['level'] == 0)):
            user['leaf']['level'] += 1
            if (user['leaf']['level'] > 20
                and user['leaf']['type'] != len(leaf_data) - 1):
              user['leaf']['type'] += 1
              await ctx.response.send_message(
                  'Upgrade Success!\nYour leaf evolved!\n"/leaf view" to check your new stats~ :D'
              )
              UpdateLeafStats(ctx.user.id, user)
              return
            await ctx.response.send_message(
                'Upgrade Success!\n"/leaf view" to check your new stats~ :D')
            UpdateLeafStats(ctx.user.id, user)
          else:
            if (user['leaf']['level'] > 0):
              db[str(ctx.user.id)]['leaf']['level'] -= 1
            elif (user['leaf']['type'] != 0):
              db[str(ctx.user.id)]['leaf']['type'] -= 1
            else:
              await ctx.response.send_message(
                  'Upgrade failed...\nHowever, your level did not decrease, for you are at the lowest level~ :D'
              )
              return
            await ctx.response.send_message(
                'Upgrade failed...\nYour leaf decreased a level\n"/leaf view" to check your new stats~ :D'
            )
        else:
          await ctx.response.send_message(
              'Upgrade procedures have been canceled.')
      else:
        await ctx.response.send_message(
            'Your account has not been initialized yet.\n"/acc init" to initialize your account~ :D'
        )
    except AttributeError:
      pass


async def setup(client):
  client.tree.add_command(Leaf(name='leaf', description='leaf commands'))
