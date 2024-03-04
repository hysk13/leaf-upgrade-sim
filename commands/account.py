import discord
from discord import app_commands
from replit import db


class Account(app_commands.Group):

  @app_commands.command(name="init", description="initializes your account")
  async def init(self, ctx: discord.Interaction):
    if not (str(ctx.user.id) in db.keys()):
      db[str(ctx.user.id)] = {
          "leaf": {
              "type": 0,
              "level": 0,
              "worth": 0,
          },
          "coins": 0,
          "start-point": 0,
      }
      await ctx.response.send_message(
          'Your account has been initialized!\nHappy Gaming~ :D')
    else:
      await ctx.response.send_message(
          'Your account has already been initialized.')

  @app_commands.command(name='delete', description='deletes your account')
  @app_commands.describe(sure='are you sure?')
  async def delete(self, ctx: discord.Interaction, sure: bool):
    if (str(ctx.user.id) in db.keys()):
      if (sure):
        del db[str(ctx.user.id)]
        await ctx.response.send_message(
            'Your account has been deleted~\nHope to see you again soon~ :D')
      else:
        await ctx.response.send_message(
            'Deletion procedures have been canceled.')
    else:
      await ctx.response.send_message(
          'Your account has not been initialized yet.\n"/acc init" to initialize your account~ :D'
      )


async def setup(client):
  client.tree.add_command(Account(name="acc", description="account commands"))
