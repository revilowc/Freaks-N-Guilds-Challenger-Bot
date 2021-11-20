import discord
import time
from discord.ext import commands

class OneButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()
        self.view.clear_items()

        await interaction.response.edit_message(view=self.view)


class OneView(discord.ui.View):
    def __init__(self, label):
        super().__init__()

        self.add_item(OneButton(label))
        self.timeout = False

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True


class TwoButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        self.label = label

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()
        self.view.clear_items()

        if self.view.label1 == self.label:
            self.view.choice = 1
        elif self.view.label2 == self.label:
            self.view.choice = 2

        await interaction.response.edit_message(view=self.view)


class TwoView(discord.ui.View):
    def __init__(self, label1, label2):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.choice = 0
        self.timeout = False

        self.add_item(TwoButton(label1))
        self.add_item(TwoButton(label2))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True


class ThreeButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        self.label = label

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()
        self.view.clear_items()

        if self.view.label1 == self.label:
            self.view.choice = 1
        elif self.view.label2 == self.label:
            self.view.choice = 2
        elif self.view.label3 == self.label:
            self.view.choice = 3

        await interaction.response.edit_message(view=self.view)


class ThreeView(discord.ui.View):
    def __init__(self, label1, label2, label3):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.choice = 0
        self.timeout = False

        self.add_item(ThreeButton(label1))
        self.add_item(ThreeButton(label2))
        self.add_item(ThreeButton(label3))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True


class FourButton(discord.ui.Button):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        self.label = label

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()
        self.view.clear_items()

        if self.view.label1 == self.label:
            self.view.choice = 1
        elif self.view.label2 == self.label:
            self.view.choice = 2
        elif self.view.label3 == self.label:
            self.view.choice = 3
        elif self.view.label4 == self.label:
            self.view.choice = 4

        await interaction.response.edit_message(view=self.view)


class FourView(discord.ui.View):
    def __init__(self, label1, label2, label3, label4):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.choice = 0
        self.timeout = False

        self.add_item(FourButton(label1))
        self.add_item(FourButton(label2))
        self.add_item(FourButton(label3))
        self.add_item(FourButton(label4))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True


async def B1(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  if alreadyb1 == False:
    alreadyb1 = True
    b1view = OneView("Sleep by the fire")

    await interaction.followup.send(
        "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
        view=b1view,
        ephemeral=True)

    await b1view.wait()

    if b1view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  elif alreadyb1 == True and unlockedb9 == True and unlockedb10 == False:
    b1view2 = TwoView("Sleep by the fire", "Go to the lake")

    await interaction.followup.send(
        "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
        view=b1view2,
        ephemeral=True)

    await b1view2.wait()

    if b1view2.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif b1view2.choice == 1:
      await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

    elif b1view2.choice == 2:
      await B9(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  elif alreadyb1 == True and unlockedb10 == True and unlockedb12 == False:
    b1view4 = TwoView("Sleep by the fire", "Dig under the snow")

    await interaction.followup.send(
        "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
        view=b1view4,
        ephemeral=True)

    await b1view4.wait()

    if b1view4.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif b1view4.choice == 1:
      await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

    elif b1view4.choice == 2:
      await B10(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  else:
    b1view3 = OneView("Sleep by the fire")

    await interaction.followup.send(
        "You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Good, good. So cold. So tired.",
        view=b1view3,
        ephemeral=True)

    await b1view3.wait()

    if b1view3.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)


async def B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
    if alreadyb2 == False:
        alreadyb2 = True

        b2view = TwoView("Follow the elf", "Go to the lake")

        await interaction.followup.send(
            "Bird songs echo in the background. Your eyes flutter open. It’s dawn. And damp. How strange, it’s not frost. It feels like spring already!",
            ephemeral=True)
        time.sleep(3)
        await interaction.followup.send(
            "You sit up quickly as you come to. You strip off your outer coat and breathe in crisp air as you take in your surroundings. Light green plants cover the forest. It looks like everything is in bloom. An elf pokes their head out from behind a tree, disappearing as quietly as it retreated.",
            ephemeral=True)
        time.sleep(5)
        await interaction.followup.send(
            "You’re thirsty and a lake is nearby, you can see it shimmering in the distance.",
            view=b2view,
            ephemeral=True)

        await b2view.wait()

        if b2view.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

        elif b2view.choice == 1:
            await B3(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

        elif b2view.choice == 2:
            await B11(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

    else:
      b2view2 = TwoView("Go to the lake", "Smell the flowers")

      await interaction.followup.send(
            "You return to the area where you awoke. Everything is in full bloom, flowers cover the previously green landscape. Butterflies flutter overhead. You start to feel sleepy again. How, you wonder? “Magic” you muse aloud, with a snort.", view=b2view2,
            ephemeral=True)
      await b2view2.wait()

      if b2view2.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

      elif b2view2.choice == 1:
        await B11(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

      elif b2view2.choice == 2:
        await B4(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B4 (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b4view = TwoView("Continue to watch", "Check your surroundings")

  await interaction.followup.send(
            "You kneel down next to a particularly lush and colorful flower. You take a long whiff and the sweet scent washes over you. A dopey smile is plastered on your face as your eyelids slide shut. You tip, landing amongst the long grass.",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
            "A loud crackle wakes you up. The ground vibrates following a thud in the distance. As you peek your eyes open you see a towering troll stepping through the trees in the distance. It’s dragging one of those spiky clubs you saw in the Guild’s Lair. The troll lets out a loud grunt, readies the club, and swings with lethal force, smashing a tree with no leaves into the forest floor below, snapping the trunk like a twig.",
            ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
            "You realize it a split second later. None of the trees have leaves. The forest floor is covered in orange and brown leaves. It’s fall? You refocus your attention on the troll.",
            view=b4view,
            ephemeral=True)

  await b4view.wait()

  if b4view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  elif b4view.choice == 1:

    await B5continue(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  elif b4view.choice == 2:

    await B5check(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B5check (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b5checkview = TwoView("Hang out", "Nah, run the fuck away")

  await interaction.followup.send(
            "You take a couple wary glances around. It’s definitely fall alright. And you’re in the same location as you were before… but the flowers aren’t there anymore? The lake glistens in the distance as you hear a loud crack. It’s that troll, snapping another tree. The sun begins to set in the distance. The temperature has dropped slightly as well, you note; the hair on your arms have begun to bristle.",
            ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
            "You continue scanning your surroundings and notice a colorful bird. The bird notices you back and squawks. Sensing movement and vibration in the ground, the bird snaps its attention to the left just in time to see the troll barreling towards it! The bird leaps into the air in a flurry of feathers and the troll swings its deadly club, barely missing it! The troll lets out a bloodcurdling scream and swivels its head, catching a glint of your armor. The troll bounds into a full-on sprint towards you! Do you hang out or nah, run the fuck away as fast as humanly possible?", view=b5checkview,
            ephemeral=True)

  await b5checkview.wait()

  if b5checkview.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  elif b5checkview.choice == 1:
    await B6(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  elif b5checkview.choice == 2:
    await B7(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B5continue (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b5continueview = TwoView("Hang out", "Nah, run the fuck away")

  await interaction.followup.send(
            "The troll saunters a bit further, clearly pleased with its work with the trunk. It lets out another groan and snaps another tree in half, grabbing it and chucking it in your general direction. As it turns, it notices something, a colorful bird, just nearby. The troll starts a light jog. It’s getting closer. The bird lets out a chirp and dashes away, flapping above the treetops, and out of sight. But the thundering hasn’t stopped. The troll is in a full-on sprint towards you! Do you hang out or nah, run the fuck away as fast as humanly possible?", view=b5continueview,
            ephemeral=True)

  await b5continueview.wait()

  if b5continueview.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  elif b5continueview.choice == 1:
    await B6(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  elif b5continueview.choice == 2:
    await B7(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B6 (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b6view = OneView("Sleep")

  await interaction.followup.send(
            "The troll continues to sprint towards you, but before it gets too close, it skids to a stop.",
            ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
            "“Didn’t want to scare you by walking slowly towards you with this club” the troll conveniently explains. “I need to smash the freshly dried wood to collect as much Ooze as possible before the night. It’s going to get cold and freeze again”",
            ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
            "“What is this place” You ask",
            ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
            "“The Forest of Freaks” grunts the troll “I know why you’re here… for the rune right? Try crossing the lake when it’s frozen… you may find what you seek. Follow me. I’ll take you somewhere safe.",
            ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
            "You nervously follow the troll. The troll continues to snap trees, drinking the tree’s Ooze as you both meander through the forest. After several hours and a long walk, stars can be seen through the branches. A chill descends upon the forest as you begin to get sleepy. The troll picks you up as you drift into dreams.", view=b6view,
            ephemeral=True)

  await b6view.wait()

  if b6view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  unlockedb9 = True
  await B1(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B7 (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b7view = OneView("Go to the light")

  await interaction.followup.send(
            "Your heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster.",
            ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
            "Your heart is pounding out of your chest, it’s hard to run. Every minute you sneak a glance back. The freak is still after you, snapping trees like an unstoppable juggernaut hell-bent on smashing you. You pick up the pace, sprinting faster. You can see a flickering light in the distance.", view=b7view,
            ephemeral=True)

  await b7view.wait()

  if b7view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  await B8(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B8 (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b8view = OneView("Fall asleep")

  await interaction.followup.send(
            "You creep closer to the light. It’s a crackling campfire, but no one is around it. How strange, you think.",
            ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
            "The warmth emanates from the fire, a respite from the cold wintery weather. You sidle up to the fire and burrow a small hole in the snow near some tree roots nearby. Tired from the run, and perhaps safe at last, you drift into dreams.", view=b8view,
            ephemeral=True)

  await b8view.wait()

  if b8view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  await B1(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B9(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b9view = OneView("Cross the lake")
  b9view2 = OneView("Go back")

  await interaction.followup.send(
            "That’s right, you remember… you’re here for the rune. The troll told you about this… was it yesterday? Was that a dream? Trolls can talk? Magic, you remember, as you convince yourself it wasn’t a dream. You’re crazy right? You’re so cold and tired, why are you trekking off into the darkness in the middle of winter?",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
            "You light a makeshift torch from the fire and set out into the blistering cold in the direction of the lake. You can see snow falling sideways, the wind is relentless. You can see the flatness of the lake in the distance as you approach. It looks frozen solid and a fresh coat of snow has covered the top.", view=b9view, ephemeral=True)

  await b9view.wait()

  if b9view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  await interaction.followup.send(
            "You cautiously tap your foot, testing the ice. It holds solid. You put all your weight on the ice and begin your trek across.",
            ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
            "The wind is brutal here. With no trees to break up the onslaught, the wind whips your hair and clothes around. The torch, your only source of light and warmth, is blown out completely. In darkness again, you continue walking. You don’t even know if you’re headed in the right direction anymore. You might die out here… You feel your fingers go numb. You’re tired. So tired.",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
            "You trek on, and in the dim moonlight you can make out the shadows of trees in the distance. You hear a piercing howl. Undeterred, you trek on, reaching the far shore. A pair of red eyes greet you on the other side, along with a toothy smile.",
            ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
            "“What you seek is back by the fire you silly little human. Dig under the snow where you wake to find the way” The face vanishes. You’re left in the cold darkness, alone. You should probably go back. So sleepy.", view=b9view2,
            ephemeral=True)

  await b9view2.wait()

  if b9view2.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  unlockedb10 = True
  await B1(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B10(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b10view = OneView("Sleep by the fire")

  await interaction.followup.send(
            "You claw through the freshly fallen snow near the roots of the tree. It’s just dirt! That evil freak on the other side… it must have tricked you!",
            ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
            "Out of the corner of your eye, you notice a few colored painted lines. You only saw them for a split second when illuminated by the fire! You excitedly brush the snow away and are greeted by the following image. What could it mean?",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send("https://media.discordapp.net/attachments/840365409445609472/911279271224414238/unknown.png", ephemeral=True)
  await interaction.followup.send(
            "Your brain is groggy. You’re cold. So cold. So sleepy. Sleep by the fire?", view=b10view,
            ephemeral=True)

  await b10view.wait()

  if b10view.timeout == True:
    await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
    return

  unlockedb12 = True
  await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B11 (interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  if unlockedb12 == False:
        b11goback = OneView("Go back")

        await interaction.followup.send(
            "The lake comes into view, glistening in the sunrise. It’s odd, this should have been frozen last night given the temperature. It’s still a bit chilly, but no ice can be seen on the vast lake.",
            ephemeral=True)
        time.sleep(4)
        await interaction.followup.send(
            "You bend down closer to the water to take a drink. It’s better than you ever could have dreamed. After your 7 minutes in heaven, you rise, thirst quenched, and ready to rock out with your smock out. It truly is scenic you think, what a bunch of happy little accidents happened for you to get here. Wait how did you get here? It was freezing last night, and before that…? The Lair… and wind… strange..",
            view=b11goback,
            ephemeral=True)

        await b11goback.wait()

        if b11goback.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

        await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

  else:
    b11view = TwoView("Go back", "Swim across the lake")

    await interaction.followup.send(
            "The lake comes into view, glistening in the sunrise. It’s odd, this should have been frozen last night given the temperature. It’s still a bit chilly, but no ice can be seen on the vast lake.",
            ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
            "You bend down closer to the water to take a drink. It’s better than you ever could have dreamed. After your 7 minutes in heaven, you rise, thirst quenched, and ready to rock out with your smock out. It truly is scenic you think, what a bunch of happy little accidents happened for you to get here. Wait how did you get here? It was freezing last night, and before that…? The Lair… and wind… strange..",
            view=b11view,
            ephemeral=True)

    await b11view.wait()

    if b11view.timeout == True:
        await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
        return

    elif b11view.choice == 1:
        await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

    elif b11view.choice == 2:
        await B12(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B12(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
  b12view = OneView("Follow")

  await interaction.followup.send(
            "You swan dive into the lake. 10’s from all the judges. Just majestic.",
            ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
            "It’s chilly in the lake but you’ve experienced worse. Walking on it last night was brutal. Was it last night? Time is weird here, you think. You focus your attention on each stroke, making it slowly further across. It’s getting hotter out. Or maybe you’re just tired. NO! You can’t be tired again! You just slept right? How are you so tired?",
            ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
            "The sun reaches it’s zenith, pummeling you with heat and warming the water bit by bit. It starts to feel like summer. You’re exhausted but are near the far shore where you think you saw the red eyes. You pathetically paddle a bit further, one kick after another. Nearly there.",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
            "An hour later you arrive at the shore. Every part of your body wants to pass out but you know you can’t. You’re here for a purpose. You’re here to become a hunter… right? Or was that just something someone told you. Wasn’t that an anime? Your memory is fuzzy…",
            ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
            "A valkyrie bursts from the forest in a beam of blinding light. “Follow me, chosen one”", view=b12view,
            ephemeral=True)

  await b12view.wait()

  if b12view.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

  await B13(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

async def B13(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):

  await interaction.followup.send(
            "Reinvigorated with a burst of energy, you crawl to your feet to see the valkyrie in all its glory. You follow it into the lush dark green forest. Just minutes later, you approach a circle of huge stones that are emitting a light orange glow. The Valkyrie motions you to go into the circle, then dashes away. You move to the center.",
            ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
            "The sunlight intensifies. Brutal heat envelops you and the stones begin to shake and glow red. Beneath you, you can feel a rumbling. You step back just before a crystal with a rune on it bursts from the center of the circle, sending loose rocks flying. You got the second rune! You slip it into your pocket as the temperature continues to rise. The rocks burst into flame!",
            ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(embed=discord.Embed(description="**Congratulations on completing the second challenge!**", color=0x000ff), ephemeral=True)

async def B3(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10):
    b3view = TwoView("I am a Celestial", "Nope, not a Celestial")
    b3goback = OneView("Go back")

    await interaction.followup.send(
        "You call out “Can I ask you a question?” “Where am I?”",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "The elf slinks out of the shadows. “So you’re not a Celestial?”",
        view=b3view,
        ephemeral=True)

    await b3view.wait()

    if b3view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif b3view.choice == 1:
        await interaction.followup.send("The elf sprints away with a shriek.",
                                        view=b3goback,
                                        ephemeral=True)

        await b3goback.wait()

        if b3goback.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

        await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)

    elif b3view.choice == 2:
        await interaction.followup.send("“So what are you then?”",
                                        ephemeral=True)
        time.sleep(1)
        await interaction.followup.send("“I… don’t know. I’m human”",
                                        ephemeral=True)
        time.sleep(1)
        await interaction.followup.send(
            "“What are you doing in the Forest of Freaks?”", ephemeral=True)
        time.sleep(1)
        await interaction.followup.send("“Searching for something”",
                                        ephemeral=True)
        time.sleep(1)
        await interaction.followup.send(
            "“Best hurry. Things change fast here. Then again… they don’t.” The elf sprints away",
            view=b3goback,
            ephemeral=True)

        await b3goback.wait()

        if b3goback.timeout == True:
            await interaction.followup.send(
                "Timed out... Don't you know how to click buttons?!",
                ephemeral=True)
            return

        await B2(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)


class ChallengeView2(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

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

        await interaction.response.defer()

        startembed = discord.Embed(
            description=
            "\n   How to play:\n\nRead the paragraph, and then click on one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.To start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!",
            color=0x000ff)
        startembed.set_author(name="Challenge 2",
                              icon_url=interaction.guild.icon.url)
        startembed.set_footer(text="Freaks N' Guilds",
                              icon_url=interaction.guild.icon.url)

        startview = OneView("Begin")

        await interaction.followup.send(embed=startembed,
                                        view=startview,
                                        ephemeral=True)
        await interaction.followup.send(interaction.user.mention,
                                        ephemeral=True)

        await startview.wait()

        await B1(interaction, alreadyb2, unlockedb12, unlockedb9, alreadyb1, unlockedb10)


class Challenge2(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    #Commands
    @commands.command(pass_context=True)
    async def challenge2(self, ctx):
        rulesembed = discord.Embed(
            description=f"Click below to begin your challenge.", color=0x000ff)
        rulesembed.set_author(name="Challenge 2", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text="Freaks N' Guilds",
                              icon_url=ctx.guild.icon.url)

        challengeview = ChallengeView2()

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
            self.client.add_view(ChallengeView2())
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Challenge2(client))
