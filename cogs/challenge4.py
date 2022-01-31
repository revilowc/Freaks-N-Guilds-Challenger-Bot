import discord
import discord.utils
from discord.ext import commands, tasks
from discord.commands import slash_command, permissions, Option

import os
import re
from dotenv import load_dotenv

load_dotenv()

embedcolor = int(os.getenv('embedcolor'), 16)
pfpurl = os.getenv('pfpurl')
footertext = os.getenv('footertext')

guildIDs = os.getenv('guildIDs')
guildIDs = guildIDs.split(',')
guildIDs = [int(x) for x in guildIDs]

whitelistroleid = int(os.getenv('whitelistroleid'))
whitelistchannelid = int(os.getenv('whitelistchannelid'))
goldroleid = int(os.getenv('godroleid'))
clientuserid = int(os.getenv('clientuserid'))
token = os.getenv('bottoken')

class Challenge4(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    @slash_command(guild_ids=guildIDs, description="Collect wallet addresses")
    async def collect(self, ctx):
        await ctx.interaction.response.defer()
        whitelistchannel = self.client.get_channel(whitelistchannelid)
        allmessages = await whitelistchannel.history(limit=None).flatten()

        completedquest3 = []
        completedquest2 = []
        completedquest1 = []
        othermethod = []
        c1and2 = []
        c2and3 = []
        call = []
        allidsandwallets = []

        for message in allmessages:
            if message.author == self.client.user:
                if "Congratulations on completing quest 3!" in message.content:
                    completedquest3.append(re.sub("[^0-9]", "", message.content.split(
                        " ")[0]))
                elif "Congratulations on completing quest 2!" in message.content:
                    completedquest2.append(re.sub("[^0-9]", "", message.content.split(
                        " ")[0]))
                elif "Congratulations on completing quest 1!" in message.content:
                    completedquest1.append(re.sub("[^0-9]", "", message.content.split(
                        " ")[0]))

                elif message.content[:3] == "Got":
                    allidsandwallets.append(re.sub("[^0-9]", "", message.content.split(
                        " ")[2]) + "/" + message.content.split(" ")[-1][2:-3])

        for idandwallet in allidsandwallets:
            if idandwallet.split("/")[0] not in completedquest1 and idandwallet.split("/")[0] not in completedquest2 and idandwallet.split("/")[0] not in completedquest3:
                try:
                    member = self.client.get_user(int(idandwallet.split("/")[0]))
                    othermethod.append(member.name + "#" + member.discriminator +
                                       "/" + idandwallet.split("/")[1])
                except:
                    continue

            if idandwallet.split("/")[0] in completedquest1:
                try:
                    member = self.client.get_user(int(idandwallet.split("/")[0]))
                    completedquest1[completedquest1.index(idandwallet.split(
                        "/")[0])] = member.name + "#" + member.discriminator + "/" + idandwallet.split("/")[1]
                except:
                    continue

            if idandwallet.split("/")[0] in completedquest2:
                try:
                    member = self.client.get_user(int(idandwallet.split("/")[0]))
                    completedquest2[completedquest2.index(idandwallet.split(
                        "/")[0])] = member.name + "#" + member.discriminator + "/" + idandwallet.split("/")[1]
                except:
                    continue

            if idandwallet.split("/")[0] in completedquest3:
                try:
                    member = self.client.get_user(int(idandwallet.split("/")[0]))
                    completedquest3[completedquest3.index(idandwallet.split(
                        "/")[0])] = member.name + "#" + member.discriminator + "/" + idandwallet.split("/")[1]
                except:
                    continue

        for id in completedquest1:
            if "/" not in id:
                try:
                    member = self.client.get_user(int(id))
                    completedquest1[completedquest1.index(
                        id)] = member.name + "#" + member.discriminator + "/" + "!!!!!!!NO WALLET ADDRESS SUBMITTED!!!!!!!"
                except:
                    continue

        for id in completedquest2:
            if "/" not in id:
                try:
                    member = self.client.get_user(int(id))
                    completedquest2[completedquest2.index(
                        id)] = member.name + "#" + member.discriminator + "/" + "!!!!!!!NO WALLET ADDRESS SUBMITTED!!!!!!!"
                except:
                    continue

        for id in completedquest3:
            if "/" not in id:
                try:
                    member = self.client.get_user(int(id))
                    completedquest3[completedquest3.index(
                        id)] = member.name + "#" + member.discriminator + "/" + "!!!!!!!NO WALLET ADDRESS SUBMITTED!!!!!!!"
                except:
                    continue

        for nameandwallet in completedquest1:
            if nameandwallet in completedquest2:
                c1and2.append(nameandwallet)

        for nameandwallet in completedquest2:
            if nameandwallet in completedquest3:
                c2and3.append(nameandwallet)

        for nameandwallet in completedquest1:
            if nameandwallet in completedquest2:
                if nameandwallet in completedquest3:
                    call.append(nameandwallet)

        completedquest1 = "\n".join(completedquest1)
        with open("completedquest1walletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(completedquest1)

        completedquest2 = "\n".join(completedquest2)
        with open("completedquest2walletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(completedquest2)

        completedquest3 = "\n".join(completedquest3)
        with open("completedquest3walletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(completedquest3)

        c1and2 = "\n".join(c1and2)
        with open("completedquest1and2walletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(c1and2)

        c2and3 = "\n".join(c2and3)
        with open("completedquest2and3walletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(c2and3)

        call = "\n".join(call)
        with open("completedallquestswalletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(call)

        othermethod = "\n".join(othermethod)
        with open("othermethodwalletaddresses.txt", "w", encoding='utf-8') as f:
            f.write(othermethod)

        await ctx.interaction.followup.send(embed=discord.Embed(description="**Finished collecting all wallet addresses and separated by quests and other methods for whitelist!**", color=embedcolor), ephemeral=True)

def setup(client):
    client.add_cog(Challenge4(client))
