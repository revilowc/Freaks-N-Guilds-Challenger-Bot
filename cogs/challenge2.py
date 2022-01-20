import discord
import time
from discord.abc import PrivateChannel
from discord.ext import commands

class B1V2(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Sleep by the fire', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B2View(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Dig under the snow', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.unlockedb12 = True
    if self.alreadyb1 == True and self.unlockedb9 == True and self.unlockedb10 == False:
        view = B1V1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    elif self.alreadyb1 == True and self.unlockedb10 == True and self.unlockedb12 == False:
        view = B1V2(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = normalB1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You claw through the freshly fallen snow near the roots of the tree. It’s just dirt! That evil freak on the other side… it must have tricked you!\n\nOut of the corner of your eye, you notice a few colored painted lines. You only saw them for a split second when illuminated by the fire! You excitedly brush the snow away and are greeted by the following image. What could it mean?\n\nYour brain is groggy. You’re cold. So cold. So sleepy. Sleep by the fire?\n\nhttps://media.discordapp.net/attachments/840365409445609472/911279271224414238/unknown.png",
          view=view,
          ephemeral=True)

class B1V1(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Sleep by the fire', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B2View(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label="Go to the lake", style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B9(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "That’s right, you remember… you’re here for the rune. The troll told you about this… was it yesterday? Was that a dream? Trolls can talk? Magic, you remember, as you convince yourself it wasn’t a dream. You’re crazy right? You’re so cold and tired, why are you trekking off into the darkness in the middle of winter?\n\nYou light a makeshift torch from the fire and set out into the blistering cold in the direction of the lake. You can see snow falling sideways, the wind is relentless. You can see the flatness of the lake in the distance as you approach. It looks frozen solid and a fresh coat of snow has covered the top.",
          view=view,
          ephemeral=True)

class B9(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Cross the lake', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.unlockedb10 = True
    if self.alreadyb1 == True and self.unlockedb9 == True and self.unlockedb10 == False:
        view = B1V1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    elif self.alreadyb1 == True and self.unlockedb10 == True and self.unlockedb12 == False:
        view = B1V2(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = normalB1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You cautiously tap your foot, testing the ice. It holds solid. You put all your weight on the ice and begin your trek across.\n\nThe wind is brutal here. With no trees to break up the onslaught, the wind whips your hair and clothes around. The torch, your only source of light and warmth, is blown out completely. In darkness again, you continue walking. You don’t even know if you’re headed in the right direction anymore. You might die out here… You feel your fingers go numb. You’re tired. So tired.\n\nYou trek on, and in the dim moonlight you can make out the shadows of trees in the distance. You hear a piercing howl. Undeterred, you trek on, reaching the far shore. A pair of red eyes greet you on the other side, along with a toothy smile.\n\n“What you seek is back by the fire you silly little human. Dig under the snow where you wake to find the way” The face vanishes. You’re left in the cold darkness, alone. You should probably go back. So sleepy.",
          view=view,
          ephemeral=True)

class normalB1(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Sleep by the fire', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B2View(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
          view=view,
          ephemeral=True)

class B7(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Go to the light", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    if self.alreadyb1 == True and self.unlockedb9 == True and self.unlockedb10 == False:
        view = B1V1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    elif self.alreadyb1 == True and self.unlockedb10 == True and self.unlockedb12 == False:
        view = B1V2(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = normalB1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "You creep closer to the light. It’s a crackling campfire, but no one is around it. How strange, you think.\n\nThe warmth emanates from the fire, a respite from the cold wintery weather. You sidle up to the fire and burrow a small hole in the snow near some tree roots nearby. Tired from the run, and perhaps safe at last, you drift into dreams.", view=view,
          ephemeral=True)

class B5Continue(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Hang out", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.unlockedb9 = True
    if self.alreadyb1 == True and self.unlockedb9 == True and self.unlockedb10 == False:
        view = B1V1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    elif self.alreadyb1 == True and self.unlockedb10 == True and self.unlockedb12 == False:
        view = B1V2(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = normalB1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "The troll continues to sprint towards you, but before it gets too close, it skids to a stop.\n\n“Didn’t want to scare you by walking slowly towards you with this club” the troll conveniently explains. “I need to smash the freshly dried wood to collect as much Ooze as possible before the night. It’s going to get cold and freeze again”\n\n“What is this place” You ask\n\n“The Forest of Freaks” grunts the troll “I know why you’re here… for the rune right? Try crossing the lake when it’s frozen… you may find what you seek. Follow me. I’ll take you somewhere safe.\n\nYou nervously follow the troll. The troll continues to snap trees, drinking the tree’s Ooze as you both meander through the forest. After several hours and a long walk, stars can be seen through the branches. A chill descends upon the forest as you begin to get sleepy. The troll picks you up as you drift into dreams.", view=view,
          ephemeral=True)

  @discord.ui.button(label="Nah, run the fuck away", style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B7(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "Your heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster.\n\nYour heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster. You can see a flickering light in the distance.", view=view,
          ephemeral=True)

class B5Check(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Hang out", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.unlockedb9 = True
    if self.alreadyb1 == True and self.unlockedb9 == True and self.unlockedb10 == False:
        view = B1V1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    elif self.alreadyb1 == True and self.unlockedb10 == True and self.unlockedb12 == False:
        view = B1V2(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = normalB1(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "The troll continues to sprint towards you, but before it gets too close, it skids to a stop.\n\n“Didn’t want to scare you by walking slowly towards you with this club” the troll conveniently explains. “I need to smash the freshly dried wood to collect as much Ooze as possible before the night. It’s going to get cold and freeze again”\n\n“What is this place” You ask\n\n“The Forest of Freaks” grunts the troll “I know why you’re here… for the rune right? Try crossing the lake when it’s frozen… you may find what you seek. Follow me. I’ll take you somewhere safe.\n\nYou nervously follow the troll. The troll continues to snap trees, drinking the tree’s Ooze as you both meander through the forest. After several hours and a long walk, stars can be seen through the branches. A chill descends upon the forest as you begin to get sleepy. The troll picks you up as you drift into dreams.", view=view,
          ephemeral=True)

  @discord.ui.button(label="Nah, run the fuck away", style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B7(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "Your heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster.\n\nYour heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster. You can see a flickering light in the distance.", view=view,
          ephemeral=True)

class B4(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Continue to watch", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B5Continue(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "The troll saunters a bit further, clearly pleased with its work with the trunk. It lets out another groan and snaps another tree in half, grabbing it and chucking it in your general direction. As it turns, it notices something, a colorful bird, just nearby. The troll starts a light jog. It’s getting closer. The bird lets out a chirp and dashes away, flapping above the treetops, and out of sight. But the thundering hasn’t stopped. The troll is in a full-on sprint towards you! Do you hang out or nah, run the fuck away as fast as humanly possible?", view=view,
          ephemeral=True)

  @discord.ui.button(label="Check your surroundings", style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B5Check(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "You take a couple wary glances around. It’s definitely fall alright. And you’re in the same location as you were before… but the flowers aren’t there anymore? The lake glistens in the distance as you hear a loud crack. It’s that troll, snapping another tree. The sun begins to set in the distance. The temperature has dropped slightly as well, you note; the hair on your arms have begun to bristle.\n\nYou continue scanning your surroundings and notice a colorful bird. The bird notices you back and squawks. Sensing movement and vibration in the ground, the bird snaps its attention to the left just in time to see the troll barreling towards it! The bird leaps into the air in a flurry of feathers and the troll swings its deadly club, barely missing it! The troll lets out a bloodcurdling scream and swivels its head, catching a glint of your armor. The troll bounds into a full-on sprint towards you! Do you hang out or nah, run the fuck away as fast as humanly possible?", view=view,
          ephemeral=True)

class B113Else(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Smell the flowers', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B4(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
           "You kneel down next to a particularly lush and colorful flower. You take a long whiff and the sweet scent washes over you. A dopey smile is plastered on your face as your eyelids slide shut. You tip, landing amongst the long grass.\n\nA loud crackle wakes you up. The ground vibrates following a thud in the distance. As you peek your eyes open you see a towering troll stepping through the trees in the distance. It’s dragging one of those spiky clubs you saw in the Guild’s Lair. The troll lets out a loud grunt, readies the club, and swings with lethal force, smashing a tree with no leaves into the forest floor below, snapping the trunk like a twig.\n\nYou realize it a split second later. None of the trees have leaves. The forest floor is covered in orange and brown leaves. It’s fall? You refocus your attention on the troll.", view=view,
          ephemeral=True)

  @discord.ui.button(label='Go to the lake', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    if self.unlockedb12 == False:
        view = B3GoBack(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = B11Else(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
        "The lake comes into view, glistening in the sunrise. It’s odd, this should have been frozen last night given the temperature. It’s still a bit chilly, but no ice can be seen on the vast lake.You bend down closer to the water to take a drink. It’s better than you ever could have dreamed. After your 7 minutes in heaven, you rise, thirst quenched, and ready to rock out with your smock out. It truly is scenic you think, what a bunch of happy little accidents happened for you to get here. Wait how did you get here? It was freezing last night, and before that…? The Lair… and wind… strange..",
        view=view,
        ephemeral=True)

class B12(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Follow", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    await interaction.response.send_message(
              "Reinvigorated with a burst of energy, you crawl to your feet to see the valkyrie in all its glory. You follow it into the lush dark green forest. Just minutes later, you approach a circle of huge stones that are emitting a light orange glow. The Valkyrie motions you to go into the circle, then dashes away. You move to the center.\n\nThe sunlight intensifies. Brutal heat envelops you and the stones begin to shake and glow red. Beneath you, you can feel a rumbling. You step back just before a crystal with a rune on it bursts from the center of the circle, sending loose rocks flying. You got the second rune! You slip it into your pocket as the temperature continues to rise. The rocks burst into flame!\n\n\nCongratulations on completing the quest! You will gain a the knight role and whitelisted role for completing this quest. Please go to the enlisted chat and send your wallet address there! Please do not spam that chat otherwise.",
        ephemeral=True)

    knightsrole = interaction.guild.get_role(902795625253449759)
    whitelistrole = interaction.guild.get_role(924152616114618378)
    peasantrole = interaction.guild.get_role(902788640571277312)
    enlistedchannel = self.client.get_channel(925268802718027796)

    await enlistedchannel.send(f"{interaction.user.mention} Congratulations on completing quest 2! Please send your wallet address here and I will store it for you.")
    await interaction.user.remove_roles(peasantrole, reason="Member completed quest 2")
    await interaction.user.add_roles(knightsrole, whitelistrole, reason="Member completed quest 2")


class B11Else(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label="Go back", style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B113Else(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You return to the area where you awoke. Everything is in full bloom, flowers cover the previously green landscape. Butterflies flutter overhead. You start to feel sleepy again. How, you wonder? “Magic” you muse aloud, with a snort.", view=view,
          ephemeral=True)

  @discord.ui.button(label='Swim across the lake', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B12(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You swan dive into the lake. 10’s from all the judges. Just majestic. It’s chilly in the lake but you’ve experienced worse. Walking on it last night was brutal. Was it last night? Time is weird here, you think. You focus your attention on each stroke, making it slowly further across. It’s getting hotter out. Or maybe you’re just tired. NO! You can’t be tired again! You just slept right? How are you so tired? \n\nThe sun reaches it’s zenith, pummeling you with heat and warming the water bit by bit. It starts to feel like summer. You’re exhausted but are near the far shore where you think you saw the red eyes. You pathetically paddle a bit further, one kick after another. Nearly there. An hour later you arrive at the shore. Every part of your body wants to pass out but you know you can’t. You’re here for a purpose. You’re here to become a hunter… right? Or was that just something someone told you. Wasn’t that an anime? Your memory is fuzzy… A valkyrie bursts from the forest in a beam of blinding light. “Follow me, chosen one”", view=view,
          ephemeral=True)

class B3(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='I am a Celestial', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B3GoBack(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
        "The elf sprints away with a shriek.",
        view=view,
        ephemeral=True)

  @discord.ui.button(label='Nope, not a Celestial', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B3GoBack(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
        "“So what are you then?”\n\n“I… don’t know. I’m human”\n\n“What are you doing in the Forest of Freaks?”\n\n“Searching for something”\n\n“Best hurry. Things change fast here. Then again… they don’t.” The elf sprints away",
        view=view,
        ephemeral=True)

class B3GoBack(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B113Else(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You return to the area where you awoke. Everything is in full bloom, flowers cover the previously green landscape. Butterflies flutter overhead. You start to feel sleepy again. How, you wonder? “Magic” you muse aloud, with a snort.", view=view,
          ephemeral=True)

class B113False(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Follow the elf', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = B3(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
        "You call out “Can I ask you a question?” “Where am I?”\n\nThe elf slinks out of the shadows. “So you’re not a Celestial?”",
        view=view,
        ephemeral=True)

  @discord.ui.button(label='Go to the lake', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    if self.unlockedb12 == False:
        view = B3GoBack(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)
    else:
        view = B11Else(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
        "The lake comes into view, glistening in the sunrise. It’s odd, this should have been frozen last night given the temperature. It’s still a bit chilly, but no ice can be seen on the vast lake.You bend down closer to the water to take a drink. It’s better than you ever could have dreamed. After your 7 minutes in heaven, you rise, thirst quenched, and ready to rock out with your smock out. It truly is scenic you think, what a bunch of happy little accidents happened for you to get here. Wait how did you get here? It was freezing last night, and before that…? The Lair… and wind… strange..",
        view=view,
        ephemeral=True)

class B2View(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Sleep by the fire', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if self.alreadyb2 == False:
        self.alreadyb2 = True
        view = B113False(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

        await interaction.response.send_message(
            "Bird songs echo in the background. Your eyes flutter open. It’s dawn. And damp. How strange, it’s not frost. It feels like spring already!\n\nYou sit up quickly as you come to. You strip off your outer coat and breathe in crisp air as you take in your surroundings. Light green plants cover the forest. It looks like everything is in bloom. An elf pokes their head out from behind a tree, disappearing as quietly as it retreated.\n\nYou’re thirsty and a lake is nearby, you can see it shimmering in the distance.",
            view=view,
            ephemeral=True)

    else:
      view = B113Else(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

      await interaction.response.send_message(
            "You return to the area where you awoke. Everything is in full bloom, flowers cover the previously green landscape. Butterflies flutter overhead. You start to feel sleepy again. How, you wonder? “Magic” you muse aloud, with a snort.", view=view,
            ephemeral=True)

class BeginView(discord.ui.View):
  def __init__(self, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, client):
    super().__init__(timeout=None)
    self.alreadyb2 = alreadyb2
    self.unlockedb12 = unlockedb12
    self.unlockedb9 = unlockedb9
    self.alreadyb1 = alreadyb1
    self.unlockedb10 = unlockedb10
    self.client = client

  @discord.ui.button(label='Begin', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    self.alreadyb2 = False
    self.unlockedb12 = False
    self.unlockedb9 = False
    self.alreadyb1 = False
    self.unlockedb10 = False
    self.alreadyb1 = True
    view = B2View(self.alreadyb2, self.unlockedb12, self.unlockedb9, self.alreadyb1, self.unlockedb10, self.client)

    await interaction.response.send_message(
          "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
          view=view,
          ephemeral=True)

class ChallengeView2(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label='Begin Challenge',
                       style=discord.ButtonStyle.blurple,
                       custom_id='persistent_view:challenge2')
    async def challenge(self, button: discord.ui.Button,
                        interaction: discord.Interaction):
        alreadyb2 = False
        unlockedb12 = False
        unlockedb9 = False
        alreadyb1 = False
        unlockedb10 = False

        startembed = discord.Embed(
            description=f"These quests are a journey to whitelist. Everyone who properly completes the quest while it is open will recieve a whitelist.\n\nHow to play:\nRead the paragraph, and then click one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.\n\nIf you ever want to return to the place you just previously were, just click ‘go back’. You will always have the option ‘go back’ available to you.\n\nTo start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!", color=0x000ff)
        startembed.set_author(name="Challenge 2",
                              icon_url=interaction.guild.icon.url)
        startembed.set_footer(text="Freaks N' Guilds",
                              icon_url=interaction.guild.icon.url)

        startview = BeginView(alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10, self.client)

        await interaction.response.send_message(interaction.user.mention, embed=startembed,
                                        view=startview,
                                        ephemeral=True)

class Challenge2(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    #Commands
    @commands.command(pass_context=True)
    async def challenge2(self, ctx):
        rulesembed = discord.Embed(
            description=f"Click below to begin your Quest.", color=0x000ff)
        rulesembed.set_author(name="Challenge 2", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text="Freaks N' Guilds",
                              icon_url=ctx.guild.icon.url)

        challengeview = ChallengeView2(self.client)

        await ctx.message.delete()

        await ctx.send(embed=rulesembed, view=challengeview)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # In order to do this you need to first send a message with the View, which is shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.client.add_view(ChallengeView2(self.client))
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Challenge2(client))
