import discord
from discord import app_commands
from replit import db

from assets.leaf_data import leaf_data


class Shop(app_commands.Group):

  @app_commands.command(name='sell')
  async def sell(self, ctx: discord.Interaction, sure: bool):
    if (str(ctx.user.id) in db.keys()):
      if (sure):
        user = db[str(ctx.user.id)]
        user['coins'] += user['leaf']['worth']
        worth = user['leaf']['worth']
        db[str(ctx.user.id)]['leaf'] = {
            "type": db[str(ctx.user.id)]['start-point'],
            "level": 0,
            "worth": 0,
        }
        await ctx.response.send_message(
            f'Successfully sold your leaf.\nWe added {worth} coins to your balance.'
        )
      else:
        await ctx.response.send_message('Sell procedures have been canceled.')
    else:
      await ctx.response.send_message(
          'Your account has not been initalized yet.\n"/acc init" to initalize your account~ :D'
      )

  @app_commands.command(name='rankup')
  async def rankup(self, ctx: discord.Interaction, sure: bool):
    if (str(ctx.user.id) in db.keys()):
      if (sure):
        user = db[str(ctx.user.id)]
        if (user['coins'] >= user['start-point'] * 50 + 100):
          if not (user['start-point'] == len(leaf_data) - 1):
            user['coins'] -= user['start-point']
            db[str(ctx.user.id)] = user
            await ctx.response.send_message(
                f'Congratulations! Upon selling, you will now start at {leaf_data[db[str(ctx.user.id)]["start-point"]]["name"]}~ :D'
            )
          else:
            await ctx.response.send_message(
                f'You are already at the highest rank!')
        else:
          await ctx.response.send_message(
              f'You do not have enough coins.\nTo rank up, you must pay {user["start-point"]*50+100} coins, but you are lacking {(user["start-point"]*50+100)-(user["coins"])}.'
          )
      else:
        await ctx.response.send_message('Rankup procedures have been canceled.'
                                        )
    else:
      await ctx.response.send_message(
          'Your account has not been initialized yet.\n"/acc init" to initialize your account~ :D'
      )


async def setup(client):
  client.tree.add_command(Shop(name="shop", description="shop commands"))
