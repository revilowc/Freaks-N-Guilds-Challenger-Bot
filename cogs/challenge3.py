import discord
from discord.abc import PrivateChannel
from discord.ext import commands

class BeginView(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Begin', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    self.c8shortcut = False
    self.c9times = 0
    self.unlockedc18 = False
    self.unlockedc13 = False
    self.unlockedc17 = False
    self.c16goback = False
    self.c17goback = False

    view = C1(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You shield your eyes from the searing heat with your arm. The flames subside but the temperature doesn’t drop. You move your arm and to your surprise, you’re surrounded by red hot lava! You look up to see towering igneous rock cliffs amidst billowing black smoke. Is this… crippling debt? Wait, no, a volcano!?\n\nA booming voice fills the crater “Choose correctly and you’ll find what you seek. Choose incorrectly and feel the fury of fire! Welcome to The Illuvar’s Gauntlet.” How ominous.\n\nYou look forward to see a thin pathway ahead. You take a deep breath and start along it, lava lapping mere feet from your own feet.",
          view=view,
          ephemeral=True)

class StartOver(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Start over', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    self.c8shortcut = False
    self.c9times = 0
    self.unlockedc18 = False
    self.unlockedc13 = False
    self.unlockedc17 = False
    self.c16goback = False
    self.c17goback = False

    view = C1(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You shield your eyes from the searing heat with your arm. The flames subside but the temperature doesn’t drop. You move your arm and to your surprise, you’re surrounded by red hot lava! You look up to see towering igneous rock cliffs amidst billowing black smoke. Is this… crippling debt? Wait, no, a volcano!?\n\nA booming voice fills the crater “Choose correctly and you’ll find what you seek. Choose incorrectly and feel the fury of fire! Welcome to The Illuvar’s Gauntlet.” How ominous.\n\nYou look forward to see a thin pathway ahead. You take a deep breath and start along it, lava lapping mere feet from your own feet.",
          view=view,
          ephemeral=True)

class C1(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Carefully walk', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You cautiously walk forward, step by step, ensuring you don’t fall into the blazing molten rock on either side of you. It looks as if the path is thinning. Or is that just a trick of the light?\n\nNo, no, it’s definitely thinning! Wait no, it’s not the path… it’s the lava! It’s rising and consuming the path! With a shriek you start to pick up the pace just as a large bubble of lava pops, sending molten lava directly in front of you, blocking your path. You hurriedly turn around looking for a way back.\n\nTo your dismay, you don’t even see the path behind you. You had been so concerned with what was in front of you that you didn’t realize you were on an incline. Everything behind you has been consumed by lava. In a frenzy you try to leap over the lava on the path in front of you, but you don’t quite make it. With a bloodcurdling scream you are seared like a well-done steak and die shortly after.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Run across the pathway', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C2(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You break out into a sprint! Several times you nearly slip into the bubbling lava, but you catch yourself. Eyes forward, you can see a small plateau. Triumphant, you reach the plateau!\n\nTo your right you see a small podium.",
          view=view,
          ephemeral=True)

class C2(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Go to the podium', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C2half(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You approach the podium and see a detailed painted image.\n\nhttps://media.discordapp.net/attachments/840365409445609472/912143629773049876/unnamed.png",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Ignore the podium', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C3(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You move past the podium. The lava continues to rise behind you. The heat creates a shimmering in your line of sight, warping your vision slightly. Undeterred, you trek on, leaping from floating island to floating island, with small rivers of lava slowly filling in the crevices between the islands.\n\nTo your left the lava begins to bubble, sending ripples your way.",
          view=view,
          ephemeral=True)

class C2half(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Continue on', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C3(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You move past the podium. The lava continues to rise behind you. The heat creates a shimmering in your line of sight, warping your vision slightly. Undeterred, you trek on, leaping from floating island to floating island, with small rivers of lava slowly filling in the crevices between the islands.\n\nTo your left the lava begins to bubble, sending ripples your way.",
          view=view,
          ephemeral=True)

class C3(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Wait', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "The lava starts to pop, sending flecks of lava your way. You duck just in time, avoiding the deadly molten rock. Your arm, on the other hand, isn’t so lucky. You feel extreme pain as the lava slices off your arm like butter. Incapacitated with pain, you begin to leap from island to island.\n\nYour vision, blurry from the heat, smoke, and your own tears, causes you to overcompensate in a jump. Your right foot touches the red hot lava, instantly searing it off and causing your leg to catch fire.\n\nYou crumple, pain unrelenting, until you realize with a fatal chuckle that this little mistake cost you an arm and a leg. Near where the lava was bubbling a volcanic freak explodes from the depths. You see the rocky form of a mini volcano freak begin to shake and explode, launching a wall of lava in your direction.\n\nYou close your eyes and accept your fate.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Run', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C4(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You pick up the pace, this ain’t no cake walk after all. This is Illuvar’s Gauntlet. You leap easily from island to island as the lava bubbles behind you. A freak bursts from the lava. You glance back and see a mini volcano with blazing eyes start to shake. You don’t wanna see the end of that. Eyes forward, you quickly continue forward.\n\nYou hear a loud explosion, but you don’t turn back. Cool people don’t look at explosions.\n\nIt’s good you didn’t, because a wall of flames lick your behind, lighting a fire under your ass. That could have been a lot worse.\n\nAfter a few more leaps of faith you reach a large area near a cliff wall. In the distance you see a wall of lava flowing down into a deep crevice.",
          view=view,
          ephemeral=True)

class C4(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Scale the cliff wall', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C8(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You climb onto a small ledge and begin bouldering along the rock wall. It’s hot, so you move swiftly but with care so you don’t fall into the crevice below.\n\nBehind you, you can hear a hissing noise. You sneak a peek. Off in the distance you can make out a large lizard with what seems like 2 heads? Glad you’re not over there, you think. You continue to move.\n\nYou’re approaching what seems to be a large barrier near a flowing wall of lava that extends into a cavern. You begin to climb down, making sure to keep your footing. A rock snaps beneath your feet and you lose your footing for just a second, dangling dangerously by your arms. Thank god you skipped leg day all those years, your arms just saved your life.\n\nYou continue your ginger descent. To your left you notice a rusty dull chain extending upward to where you saw the lizard freak. You reach the ground successfully and breathe a sigh of relief just before noticing how dense the air is here. You can see a small opening near where the lava is flowing.\n\nYou see an inscription reading “Cave of Daggers”\n\nWhat should you do now?",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Continue walking forward', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C5(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You continue walking forward. The lava behind you seems to be receding, it seems you’re past the worst of it. “But this is The Illuvar’s Gauntlet” you think with a smirk. It can’t be that easy.\n\nRight on cue a giant lizard with 2 heads leaps from the shadows into your path! One head hisses at you while the other bares it’s serrated teeth, ready to chow down on some juicy human flesh.\n\nYou hurriedly glance around. You notice a rock near your feet and what looks to be a dull shine of metal just behind the lizard freak.",
          view=view,
          ephemeral=True)

class C5(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Investigate the shine', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "Your curiosity is unquenchable. Even in the face of certain danger you truly believe you can get past the lizard to go for this unknown metal object.\n\nYou kick some loose rocks at the lizard’s toothy grin as a distraction, causing it to welp in pain. You take your chance and sprint right at the shiny object. You’re about to snatch it when you feel a sharp pain in your ankle; the other head has found its target. To your dismay, you’re lifted upside down by your ankle and are twisted to see the flipped face of the second head.\n\nIt’s all over, you think, just before the lizard chomps down on its juicy treat.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Pick up the rock', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C6(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You pick up the rock for the barest of protection, ready for a fight. The lizard starts forward and you leap to the side, narrowly evading a sudden chomp from one of the heads. You fight back with a swift kick to the jaw just as the second head swivels to attack. It opens its mouth and you see your chance. You chuck the stone and land it directly in the lizard’s gaping maw.\n\nDefenseless, you remember the dull shiny object. You leap towards it while the lizard is stunned to find a chain. With a quick flick of da wrists, you free the chain from the rubble, enough to notice one end is bolted to the ground. The other end dangles down the edge of a cliff.\n\nThe lizard strikes with both heads towards you, giving you a split-second decision!",
          view=view,
          ephemeral=True)

class C6(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Stay and fight', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C7(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You swing the chain in a loop, catching both heads as they’re extended. You leap forward, holding the chain tight, cinching it around both necks. The lizard freak claws at you, slicing into your skin. You stomp on its fingers and climb onto its back just before it could strike again. It flicks its tail in an attempt to dislodge you, but to no avail, you’re secure.\n\nAs you tighten the chain around the two necks, the lizard gasps for air. Exasperated, it sputters out **“You’ve beaten me, so I’ll give you some advice. When you get to the bottom, wait if you want to live”.**\n\n“I’ll be sure to do that” you quip. Keeping the chain tight around the lizard and in your hands, you leap off the edge of the rocks and rappel down the cliff.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Rappel down the cliff', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C8(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You grip the chain tightly as you move down one step at a time. You can hear the lizard gnashing its teeth up above. Behind you, a lava flows into the cavern below.\n\nAfter several minutes of descent, you reach the bottom. The air is dense here, and you can see a small opening near where the lava is flowing.\n\nYou see an inscription reading “Cave of Daggers”\n\nWhat should you do now?",
          view=view,
          ephemeral=True)

class C7(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Rappel down the cliff', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C8(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You grip the chain tightly as you move down one step at a time. You can hear the lizard gnashing its teeth up above. Behind you, a lava flows into the cavern below.\n\nAfter several minutes of descent, you reach the bottom. The air is dense here, and you can see a small opening near where the lava is flowing.\n\nYou see an inscription reading “Cave of Daggers”\n\nWhat should you do now?",
          view=view,
          ephemeral=True)

class C8(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Wait here', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You take a moment to rest, trying to catch your breath. You breathe in the dense air, filling your lungs with smoke. You cough several times and determine that short breaths are the way to go for now. You rest more.\n\nJust as you’re ready for action, the two headed lizard crashes down in front of you with a loud shriek. No time to react, you wince and shield your face just before the lizard feasts on your flesh.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Crawl through opening', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.c9times += 1
    view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You trek onward, no time for rest. Besides, with air quality this bad, you wouldn’t want to stay here anyway. You wriggle your way through the small opening, feeling the intense heat of the flowing lava tinge your side.\n\nWhen you’re halfway through you hear a loud thud and a shriek behind you. With a burst of strength, you pull your legs through the opening, rolling into the cavern, body intact. Peering back through the hole, you see a toothy snout trying to poke its way in. If you had waited seconds longer, your leg may not have been attached to your body any longer. You let out a sigh of relief and boop the snoot, quickly retreating your precious hand. Worth it.\n\nYou turn your attention to the Cave of Daggers. Multiple paths extend in front of you. A booming voice echoes from within:\n\n“You may only enter this room 4 times. This is your first. There is but one true path.”",
          view=view,
          ephemeral=True)

class C18(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='FINISH HIM!!!', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    await interaction.response.send_message(
        "You leap towards the other head, dagger drawn and ready. You land, stabbing straight down with the dagger, lodging it next to the first dagger.\n\nYou grip both, each with one hand and yank in opposite directions, sending the head of the lizard flying while releasing the daggers.\n\nTriumphant against your foe, you let out a deep breath. A blinding light erupts from beneath your feet, and after a few moments of stunned glory, a voice calls out: KO!!!\n\nThe rune materializes before your eyes as a championship belt. Congratulations! You are a worthy Illuvar!\n\n\nCongratulations on completing the quest! You will gain a the knight role and whitelisted role for completing this quest. Please go to the enlisted chat and send your wallet address there! Please do not spam that chat otherwise.",
        ephemeral=True)

    knightsrole = interaction.guild.get_role(902795625253449759)
    whitelistrole = interaction.guild.get_role(924152616114618378)
    peasantrole = interaction.guild.get_role(902788640571277312)
    enlistedchannel = self.client.get_channel(925268802718027796)

    await enlistedchannel.send(f"{interaction.user.mention} Congratulations on completing quest 3! Please send your wallet address here and I will store it for you.")
    await interaction.user.remove_roles(peasantrole, reason="Member completed quest 3")
    await interaction.user.add_roles(knightsrole, whitelistrole, reason="Member completed quest 3")

class C11(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Press small yellow button', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You press the yellow button. A siren sounds and electricity courses through the control panel, frying it. You hear a loud pop behind you as the lights explode, sending shattered glass through the air.\n\nYou shield your face. A little glass can’t hurt you.\n\nA big piece of glass goes right through your arm and into your head. Shocked that your arms couldn’t shield you, you stagger back and fall into the panoramic window with a yelp. This window wasn’t up to safety standards, you realize angrily, as it begins to crack.\n\nBefore you can say “Whew, that was a close one”, it breaks into thousands of little pieces that fall, along with you, into the large spiked pit below.\n\nShoulda pressed the red button, you think, seconds before you’re impaled by a stick in the pit.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Press big red button', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    self.unlockedc13 = True
    view = C9GoBack(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "YOLO, you think, seconds before slamming your flabby palm onto the giant red button. You’ve always wanted to do that.\n\nBehind you the gears spring to life, groaning under the lack of use. You hear a gushing noise, like water bursting out of a dam.\n\n“Wow, that’s exactly what it is” you say out loud, realizing you’re smarter than you look. The gushing continues, becoming faster and louder. Out the window you can see murky water quickly filling up the pit through a steel opening you hadn’t noticed before!\n\nThe control panel with the buttons crackles with electricity and smoke begins to come out of it. Time to go, you think, as you turn around, just before a loud pop signals the end of the control panel’s brief 15 seconds of fame.",
          view=view,
          ephemeral=True)

class C15not13(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Cross bridge', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "Let’s go check out that gold smoke, shall we? You gingerly step onto the bridge. It groans under your weight. “Knew I should have dieted” you muse as you take another step.\n\nHandholds are scarce, so you begin to crawl across. You try to keep your eyes set on the far side rather than looking down. Those sticks look rough.\n\nNear the middle you reach an area where 2 planks are missing. It’ll require you to stretch across, so you extend your body ever so slightly and put your weight onto the far plank.\n\nWith a snap, the plank cracks and swings down! Thinking quickly, you reach your other hand out to grab the next panel! Thankfully this one is sturdy, but the fast movement puts strain on the rope. You have moments to catch your breath before the whole bridge snaps in two! You grab hold of the panel with all your might as you’re headed straight for the far wall, falling like a pendulum above the pit. With a loud smack, you nail the wall, definitely breaking a finger or two.\n\nGrimacing in pain, you begin to climb up the makeshift ladder that was previously a bridge.\n\nMiraculously, you reach the top without issue. Who woulda thought?\n\nYou get a better look at the gold smoke billowing out of the opening. How strange… is that… your girlfriend on the other side?\n\nYou start to crawl through towards what looks to be her. Delirious and confused, you see her form metamorph into a skeleton that reaches out to you. Is this a metaphor? You black out.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.c9times += 1

    if self.c9times > 4:
        view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nA dense smoke begins to fill the room. A bellowing laugh emanates from the darkness: “Hahaha you fool! I told you not to return after 4 visits. Best of luck next time”\n\nYou feel woozy after breathing the smoke. You pass out.\n\n\n**You lose... Start over?**",
              view=view,
              ephemeral=True)

    elif not self.unlockedc13:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc13 and not self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nWith a gasp, you suddenly realize something has changed. The path that was previously submerged has been drained of all its murky water!",
              view=view,
              ephemeral=True)

    elif self.unlockedc17 and self.unlockedc18:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nYou wonder what the Eye of Illusion could reveal. What did that eyeball icon mean on the podium where you got the visor?",
              view=view,
              ephemeral=True)

class C15(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Swim across', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C16(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You hop into the murky water. Wouldn’t want to dive in, you know what’s down there.\n\nWith one hand on the bridge, you move swiftly across and climb onto the opposite bank.\n\nAhead of you is the opening with the gold smoke. Above it is an eyeball icon.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.c9times += 1

    if self.c9times > 4:
        view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nA dense smoke begins to fill the room. A bellowing laugh emanates from the darkness: “Hahaha you fool! I told you not to return after 4 visits. Best of luck next time”\n\nYou feel woozy after breathing the smoke. You pass out.\n\n\n**You lose... Start over?**",
              view=view,
              ephemeral=True)

    elif not self.unlockedc13:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc13 and not self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nWith a gasp, you suddenly realize something has changed. The path that was previously submerged has been drained of all its murky water!",
              view=view,
              ephemeral=True)

    elif self.unlockedc17 and self.unlockedc18:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nYou wonder what the Eye of Illusion could reveal. What did that eyeball icon mean on the podium where you got the visor?",
              view=view,
              ephemeral=True)

class C16(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Go to gold smoke', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if not self.unlockedc17:
      view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You crawl towards the opening and get a better look at the gold smoke billowing out of the opening. How strange… is that… your girlfriend on the other side?\n\nYou start to crawl through towards what looks to be her. Delirious and confused, you see her form metamorph into a skeleton that reaches out to you. Is this a metaphor? You black out.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

    else:
      view = C17(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You recognize the eyeball icon from the pedestal, so you don your gold visor before going forward.\n\nThe gold smoke turns a deep purple color but you can make out a shadowy figure further in the cave!\n\nYou crawl through the opening, holding your breath to not breathe the smoke. Halfway through, you realize all that glitters isn’t gold, only shooting stars break the mold. This is a metaphor, right?\n\nAt the exit, you make out the frame of a small impish freak belching out the purple smoke. The imp snaps its gaze toward you and lets out a devilish squeak before leaping out of sight.\n\nThe smoke dissipates quickly and you rise to your feet. Ahead of you is a stone podium with 2 daggers stuck in it.\n\n***You reach down and triumphantly unearth the Twin Daggers from the stone.***\n\nAs light shimmers down on your glorious moment, you notice an inscription on the stone **“Slay the lizard.”**\n\nhttps://media.discordapp.net/attachments/840365409445609472/912436854261952572/unnamed_1.png",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    view = C15Again(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You swim back across the murky water as quickly as you can. You reach the other side easily and can see the narrow passage ahead.",
          view=view,
          ephemeral=True)

class C17(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    self.unlockedc18 = True
    view = C16Again(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You exit the room with the Twin Daggers podium and see the rope bridge with the water underneath it. Swim across the water?",
          view=view,
          ephemeral=True)

class C16Again(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Swim across', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C15Again(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You swim back across the murky water as quickly as you can. You reach the other side easily and can see the narrow passage ahead.",
          view=view,
          ephemeral=True)

class C15Again(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Go through passage', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.c9times += 1

    if self.c9times > 4:
        view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nA dense smoke begins to fill the room. A bellowing laugh emanates from the darkness: “Hahaha you fool! I told you not to return after 4 visits. Best of luck next time”\n\nYou feel woozy after breathing the smoke. You pass out.\n\n\n**You lose... Start over?**",
              view=view,
              ephemeral=True)

    elif not self.unlockedc13:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc13 and not self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nWith a gasp, you suddenly realize something has changed. The path that was previously submerged has been drained of all its murky water!",
              view=view,
              ephemeral=True)

    elif self.unlockedc17 and self.unlockedc18:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nYou wonder what the Eye of Illusion could reveal. What did that eyeball icon mean on the podium where you got the visor?",
              view=view,
              ephemeral=True)

  @discord.ui.button(label='Cross water again', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C16(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You hop into the murky water. Wouldn’t want to dive in, you know what’s down there.\n\nWith one hand on the bridge, you move swiftly across and climb onto the opposite bank.\n\nAhead of you is the opening with the gold smoke. Above it is an eyeball icon.",
          view=view,
          ephemeral=True)

class C9GoBack(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Go back', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    self.c9times += 1

    if self.c9times > 4:
        view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nA dense smoke begins to fill the room. A bellowing laugh emanates from the darkness: “Hahaha you fool! I told you not to return after 4 visits. Best of luck next time”\n\nYou feel woozy after breathing the smoke. You pass out.\n\n\n**You lose... Start over?**",
              view=view,
              ephemeral=True)

    elif not self.unlockedc13:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc13 and not self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nWith a gasp, you suddenly realize something has changed. The path that was previously submerged has been drained of all its murky water!",
              view=view,
              ephemeral=True)

    elif self.unlockedc17 and self.unlockedc18:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?",
              view=view,
              ephemeral=True)

    elif self.unlockedc17:
        view = C9(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

        await interaction.response.send_message(
              "You’re once again in the main room. How many times was this again? Once when you came in, then you’ve got 3 more, which one is this?\n\nYou wonder what the Eye of Illusion could reveal. What did that eyeball icon mean on the podium where you got the visor?",
              view=view,
              ephemeral=True)

class C9(discord.ui.View):
  def __init__(self, c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, client):
    super().__init__(timeout=None)
    self.c8shortcut = c8shortcut
    self.c9times = c9times
    self.unlockedc18 = unlockedc18
    self.unlockedc13 = unlockedc13
    self.unlockedc17 = unlockedc17
    self.c16goback = c16goback
    self.c17goback = c17goback
    self.client = client

  @discord.ui.button(label='Leave Cave', style=discord.ButtonStyle.blurple)
  async def button1(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()
    if not self.unlockedc18:
      view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You crawl out of the Cave of Daggers through the small opening from which you entered.\n\nThe two headed lizard turns to greet you, shocked and delighted by the sight of your presence.\n\nYou try to crawl back but it’s too late, the lizard strikes fast, drooling from the idea of a free lunch.\n\nGobble, gobble, you think, just before you’re torn apart by the 2 heads.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)
    else:
      view = C18(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You crawl out of the Cave of Daggers through the small opening from which you entered.\n\nThe two headed lizard turns to greet you, shocked and delighted by the sight of your presence. A tasty lunch perhaps!\n\nWith lightning speed, you unsheathe one of your daggers, causing the lizard to cower back slightly. The second head pulls back, getting ready to strike!\n\nWith your eyes on the first head, the second head darts forward, but isn’t fast enough – you swing around and plunge the dagger into its neck. The lizard recoils with one head, ripping the dagger from your hand, still stuck deeply in the neck of one head. The other head makes a desperate bid for your waist, seeking revenge.\n\nBut the lizard is nowhere near fast enough for this Illuvar. You snatch the other blade and, having learned from your first attempt, grip it tightly and slice the head clean off. Blood sprays from the neck into the flowing lava, instantly vaporizing.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Path of Greenery', style=discord.ButtonStyle.blurple)
  async def button2(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You start down the path. The dense air is replaced by damp humidity as you move further into the cave, moss creeping up the walls.\n\nPlants have sprouted and give off a low glow. Magic, you think, until you realize it’s bioluminescence!\n\nScrawled on the wall amidst hanging vines you read the inscription: **“Third, swim over the pit.”**\n\nYou continue onward, pushing humongous leaves out of the way. With each step you grow more concerned, you’ve been walking for more than 20 minutes. Could you get lost? You wonder, but continue to wander.\n\nYou glance behind you. The bioluminescent plants have stopped glowing. A darkness falls over the cave as you turn your attention forward again. A bulbous light appears in the distance. You go to it.\n\nJust mere feet in front of the bulb, you reach out to touch it.\n\nSeveral vines shoot from the darkness, ensnaring your ligaments! The light bulb brightens to reveal to your horror, a massive plant with eyes. It’s alive?! Before you’re even able to ridicule yourself for not realizing that plants are, of course, alive, the vines deposit you into a sticky solution in the plant’s… mouth?\n\nThe pain is instant. You try to escape, crawling away in pain, but the sticky substance eats away at your armor, eventually reaching your skin. The acidic solution burns through you as the vines pull you closer to your ultimate fate.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Path of Darkness', style=discord.ButtonStyle.blurple)
  async def button3(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "The pathway ahead Is pitch black.\n\nYou stumble forward, wondering why you chose this path. But you’re not afraid of the dark, no! You call out ahead of you, trying to use echolocation or something like that. The silence you’re greeted with is deafening.\n\nYou continue down the winding path and can’t see anything anymore. The twists of the cave hide all.\n\nYou feel the walls of the cave, gingerly inching forward. You feel what seems to be an arrow! What luck! If it is an arrow anyway…\n\nYou follow the direction of the arrow with your fingers and reach another! It’s a trail, you think!\n\nAfter about 15 minutes of following these arrows, you bump your head on a post made of a cold material… metal maybe? It’s a bit rugged. You slide your hands up the pole until you reach the top of it. **You can make out the number 1, or what seems like a 1, and the word “Red”.**\n\nCurious, you look for more clues. It’s at this moment that you lose your footing and unexpectedly tumble down a deep cavern in the darkness!\n\nMoments later you come to a crashing halt and bang your head on a rock. You’re definitely bleeding, you realize. You start to feel woozy. You pass out and bleed in darkness.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Path of Fire', style=discord.ButtonStyle.blurple)
  async def button4(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You start down the path of fire. It’s blazing hot in here. Didn’t you do that enough already in the volcano?! Wait, this still is the volcano, duh.\n\nDeeper and deeper you go, lava seeping from the cracks in the walls. This is dangerous, but you’re here for the rune. You won’t stop until you get it! Or until you have some farming to do in FarmVilleDAO.\n\nScrawled on the wall you can make out a charcoal inscription: **”Second, go where the water was.”**\n\nYou make a mental note of that. Wait, was this your first, second, or third time down these paths? You think back to the inscription above the cave entrance “Cave of Daggers”. Is every path booby trapped? Can someone find their way through a faster way?\n\nBefore you have much more time to ponder the rabbit hole of possibilities, you hear a loud bang – one of the walls has blown apart, sending lava bursting into the cave! You try running forward but your feet are no match for liquid death.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Path of Steel', style=discord.ButtonStyle.blurple)
  async def button5(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    view = C11(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

    await interaction.response.send_message(
          "You start down the steel path. It looks oddly man-made. It forms almost a perfect tube, winding about, encasing you in smooth metal.\n\nAfter several minutes of walking, you approach a large room with exposed gears everywhere.\n\nIn front of you is a panoramic window and you can see a long rickety rope bridge extending over a pit of spikes. Past the bridge is a small opening with an eyeball icon above it. It looks like gold shimmering smoke is slowly coming out of the opening. How strange.\n\nRight beneath the window you see two buttons. A big red button and a small yellow button.",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Submerged Path', style=discord.ButtonStyle.blurple)
  async def button6(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if not self.unlockedc13:
      view = StartOver(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You head to an opening in the cave. Murky water greets you, the stench sending shivers down your spine. You step into the water. It’s warm. This is a mistake you think, but you commit. You ain’t no bitch.\n\nYou take a deep breath and dive headfirst into the water, plunging into darkness.\n\nYou’re feeling around in the water, swimming deeper and deeper into the cave, staying near the ceiling. You reach an area that seems blocked.\n\nYou keep swimming\n\nStarting to run out of breath, you realize with a gasp that you shouldn’t be gasping, no, that breath needs to be saved!\n\nYou quickly turn around and start clawing at the ceiling, trying to find your way back. This was a terrible idea; you can’t breathe underwater and who knows how long this cave is!\n\nMoments before you run out of breath, you finally understand why the water was warm in the first place. It’s in a volcano… oh and that’s why it was murky, because of the soot! With your final eureka moment, you let out a final gasp of desperation before swallowing the foulest water known to Illuvar.\n\n\n**You lose... Start over?**",
          view=view,
          ephemeral=True)
    else:
      self.unlockedc17 = True
      view = C9GoBack(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "The pathway ahead is damp and slippery. And stinky, you think, as the stench hits your nostrils. You slide down the path and try to block out the smell, to no avail. It surrounds you. Such is the price of adventure.\n\nYou look up, the ceiling is much higher than you originally realized, nearly 15 feet above your head. You see the ceiling dip ahead, creating a small opening at the end of the pathway. You crawl through the pathway, moving some sludgy silt to wriggle through.\n\nYou emerge into a small room now with a golden object sitting atop a podium.\n\nYou approach the podium and pick up my precious. The gold thing looks like a large visor that can snap over your eyes. On the podium you read ***“See past all that glitters with the Eye of Illusion” with an icon of a gold eyeball beneath it.***",
          view=view,
          ephemeral=True)

  @discord.ui.button(label='Narrow Path', style=discord.ButtonStyle.blurple)
  async def button7(self, button: discord.ui.Button, interaction: discord.Interaction):
    self.stop()

    if not self.unlockedc13:
      view = C15not13(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You start down the narrow path. Sidling through the tight rock walls, you curse yourself for not dieting when your girlfriend begged you to. You didn’t need it, you thought. But now you’re stuck between a rock and a hard place. With a thrust you free yourself, only to be greeted once again by the tight walls.\n\nAfter what seemed like an eternity but actually was only about a minute, you can see the exit. Satisfied, you reach the opening and breathe a sigh of relief.\n\nAhead of you is a rickety rope bridge, extending over what looks to be a large pit. You gaze into the pit, seeing large pointy sticks at the bottom. It doesn’t look like there’s no way over the pit except the bridge.\n\nOn the other side of the bridge is a small opening in the cavern wall. Shimmering gold smoke seems to emanate from within, and an eyeball icon is inscribed above the opening. It’s difficult to see much else due to the distance. On the right side of the room you can see a large glass window near the ceiling, surrounded by metal. Wonder what that could be…",
          view=view,
          ephemeral=True)

    else:
      view = C15(self.c8shortcut, self.c9times, self.unlockedc18, self.unlockedc13, self.unlockedc17, self.c16goback, self.c17goback, self.client)

      await interaction.response.send_message(
          "You start down the narrow path. Sidling through the tight rock walls, you curse yourself for not dieting when your girlfriend begged you to. You didn’t need it, you thought. But now you’re stuck between a rock and a hard place. With a thrust you free yourself, only to be greeted once again by the tight walls.\n\nAfter what seemed like an eternity but actually was only about a minute, you can see the exit. Satisfied, you reach the opening and breathe a sigh of relief.\n\nAhead of you is a rickety rope bridge, extending over what looks to be a large body of water, lapping the bottom of the bridge. No point crossing the bridge, might as well swim.",
          view=view,
          ephemeral=True)

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
        c9times = 0
        unlockedc18 = False
        unlockedc13 = False
        unlockedc17 = False
        c16goback = False
        c17goback = False

        startembed = discord.Embed(
            description=
            "A grind where mistakes mean death...\n\nThese quests are a journey to whitelist. Everyone who properly completes the quest while it is open will recieve a whitelist.\n\nHow to play:\nRead the paragraph, and then click one of the prompted responses to move on.\nYou will have some obvious options available to you, so you will not have to guess or grasp at straws.\n\nIf you ever want to return to the place you just previously were, just click ‘go back’. You will always have the option ‘go back’ available to you.\n\nTo start, click the begin button. Look for hints, read carefully, and...\nGOOD LUCK!",
            color=0x000ff)
        startembed.set_author(name="Challenge 3",
                              icon_url=interaction.guild.icon.url)
        startembed.set_footer(text="Freaks N' Guilds",
                              icon_url=interaction.guild.icon.url)

        view = BeginView(c8shortcut, c9times, unlockedc18, unlockedc13, unlockedc17, c16goback, c17goback, self.client)

        await interaction.response.send_message(embed=startembed,
                                        view=view,
                                        ephemeral=True)

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
            self.client.add_view(ChallengeView3(self.client))
            self.persistent_views_added = True

def setup(client):
    client.add_cog(Challenge3(client))
