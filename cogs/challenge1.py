import discord
import time
from discord.abc import PrivateChannel
from discord.ext import commands

class BeginView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Begin', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    rockview = RockView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("...\n\n...\n\nHuh? Are you dead…?\n\nIt looks like they’re breathing.\n\nWAKE UP SWINE!\n\nYou feel a studded boot press into your back. Dazed, you sit up. It’s hard to see, light seems so far away. Your eyes begin to adjust to the darkness.\n\nYou let out a loud gasp as the freakish face of an ogre, snot dribbling down his chin, comes into view. A second ogre peers from the left. 'What do you want?' you say.\n\n'Do you not remember? Do you not know?' the second ogre grumbled under its breath.\n\nThe Creator of Worlds has shaken up the planet, mixing light and dark freaks together. What once was a peaceful land is now teeming with conflict. The Creator of Worlds proclaimed to the land that a contest would be held to determine who is most worthy to become the first hunters, guild members; owners of us freaks. There are only 2000 spots available. If you can open the ancient chest, you’ll claim your rightful spot. But to open the chest, you’ll need the 4 runes. Each rune can be found in a particular location in the land. The first will lead to the second, and so on.\n\nKinda like that Earth movie ‘Ready Slayer Won’” grumbled the second ogre.\n\nRight, you gotta find the 4 runes. The first one is around here somewhere, in the Guild’s Lair.\n\nYou stand up, and memories flood into your brain, tuning out the sounds of the ogres. It’s odd, this isn’t your first time here you don’t think. You have memories of great battles, hunting freaks, and forming friendships with guilds. You begin to feel power course through your body. You know you’re meant for something more. Could you be a hunter?\n\nWe freaks can’t become hunters, nor would we want to, we want the Ooze, that’s all we’re here for” said the first ogre, droning on.\n\nYou thank the ogres and tell them to keep moving. Maybe it’s a trick of the light, but your eyes have adjusted so well to the darkness that you can see distinct shapes of shrubbery and rock formations. You sense that you’re supposed to go to the rock formation...", view=rockview, ephemeral=True)

class RockView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Go to rock', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    pilferview = PilferView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach the rock formation. The vitality inside you is getting stronger and your eyes have almost perfect night vision at this point. You climb down and around the rocks until you see a cave entrance.\n\nYou peer into the cave and see mounds of treasure. Pilfer?", view=pilferview, ephemeral=True)

class PilferView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Pilfer', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    pilfermoreview = PilferMoreView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou rummage through the treasure finding all sorts of interesting trinkets. Swords from long forgotten battles. Ruby encrusted armor with 4 arm holes, or what look like arm holes anyway. Helmets forged in volcanic pyres, glowing with elven magic. How do you know all of this, you wonder? The memories float in and out from times long ago. Continue pilfering?", view=pilfermoreview, ephemeral=True)

class PilferMoreView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Pilfer more', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    pilferevenmoreview = PilferEvenMoreView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou dive into another pile of treasure, right into a goopy pile of Ooze. Its weird texture envelops your arm and stimulates it, giving you a burst of energy. You wonder what else it could stimulate when all of a sudden, a low rumbling comes from within the planet, causing some rocks to fall from the ceiling. You leap out of the way as a giant boulder crashes down into the pile of treasure, splattering Ooze all over the trinkets and weapons. Rattled but unafraid, you continue rummaging, curious about what secrets this Guild’s Lair hides. Pilfer some more?", view=pilferevenmoreview, ephemeral=True)

class PilferEvenMoreView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Pilfer more', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    keepgoingview = KeepGoingView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou grab a spiked club and consider using it. Nah, too top heavy. You grab a pair of glowing nunchuks and start to spin them like a drunken toddler. They start to warm as you spin faster and faster, and suddenly a burst of flame explodes out of the end illuminating the cave and searing your hair. Wow that smells awful, you think, dropping the scorching weapon as you extinguish your now burnt head. You hadn’t noticed before the burst of flame, but there was a reflection deeper in the cave. There’s something shiny back there… something… precious? My precious?", view=keepgoingview, ephemeral=True)

class KeepGoingView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Keep going', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A1FinalRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.", view=view, ephemeral=True)

class GoBackView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A1FinalRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.", view=view, ephemeral=True)

class A1FinalRoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Pilfer more', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = GoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou climb over the mound of treasure, making your way to the side of the cave. A skeleton of a freak is seen clinging to a broken, rusted machete. \n\nYou snag the machete and chop the head off, just to be sure.\n\nNever know how long that thing has been dead right? 'Double Tap' you scream aloud, as the skull rolls across the rocks.\n\nYou’re not sure why, but you felt compelled to yell it, as if it was second nature.\n\nYou poke into the mound of treasure with the rusted machete. Gold coins spill onto your feet. Worthless, you think in contempt. It doesn’t look like anything here is worth taking or exploring. \n\nYou’ve reached a dead end.", view=view, ephemeral=True)

  @discord.ui.button(label='Climb on boulder', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if self.x < 2:
        self.x = self.x + 3

        view = A3P1RoomView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou climb onto the fallen boulder, slipping on your way up, knocking your nose. Blood trickles down your face. You stare up towards the alcove from which it fell. You think you can reach it if you can just get close enough… You spot a convenient ladder amidst the rubble. \n\nYou prop it on top of the boulder, giving you access to the alcove. \n\nWant to climb the ladder?", view=view, ephemeral=True)

    else:
        view = GoBackView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou climb atop the boulder. That’s a niiiiice boulder. Looks like some pieces from the broken ladder, there’s nothing else interesting here.", view=view, ephemeral=True)

  @discord.ui.button(label='Go deeper into the lair', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A5RoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou delve further into the cave, climbing over rocks and disturbingly sharp weapons. \n\nYou reach a fork in the path. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts, which must have been creating the shiny reflection you saw earlier in the cave! \n\nShould you go right or left...?", view=view, ephemeral=True)

class A3P1RoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Climb ladder', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A3P1TwoRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou start climbing the ladder and it snaps, sending you down into the pile of treasure below. Couldn’t be that easy you think. Ooze seeps around your feet.\n\nYour nerves in your legs activate with intense energy and you try pushing off of them with all your force.\n\nYou shoot into the air 20 feet, bashing your poor nose once again, this time on the ceiling of the cave.\n\nMore blood falls down your chin as you flop back face down into the pile of Ooze on the floor. The blood stops. The pain subsides as you feel jolts of energy course through your body again.\n\nYou touch your nose and realize its completely healed! Determined and rejuvenated, you look to the alcove again.\n\nYou leap towards it, easily sailing in!\n\nIn front of you is what looks like a shimmering staff. You swing the staff, loosing a blast of pure energy in front of you.\n\nThe energy ricochets, knocking you back down, smacking you into the boulder and sending you faceplanting once again into the pile of Ooze.\n\nUnder further inspection, the staff looks as if it’s covered in runes. You wonder if swinging the staff again will cause the same effect.\n\nDoesn't look like there is anything left to do on this boulder. I do have this sweet staff now though...", view=view, ephemeral=True)

class A3P1TwoRoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A1FinalRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.", view=view, ephemeral=True)

  @discord.ui.button(label='Swing staff', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = GoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\nYou swing the staff, loosing a blast of energy directly in front of you. The blast sends treasure and copious amounts of weapons flying, but you don’t see any major changes in the cave. I should save this thing in case I need it later. \n probably should head back now", view=view, ephemeral=True)

class A5RoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Left', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.p = self.p + 3

    view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach a giant mirror as you examine yourself for the first time. Damn, you’re a catch. You’re human, that’s for sure.\n\n From the look of it, this mirror is the only thing down this path, besides some treasure and armor. You try some armor on for the fun of it. Damn, you look even better now.\n\nYou decide to keep the armor because you’re here pilfering, and no one but you would look this good in it anyway.\n\nThat’s enough, you think, you can’t just stare at yourself all day, you’ve got runes to find. Tendies to make. Gains for days.\n\nYou should probably go back, or you can just stare at yourself some more...", view=view, ephemeral=True)

  @discord.ui.button(label='Right', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if self.y < 2:
        if self.x > 1:

            view = A7RoomView(self.x, self.y, self.p, self.l, self.client)

            await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

        else:
            view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

            await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

    else:

        view = A7BackRoomView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou approach the small entrance. You can see a large room behind it. Will you crawl through, or go back to the fork in the cave?", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A1FinalRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.", view=view, ephemeral=True)

class A5BackRoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Left', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    if self.p < 2:

        view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou approach a giant mirror as you examine yourself for the first time. Damn, you’re a catch. You’re human, that’s for sure.\n\n From the look of it, this mirror is the only thing down this path, besides some treasure and armor. You try some armor on for the fun of it. Damn, you look even better now.\n\nYou decide to keep the armor because you’re here pilfering, and no one but you would look this good in it anyway.\n\nThat’s enough, you think, you can’t just stare at yourself all day, you’ve got runes to find. Tendies to make. Gains for days.\n\nYou should probably go back, or you can just stare at yourself some more...", view=view, ephemeral=True)

    else:

        view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nWoah who’s that you see? Oh yeah, it’s you in the mirror, check that out. Damn you look good in your armor. There doesn’t seem to be anything else here.", view=view, ephemeral=True)


  @discord.ui.button(label='Right', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if self.y < 2:
        if self.x > 1:

            view = A7RoomView(self.x, self.y, self.p, self.l, self.client)

            await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

        else:
            view = A7BackRoomView(self.x, self.y, self.p, self.l, self.client)

            await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

    else:

        view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou approach the small entrance. You can see a large room behind it. Will you crawl through, or go back to the fork in the cave?", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A1FinalRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re near some mounds of treasure and the giant boulder. What will you do? You can pilfer some more, you can climb on top of the fallen boulder, or you can go deeper into the lair.", view=view, ephemeral=True)

class A5BackRoomGoBackView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A5BackRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re deep in the cave at a fork in the path. Behind you are the piles of treasure you pilfered and the giant boulder. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts. Should you right, left, or to the go back...?", view=view, ephemeral=True)

class A7RoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Swing Staff', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.y = self.y + 3
    self.l = self.l + 3

    view = A8RoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou swing the staff, loosing a blast of energy. The energy forcefully slams into the rocks, sending them flying through the cave, scraping you on the way by.\n\n You stumble and fall back from the force. As the dust settles, you see that the pathway has been cleared enough to wriggle your way through.\n\nYou crawl through the opening and find yourself in a large regal room. This must be where the guild met before they disappeared. A 6-foot round table sits in the middle, surrounded by chairs.\n\n You wonder how they got the table into the cave until you remember, “magic!” Makes sense.\n\nIn the corner you see a locked treasure chest. \n\nYou also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks. \n\nAt the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re deep in the cave at a fork in the path. Behind you are the piles of treasure you pilfered and the giant boulder. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts. Should you right, left, or to the go back...?", view=view, ephemeral=True)

class A7BackRoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Crawl Through', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.y = self.y + 3
    self.l = self.l + 3

    view = A8RoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou swing the staff, loosing a blast of energy. The energy forcefully slams into the rocks, sending them flying through the cave, scraping you on the way by.\n\n You stumble and fall back from the force. As the dust settles, you see that the pathway has been cleared enough to wriggle your way through.\n\nYou crawl through the opening and find yourself in a large regal room. This must be where the guild met before they disappeared. A 6-foot round table sits in the middle, surrounded by chairs.\n\n You wonder how they got the table into the cave until you remember, “magic!” Makes sense.\n\nIn the corner you see a locked treasure chest. \n\nYou also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks. \n\nAt the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A5BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re deep in the cave at a fork in the path. Behind you are the piles of treasure you pilfered and the giant boulder. To your right you see a pile of loose rocks blocking a path. To your left you see a mirror of sorts. Should you right, left, or to the go back...?", view=view, ephemeral=True)

class A8BackRoomGoBackView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A8BackRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou’re in a large regal room. A 6-foot round table sits in the middle, surrounded by chairs. In the corner you see a locked treasure chest.\n\n You also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks.\n\n. At the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne.", view=view, ephemeral=True)

class A8RoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Chest', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = DropdownView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach the chest in the corner. It’s adorned in gold and jewels. A crown is visible near the lock. An inscription on the chest reads 'To find the private key, Speak aloud the owner’s name'.\n\nChoose the owner's name correctly or you will have to restart.", view=view, ephemeral=True)

  @discord.ui.button(label='Tapestry', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A8BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou move closer to the tapestry. It looks almost like a family tree, except inscribed on the top is “The Golden Guild” Apparently, it’s a guild tree.\n\n7 large branches extend from the base. Each branch features more than 20 freaks, made up of different races. You recognize some freaks from your memories, and a few ogres are featured as well – you recognize them from earlier in the day since the snot dribbling from their nose is unmistakable.\n\nWhat looks to be elves are on some of the branches, amidst some other mysterious freaks. Most of them are creatures you’ve never seen before, at least that’s what you remember.\n\nYour eyes scan the tree looking for more information. 7 names are scribbled into the branches of the tree. From left to right, you read: Chad the Chiseled, Missy the Inaccurate, Clair the Clairvoyant, Satoshi the Wise, Wanda the Witch, Vlad the Game Stopper, and Kaiju the Nifty.\n\nSatisfied, you don’t think staring at this tapestry will get you any closer to the rune you seek.", view=view, ephemeral=True)

  @discord.ui.button(label='Sit in throne', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A8BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n...\n\nFit for a king, isn’t it? You plop your undeserving fat ass down on the throne, feeling the soft velvet smush under your weight. It’s the armor weighing you down, obviously.\n\n You don’t look fat in it. Seriously.\n\nYou can see the whole room from this view. The tapestry hangs regally from the wall, and you can hear drips of water splash in the corner. It’s damp. Wonder why the table hasn’t warped yet… oh yeah, magic, you remember.\n\nThe other 6 chairs around the table form a circle. It seems like many decisions have been argued over in this room. You bang your hand on the table, acting as if you’re in an argument. The edge of the table begins to glow, spreading a light film over the table. \n\nYou can see a pattern of cubes encircling the table, bound by a chain. In front of you, a crown is inscribed into the table, with the word ‘wise’ on it.\n\nThe glow dissipates. Satisfied, you know it’s time to rise. This is no time to sit on your ass.", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button4(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A7BackRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

class A8BackRoomView(discord.ui.View):
  def __init__(self, x, y, p, l, client):
    super().__init__(timeout=None)
    self.x = x
    self.y = y
    self.p = p
    self.l = l
    self.client = client

  @discord.ui.button(label='Chest', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = DropdownView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach the chest in the corner. It’s adorned in gold and jewels. A crown is visible near the lock. An inscription on the chest reads 'To find the private key, Speak aloud the owner’s name'.\n\nChoose the owner's name correctly or you will have to restart.", view=view, ephemeral=True)

  @discord.ui.button(label='Tapestry', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A8BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou move closer to the tapestry. It looks almost like a family tree, except inscribed on the top is “The Golden Guild” Apparently, it’s a guild tree.\n\n7 large branches extend from the base. Each branch features more than 20 freaks, made up of different races. You recognize some freaks from your memories, and a few ogres are featured as well – you recognize them from earlier in the day since the snot dribbling from their nose is unmistakable.\n\nWhat looks to be elves are on some of the branches, amidst some other mysterious freaks. Most of them are creatures you’ve never seen before, at least that’s what you remember.\n\nYour eyes scan the tree looking for more information. 7 names are scribbled into the branches of the tree. From left to right, you read: Chad the Chiseled, Missy the Inaccurate, Clair the Clairvoyant, Satoshi the Wise, Wanda the Witch, Vlad the Game Stopper, and Kaiju the Nifty.\n\nSatisfied, you don’t think staring at this tapestry will get you any closer to the rune you seek.", view=view, ephemeral=True)

  @discord.ui.button(label='Sit in throne', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A8BackRoomGoBackView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n...\n\nFit for a king, isn’t it? You plop your undeserving fat ass down on the throne, feeling the soft velvet smush under your weight. It’s the armor weighing you down, obviously.\n\n You don’t look fat in it. Seriously.\n\nYou can see the whole room from this view. The tapestry hangs regally from the wall, and you can hear drips of water splash in the corner. It’s damp. Wonder why the table hasn’t warped yet… oh yeah, magic, you remember.\n\nThe other 6 chairs around the table form a circle. It seems like many decisions have been argued over in this room. You bang your hand on the table, acting as if you’re in an argument. The edge of the table begins to glow, spreading a light film over the table. \n\nYou can see a pattern of cubes encircling the table, bound by a chain. In front of you, a crown is inscribed into the table, with the word ‘wise’ on it.\n\nThe glow dissipates. Satisfied, you know it’s time to rise. This is no time to sit on your ass.", view=view, ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button4(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = A7BackRoomView(self.x, self.y, self.p, self.l, self.client)

    await interaction.response.send_message("\n\nYou approach the pile of loose rocks.\n\nThere seems to be a pathway behind the rocks, but they’re too heavy to move. A blast of energy might help clear it.\n\n...", view=view, ephemeral=True)

class Dropdown(discord.ui.Select):
    def __init__(self, x, y, p, l, client):
        self.client = client
        self.x = x
        self.y = y
        self.p = p
        self.l = l
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
          await interaction.response.defer()

          walletembed = discord.Embed(description="Congratulations on completing the quest! The first 50 people to complete will be added to the free mint whitelist and the next 300 will be whitelisted. You will gain a role for completing this quest and we will manually assign the roles for the winners! Please send your wallet address here! (Make sure to send only your wallet address and no extra random text!)", color=0x000ff)
          walletembed.set_footer(text="Freaks N' Guilds",
                                icon_url=self.client.user.avatar.url)

          dmmessage = await interaction.user.send(embed=walletembed)

          await interaction.followup.send(embed=discord.Embed(description=f"Congratulations on completing the quest! The first 50 people to complete will be added to the free mint whitelist and the next 300 will be whitelisted. You will gain a role for completing this quest and we will manually assign the roles for the winners! Please [check your DMs]({dmmessage.jump_url}) and send your wallet address there! (Make sure to send only your wallet address and no extra random text!)", color=0x000ff),
              ephemeral=True)

          walletaddress = (await self.client.wait_for('message', check=lambda message: message.author == interaction.user and isinstance(message.channel, PrivateChannel))).content

          await interaction.user.send("Got it! I've stored your wallet address.")

          f = open("walletaddresses.txt", "a")
          f.write(f"{interaction.user.name}#{interaction.user.discriminator}:{walletaddress},\n")
          f.close()

          knightsrole = interaction.guild.get_role(902795625253449759)
          await interaction.user.add_roles(knightsrole)

        else:
          startoverview = BeginView(self.view.x, self.view.y, self.view.p, self.view.l, self.view.client)

          await interaction.response.send_message(embed=discord.Embed(description="**Welp, looks like you got it wrong. Now you have to start over...**", color=0x000ff), view=startoverview, ephemeral=True)

class OneButton(discord.ui.Button):
    def __init__(self, label, x, y, p, l, client):
        super().__init__(label=label, style=discord.ButtonStyle.blurple)
        self.client = client
        self.x = x
        self.y = y
        self.p = p
        self.l = l

    async def callback(self, interaction: discord.Interaction):
        view = A8BackRoomView(self.x, self.y, self.p, self.l, self.client)

        await interaction.response.send_message("\n\nYou’re in a large regal room. A 6-foot round table sits in the middle, surrounded by chairs. In the corner you see a locked treasure chest.\n\n You also notice a tapestry near where you entered the room, adorned with decorations and a tree behind several images of freaks.\n\n. At the opposite end of the room near the table is a gold throne. None of the other chairs are thrones, this one is clearly special.\n\nWhat will you do? You can approach the chest, examine the tapestry, or sit in the throne.", view=view, ephemeral=True)

class DropdownView(discord.ui.View):
    def __init__(self, x, y, p, l, client):
        super().__init__(timeout=None)
        self.client = client
        self.x = x
        self.y = y
        self.p = p
        self.l = l

        self.add_item(Dropdown(self.x, self.y, self.p, self.l, self.client))
        self.add_item(OneButton("Go back", self.x, self.y, self.p, self.l, self.client))

class ChallengeView1(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label='Begin Challenge',
                       style=discord.ButtonStyle.blurple,
                       custom_id='persistent_view:challenge1')
    async def challenge(self, button: discord.ui.Button, interaction: discord.Interaction):

        x = 0
        y = 0
        p = 0
        l = 0

        startembed = discord.Embed(description=f"These quests are a race to complete. The first 75 to complete each quest will be whitelisted for an allowed to mint 1 Celestial Key For FREE. The next 300 to finish will be whitelisted for the mint at a reduced price. When you have completed all the quests you will be DMed by {self.client.user.mention} and prompted to enter your wallet address. It will only ask for you wallet address - do not add random text!\n\nHow to play:\nRead the paragraph, and then type one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.\n\nIf you ever want to return to the place you just previously were, just click ‘go back’. You will always have the option ‘go back’ available to you.\n\nTo start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!", color=0x000ff)
        startembed.set_author(name="Challenge 1",
                              icon_url=interaction.guild.icon.url)
        startembed.set_footer(text="Freaks N' Guilds",
                              icon_url=interaction.guild.icon.url)

        view = BeginView(x, y, p, l, self.client)

        await interaction.response.send_message(interaction.user.mention, embed=startembed, view=view, ephemeral=True)

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
