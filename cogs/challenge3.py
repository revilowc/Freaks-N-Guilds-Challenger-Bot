import discord
import time
from discord.abc import PrivateChannel
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

class FiveButton(discord.ui.Button):
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
        elif self.view.label5 == self.label:
            self.view.choice = 5

        await interaction.response.edit_message(view=self.view)


class FiveView(discord.ui.View):
    def __init__(self, label1, label2, label3, label4, label5):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.choice = 0
        self.timeout = False

        self.add_item(FiveButton(label1))
        self.add_item(FiveButton(label2))
        self.add_item(FiveButton(label3))
        self.add_item(FiveButton(label4))
        self.add_item(FiveButton(label5))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True

class SixButton(discord.ui.Button):
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
        elif self.view.label5 == self.label:
            self.view.choice = 5
        elif self.view.label6 == self.label:
            self.view.choice = 6

        await interaction.response.edit_message(view=self.view)


class SixView(discord.ui.View):
    def __init__(self, label1, label2, label3, label4, label5, label6):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.label6 = label6
        self.choice = 0
        self.timeout = False

        self.add_item(SixButton(label1))
        self.add_item(SixButton(label2))
        self.add_item(SixButton(label3))
        self.add_item(SixButton(label4))
        self.add_item(SixButton(label5))
        self.add_item(SixButton(label6))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True

class SevenButton(discord.ui.Button):
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
        elif self.view.label5 == self.label:
            self.view.choice = 5
        elif self.view.label6 == self.label:
            self.view.choice = 6
        elif self.view.label7 == self.label:
            self.view.choice = 7

        await interaction.response.edit_message(view=self.view)


class SevenView(discord.ui.View):
    def __init__(self, label1, label2, label3, label4, label5, label6, label7):
        super().__init__()
        self.label1 = label1
        self.label2 = label2
        self.label3 = label3
        self.label4 = label4
        self.label5 = label5
        self.label6 = label6
        self.label7 = label7
        self.choice = 0
        self.timeout = False

        self.add_item(SevenButton(label1))
        self.add_item(SevenButton(label2))
        self.add_item(SevenButton(label3))
        self.add_item(SevenButton(label4))
        self.add_item(SevenButton(label5))
        self.add_item(SevenButton(label6))
        self.add_item(SevenButton(label7))

    async def on_timeout(self):
        # *_original_message methods can be used after the initial response,
        # available until the interaction's webhook expires
        self.stop()
        self.timeout = True



async def C1(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c1view = TwoView("Run across the pathway", "Carefully walk")

  await interaction.followup.send(
        "You shield your eyes from the searing heat with your arm. The flames subside but the temperature doesn’t drop. You move your arm and to your surprise, you’re surrounded by red hot lava! You look up to see towering igneous rock cliffs amidst billowing black smoke. Is this… crippling debt? Wait, no, a volcano!?",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "A booming voice fills the crater “Choose correctly and you’ll find what you seek. Choose incorrectly and feel the fury of fire! Welcome to The Illuvar’s Gauntlet.” How ominous.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "You look forward to see a thin pathway ahead. You take a deep breath and start along it, lava lapping mere feet from your own feet.", view=c1view,
        ephemeral=True)

  await c1view.wait()

  if c1view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c1view.choice == 2:
    await interaction.followup.send(
        "You cautiously walk forward, step by step, ensuring you don’t fall into the blazing molten rock on either side of you. It looks as if the path is thinning. Or is that just a trick of the light?",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "No, no, it’s definitely thinning! Wait no, it’s not the path… it’s the lava! It’s rising and consuming the path! With a shriek you start to pick up the pace just as a large bubble of lava pops, sending molten lava directly in front of you, blocking your path. You hurriedly turn around looking for a way back.",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "To your dismay, you don’t even see the path behind you. You had been so concerned with what was in front of you that you didn’t realize you were on an incline. Everything behind you has been consumed by lava. In a frenzy you try to leap over the lava on the path in front of you, but you don’t quite make it. With a bloodcurdling scream you are seared like a well-done steak and die shortly after.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif c1view.choice == 1:
    await C2(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C2(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c2view = TwoView("Go to the podium", "Ignore the podium")

  await interaction.followup.send(
        "You break out into a sprint! Several times you nearly slip into the bubbling lava, but you catch yourself. Eyes forward, you can see a small plateau. Triumphant, you reach the plateau!",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "To your right you see a small podium.", view=c2view,
        ephemeral=True)

  await c2view.wait()

  if c2view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c2view.choice == 1:
    c2view2 = OneView("Continue on")

    await interaction.followup.send(
        "You approach the podium and see a detailed painted image.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "https://media.discordapp.net/attachments/840365409445609472/912143629773049876/unnamed.png", view=c2view2,
        ephemeral=True)

    await c2view2.wait()

    if c2view2.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    await C3(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif c2view.choice == 2:
    await C3(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C3(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c3view = TwoView("Run", "Wait")

  await interaction.followup.send(
        "You move past the podium. The lava continues to rise behind you. The heat creates a shimmering in your line of sight, warping your vision slightly. Undeterred, you trek on, leaping from floating island to floating island, with small rivers of lava slowly filling in the crevices between the islands.",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "To your left the lava begins to bubble, sending ripples your way.", view=c3view,
        ephemeral=True)

  await c3view.wait()

  if c3view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c3view.choice == 2:
    await interaction.followup.send(
        "The lava starts to pop, sending flecks of lava your way. You duck just in time, avoiding the deadly molten rock. Your arm, on the other hand, isn’t so lucky. You feel extreme pain as the lava slices off your arm like butter. Incapacitated with pain, you begin to leap from island to island.",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "Your vision, blurry from the heat, smoke, and your own tears, causes you to overcompensate in a jump. Your right foot touches the red hot lava, instantly searing it off and causing your leg to catch fire.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You crumple, pain unrelenting, until you realize with a fatal chuckle that this little mistake cost you an arm and a leg. Near where the lava was bubbling a volcanic freak explodes from the depths. You see the rocky form of a mini volcano freak begin to shake and explode, launching a wall of lava in your direction.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "You close your eyes and accept your fate.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif c3view.choice == 1:
    await C4(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C4(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c4view = TwoView("Continue walking forward", "Scale the cliff wall")

  await interaction.followup.send(
        "You pick up the pace, this ain’t no cake walk after all. This is Illuvar’s Gauntlet. You leap easily from island to island as the lava bubbles behind you. A freak bursts from the lava. You glance back and see a mini volcano with blazing eyes start to shake. You don’t wanna see the end of that. Eyes forward, you quickly continue forward.",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "You hear a loud explosion, but you don’t turn back. Cool people don’t look at explosions.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "It’s good you didn’t, because a wall of flames lick your behind, lighting a fire under your ass. That could have been a lot worse.",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "After a few more leaps of faith you reach a large area near a cliff wall. In the distance you see a wall of lava flowing down into a deep crevice.", view=c4view,
        ephemeral=True)

  await c4view.wait()

  if c4view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c4view.choice == 1:
    await C5(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif c4view.choice == 2:
    c8shortcut = True
    await C8(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C5(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c5view = TwoView("Investigate the shine", "Pick up the rock")

  await interaction.followup.send(
        "You continue walking forward. The lava behind you seems to be receding, it seems you’re past the worst of it. “But this is The Illuvar’s Gauntlet” you think with a smirk. It can’t be that easy.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "Right on cue a giant lizard with 2 heads leaps from the shadows into your path! One head hisses at you while the other bares it’s serrated teeth, ready to chow down on some juicy human flesh.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "You hurriedly glance around. You notice a rock near your feet and what looks to be a dull shine of metal just behind the lizard freak.", view=c5view,
        ephemeral=True)

  await c5view.wait()

  if c5view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c5view.choice == 1:
    await interaction.followup.send(
        "Your curiosity is unquenchable. Even in the face of certain danger you truly believe you can get past the lizard to go for this unknown metal object.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You kick some loose rocks at the lizard’s toothy grin as a distraction, causing it to welp in pain. You take your chance and sprint right at the shiny object. You’re about to snatch it when you feel a sharp pain in your ankle; the other head has found its target. To your dismay, you’re lifted upside down by your ankle and are twisted to see the flipped face of the second head.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "It’s all over, you think, just before the lizard chomps down on its juicy treat.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif c5view.choice == 2:
    await C6(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C6(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c6view = TwoView("Stay and fight", "Rappel down the cliff")

  await interaction.followup.send(
        "You pick up the rock for the barest of protection, ready for a fight. The lizard starts forward and you leap to the side, narrowly evading a sudden chomp from one of the heads. You fight back with a swift kick to the jaw just as the second head swivels to attack. It opens its mouth and you see your chance. You chuck the stone and land it directly in the lizard’s gaping maw.",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "Defenseless, you remember the dull shiny object. You leap towards it while the lizard is stunned to find a chain. With a quick flick of da wrists, you free the chain from the rubble, enough to notice one end is bolted to the ground. The other end dangles down the edge of a cliff.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "The lizard strikes with both heads towards you, giving you a split-second decision!", view=c6view,
        ephemeral=True)

  await c6view.wait()

  if c6view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c6view.choice == 1:
    await C7(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif c6view.choice == 2:
    await C8(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C7(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c7view = OneView("Rappel down the cliff")

  await interaction.followup.send(
        "You swing the chain in a loop, catching both heads as they’re extended. You leap forward, holding the chain tight, cinching it around both necks. The lizard freak claws at you, slicing into your skin. You stomp on its fingers and climb onto its back just before it could strike again. It flicks its tail in an attempt to dislodge you, but to no avail, you’re secure.",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "As you tighten the chain around the two necks, the lizard gasps for air. Exasperated, it sputters out **“You’ve beaten me, so I’ll give you some advice. When you get to the bottom, wait if you want to live”.**",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "“I’ll be sure to do that” you quip. Keeping the chain tight around the lizard and in your hands, you leap off the edge of the rocks and rappel down the cliff.", view=c7view,
        ephemeral=True)

  await c7view.wait()

  if c7view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  await C8(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C8(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c8view = TwoView("Wait here", "Crawl through opening")

  if c8shortcut == True:
    await interaction.followup.send(
        "You climb onto a small ledge and begin bouldering along the rock wall. It’s hot, so you move swiftly but with care so you don’t fall into the crevice below.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "Behind you, you can hear a hissing noise. You sneak a peek. Off in the distance you can make out a large lizard with what seems like 2 heads? Glad you’re not over there, you think. You continue to move.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You’re approaching what seems to be a large barrier near a flowing wall of lava that extends into a cavern. You begin to climb down, making sure to keep your footing. A rock snaps beneath your feet and you lose your footing for just a second, dangling dangerously by your arms. Thank god you skipped leg day all those years, your arms just saved your life.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "You continue your ginger descent. To your left you notice a rusty dull chain extending upward to where you saw the lizard freak. You reach the ground successfully and breathe a sigh of relief just before noticing how dense the air is here. You can see a small opening near where the lava is flowing.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "You see an inscription reading “Cave of Daggers”",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "What should you do now?", view=c8view,
        ephemeral=True)

  else:
    await interaction.followup.send(
        "You grip the chain tightly as you move down one step at a time. You can hear the lizard gnashing its teeth up above. Behind you, a lava flows into the cavern below.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "After several minutes of descent, you reach the bottom. The air is dense here, and you can see a small opening near where the lava is flowing.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You see an inscription reading “Cave of Daggers”",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "What should you do now?", view=c8view,
        ephemeral=True)

  await c8view.wait()

  if c8view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c8view.choice == 1:
    await interaction.followup.send(
        "You take a moment to rest, trying to catch your breath. You breathe in the dense air, filling your lungs with smoke. You cough several times and determine that short breaths are the way to go for now. You rest more.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "Just as you’re ready for action, the two headed lizard crashes down in front of you with a loud shriek. No time to react, you wince and shield your face just before the lizard feasts on your flesh.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif c8view.choice == 2:
    await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  if c9times == 1:
    c9times += 1

    c9view = SevenView("Leave Cave", "Path of Greenery", "Path of Steel", "Narrow Path", "Path of Fire", "Submerged Path", "Path of Darkness")

    await interaction.followup.send(
        "You trek onward, no time for rest. Besides, with air quality this bad, you wouldn’t want to stay here anyway. You wriggle your way through the small opening, feeling the intense heat of the flowing lava tinge your side.",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "When you’re halfway through you hear a loud thud and a shriek behind you. With a burst of strength, you pull your legs through the opening, rolling into the cavern, body intact. Peering back through the hole, you see a toothy snout trying to poke its way in. If you had waited seconds longer, your leg may not have been attached to your body any longer. You let out a sigh of relief and boop the snoot, quickly retreating your precious hand. Worth it.",
        ephemeral=True)
    time.sleep(6)
    await interaction.followup.send(
        "You turn your attention to the Cave of Daggers. Multiple paths extend in front of you. A booming voice echoes from within:",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "“You may only enter this room 4 times. This is your first. There is but one true path.”", view=c9view,
        ephemeral=True)

    await c9view.wait()

    if c9view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c9view.choice == 1:
      await C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 2:
      await C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 3:
      await C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 4:
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 5:
      await C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 6:
      await C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 7:
      await C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif c9times == 5:
    await interaction.followup.send(
        "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "A dense smoke begins to fill the room. A bellowing laugh emanates from the darkness: “Hahaha you fool! I told you not to return after 4 visits. Best of luck next time”",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You feel woozy after breathing the smoke. You pass out.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif unlockedc13 == False:
    c9times += 1

    c9view = SevenView("Leave Cave", "Path of Greenery", "Path of Steel", "Narrow Path", "Path of Fire", "Submerged Path", "Path of Darkness")

    await interaction.followup.send(
        "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?", view = c9view,
        ephemeral=True)

    await c9view.wait()

    if c9view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c9view.choice == 1:
      await C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 2:
      await C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 3:
      await C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 4:
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 5:
      await C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 6:
      await C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 7:
      await C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif unlockedc13 == True and unlockedc17 == False:
    c9times += 1

    c9view = SevenView("Leave Cave", "Path of Greenery", "Path of Steel", "Narrow Path", "Path of Fire", "Submerged Path", "Path of Darkness")

    await interaction.followup.send(
        "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "With a gasp, you suddenly realize something has changed. The path that was previously submerged has been drained of all its murky water!", view = c9view,
        ephemeral=True)

    await c9view.wait()

    if c9view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c9view.choice == 1:
      await C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 2:
      await C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 3:
      await C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 4:
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 5:
      await C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 6:
      await C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 7:
      await C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif unlockedc17 == True and unlockedc18 == True:
    c9view = SevenView("Leave Cave", "Path of Greenery", "Path of Steel", "Narrow Path", "Path of Fire", "Submerged Path", "Path of Darkness")

    await interaction.followup.send(
        "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?", view = c9view,
        ephemeral=True)

    await c9view.wait()

    if c9view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c9view.choice == 1:
      await C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 2:
      await C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 3:
      await C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 4:
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 5:
      await C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 6:
      await C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 7:
      await C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif unlockedc17 == True:
    c9view = SevenView("Leave Cave", "Path of Greenery", "Path of Steel", "Narrow Path", "Path of Fire", "Submerged Path", "Path of Darkness")

    await interaction.followup.send(
        "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You wonder what the Eye of Illusion could reveal. What did that eyeball icon mean on the podium where you got the visor?", view = c9view,
        ephemeral=True)

    await c9view.wait()

    if c9view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c9view.choice == 1:
      await C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 2:
      await C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 3:
      await C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 4:
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 5:
      await C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 6:
      await C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c9view.choice == 7:
      await C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C10(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  await interaction.followup.send(
        "You start down the path. The dense air is replaced by damp humidity as you move further into the cave, moss creeping up the walls.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "Plants have sprouted and give off a low glow. Magic, you think, until you realize it’s bioluminescence!",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "Scrawled on the wall amidst hanging vines you read the inscription: **“Third, swim over the pit.”**",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "You continue onward, pushing humongous leaves out of the way. With each step you grow more concerned, you’ve been walking for more than 20 minutes. Could you get lost? You wonder, but continue to wander.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "You glance behind you. The bioluminescent plants have stopped glowing. A darkness falls over the cave as you turn your attention forward again. A bulbous light appears in the distance. You go to it.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "Just mere feet in front of the bulb, you reach out to touch it.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "Several vines shoot from the darkness, ensnaring your ligaments! The light bulb brightens to reveal to your horror, a massive plant with eyes. It’s alive?! Before you’re even able to ridicule yourself for not realizing that plants are, of course, alive, the vines deposit you into a sticky solution in the plant’s… mouth?",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "The pain is instant. You try to escape, crawling away in pain, but the sticky substance eats away at your armor, eventually reaching your skin. The acidic solution burns through you as the vines pull you closer to your ultimate fate.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

async def C11(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c11view = TwoView("Press big red button", "Press small yellow button")

  await interaction.followup.send(
        "You start down the steel path. It looks oddly man-made. It forms almost a perfect tube, winding about, encasing you in smooth metal.",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "After several minutes of walking, you approach a large room with exposed gears everywhere.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "In front of you is a panoramic window and you can see a long rickety rope bridge extending over a pit of spikes. Past the bridge is a small opening with an eyeball icon above it. It looks like gold shimmering smoke is slowly coming out of the opening. How strange.",
        ephemeral=True)
  time.sleep(5)
  await interaction.followup.send(
        "Right beneath the window you see two buttons. A big red button and a small yellow button.", view=c11view,
        ephemeral=True)
  time.sleep(1)

  await c11view.wait()

  if c11view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  elif c11view.choice == 2:
    await interaction.followup.send(
        "You press the yellow button. A siren sounds and electricity courses through the control panel, frying it. You hear a loud pop behind you as the lights explode, sending shattered glass through the air.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You shield your face. A little glass can’t hurt you.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "A big piece of glass goes right through your arm and into your head. Shocked that your arms couldn’t shield you, you stagger back and fall into the panoramic window with a yelp. This window wasn’t up to safety standards, you realize angrily, as it begins to crack.",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "Before you can say “Whew, that was a close one”, it breaks into thousands of little pieces that fall, along with you, into the large spiked pit below.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Shoulda pressed the red button, you think, seconds before you’re impaled by a stick in the pit.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  elif c11view.choice == 1:
    c11view2 = OneView("Go back")

    await interaction.followup.send(
        "YOLO, you think, seconds before slamming your flabby palm onto the giant red button. You’ve always wanted to do that.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Behind you the gears spring to life, groaning under the lack of use. You hear a gushing noise, like water bursting out of a dam.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "“Wow, that’s exactly what it is” you say out loud, realizing you’re smarter than you look. The gushing continues, becoming faster and louder. Out the window you can see murky water quickly filling up the pit through a steel opening you hadn’t noticed before!",
        ephemeral=True)
    time.sleep(4)
    await interaction.followup.send(
        "The control panel with the buttons crackles with electricity and smoke begins to come out of it. Time to go, you think, as you turn around, just before a loud pop signals the end of the control panel’s brief 15 seconds of fame.", view=c11view2,
        ephemeral=True)

    await c11view2.wait()

    if c11view2.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    unlockedc13 = True
    await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C13(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  if unlockedc13 == False:
    await interaction.followup.send(
        "You head to an opening in the cave. Murky water greets you, the stench sending shivers down your spine. You step into the water. It’s warm. This is a mistake you think, but you commit. You ain’t no bitch.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You take a deep breath and dive headfirst into the water, plunging into darkness.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "You’re feeling around in the water, swimming deeper and deeper into the cave, staying near the ceiling. You reach an area that seems blocked.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You keep swimming",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "Starting to run out of breath, you realize with a gasp that you shouldn’t be gasping, no, that breath needs to be saved!",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You quickly turn around and start clawing at the ceiling, trying to find your way back. This was a terrible idea; you can’t breathe underwater and who knows how long this cave is!",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Moments before you run out of breath, you finally understand why the water was warm in the first place. It’s in a volcano… oh and that’s why it was murky, because of the soot! With your final eureka moment, you let out a final gasp of desperation before swallowing the foulest water known to Illuvar.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  else:
    c13view = OneView("Go back")

    await interaction.followup.send(
        "The pathway ahead is damp and slippery. And stinky, you think, as the stench hits your nostrils. You slide down the path and try to block out the smell, to no avail. It surrounds you. Such is the price of adventure.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You look up, the ceiling is much higher than you originally realized, nearly 15 feet above your head. You see the ceiling dip ahead, creating a small opening at the end of the pathway. You crawl through the pathway, moving some sludgy silt to wriggle through.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "You emerge into a small room now with a golden object sitting atop a podium.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "You approach the podium and pick up my precious. The gold thing looks like a large visor that can snap over your eyes. On the podium you read ***“See past all that glitters with the Eye of Illusion” with an icon of a gold eyeball beneath it.***", view=c13view,
        ephemeral=True)

    await c13view.wait()

    if c13view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    unlockedc17 = True
    await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  if unlockedc13 == False:
    c15view = TwoView("Go back", "Cross bridge")

    await interaction.followup.send(
        "You start down the narrow path. Sidling through the tight rock walls, you curse yourself for not dieting when your girlfriend begged you to. You didn’t need it, you thought. But now you’re stuck between a rock and a hard place. With a thrust you free yourself, only to be greeted once again by the tight walls.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "After what seemed like an eternity but actually was only about a minute, you can see the exit. Satisfied, you reach the opening and breathe a sigh of relief.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Ahead of you is a rickety rope bridge, extending over what looks to be a large pit. You gaze into the pit, seeing large pointy sticks at the bottom. It doesn’t look like there’s no way over the pit except the bridge.",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "On the other side of the bridge is a small opening in the cavern wall. Shimmering gold smoke seems to emanate from within, and an eyeball icon is inscribed above the opening. It’s difficult to see much else due to the distance. On the right side of the room you can see a large glass window near the ceiling, surrounded by metal. Wonder what that could be…", view=c15view,
        ephemeral=True)

    await c15view.wait()

    if c15view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c15view.choice == 2:
      await interaction.followup.send(
        "Let’s go check out that gold smoke, shall we? You gingerly step onto the bridge. It groans under your weight. “Knew I should have dieted” you muse as you take another step.",
        ephemeral=True)
      time.sleep(3)
      await interaction.followup.send(
        "Handholds are scarce, so you begin to crawl across. You try to keep your eyes set on the far side rather than looking down. Those sticks look rough.",
        ephemeral=True)
      time.sleep(2)
      await interaction.followup.send(
        "Near the middle you reach an area where 2 planks are missing. It’ll require you to stretch across, so you extend your body ever so slightly and put your weight onto the far plank.",
        ephemeral=True)
      time.sleep(3)
      await interaction.followup.send(
        "With a snap, the plank cracks and swings down! Thinking quickly, you reach your other hand out to grab the next panel! Thankfully this one is sturdy, but the fast movement puts strain on the rope. You have moments to catch your breath before the whole bridge snaps in two! You grab hold of the panel with all your might as you’re headed straight for the far wall, falling like a pendulum above the pit. With a loud smack, you nail the wall, definitely breaking a finger or two.",
        ephemeral=True)
      time.sleep(7)
      await interaction.followup.send(
        "Grimacing in pain, you begin to climb up the makeshift ladder that was previously a bridge.",
        ephemeral=True)
      time.sleep(1)
      await interaction.followup.send(
        "Miraculously, you reach the top without issue. Who woulda thought?",
        ephemeral=True)
      time.sleep(1)
      await interaction.followup.send(
        "You get a better look at the gold smoke billowing out of the opening. How strange… is that… your girlfriend on the other side?",
        ephemeral=True)
      time.sleep(2)
      await interaction.followup.send(
        "You start to crawl through towards what looks to be her. Delirious and confused, you see her form metamorph into a skeleton that reaches out to you. Is this a metaphor? You black out.",
        ephemeral=True)
      time.sleep(3)
      await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

    elif c15view.choice == 1:
      await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif unlockedc17 == True and c16goback == False:
    c15view = TwoView("Go back", "Swim across")

    await interaction.followup.send(
        "You start down the narrow path. Sidling through the tight rock walls, you curse yourself for not dieting when your girlfriend begged you to. You didn’t need it, you thought. But now you’re stuck between a rock and a hard place. With a thrust you free yourself, only to be greeted once again by the tight walls.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "After what seemed like an eternity but actually was only about a minute, you can see the exit. Satisfied, you reach the opening and breathe a sigh of relief.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Ahead of you is a rickety rope bridge, extending over what looks to be a large body of water, lapping the bottom of the bridge. No point crossing the bridge, might as well swim.", view = c15view,
        ephemeral=True)

    await c15view.wait()

    if c15view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c15view.choice == 1:
      await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c15view.choice == 2:
      await C16(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  elif c16goback == True:
    c15view = TwoView("Go through passage", "Cross water again")

    await interaction.followup.send(
        "You swim back across the murky water as quickly as you can. You reach the other side easily and can see the narrow passage ahead.", view = c15view,
        ephemeral=True)

    await c15view.wait()

    if c15view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c15view.choice == 1:
      await C9(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c15view.choice == 2:
      await C16(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C16(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  if c17goback == False:
    c16view = TwoView("Go back", "Go to gold smoke")

    await interaction.followup.send(
        "You hop into the murky water. Wouldn’t want to dive in, you know what’s down there.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "With one hand on the bridge, you move swiftly across and climb onto the opposite bank.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "Ahead of you is the opening with the gold smoke. Above it is an eyeball icon.", view=c16view,
        ephemeral=True)

    await c16view.wait()

    if c16view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    elif c16view.choice == 1:
      c16goback = True
      await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

    elif c16view.choice == 2:
      if unlockedc17 == False:
        await interaction.followup.send(
        "You crawl towards the opening and get a better look at the gold smoke billowing out of the opening. How strange… is that… your girlfriend on the other side?",
        ephemeral=True)
        time.sleep(3)
        await interaction.followup.send(
        "You start to crawl through towards what looks to be her. Delirious and confused, you see her form metamorph into a skeleton that reaches out to you. Is this a metaphor? You black out.",
        ephemeral=True)
        time.sleep(4)
        await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

      else:
        await C17(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

  else:
    c16view2 = OneView("Swim across")

    await interaction.followup.send(
        "You exit the room with the Twin Daggers podium and see the rope bridge with the water underneath it. Swim across the water?", view=c16view2,
        ephemeral=True)

    await c16view2.wait()

    if c16view2.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    c16goback = True
    await C15(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)

async def C17(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  c17view = OneView("Go back")

  await interaction.followup.send(
        "You recognize the eyeball icon from the pedestal, so you don your gold visor before going forward.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "The gold smoke turns a deep purple color but you can make out a shadowy figure further in the cave!",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "You crawl through the opening, holding your breath to not breathe the smoke. Halfway through, you realize all that glitters isn’t gold, only shooting stars break the mold. This is a metaphor, right?",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "At the exit, you make out the frame of a small impish freak belching out the purple smoke. The imp snaps its gaze toward you and lets out a devilish squeak before leaping out of sight.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "The smoke dissipates quickly and you rise to your feet. Ahead of you is a stone podium with 2 daggers stuck in it.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "***You reach down and triumphantly unearth the Twin Daggers from the stone.***",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "As light shimmers down on your glorious moment, you notice an inscription on the stone **“Slay the lizard.”**",
        ephemeral=True)
  await interaction.followup.send(
        "https://media.discordapp.net/attachments/840365409445609472/912436854261952572/unnamed_1.png", view=c17view,
        ephemeral=True)

  await c17view.wait()

  if c17view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

  unlockedc18 = True
  c17goback = True
  await C16(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client)


async def C12(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  await interaction.followup.send(
        "You start down the path of fire. It’s blazing hot in here. Didn’t you do that enough already in the volcano?! Wait, this still is the volcano, duh.",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "Deeper and deeper you go, lava seeping from the cracks in the walls. This is dangerous, but you’re here for the rune. You won’t stop until you get it! Or until you have some farming to do in FarmVilleDAO.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "Scrawled on the wall you can make out a charcoal inscription: **”Second, go where the water was.”**",
        ephemeral=True)
  time.sleep(1)

  await interaction.followup.send(
        "You make a mental note of that. Wait, was this your first, second, or third time down these paths? You think back to the inscription above the cave entrance “Cave of Daggers”. Is every path booby trapped? Can someone find their way through a faster way?",
        ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
        "Before you have much more time to ponder the rabbit hole of possibilities, you hear a loud bang – one of the walls has blown apart, sending lava bursting into the cave! You try running forward but your feet are no match for liquid death.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

async def C14(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  await interaction.followup.send(
        "The pathway ahead Is pitch black.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "You stumble forward, wondering why you chose this path. But you’re not afraid of the dark, no! You call out ahead of you, trying to use echolocation or something like that. The silence you’re greeted with is deafening.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        "You continue down the winding path and can’t see anything anymore. The twists of the cave hide all.",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "You feel the walls of the cave, gingerly inching forward. You feel what seems to be an arrow! What luck! If it is an arrow anyway…",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "You follow the direction of the arrow with your fingers and reach another! It’s a trail, you think!",
        ephemeral=True)
  time.sleep(1)
  await interaction.followup.send(
        "After about 15 minutes of following these arrows, you bump your head on a post made of a cold material… metal maybe? It’s a bit rugged. You slide your hands up the pole until you reach the top of it. **You can make out the number 1, or what seems like a 1, and the word “Red”.**",
        ephemeral=True)
  time.sleep(4)
  await interaction.followup.send(
        "Curious, you look for more clues. It’s at this moment that you lose your footing and unexpectedly tumble down a deep cavern in the darkness!",
        ephemeral=True)
  time.sleep(2)
  await interaction.followup.send(
        "Moments later you come to a crashing halt and bang your head on a rock. You’re definitely bleeding, you realize. You start to feel woozy. You pass out and bleed in darkness.",
        ephemeral=True)
  time.sleep(3)
  await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

async def C18(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
  if unlockedc18 == False:

    await interaction.followup.send(
        "You crawl out of the Cave of Daggers through the small opening from which you entered.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "The two headed lizard turns to greet you, shocked and delighted by the sight of your presence.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "You try to crawl back but it’s too late, the lizard strikes fast, drooling from the idea of a free lunch.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "Gobble, gobble, you think, just before you’re torn apart by the 2 heads.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        embed=discord.Embed(description="**You lose... Go back to the top of this channel and click `begin challenge` to start again.**", color=0x000ff),
        ephemeral=True)

  else:
    c18view = OneView("FINISH HIM!!!")

    await interaction.followup.send(
        "You crawl out of the Cave of Daggers through the small opening from which you entered.",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(
        "The two headed lizard turns to greet you, shocked and delighted by the sight of your presence. A tasty lunch perhaps!",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "With lightning speed, you unsheathe one of your daggers, causing the lizard to cower back slightly. The second head pulls back, getting ready to strike!",
        ephemeral=True)
    time.sleep(3)
    await interaction.followup.send(
        "With your eyes on the first head, the second head darts forward, but isn’t fast enough – you swing around and plunge the dagger into its neck. The lizard recoils with one head, ripping the dagger from your hand, still stuck deeply in the neck of one head. The other head makes a desperate bid for your waist, seeking revenge.",
        ephemeral=True)
    time.sleep(5)
    await interaction.followup.send(
        "But the lizard is nowhere near fast enough for this Illuvar. You snatch the other blade and, having learned from your first attempt, grip it tightly and slice the head clean off. Blood sprays from the neck into the flowing lava, instantly vaporizing.", view=c18view,
        ephemeral=True)

    await c18view.wait()

    if c18view.timeout == True:
        await interaction.followup.send(
            "Timed out... Don't you know how to click buttons?!",
            ephemeral=True)
        return

    await interaction.followup.send(
        "You leap towards the other head, dagger drawn and ready. You land, stabbing straight down with the dagger, lodging it next to the first dagger. ",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "You grip both, each with one hand and yank in opposite directions, sending the head of the lizard flying while releasing the daggers.",
        ephemeral=True)
    time.sleep(2)
    await interaction.followup.send(
        "Triumphant against your foe, you let out a deep breath. A blinding light erupts from beneath your feet, and after a few moments of stunned glory, a voice calls out: KO!!!",
        ephemeral=True)
    time.sleep(2)

    walletembed = discord.Embed(description="Congratulations on completing the quest! The first 50 people to complete will be added to the free mint whitelist and the next 300 will be whitelisted. You will gain a role for completing this quest and we will manually assign the roles for the winners! Please send your wallet address here! (Make sure to send only your wallet address and no extra random text!)", color=0x000ff)
    walletembed.set_footer(text="Freaks N' Guilds",
                          icon_url=client.user.avatar.url)

    dmmessage = await interaction.user.send(embed=walletembed)

    await interaction.followup.send(
        f"The rune materializes before your eyes as a championship belt. Congratulations! You are a worthy Illuvar!",
        ephemeral=True)
    time.sleep(1)
    await interaction.followup.send(embed=discord.Embed(description=f"Congratulations on completing the quest! The first 50 people to complete will be added to the free mint whitelist and the next 300 will be whitelisted. You will gain a role for completing this quest and we will manually assign the roles for the winners! Please [check your DMs]({dmmessage.jump_url}) and send your wallet address there! (Make sure to send only your wallet address and no extra random text!)", color=0x000ff),
        ephemeral=True)

    walletaddress = (await client.wait_for('message', check=lambda message: message.author == interaction.user and isinstance(message.channel, PrivateChannel))).content

    await interaction.user.send("Got it! I've stored your wallet address.")

    f = open("walletaddresses.txt", "a")
    f.write(f"\n{interaction.user.name}#{interaction.user.discriminator}:{walletaddress},")
    f.close()

    knightsrole = interaction.guild.get_role(902795625253449759)
    await interaction.user.add_roles(knightsrole)

class ChallengeView3(discord.ui.View):
    def __init__(self, client):
        super().__init__(timeout=None)
        self.client = client

    @discord.ui.button(label='Begin Challenge',
                       style=discord.ButtonStyle.blurple,
                       custom_id='persistent_view:challenge3')
    async def challenge(self, button: discord.ui.Button,
                        interaction: discord.Interaction):
        c8shortcut = False
        c9times = 1
        unlockedc18 = False
        unlockedc13 = False
        unlockedc17 = False
        c16goback = False
        c17goback = False

        await interaction.response.defer()

        startembed = discord.Embed(
            description=
            "A grind where mistakes mean death...\n\nHow to play:\n\nRead the paragraph, and then click on one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.To start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!",
            color=0x000ff)
        startembed.set_author(name="Challenge 3",
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

        await C1(interaction, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, self.client)


class Challenge3(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.persistent_views_added = False

    #Commands
    @commands.command(pass_context=True)
    async def challenge3(self, ctx):
        rulesembed = discord.Embed(
            description=f"Click below to begin your challenge.", color=0x000ff)
        rulesembed.set_author(name="Challenge 3", icon_url=ctx.guild.icon.url)
        rulesembed.set_footer(text="Freaks N' Guilds",
                              icon_url=ctx.guild.icon.url)

        challengeview = ChallengeView3(self.client)

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
            self.client.add_view(ChallengeView3(self.client))
            self.persistent_views_added = True


def setup(client):
    client.add_cog(Challenge3(client))
