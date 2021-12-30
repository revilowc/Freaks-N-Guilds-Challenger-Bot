import discord
import time
from discord.ext import commands

class Dropdown(discord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Clair the Clairvoyant'),
            discord.SelectOption(label='Wanda the Witch'),
            discord.SelectOption(label='Vlad the Game Stopper'),
            discord.SelectOption(label='Satoshi the Wise'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Select the name of the owner...',
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == 'Satoshi the Wise':
          self.view.win = True

        self.view.clear_items()
        self.view.stop()

        await interaction.response.edit_message(view=self.view)



class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.win = False
        self.timeout = False

        self.add_item(Dropdown())

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True

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


async def intro_room(interaction, x, y, p, l):
    rockview = OneView("Go to rock")

    await interaction.followup.send("...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send("\nHuh? Are you dead…?", ephemeral=True)
    await interaction.followup.send("\n\nIt looks like they’re breathing",
                                    ephemeral=True)
    time.sleep(1)
    await interaction.followup.send("\n\nWAKE UP SWINE!", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou feel a studded boot press into your back. Dazed, you sit up. It’s hard to see, light seems so far away. Your eyes begin to adjust to the darkness.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou let out a loud gasp as the freakish face of an ogre, snot dribbling down his chin, comes into view. A second ogre peers from the left. 'What do you want?' you say.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\n'Do you not remember? Do you not know?' the second ogre grumbled under its breath.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nThe Creator of Worlds has shaken up the planet, mixing light and dark freaks together. What once was a peaceful land is now teeming with conflict. The Creator of Worlds proclaimed to the land that a contest would be held to determine who is most worthy to become the first hunters, guild members; owners of us freaks. There are only 2000 spots available. If you can open the ancient chest, you’ll claim your rightful spot. But to open the chest, you’ll need the 4 runes. Each rune can be found in a particular location in the land. The first will lead to the second, and so on",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nKinda like that Earth movie ‘Ready Slayer Won’” grumbled the second ogre",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nRight, you gotta find the 4 runes. The first one is around here somewhere, in the Guild’s Lair",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou stand up, and memories flood into your brain, tuning out the sounds of the ogres. It’s odd, this isn’t your first time here you don’t think. You have memories of great battles, hunting freaks, and forming friendships with guilds. You begin to feel power course through your body. You know you’re meant for something more. Could you be a hunter?",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nWe freaks can’t become hunters, nor would we want to, we want the Ooze, that’s all we’re here for” said the first ogre, droning on.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou thank the ogres and tell them to keep moving. Maybe it’s a trick of the light, but your eyes have adjusted so well to the darkness that you can see distinct shapes of shrubbery and rock formations. You sense that you’re supposed to go to the rock formation...",
        view=rockview,
        ephemeral=True)

    await rockview.wait()

    if rockview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1_room(interaction, x, y, p, l)


async def A1_room(interaction, x, y, p, l):
    pilferview = OneView("Pilfer")

    await interaction.followup.send(
        "\n\nYou approach the rock formation. The vitality inside you is getting stronger and your eyes have almost perfect night vision at this point. You climb down and around the rocks until you see a cave entrance.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\nYou peer into the cave and see mounds of treasure. Pilfer?",
        view=pilferview,
        ephemeral=True)

    await pilferview.wait()

    if pilferview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1P1_room(interaction, x, y, p, l)


async def A1P1_room(interaction, x, y, p, l):
    pilfermoreview = OneView("Pilfer more")

    await interaction.followup.send(
        "\n\nYou rummage through the treasure finding all sorts of interesting trinkets. Swords from long forgotten battles. Ruby encrusted armor with 4 arm holes, or what look like arm holes anyway. Helmets forged in volcanic pyres, glowing with elven magic. How do you know all of this, you wonder? The memories float in and out from times long ago. Continue pilfering?",
        view=pilfermoreview,
        ephemeral=True)

    await pilfermoreview.wait()

    if pilfermoreview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1P2_room(interaction, x, y, p, l)


async def A1P2_room(interaction, x, y, p, l):
    pilfermoreview2 = OneView("Pilfer more")

    await interaction.followup.send(
        "\n\nYou dive into another pile of treasure, right into a goopy pile of Ooze. Its weird texture envelops your arm and stimulates it, giving you a burst of energy. You wonder what else it could stimulate when all of a sudden, a low rumbling comes from within the planet, causing some rocks to fall from the ceiling. You leap out of the way as a giant boulder crashes down into the pile of treasure, splattering Ooze all over the trinkets and weapons. Rattled but unafraid, you continue rummaging, curious about what secrets this Guild’s Lair hides. Pilfer some more?",
        view=pilfermoreview2,
        ephemeral=True)

    await pilfermoreview2.wait()

    if pilfermoreview2.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1P3_room(interaction, x, y, p, l)


async def A1P3_room(interaction, x, y, p, l):
    keepgoingview = OneView("Keep going")

    await interaction.followup.send(
        "\n\nYou grab a spiked club and consider using it. Nah, too top heavy. You grab a pair of glowing nunchuks and start to spin them like a drunken toddler. They start to warm as you spin faster and faster, and suddenly a burst of flame explodes out of the end illuminating the cave and searing your hair. Wow that smells awful, you think, dropping the scorching weapon as you extinguish your now burnt head. You hadn’t noticed before the burst of flame, but there was a reflection deeper in the cave. There’s something shiny back there… something… precious? My precious?",
        view=keepgoingview,
        ephemeral=True)

    await keepgoingview.wait()

    if keepgoingview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1Final_room(interaction, x, y, p, l)


async def A1Final_room(interaction, x, y, p, l):

    A13choicesview = ThreeView("Pilfer more", "Climb on boulder",
                               "Go deeper into the lair")

    await interaction.followup.send(
        "\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.",
        view=A13choicesview,
        ephemeral=True)

    await A13choicesview.wait()

    if A13choicesview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    elif A13choicesview.choice == 1:
        await A2_room(interaction, x, y, p, l)

    elif A13choicesview.choice == 2:
        if x < 2:
            await A3P1_room(interaction, x, y, p, l)
        else:
            await A3Z2_room(interaction, x, y, p, l)

    elif A13choicesview.choice == 3:
        await A5_room(interaction, x, y, p, l)


async def A2_room(interaction, x, y, p, l):
    gobackview = OneView("Go back")

    await interaction.followup.send(
        "\n\nYou climb over the mound of treasure, making your way to the side of the cave. A skeleton of a freak is seen clinging to a broken, rusted machete. \n\nYou snag the machete and chop the head off, just to be sure.\n\nNever know how long that thing has been dead right? 'Double Tap' you scream aloud, as the skull rolls across the rocks.\n\nYou’re not sure why, but you felt compelled to yell it, as if it was second nature.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "\n\nYou poke into the mound of treasure with the rusted machete. Gold coins spill onto your feet. Worthless, you think in contempt. It doesn’t look like anything here is worth taking or exploring. \n\nYou’ve reached a dead end.",
        view=gobackview,
        ephemeral=True)

    await gobackview.wait()

    if gobackview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1Final_room(interaction, x, y, p, l)


async def A3P1_room(interaction, x, y, p, l):
    x = x + 3
    climbview = OneView("Climb ladder")

    await interaction.followup.send(
        "\n\nYou climb onto the fallen boulder, slipping on your way up, knocking your nose. Blood trickles down your face. You stare up towards the alcove from which it fell. You think you can reach it if you can just get close enough… You spot a convenient ladder amidst the rubble. \n\nYou prop it on top of the boulder, giving you access to the alcove. \n\nWant to climb the ladder?",
        view=climbview,
        ephemeral=True)

    await climbview.wait()

    if climbview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    A3P12choiceview = TwoView("Go back", "Swing staff")

    await interaction.followup.send(
        "\n\nYou start climbing the ladder and it snaps, sending you down into the pile of treasure below. Couldn’t be that easy you think. Ooze seeps around your feet.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nYour nerves in your legs activate with intense energy and you try pushing off of them with all your force.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou shoot into the air 20 feet, bashing your poor nose once again, this time on the ceiling of the cave.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nMore blood falls down your chin as you flop back face down into the pile of Ooze on the floor. The blood stops. The pain subsides as you feel jolts of energy course through your body again.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nYou touch your nose and realize its completely healed! Determined and rejuvenated, you look to the alcove again.",
        ephemeral=True)
    await interaction.followup.send(
        "\n\nYou leap towards it, easily sailing in!", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nIn front of you is what looks like a shimmering staff. You swing the staff, loosing a blast of pure energy in front of you.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nThe energy ricochets, knocking you back down, smacking you into the boulder and sending you faceplanting once again into the pile of Ooze.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nUnder further inspection, the staff looks as if it’s covered in runes. You wonder if swinging the staff again will cause the same effect.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nDoesn't look like there is anything left to do on this boulder. I do have this sweet staff now though...",
        view=A3P12choiceview,
        ephemeral=True)

    await A3P12choiceview.wait()

    if A3P12choiceview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    elif A3P12choiceview.choice == 1:

        await A1Final_room(interaction, x, y, p, l)

    elif A3P12choiceview.choice == 2:
        gobackview2 = OneView("Go back")

        await interaction.followup.send(
            "\nYou swing the staff, loosing a blast of energy directly in front of you. The blast sends treasure and copious amounts of weapons flying, but you don’t see any major changes in the cave. I should save this thing in case I need it later. \n probably should head back now",
            view=gobackview2,
            ephemeral=True)

        await gobackview2.wait()

        if gobackview2.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

        await A1Final_room(interaction, x, y, p, l)


async def A3Z2_room(interaction, x, y, p, l):
    gobackview3 = OneView("Go back")

    await interaction.followup.send(
        "\n\nYou climb atop the boulder. That’s a niiiiice boulder. Looks like some pieces from the broken ladder, there’s nothing else interesting here.",
        view=gobackview3,
        ephemeral=True)

    await gobackview3.wait()

    if gobackview3.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A1Final_room(interaction, x, y, p, l)


async def A5_room(interaction, x, y, p, l):
    # some prompts
    leftrightview = ThreeView("Left", "Right", "Go back")

    await interaction.followup.send(
        "\n\nYou delve further into the cave, climbing over rocks and disturbingly sharp weapons. \n\nYou reach a fork in the path. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts, which must have been creating the shiny reflection you saw earlier in the cave! \n\nShould you go right or left...?",
        view=leftrightview,
        ephemeral=True)

    await leftrightview.wait()

    if leftrightview.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    elif leftrightview.choice == 1:
        await A6_room(interaction, x, y, p, l)

    elif leftrightview.choice == 2:
        if y < 2:
            await A7_room(interaction, x, y, p, l)
        else:
            await A7back_room(interaction, x, y, p, l)

    elif leftrightview.choice == 3:
        await A1Final_room(interaction, x, y, p, l)


async def A5back_room(interaction, x, y, p, l):
    # some prompts
    leftrightview2 = ThreeView("Left", "Right", "Go back")

    await interaction.followup.send(
        "\n\nYou’re deep in the cave at a fork in the path. Behind you are the piles of treasure you pilfered and the giant boulder. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts. Should you right, left, or to the go back...?",
        view=leftrightview2,
        ephemeral=True)

    await leftrightview2.wait()

    if leftrightview2.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    elif leftrightview2.choice == 1:
        if p < 2:
            await A6_room(interaction, x, y, p, l)
        else:
            await A6back_room(interaction, x, y, p, l)

    elif leftrightview2.choice == 2:
        if y < 2:
            await A7_room(interaction, x, y, p, l)
        else:
            await A7back_room(interaction, x, y, p, l)

    elif leftrightview2.choice == 3:
        await A1Final_room(interaction, x, y, p, l)


async def A6_room(interaction, x, y, p, l):
    p = p + 3
    gobackview4 = OneView("Go back")

    await interaction.followup.send(
        "\n\nYou approach a giant mirror as you examine yourself for the first time. Damn, you’re a catch. You’re human, that’s for sure.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\n From the look of it, this mirror is the only thing down this path, besides some treasure and armor. You try some armor on for the fun of it. Damn, you look even better now.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nYou decide to keep the armor because you’re here pilfering, and no one but you would look this good in it anyway.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nThat’s enough, you think, you can’t just stare at yourself all day, you’ve got runes to find. Tendies to make. Gains for days.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou should probably go back, or you can just stare at yourself some more...",
        view=gobackview4,
        ephemeral=True)

    await gobackview4.wait()

    if gobackview4.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A5back_room(interaction, x, y, p, l)


async def A6back_room(interaction, x, y, p, l):
    gobackview5 = OneView("Go back")

    await interaction.followup.send(
        "\n\nWoah who’s that you see? Oh yeah, it’s you in the mirror, check that out. Damn you look good in your armor. There doesn’t seem to be anything else here.", view=gobackview5,
        ephemeral=True)

    await gobackview5.wait()

    if gobackview5.timeout == True:
      await interaction.followup.send(
        "Timed out... Don't you know how to click buttons?!", ephemeral=True)
      return

    await A5back_room(interaction, x, y, p, l)


async def A7_room(interaction, x, y, p, l):
    # some prompts
    await interaction.followup.send(
        "\n\nYou approach the pile of loose rocks.", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.",
        ephemeral=True)

    if x > 1:
        A7view = TwoView("Swing Staff", "Go back")

        await interaction.followup.send("\n...", view=A7view, ephemeral=True)

        await A7view.wait()

        if A7view.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

        elif A7view.choice == 1:
            y = y + 3
            await A8_room(interaction, x, y, p, l)

        elif A7view.choice == 2:
            await A5back_room(interaction, x, y, p, l)

    else:
        A7view = OneView("Go back")

        await interaction.followup.send("\n...", view=A7view, ephemeral=True)

        await A7view.wait()

        if A7view.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

        await A5back_room(interaction, x, y, p, l)


async def A7back_room(interaction, x, y, p, l):
    A7backview = TwoView("Go back", "Crawl through")
    await interaction.followup.send(
        "\n\nYou approach the small entrance. You can see a large room behind it. Will you crawl through, or go back to the fork in the cave?",view=A7backview,
        ephemeral=True)

    await A7backview.wait()

    if A7backview.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    elif A7backview.choice == 1:
        await A5back_room(interaction, x, y, p, l)
    elif A7backview.choice == 2:
        await A8back_room(interaction, x, y, p, l)


async def A8_room(interaction, x, y, p, l):
    l = l + 3
    # some prompts
    A8view = FourView("Chest", "Tapestry", "Sit in throne", "Go back")
    await interaction.followup.send(
        "\n\nYou swing the staff, loosing a blast of energy. The energy forcefully slams into the rocks, sending them flying through the cave, scraping you on the way by.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\n You stumble and fall back from the force. As the dust settles, you see that the pathway has been cleared enough to wriggle your way through.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nYou crawl through the opening and find yourself in a large regal room. This must be where the guild met before they disappeared. A 6-foot round table sits in the middle, surrounded by chairs.\n\n You wonder how they got the table into the cave until you remember, “magic!” Makes sense.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "\n\nIn the corner you see a locked treasure chest. \n\nYou also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks. \n\nAt the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne",view=A8view,
        ephemeral=True)

    await A8view.wait()

    if A8view.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    elif A8view.choice == 1:
        await A11_room(interaction, x, y, p, l)
    elif A8view.choice == 2:
        await A9_room(interaction, x, y, p, l)
    elif A8view.choice == 3:
        await A10_room(interaction, x, y, p, l)
    elif A8view.choice == 4:
        await A7back_room(interaction, x, y, p, l)


async def A8back_room(interaction, x, y, p, l):
    A8backview = FourView("Chest", "Tapestry", "Sit in throne", "Go back")
    await interaction.followup.send(
        "\n\nYou’re in a large regal room. A 6-foot round table sits in the middle, surrounded by chairs. In the corner you see a locked treasure chest. ",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\n You also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks. ",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\n. At the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne.",view=A8backview,
        ephemeral=True)

    await A8backview.wait()

    if A8backview.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    elif A8backview.choice == 1:
        await A11_room(interaction, x, y, p, l)
    elif A8backview.choice == 2:
        await A9_room(interaction, x, y, p, l)
    elif A8backview.choice == 3:
        await A10_room(interaction, x, y, p, l)
    elif A8backview.choice == 4:
        await A7back_room(interaction, x, y, p, l)


async def A9_room(interaction, x, y, p, l):
    gobackview6 = OneView("Go back")

    await interaction.followup.send(
        "\n\nYou move closer to the tapestry. It looks almost like a family tree, except inscribed on the top is “The Golden Guild” Apparently, it’s a guild tree.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\n7 large branches extend from the base. Each branch features more than 20 freaks, made up of different races. You recognize some freaks from your memories, and a few ogres are featured as well – you recognize them from earlier in the day since the snot dribbling from their nose is unmistakable.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "\n\nWhat looks to be elves are on some of the branches, amidst some other mysterious freaks. Most of them are creatures you’ve never seen before, at least that’s what you remember.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "\n\nYour eyes scan the tree looking for more information. 7 names are scribbled into the branches of the tree. From left to right, you read: Chad the Chiseled, Missy the Inaccurate, Clair the Clairvoyant, Satoshi the Wise, Wanda the Witch, Vlad the Game Stopper, and Kaiju the Nifty.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "\n\nSatisfied, you don’t think staring at this tapestry will get you any closer to the rune you seek.", view=gobackview6,
        ephemeral=True)

    await gobackview6.wait()

    if gobackview6.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    await A8back_room(interaction, x, y, p, l)


async def A10_room(interaction, x, y, p, l):
    gobackview7 = OneView("Go back")

    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nFit for a king, isn’t it? You plop your undeserving fat ass down on the throne, feeling the soft velvet smush under your weight. It’s the armor weighing you down, obviously",
        ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\n You don’t look fat in it. Seriously.", ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou can see the whole room from this view. The tapestry hangs regally from the wall, and you can hear drips of water splash in the corner. It’s damp. Wonder why the table hasn’t warped yet… oh yeah, magic, you remember.",
        ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nThe other 6 chairs around the table form a circle. It seems like many decisions have been argued over in this room. You bang your hand on the table, acting as if you’re in an argument. The edge of the table begins to glow, spreading a light film over the table.",
        ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nYou can see a pattern of cubes encircling the table, bound by a chain. In front of you, a crown is inscribed into the table, with the word ‘wise’ on it.",
        ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nThe glow dissipates. Satisfied, you know it’s time to rise. This is no time to sit on your ass.",
        ephemeral=True)
    await interaction.followup.send("\n...", view=gobackview7, ephemeral=True)

    await gobackview7.wait()

    if gobackview7.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    await A8back_room(interaction, x, y, p, l)


async def A11_room(interaction, x, y, p, l):
    dropdownview = DropdownView()

    await interaction.followup.send(
        "\n\nYou approach the chest in the corner. It’s adorned in gold and jewels. A crown is visible near the lock. An inscription on the chest reads 'To find the private key, Speak aloud the owner’s name'.",
        ephemeral=True)
    await interaction.followup.send("\n...", ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "\n\nChoose the owner's name correctly or you will have to restart.",
        view=dropdownview,
        ephemeral=True)

    await dropdownview.wait()

    if dropdownview.timeout == True:
          await interaction.followup.send("Timed out... Don't you know how to click buttons?!", ephemeral=True)
          return

    elif dropdownview.win == True:

        await interaction.followup.send(embed=discord.Embed(
            description=
            f"**Congratulations {interaction.user.name} - You Win!**",
            color=0x000ff),
                                        ephemeral=True)

    else:

        await interaction.followup.send(embed=discord.Embed(
            description=
            "**Welp, looks like you got it wrong. Now you have to start over.**",
            color=0x000ff),
                                        ephemeral=True)


class ChallengeView1(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label='Begin Challenge',
                       style=discord.ButtonStyle.blurple,
                       custom_id='persistent_view:challenge1')
    async def challenge(self, button: discord.ui.Button,
                        interaction: discord.Interaction):
        x = 0
        y = 0
        p = 0
        l = 0

        await interaction.response.defer()

        startembed = discord.Embed(
            description=
            f"These quests are a race to complete. The first 75 to complete each quest will be whitelisted for an allowed to mint 1 Celestial Key For FREE. The next 300 to finish will be whitelisted for the mint at a reduced price. When you have completed all the quests you will be DMed by {self.client.user.mention} and prompted to enter your wallet address. It will only ask for you wallet address - do not add random text!\n\nHow to play:\nRead the paragraph, and then type one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.\n\nIf you ever want to return to the place you just previously were, just click ‘go back’. You will always have the option ‘go back’ available to you.\n\nTo start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!",
            color=0x000ff)
        startembed.set_author(name="Challenge 1",
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

        await intro_room(interaction, x, y, p, l)


class Challenge1(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    #Commands
    @commands.command(pass_context=True)
    async def challenge1(self, ctx):
        rulesembed = discord.Embed(
            description=f"Click below to begin your challenge.", color=0x000ff)
        rulesembed.set_author(name="Challenge 1", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text="Freaks N' Guilds",
                              icon_url=ctx.guild.icon.url)

        challengeview = ChallengeView1(self.client)

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
            self.client.add_view(ChallengeView1(self.client))
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Challenge1(client))
