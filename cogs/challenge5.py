import discord
import discord.utils
from discord.ext import commands, tasks
from discord.commands import slash_command, permissions, Option

import os
import datetime
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


class BeginView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.msg = None

    @discord.ui.button(label='Begin', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E1(datetime.datetime.utcnow())

        await interaction.response.send_message(
            """
“Wait!” you hear distantly in your head.

You know that voice, the strained sound of your true love, Anorak.

You first met Anorak, a Time Wizard, 12 years ago. Or was it 20? He was a legendary being of Uruhan, but still young and not fully trained yet. Your love was forbidden, due to your stature as a Celestial. You didn’t care though, the World Maker could not understand the depth of your connection. It borders on telepathic, but it’s still weak.

When you heard of the World Maker’s decision to destroy the false peace of Uruhan, you quickly relayed a warning to Anorak... a mere 60 seconds before the Great Jumbling that sent Uruhan into chaos. The chaos would eventually kill Anorak.

But now you find yourself in a strange limbo, amidst fractured realities and timelines, stuck in the same harrowing minute before the Great Jumbling, with one goal: Find and save Anorak from Uruhan before he is killed. The future is not yet set in stone.

Only Anorak could have mustered the power to bring you to this mystical place among realities. You know it’s his voice. You’re willing to risk your own life to save his.

“Wait!” he calls out again.

You heard this before too, his reaction to the news that the World Maker was going to destroy the false peace.

But there’s no time to waste. It’s time to begin your quest. Or is all time happening simultaneously once you enter?
        """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class RestartView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.msg = None

    @discord.ui.button(label='Start Again', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E1(datetime.datetime.utcnow())

        await interaction.response.send_message(
            """
“Wait!” you hear distantly in your head.

You know that voice, the strained sound of your true love, Anorak.

You first met Anorak, a Time Wizard, 12 years ago. Or was it 20? He was a legendary being of Uruhan, but still young and not fully trained yet. Your love was forbidden, due to your stature as a Celestial. You didn’t care though, the World Maker could not understand the depth of your connection. It borders on telepathic, but it’s still weak.

When you heard of the World Maker’s decision to destroy the false peace of Uruhan, you quickly relayed a warning to Anorak... a mere 60 seconds before the Great Jumbling that sent Uruhan into chaos. The chaos would eventually kill Anorak.

But now you find yourself in a strange limbo, amidst fractured realities and timelines, stuck in the same harrowing minute before the Great Jumbling, with one goal: Find and save Anorak from Uruhan before he is killed. The future is not yet set in stone.

Only Anorak could have mustered the power to bring you to this mystical place among realities. You know it’s his voice. You’re willing to risk your own life to save his.

“Wait!” he calls out again.

You heard this before too, his reaction to the news that the World Maker was going to destroy the false peace.

But there’s no time to waste. It’s time to begin your quest. Or is all time happening simultaneously once you enter?
        """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E1(discord.ui.View):
    def __init__(self, starttime):
        super().__init__(timeout=60.0)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Enter Sanctuary', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        if (datetime.datetime.utcnow() - self.starttime).total_seconds() > 50:

            view = E27(self.starttime)

            await interaction.response.send_message(
                """
You enter the tunnel, a rich mosaic of possibilities, but every window shows Anorak sitting in a sanctuary amidst ancient artifacts and trinkets.

“You’re nearly here!” you hear Anorak excitedly quip!
                """, view=view, ephemeral=True)

        else:

            view = E2(self.starttime)

            await interaction.response.send_message(
                """
You enter the tunnel, a rich mosaic of possibilities, all barreling toward the same apocalyptic end.

“NO NO NO, this is all wrong!” you hear Anorak moan inside your head.

“I’m coming” you say to yourself, hoping he can hear it, hoping it will bring him solace. You don’t agree with the World Maker’s decision, but who are you to oppose him?

Deeper and deeper you go into the fractal tunnel, until you realize you’re completely lost in both time and space. The possibilities collide and reform giving you a glimpse of your love Anorak in 6 separate locations. Which window will you enter?
                """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E27(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Wait', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = RestartView()

        await interaction.response.send_message(
            """
            “What are you doing?! You waited?! I can’t hold this spell any longer!!” Anorak shouts a million times to your concerned face.

            The windows shatter. The fracture crackles with light and in an instant, there is nothing. You’ve been blipped out of existence.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Enter Sanctuary', style=discord.ButtonStyle.blurple)
    async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E29(self.starttime)

        await interaction.response.send_message(
            """
“You found me! I knew you could!” Anorak blurts. “Let’s end this and get out of here my love!”

The sanctuary is a regal sight with towering buttresses and intricate stained glass windows. The fractal can be seen outside, changing the color of the windows. If you weren’t under such time pressure, you could appreciate the beauty and work that was put into making the window make some semblance of sense.

With Anorak in your arms you loose a blast of power at the window, shattering the glass. You shoot towards the fractal, to freedom and safety.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E29(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Exit Fractal', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E30(self.starttime)

        await interaction.response.send_message(
            """
“Just one more thing for this spell to be complete” Anorak whispers

“WHY IS IT ALWAYS ONE MORE THING?!!” You shout, worriedly

“Kiss me.”

“I fractured reality for the one constant of our love, and this one constant is the only thing that can repair it.”
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E30(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Kiss Anorak', style=discord.ButtonStyle.blurple)
    async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        knightsrole = interaction.guild.get_role(knightroleid)
        peasantrole = interaction.guild.get_role(peasantroleid)

        await interaction.user.remove_roles(peasantrole, reason="Member completed Quest 5")
        await interaction.user.add_roles(knightsrole, reason="Member completed Quest 5")

        congratsmsg = await enlistedchannel.send(f"{interaction.user.mention} Congratulations on completing Quest 5! Please send your wallet address here and I will store it for you.")

        await interaction.response.send_message(
            f"""
The fractured reality snaps out of existence. You and Anorak stare into each other’s arms from the heavens as the World Maker brings down his fist to destroy the false peace of Uruhan.

The world has forever changed
But your love will never change, forever.

[Congratulations you have completed Quest 5]({congratsmsg.jump_url}), go to {enlistedchannel.mention} and submit your wallet address there! To submit your wallet address, just copy and paste it directly into the chat. NO COMMAND REQUIRED!!! Please do not spam that chat otherwise. Well done!
            """, ephemeral=True)

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E2(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Vast Ocean', style=discord.ButtonStyle.blurple)
    async def e3(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E3(self.starttime)

        await interaction.response.send_message(
            """
You dive headfirst towards the vast ocean. While falling in flight, you glance back up to the sky, seeing the spider web of possibilities crackling above you.

Anorak’s face appears massively in the waves, formed entirely from water. He opens his mouth to speak, sending water swirling into an intense whirlpool.

“My love for you is eternal” booms the face, moments before you splashdown into the iris.

Immediately after hitting the water you are pulled deeper into the ocean. To your surprise, gravity flips and you are greeted with a majestic sight: an icy city built on the underside of the water. The water forms the new ground, blocking any chance of returning.

A giant gazelle-like creature appears from the depths, sporting large talons from its head. It metamorphs into a crab, still with large talons, and starts to approach. “What a weird creature” you think, moments before making your decision.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Snowy Peak', style=discord.ButtonStyle.blurple)
    async def e4(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E4(self.starttime)

        await interaction.response.send_message(
            """
The cold smacks you like a brick wall, wind howling as you trek closer to the massive ice-topped mountain.

You hear Anorak’s voice calling from within the wind: “You know where to find me”

Except you don’t. That’s why you’re here, frozen in this tundra. One foot in front of the other, you trudge through the snow.

The looming mountain suddenly moves closer to you! Seconds later, you’re on the cliff wall, clinging to ice, a kilometer above the ground. You look up and an avalanche of snow begins to scream towards you.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Spinning Nebula', style=discord.ButtonStyle.blurple)
    async def e5(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E5(self.starttime)

        await interaction.response.send_message(
            """
The emptiness of space envelops your reality, plunging you into cold darkness. Stars dance around the remains of a galaxy, forming an amorphous cloud of cosmic dust. The nebula stretches to eternity, swaddling you in it’s heavenly wisps.

Deep within your brain you can make out Anorak’s fading voice “Find me in the final moments”

“No, hold on Anorak, I’m coming for you” you reply with your eyes clenched shut.

You open your eyes to see the nebula swirling around you, faster and faster, battering you with tiny dust particles from the ether. The dust storm emits a bolt of lightning, directed straight at you.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Haunted Graveyard', style=discord.ButtonStyle.blurple)
    async def e6(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E6(self.starttime)

        await interaction.response.send_message(
            """
You step bravely into the world of shadows. The sky is an unnatural purple color and scraggly trees line the horizon. The mysterious fractal crackles behind you in midair, the other possibilities collapsing on themselves until they disappear entirely.

You’re in an eternal field of graves. A spirit-like figure rises in the distance and disappears milliseconds before a decaying hand shoots up from the ground in front of you! Startled, you fall backwards, hitting your head on the ground. As you turn your head, you gasp, coming face to face with a half decomposed head of Anorak.

His jaw cracks open, sound creepily emanating from beyond the veil: “I’ve killed us both”
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Toxic Cave', style=discord.ButtonStyle.blurple)
    async def e7(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E7(self.starttime)

        await interaction.response.send_message(
            """
A swarm of vampire bats fly out of the possibility ahead. Undeterred you move towards the window, closing yourself into the damp cave. Pools of toxic blue sludge bubble ominously. You begin forward, a torch in hand. How did you get a torch?

You wave the torch in front of you, dispelling the darkness. From the sludge, a tentacle appears and snaps up your torch! To your dismay, it pulls the flame into the poisonous pool! When it touches the blue viscous gel, the pool ignites in an explosion, sending rocks flying.

“You’ll be trapped here!” Anorak shouts amidst the chaos of the blast. Forewarning be damned.

When the dust settles you can see the toxic ooze slowly creeping deeper into the cave with a life of its own. To your left you can see a fractal window leading to an Autumn forest.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Forest of Freaks', style=discord.ButtonStyle.blurple)
    async def e8(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E8(self.starttime)

        await interaction.response.send_message(
            """
You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? The last thing you remember… you check your pocket to make sure the crystal with the rune on it is still there. Wait. Something’s different this time. You don’t have the crystal, nor do you need one, you’re searching for... Anorak! Wait, how did you get to sleep? You were just in the fractal? Memories of past quests rush through time.

Is this a dream? You wonder, moments before a hallucination of Anorak enters your thoughts.

“I’m sorry I wasn’t skilled enough” the hallucination says sorrowfully.

The snow falls quietly amidst the warmth of the crackling fire.

So cold. So tired. Sleep by the fire?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E3(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Let Crab Grab You', style=discord.ButtonStyle.blurple)
    async def e13(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E13(self.starttime)

        await interaction.response.send_message(
            """
You feel sharp talons pierce your skin. It’s painful, but you’ve been through worse. You’re a Celestial on a quest after all, you knew it would be dangerous. A giant hawk-like creature has you in it’s claws, carrying you into a cloud.

From within the vaporous cloud you hear Anorak’s voice in your head again: “I cannot hold on much longer.”

Is this hawk Anorak? Or was Anorak referring to holding this fractal open?

The hawk drops you into a stick nest and lands with a screech. You’re face to beak with this freak when you hear a crackling behind you. Sensing your opportunity, you leap backwards just as the creature strikes with a blitz of speed.

You flip around, reaching toward the crackling light, narrowly avoiding the hawk’s beak.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Explore City', style=discord.ButtonStyle.blurple)
    async def e9(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E9(self.starttime)

        await interaction.response.send_message(
            """
An icy city reaches down into the depths of the ocean, defying logic and reality. Octopi make their way around the blocky buildings, zooming around the frozen metropolis. You swim through the canals of the underwater, upside down location, peeking into endless glassy windows within the megastructures.

Anorak sits within one. Excited, you try to reach him, smashing through the ice window. A barrage of bubbles floods out as the water displaces the air, sucking you into the room. You look up only to see Anorak transform into an octopus that was camouflaged as... him? The octopus launches a cloud of black ink towards you, clouding your vision.

This couldn’t have been Anorak. But where is he then, you wonder, waiting for the ink to clear.

You notice a large mural on the wall. It looks like a forest in Autumn. But oddly... something is moving in the distance.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E4(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Let Go', style=discord.ButtonStyle.blurple)
    async def e12(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E12(self.starttime)

        await interaction.response.send_message(
            """
You begin to slide on the ice. You hit a rock jutting out from the mountain you’re on, sending you cartwheeling in midair, now falling to the ground below. But it’s not ground you’re rushing towards anymore. It’s undulating now, like an ocean?

A huge feathered hawk-looking creature screeches above you. You orient yourself to face the hawk which bares its claws, ready to catch you. You know you can blast it with magic, but you’ll fall into the ocean below. What will you do?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Try to Dodge', style=discord.ButtonStyle.blurple)
    async def e16(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E16(self.starttime)

        await interaction.response.send_message(
            """
In an attempt to dodge, you leap to the side and are once again covered in cold darkness. You wonder if you made the right decision. This darkness is... deafening, yet peaceful.

In your cold tomb you wait for what seems like hours. But it can’t be.. it’s only a minute right?

“I love you” says Anorak’s voice in your head.

You can’t tell if it’s real or if it’s just what you want to hear. This nothingness is what you’d feel without him, you can’t let him go. You choose to live. You choose both of you to live.

A seed appears. And then another. And another. The seedlings begin to bloom, shooting green into the darkness. Seconds later, vines snake around and grass appears, turning the black landscape into a lush jungle.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E5(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Touch the Lightning', style=discord.ButtonStyle.blurple)
    async def e15(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E15(self.starttime)

        await interaction.response.send_message(
            """
The electricity courses through your body, sending tingles down your spine. You’ve never felt this much pure power before. Your vision crystalizes for a moment, as if you were looking through facets of a gemstone. The multitude of possibilities all exist simultaneously.

As quickly as the power is transferred, it dissipates. You’re left exhausted and floating in empty space. It’s just you now, alone.

Is it over?

Are you stuck in a reality where the World Maker never even existed? There’s nothing here.

You begin to feel cold. Shadowy claws appear above you. “This isn’t over”, you think.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Stay in Dust Storm', style=discord.ButtonStyle.blurple)
    async def e19(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E19(self.starttime)

        await interaction.response.send_message(
            """
The dust storm whips around you, battering your skin. The wind is ruthless. It sweeps you off your feet, launching you into the swirl of the dusty tornado. Around and around you go, amidst several species of freaks. You can see Ogres, Trolls, Fairies, Vampires, Skeletons, Werewolves, and more. Could this be the start of the Great Jumbling? A premonition perhaps?

Anorak’s face suddenly appears on an Ogre. It grumbles “Fractured realities can never sustain us” before it’s pulled away by the cyclone.

You’re tossed unceremoniously from the vortex into a decrepit house through a window. You take in your new surroundings, noticing wood paneling. It hides many secrets and many years of haunted history. The floors creak as you walk on them and spiders scurry past, disrupted by your unnatural entrance.

You make your way downstairs to find a feast set out on the table, illuminated by candlelight.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E6(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Stay', style=discord.ButtonStyle.blurple)
    async def e18(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E18(self.starttime)

        await interaction.response.send_message(
            """
Unnerved, you tear your gaze away, only to see a smattering of decaying hands rising from the ground. They animate, grasping at your ankles, determined to pull you into the underworld. You release a blast of magic at one of the hands, which spawns several more like a hydra.

You turn and begin to run, leaping over extended zombified hands. Everything around you begins to die and decompose at an alarming rate. The plants turn black, turning to an ashy dust.

You risk a glance behind you. Bad choice.

A horde of zombie freaks crawl over each other in a mass of dead flesh, ravenous for your brainz. You flip around to see the ash has formed into a large sandy tornado and you’re headed right toward it. You see a grave hole to your right that you can take cover in.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Run Away', style=discord.ButtonStyle.blurple)
    async def e22(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E22(self.starttime)

        await interaction.response.send_message(
            """
You break into a light jog. The grass feels cool underneath your feet as you run up the lone hill in the field. Up, up, up, you climb, unsure of exactly where you are or where you’re headed. You can see the fractal crackling in the sky, showing the coming apocalypse in every possibility. You reach the top and stare out at the land of Uruhan. What a peaceful land it was. Why did the World Maker have to destroy this peace you wonder?

Anorak’s face appears in the clouds. You can hear his voice throughout the land “Don’t start yet!” he yells.

Agreed, you think. You can see a lake in the distance by a forest of trees, a huge mountain covered in ice, a ghastly village shrouded in shadow, an explosive volcano spewing lava, a tropical beach near an ocean, and all the destruction imminent within the sky. It’s time to move, no time to waste.

You start running towards the tropical beach near the volcano, you’re drawn there for some reason.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E7(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Go Deeper in Cave', style=discord.ButtonStyle.blurple)
    async def e21(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E21(self.starttime)

        await interaction.response.send_message(
            """
You delve into the tunnel, blue toxic slime leading the way. You crawl to get further and accidentally touch the gel. It’s sticky and won’t let go, it uses some type of suction. Next thing you know, the gel is seeping into your skin and your veins, turning your skin a toxic blue.

You continue to crawl further, wondering what the sludge could do to you. You haven’t yet felt any effects other than a strange magnetic pull, yanking you deeper and deeper into the hole you’ve found yourself in.

You reach a fork in the tunnel. The magnetic pull wants you to go left towards a bright open field. To your right you see a whirling tornado of dust.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Enter Forest', style=discord.ButtonStyle.blurple)
    async def e25(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E25(self.starttime)

        await interaction.response.send_message(
            """
The forest is shedding leaves. It’s Autumn, and the colorful collection falls slowly to the ground. You walk through the peaceful woody area towards a lake, freshly fallen leaves crunching underneath your feet.

You hear Anorak quietly in your head “You’re fading from me”.

“Am I getting hotter or colder? Colder” you muse, skin bristling from the chill. This place would be such a nice date spot if the world wasn’t ending. The time for peace is later, the time for action is now.

You decide to turn around, paying attention to Anorak’s latest message.

You hope his message was meant for you at this time. The longer you’re here the more you wonder if time itself is Jumbled. Is all of this happening simultaneously in the fractured reality?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E8(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Sleep by Fire', style=discord.ButtonStyle.blurple)
    async def e24(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E24(self.starttime)

        await interaction.response.send_message(
            """
Bird songs echo in the background. Your eyes flutter open. It’s dawn. And damp. How strange, it’s not frost. It feels like Spring already!

You sit up quickly as you come to. You breathe in crisp air as you take in your surroundings. Light green plants cover the forest. It looks like everything is in bloom. An elf pokes their head out from behind a tree, disappearing as quietly as it retreats to a field.

You’re thirsty and a lake is nearby, you can see it shimmering in the distance.

Will you follow the elf or go to the lake?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Go to Lake', style=discord.ButtonStyle.blurple)
    async def e10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E10(self.starttime)

        await interaction.response.send_message(
            """
You find yourself in a deep underwater trench. How strange, this isn’t where you expected to see. Where did the ice go? The fractal you went through must be changing realities much more quickly than you anticipated.

You swim deeper into the trench, towards a school of sea creatures. A turtle floats closer to your face.

While looking into your eyes, you hear Anorak’s voice in your head: “Don’t panic”

You reach out to the turtle. As you do, the turtle rapidly grows in size and opens it’s now massive mouth. Before you can even comprehend what’s happening, the turtle snaps it’s mouth around you, plunging you into the darkness of it’s belly.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E9(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Approach Mural', style=discord.ButtonStyle.blurple)
    async def e25(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E25(self.starttime)

        await interaction.response.send_message(
            """
The forest is shedding leaves. It’s Autumn, and the colorful collection falls slowly to the ground. You walk through the peaceful woody area towards a lake, freshly fallen leaves crunching underneath your feet.

You hear Anorak quietly in your head “You’re fading from me”.

“Am I getting hotter or colder? Colder” you muse, skin bristling from the chill. This place would be such a nice date spot if the world wasn’t ending. The time for peace is later, the time for action is now.

You decide to turn around, paying attention to Anorak’s latest message.

You hope his message was meant for you at this time. The longer you’re here the more you wonder if time itself is Jumbled. Is all of this happening simultaneously in the fractured reality?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Return to City', style=discord.ButtonStyle.blurple)
    async def e10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E10(self.starttime)

        await interaction.response.send_message(
            """
You find yourself in a deep underwater trench. How strange, this isn’t where you expected to see. Where did the ice go? The fractal you went through must be changing realities much more quickly than you anticipated.

You swim deeper into the trench, towards a school of sea creatures. A turtle floats closer to your face.

While looking into your eyes, you hear Anorak’s voice in your head: “Don’t panic”

You reach out to the turtle. As you do, the turtle rapidly grows in size and opens it’s now massive mouth. Before you can even comprehend what’s happening, the turtle snaps it’s mouth around you, plunging you into the darkness of it’s belly.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E10(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label="Don't Panic", style=discord.ButtonStyle.blurple)
    async def e11(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E11(self.starttime)

        await interaction.response.send_message(
            """
You find yourself in darkness. You can hear a creature’s sounds echo around you, but it’s impossible to see anything here. You listened to Anorak, but this place is strange. Fractaled realities are no joke.

Anorak’s voice echoes all around you: “Only enter the fracture during the window”

“Enter during the window? Not through the window? What window?” You think aloud, hoping Anorak will respond, but you’re greeted with silence. You wonder what Anorak could mean. But could he just be confused?

A small light appears nearby. It begins to sparkle and flash, growing in a crackle pattern. Could this be the window Anorak was talking about? A burst of lightning shoots from the crackle, beckoning to you.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E11(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Touch the Lightning', style=discord.ButtonStyle.blurple)
    async def e15(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E15(self.starttime)

        await interaction.response.send_message(
            """
The electricity courses through your body, sending tingles down your spine. You’ve never felt this much pure power before. Your vision crystalizes for a moment, as if you were looking through facets of a gemstone. The multitude of possibilities all exist simultaneously.

As quickly as the power is transferred, it dissipates. You’re left exhausted and floating in empty space. It’s just you now, alone.

Is it over?

Are you stuck in a reality where the World Maker never even existed? There’s nothing here.

You begin to feel cold. Shadowy claws appear above you. “This isn’t over”, you think.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Enter the Crackle', style=discord.ButtonStyle.blurple)
    async def e14(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E14(self.starttime)

        await interaction.response.send_message(
            """
A flash of light. You’re falling. Through trees, vines, plants, greenery... You smash through a seemingly endless rush of lush jungle plants until you land near a gurgling stream. The crackle you traveled through can be seen through the canopy above. It glistens in the sky, growing larger. Chunks of sky seem to be falling, warping the very reality you’re a part of.

You turn back to the stream which has turned an unnatural purple. It sloshes around the riverbed, quickly extending past it’s natural course. You hear a voice emanating from behind you. As you turn to identify the voice, you see a caterpillar with trippy patterns growing wings.

The now-butterfly flutters closer to you and whispers as Anorak: “Wait before reality fractures. Be patient”. It spontaneously combusts and the wings fall to the ground. A grave emerges from the ground.

You turn back to the stream which could be described as anything but. The ‘stream’ has turned into a huge purple wave, blocking out the sky. More graves begin to emerge from the ground.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E12(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Let Hawk Grab You', style=discord.ButtonStyle.blurple)
    async def e13(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E13(self.starttime)

        await interaction.response.send_message(
            """
You feel sharp talons pierce your skin. It’s painful, but you’ve been through worse. You’re a Celestial on a quest after all, you knew it would be dangerous. A giant hawk-like creature has you in it’s claws, carrying you into a cloud.

From within the vaporous cloud you hear Anorak’s voice in your head again: “I cannot hold on much longer.”

Is this hawk Anorak? Or was Anorak referring to holding this fractal open?

The hawk drops you into a stick nest and lands with a screech. You’re face to beak with this freak when you hear a crackling behind you. Sensing your opportunity, you leap backwards just as the creature strikes with a blitz of speed.

You flip around, reaching toward the crackling light, narrowly avoiding the hawk’s beak.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Fall into Ocean', style=discord.ButtonStyle.blurple)
    async def e10(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E10(self.starttime)

        await interaction.response.send_message(
            """
You find yourself in a deep underwater trench. How strange, this isn’t where you expected to see. Where did the ice go? The fractal you went through must be changing realities much more quickly than you anticipated.

You swim deeper into the trench, towards a school of sea creatures. A turtle floats closer to your face.

While looking into your eyes, you hear Anorak’s voice in your head: “Don’t panic”

You reach out to the turtle. As you do, the turtle rapidly grows in size and opens it’s now massive mouth. Before you can even comprehend what’s happening, the turtle snaps it’s mouth around you, plunging you into the darkness of it’s belly.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E13(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Enter the Crackle', style=discord.ButtonStyle.blurple)
    async def e14(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E14(self.starttime)

        await interaction.response.send_message(
            """
A flash of light. You’re falling. Through trees, vines, plants, greenery... You smash through a seemingly endless rush of lush jungle plants until you land near a gurgling stream. The crackle you traveled through can be seen through the canopy above. It glistens in the sky, growing larger. Chunks of sky seem to be falling, warping the very reality you’re a part of.

You turn back to the stream which has turned an unnatural purple. It sloshes around the riverbed, quickly extending past it’s natural course. You hear a voice emanating from behind you. As you turn to identify the voice, you see a caterpillar with trippy patterns growing wings.

The now-butterfly flutters closer to you and whispers as Anorak: “Wait before reality fractures. Be patient”. It spontaneously combusts and the wings fall to the ground. A grave emerges from the ground.

You turn back to the stream which could be described as anything but. The ‘stream’ has turned into a huge purple wave, blocking out the sky. More graves begin to emerge from the ground.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E14(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Stay Near Graves', style=discord.ButtonStyle.blurple)
    async def e18(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E18(self.starttime)

        await interaction.response.send_message(
            """
Unnerved, you tear your gaze away, only to see a smattering of decaying hands rising from the ground. They animate, grasping at your ankles, determined to pull you into the underworld. You release a blast of magic at one of the hands, which spawns several more like a hydra.

You turn and begin to run, leaping over extended zombified hands. Everything around you begins to die and decompose at an alarming rate. The plants turn black, turning to an ashy dust.

You risk a glance behind you. Bad choice.

A horde of zombie freaks crawl over each other in a mass of dead flesh, ravenous for your brainz. You flip around to see the ash has formed into a large sandy tornado and you’re headed right toward it. You see a grave hole to your right that you can take cover in.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Run into Jungle', style=discord.ButtonStyle.blurple)
    async def e17(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E17(self.starttime)

        await interaction.response.send_message(
            """
You sprint into the jungle, waving away shrubbery and those annoying gnatty insects that buzz in your ears. Come to think of it, that buzzing sounds like something familiar!

“Your window is in the final 10 seconds” Anorak buzzes in your ear.

Glad you didn’t slap that fly, you think. “What window, Anorak, be more specific! There’s infinite windows!” And what was that little bit about the final 10 seconds?

No time to think, you think, paradoxically. Nothing here makes sense in reality anyway. Is this a simulation? Are you alive? Is life worth living? For Anorak, for love, it is worth living.

Deeper into the jungle you trek, pushing aside colorful flora. You can sense freaks are here. Too bad the Great Jumbling would displace them all. You wonder if their species will ever be seen again.

To your left you spot a tunnel covered in moss and greenery, but what caught your eye was a mystical blue gel, pulsating and moving closer to the tunnel, almost beckoning to you. To your right you see a clearing in the jungle with a fully set table with a massive feast. How can that be possible? It must be a mirage or a trick of the mind?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E15(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Wait', style=discord.ButtonStyle.blurple)
    async def e13(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E13(self.starttime)

        await interaction.response.send_message(
            """
You feel sharp talons pierce your skin. It’s painful, but you’ve been through worse. You’re a Celestial on a quest after all, you knew it would be dangerous. A giant hawk-like creature has you in it’s claws, carrying you into a cloud.

From within the vaporous cloud you hear Anorak’s voice in your head again: “I cannot hold on much longer.”

Is this hawk Anorak? Or was Anorak referring to holding this fractal open?

The hawk drops you into a stick nest and lands with a screech. You’re face to beak with this freak when you hear a crackling behind you. Sensing your opportunity, you leap backwards just as the creature strikes with a blitz of speed.

You flip around, reaching toward the crackling light, narrowly avoiding the hawk’s beak.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Avoid the Claws', style=discord.ButtonStyle.blurple)
    async def e16(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E16(self.starttime)

        await interaction.response.send_message(
            """
In an attempt to dodge, you leap to the side and are once again covered in cold darkness. You wonder if you made the right decision. This darkness is... deafening, yet peaceful.

In your cold tomb you wait for what seems like hours. But it can’t be.. it’s only a minute right?

“I love you” says Anorak’s voice in your head.

You can’t tell if it’s real or if it’s just what you want to hear. This nothingness is what you’d feel without him, you can’t let him go. You choose to live. You choose both of you to live.

A seed appears. And then another. And another. The seedlings begin to bloom, shooting green into the darkness. Seconds later, vines snake around and grass appears, turning the black landscape into a lush jungle.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E16(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Explore Jungle', style=discord.ButtonStyle.blurple)
    async def e17(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E17(self.starttime)

        await interaction.response.send_message(
            """
You sprint into the jungle, waving away shrubbery and those annoying gnatty insects that buzz in your ears. Come to think of it, that buzzing sounds like something familiar!

“Your window is in the final 10 seconds” Anorak buzzes in your ear.

Glad you didn’t slap that fly, you think. “What window, Anorak, be more specific! There’s infinite windows!” And what was that little bit about the final 10 seconds?

No time to think, you think, paradoxically. Nothing here makes sense in reality anyway. Is this a simulation? Are you alive? Is life worth living? For Anorak, for love, it is worth living.

Deeper into the jungle you trek, pushing aside colorful flora. You can sense freaks are here. Too bad the Great Jumbling would displace them all. You wonder if their species will ever be seen again.

To your left you spot a tunnel covered in moss and greenery, but what caught your eye was a mystical blue gel, pulsating and moving closer to the tunnel, almost beckoning to you. To your right you see a clearing in the jungle with a fully set table with a massive feast. How can that be possible? It must be a mirage or a trick of the mind?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E17(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Crawl in Tunnel', style=discord.ButtonStyle.blurple)
    async def e21(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E21(self.starttime)

        await interaction.response.send_message(
            """
You delve into the tunnel, blue toxic slime leading the way. You crawl to get further and accidentally touch the gel. It’s sticky and won’t let go, it uses some type of suction. Next thing you know, the gel is seeping into your skin and your veins, turning your skin a toxic blue.

You continue to crawl further, wondering what the sludge could do to you. You haven’t yet felt any effects other than a strange magnetic pull, yanking you deeper and deeper into the hole you’ve found yourself in.

You reach a fork in the tunnel. The magnetic pull wants you to go left towards a bright open field. To your right you see a whirling tornado of dust.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Sit at Table', style=discord.ButtonStyle.blurple)
    async def e20(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E20(self.starttime)

        await interaction.response.send_message(
            """
You sit at the table amidst a cornucopia of food. The spooky atmosphere casts a pall over the bountiful meal. You wish you weren’t in such a rush so you could truly appreciate the experience, but there’s no time to waste, you have to find Anorak before the fracture collapses in on itself!

Your thought is interrupted by the ethereal presence of a spirit at the head of the table. You recognize him immediately, your true love Anorak.

“My spell was faulty” Anorak muses, his shape shifting in the presence of low air currents.

Before you have time to comprehend, more spirits appear at the table. You look down at your hands only to find that you, too, have been transformed into a ghost! Startled, you back away from the table, tipping the chair as you go. The fantoms give chase, swirling and floating through any obstacles in their way.

You trip, much to the amusement of the ghosts. You see an elemental crack just within reach. As you drag yourself closer and dip your head in, you can hear the ghosts cackling. Everything goes white as you...
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E18(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Run into Dust Storm', style=discord.ButtonStyle.blurple)
    async def e19(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E19(self.starttime)

        await interaction.response.send_message(
            """
The dust storm whips around you, battering your skin. The wind is ruthless. It sweeps you off your feet, launching you into the swirl of the dusty tornado. Around and around you go, amidst several species of freaks. You can see Ogres, Trolls, Fairies, Vampires, Skeletons, Werewolves, and more. Could this be the start of the Great Jumbling? A premonition perhaps?

Anorak’s face suddenly appears on an Ogre. It grumbles “Fractured realities can never sustain us” before it’s pulled away by the cyclone.

You’re tossed unceremoniously from the vortex into a decrepit house through a window. You take in your new surroundings, noticing wood paneling. It hides many secrets and many years of haunted history. The floors creak as you walk on them and spiders scurry past, disrupted by your unnatural entrance.

You make your way downstairs to find a feast set out on the table, illuminated by candlelight.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Dodge into Grave', style=discord.ButtonStyle.blurple)
    async def e16(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E16(self.starttime)

        await interaction.response.send_message(
            """
In an attempt to dodge, you leap to the side and are once again covered in cold darkness. You wonder if you made the right decision. This darkness is... deafening, yet peaceful.

In your cold tomb you wait for what seems like hours. But it can’t be.. it’s only a minute right?

“I love you” says Anorak’s voice in your head.

You can’t tell if it’s real or if it’s just what you want to hear. This nothingness is what you’d feel without him, you can’t let him go. You choose to live. You choose both of you to live.

A seed appears. And then another. And another. The seedlings begin to bloom, shooting green into the darkness. Seconds later, vines snake around and grass appears, turning the black landscape into a lush jungle.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E19(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Sit at Table', style=discord.ButtonStyle.blurple)
    async def e20(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E20(self.starttime)

        await interaction.response.send_message(
            """
You sit at the table amidst a cornucopia of food. The spooky atmosphere casts a pall over the bountiful meal. You wish you weren’t in such a rush so you could truly appreciate the experience, but there’s no time to waste, you have to find Anorak before the fracture collapses in on itself!

Your thought is interrupted by the ethereal presence of a spirit at the head of the table. You recognize him immediately, your true love Anorak.

“My spell was faulty” Anorak muses, his shape shifting in the presence of low air currents.

Before you have time to comprehend, more spirits appear at the table. You look down at your hands only to find that you, too, have been transformed into a ghost! Startled, you back away from the table, tipping the chair as you go. The fantoms give chase, swirling and floating through any obstacles in their way.

You trip, much to the amusement of the ghosts. You see an elemental crack just within reach. As you drag yourself closer and dip your head in, you can hear the ghosts cackling. Everything goes white as you...
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E20(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Close Eyes', style=discord.ButtonStyle.blurple)
    async def e24(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E24(self.starttime)

        await interaction.response.send_message(
            """
Bird songs echo in the background. Your eyes flutter open. It’s dawn. And damp. How strange, it’s not frost. It feels like Spring already!

You sit up quickly as you come to. You breathe in crisp air as you take in your surroundings. Light green plants cover the forest. It looks like everything is in bloom. An elf pokes their head out from behind a tree, disappearing as quietly as it retreats to a field.

You’re thirsty and a lake is nearby, you can see it shimmering in the distance.

Will you follow the elf or go to the lake?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Envision a Beach', style=discord.ButtonStyle.blurple)
    async def e23(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E23(self.starttime)

        await interaction.response.send_message(
            """
The coastline is peaceful, ocean lapping against the tropical trees. A massive volcano spews black smoke into the sky, crackling with static electricity. It's an ominous presence, warning about the coming Jumbling. A rumbling can be felt beneath your feet, just before a huge plume of smoke is belched from the volcano, along with several streams of lava.

Anorak’s face appears in the smoke, his mouth sparking with electricity as he speaks aloud “Wait, don’t enter the fracture”

Weird, you’re already in the fracture. Give me something better next time my love, you think, slightly annoyed.

Your annoyance is short lived though, molten rock is shooting towards you at rapid speed. Your skin starts to glow blue, it’s as if you have a chilled suit of armor around you but you don’t remember how... You close your eyes and can feel your skin getting colder. Should you risk it?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E21(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Go to Dust Tornado', style=discord.ButtonStyle.blurple)
    async def e19(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E19(self.starttime)

        await interaction.response.send_message(
            """
The dust storm whips around you, battering your skin. The wind is ruthless. It sweeps you off your feet, launching you into the swirl of the dusty tornado. Around and around you go, amidst several species of freaks. You can see Ogres, Trolls, Fairies, Vampires, Skeletons, Werewolves, and more. Could this be the start of the Great Jumbling? A premonition perhaps?

Anorak’s face suddenly appears on an Ogre. It grumbles “Fractured realities can never sustain us” before it’s pulled away by the cyclone.

You’re tossed unceremoniously from the vortex into a decrepit house through a window. You take in your new surroundings, noticing wood paneling. It hides many secrets and many years of haunted history. The floors creak as you walk on them and spiders scurry past, disrupted by your unnatural entrance.

You make your way downstairs to find a feast set out on the table, illuminated by candlelight.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Go to Field', style=discord.ButtonStyle.blurple)
    async def e22(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E22(self.starttime)

        await interaction.response.send_message(
            """
You break into a light jog. The grass feels cool underneath your feet as you run up the lone hill in the field. Up, up, up, you climb, unsure of exactly where you are or where you’re headed. You can see the fractal crackling in the sky, showing the coming apocalypse in every possibility. You reach the top and stare out at the land of Uruhan. What a peaceful land it was. Why did the World Maker have to destroy this peace you wonder?

Anorak’s face appears in the clouds. You can hear his voice throughout the land “Don’t start yet!” he yells.

Agreed, you think. You can see a lake in the distance by a forest of trees, a huge mountain covered in ice, a ghastly village shrouded in shadow, an explosive volcano spewing lava, a tropical beach near an ocean, and all the destruction imminent within the sky. It’s time to move, no time to waste.

You start running towards the tropical beach near the volcano, you’re drawn there for some reason.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E22(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Continue to Beach', style=discord.ButtonStyle.blurple)
    async def e23(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E23(self.starttime)

        await interaction.response.send_message(
            """
The coastline is peaceful, ocean lapping against the tropical trees. A massive volcano spews black smoke into the sky, crackling with static electricity. It's an ominous presence, warning about the coming Jumbling. A rumbling can be felt beneath your feet, just before a huge plume of smoke is belched from the volcano, along with several streams of lava.

Anorak’s face appears in the smoke, his mouth sparking with electricity as he speaks aloud “Wait, don’t enter the fracture”

Weird, you’re already in the fracture. Give me something better next time my love, you think, slightly annoyed.

Your annoyance is short lived though, molten rock is shooting towards you at rapid speed. Your skin starts to glow blue, it’s as if you have a chilled suit of armor around you but you don’t remember how... You close your eyes and can feel your skin getting colder. Should you risk it?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E23(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Close Eyes', style=discord.ButtonStyle.blurple)
    async def e26(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E26(self.starttime)

        await interaction.response.send_message(
            """
You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? Last thing you remember is turning around and closing your eyes... that’s right, you remember. It’s not magic this time, just time travel through a multiverse of realities.

Anorak’s face emerges from the fire, his face full of compassion and warmth. Or maybe that’s just the fire’s warmth... “50 seconds must pass”

“Huh, that one’s oddly specific” you think. “Where must 50 seconds pass?”

Your thoughts are interrupted by an impatient sky, lightning shooting across the heavens as a harbinger of the coming destruction. This fractured reality can only survive for a minute, but because Anorak has created this fracture, shouldn't it act as a loop, trapping you but also giving you your best chance to find him? You will succeed; you will find Anorak. You’re sure of it.

You’re sitting on an icy slope. The only light here comes from the fire.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Dive into the Ocean', style=discord.ButtonStyle.blurple)
    async def e9(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E9(self.starttime)

        await interaction.response.send_message(
            """
An icy city reaches down into the depths of the ocean, defying logic and reality. Octopi make their way around the blocky buildings, zooming around the frozen metropolis. You swim through the canals of the underwater, upside down location, peeking into endless glassy windows within the megastructures.

Anorak sits within one. Excited, you try to reach him, smashing through the ice window. A barrage of bubbles floods out as the water displaces the air, sucking you into the room. You look up only to see Anorak transform into an octopus that was camouflaged as... him? The octopus launches a cloud of black ink towards you, clouding your vision.

This couldn’t have been Anorak. But where is he then, you wonder, waiting for the ink to clear.

You notice a large mural on the wall. It looks like a forest in Autumn. But oddly... something is moving in the distance.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E24(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Go to Lake', style=discord.ButtonStyle.blurple)
    async def e25(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E25(self.starttime)

        await interaction.response.send_message(
            """
The forest is shedding leaves. It’s Autumn, and the colorful collection falls slowly to the ground. You walk through the peaceful woody area towards a lake, freshly fallen leaves crunching underneath your feet.

You hear Anorak quietly in your head “You’re fading from me”.

“Am I getting hotter or colder? Colder” you muse, skin bristling from the chill. This place would be such a nice date spot if the world wasn’t ending. The time for peace is later, the time for action is now.

You decide to turn around, paying attention to Anorak’s latest message.

You hope his message was meant for you at this time. The longer you’re here the more you wonder if time itself is Jumbled. Is all of this happening simultaneously in the fractured reality?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Follow Elf to Field', style=discord.ButtonStyle.blurple)
    async def e22(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E22(self.starttime)

        await interaction.response.send_message(
            """
You break into a light jog. The grass feels cool underneath your feet as you run up the lone hill in the field. Up, up, up, you climb, unsure of exactly where you are or where you’re headed. You can see the fractal crackling in the sky, showing the coming apocalypse in every possibility. You reach the top and stare out at the land of Uruhan. What a peaceful land it was. Why did the World Maker have to destroy this peace you wonder?

Anorak’s face appears in the clouds. You can hear his voice throughout the land “Don’t start yet!” he yells.

Agreed, you think. You can see a lake in the distance by a forest of trees, a huge mountain covered in ice, a ghastly village shrouded in shadow, an explosive volcano spewing lava, a tropical beach near an ocean, and all the destruction imminent within the sky. It’s time to move, no time to waste.

You start running towards the tropical beach near the volcano, you’re drawn there for some reason.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E25(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label='Turn Around', style=discord.ButtonStyle.blurple)
    async def e26(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E26(self.starttime)

        await interaction.response.send_message(
            """
You awaken, shivering. You’re in the snow, in a dense forest. It’s dark out, and it feels like the dead of winter. A crackling fire emits a soft glow of light around you. You’re so tired. It’s cold. So cold. How did you get here, you wonder? Last thing you remember is turning around and closing your eyes... that’s right, you remember. It’s not magic this time, just time travel through a multiverse of realities.

Anorak’s face emerges from the fire, his face full of compassion and warmth. Or maybe that’s just the fire’s warmth... “50 seconds must pass”

“Huh, that one’s oddly specific” you think. “Where must 50 seconds pass?”

Your thoughts are interrupted by an impatient sky, lightning shooting across the heavens as a harbinger of the coming destruction. This fractured reality can only survive for a minute, but because Anorak has created this fracture, shouldn't it act as a loop, trapping you but also giving you your best chance to find him? You will succeed; you will find Anorak. You’re sure of it.

You’re sitting on an icy slope. The only light here comes from the fire.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class E26(discord.ui.View):
    def __init__(self, starttime):
        if (60 - (datetime.datetime.utcnow() - starttime).total_seconds()) < 0:
            timeout = 1.0
        else:
            timeout = 60 - (datetime.datetime.utcnow() - starttime).total_seconds()

        super().__init__(timeout=timeout)
        self.msg = None
        self.starttime = starttime

    @discord.ui.button(label="Extinguish Fire", style=discord.ButtonStyle.blurple)
    async def e11(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E11(self.starttime)

        await interaction.response.send_message(
            """
You find yourself in darkness. You can hear a creature’s sounds echo around you, but it’s impossible to see anything here. You listened to Anorak, but this place is strange. Fractaled realities are no joke.

Anorak’s voice echoes all around you: “Only enter the fracture during the window”

“Enter during the window? Not through the window? What window?” You think aloud, hoping Anorak will respond, but you’re greeted with silence. You wonder what Anorak could mean. But could he just be confused?

A small light appears nearby. It begins to sparkle and flash, growing in a crackle pattern. Could this be the window Anorak was talking about? A burst of lightning shoots from the crackle, beckoning to you.
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    @discord.ui.button(label='Slide Down Ice', style=discord.ButtonStyle.blurple)
    async def e12(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.stop()
        self.clear_items()

        await self.msg.edit(view=self)

        view = E12(self.starttime)

        await interaction.response.send_message(
            """
You begin to slide on the ice. You hit a rock jutting out from the mountain you’re on, sending you cartwheeling in midair, now falling to the ground below. But it’s not ground you’re rushing towards anymore. It’s undulating now, like an ocean?

A huge feathered hawk-looking creature screeches above you. You orient yourself to face the hawk which bares its claws, ready to catch you. You know you can blast it with magic, but you’ll fall into the ocean below. What will you do?
            """, view=view, ephemeral=True)

        view.msg = await interaction.original_message()

    async def on_timeout(self):
        if self.msg:

            view = RestartView()
            await self.msg.edit(
                """
“I CAN’T HOLD IT ANY LONGER” Anorak screams in your head telepathically.

The fractured reality that could be seen in the sky shatters into a billion possibilities as the massive fist of the World Maker pummels down through the air.

The fist makes an impact, sending the land of Uruhan into chaos.

Your final moments of life close around you. You telepathically send one last message - “ANORAK, I LOV...........”
            """, view=view)

            view.msg = self.msg


class ChallengeView5(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Begin Quest', style=discord.ButtonStyle.blurple, custom_id='persistent_view:challenge5')
    async def challenge(self, button: discord.ui.Button, interaction: discord.Interaction):

        startembed = discord.Embed(
            description=f"You will have 60 seconds until this quest self-destructs. You may retry the quest as many times as you wish, but you will only have 60 seconds each time. Good luck!", color=0x000ff)
        startembed.set_author(name="Quest 5", icon_url=interaction.guild.icon.url)
        startembed.set_footer(text=footertext, icon_url=interaction.guild.icon.url)

        view = BeginView()

        await interaction.response.send_message(interaction.user.mention, embed=startembed, view=view, ephemeral=True)

        view.msg = await interaction.original_message()


class Challenge5(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    # Commands
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.channel_id == 912904607477399603 and str(payload.emoji) == "\U0001f6b3":
            check = payload.member.guild.get_role(916144076296945704)
            await payload.member.add_roles(check)

    @slash_command(guild_ids=guildIDs, description="Creates Quest 5", default_permission=False)
    @permissions.has_role(godroleid)
    async def quest5(self, ctx):
        rulesembed = discord.Embed(description=f"Click below to begin the quest.", color=embedcolor)
        rulesembed.set_author(name="Quest 5", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text=footertext, icon_url=ctx.guild.icon.url)

        view = ChallengeView5()

        await ctx.send(embed=rulesembed, view=view)
        await ctx.respond(embed=discord.Embed(description="**Created Quest 5 message for users!**", color=embedcolor), ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        global enlistedchannel
        enlistedchannel = self.client.get_channel(whitelistchannelid)
        if not self.persistent_views_added:
            self.client.add_view(ChallengeView5())
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Challenge5(client))
