import discord
from discord.ui import View
import os
from keep_alive import keep_alive
import tracery

line = '\n'

scenarioNodes = [
  "You've woken up on a deserted island with a half empty Hydro Flask® with liquid and two Nature Valley Granola Bars (the crumbly kind). In your pockets is a lighter, a single soggy cigarette, and a wrinkled up raffle ticket.  You're feeling ok, a little thirsty and not too hungry. What would you like to do?",
  "As you eat the granola bars, a nearby bear smells it and starts to run after you. What would you like to do?",
  "That was not water from the Hydro Flask® my friend. Your nose seems to have received some trauma from falling off the boat yesterday and you couldn't smell the liquid. It was pure vodka. You are now very drunk and dehydrated. What would you like to do?",
  "You grab your things and walk along the shoreline looking for other survivors. You start to remember bits of what happened last night, a faint memory of pocketing the raffle ticket, another memory of dumping out water into the ocean from your Hydro Flask® and filling it up with vodka. You must have been on a boat party of some sort.",
  "The bear was a grizzly bear and seeing you run angered it. The bear catches up to you easily and eats you",
  "As you scramble to finish the crumbly bits of the granola, the bear eats you.",
  "As yuo eatt teh grranloa bers, a neearbey beaar smels ti nd starrrs to runn fter yu. Wht wuld yu likke ta do?",
  "You start to sober up and begin exploring the island. You grab your things and walk along the shoreline looking for other survivors. You start to remember bits of what happened last night, a faint memory of pocketing the raffle ticket, another memory of dumping out water from your Hydro Flask® into the ocean and filling it up with some vodka. You must have been on a boat party of some sort.",
  "Well it doesn't really matter if it was a boat party or not. You're still stuck on this island. You save the vodka for later. You're starting to get a bit hungry. What would you like to do?",
  "You are drunk, your running is closer to a mild stagger in a spiral formation. The bear catches up to you easily and eats you",
  "The drunchies were strong with you as stuff the granola bars in your mouth. The bear walks up to you and eats you",
  "You save the granola for later. You come across the edge of some woodlands and spot a fuzzy grizzly bear in the distance. Good thing you didn't eat yet or it would've came right at you. You back up and head the opposite direction of the island where the bear wouldn't smell you. On the way you spot a small stream and some mysterious berries. You're still hungry though, what would you like to do?",
  "Someone didn't pay attention in  berry picking class. The mysterious berry was poison!! That is too bad. :( You immediately fall over and die of poison.",
  "You find a stick and sharpen the end with a rock. Somehow you are successful in fishing. What do you do next?",
  "There was some salmonella in the fish that cooking would've avoided. Freshwater fish cannot be sashimi. You feel pretty good for a few hours but after 6-8 hours your stomach starts to feel really really weird. Eventually you die of dysentery.",
  "You gather some tinder and burnables and soak a bit with your vodka which catches on fire easily. The use the rest of the vodka to clean the fish. You cover the fish in the granola like a weird katsu and have a tasty meal. You fill the empty Hydro Flask® with stream water and boil it to rehydrate yourself. It's getting pretty late now, what would you like to do?",
  "Turns out, this island has freak weather and freezes to negative temps at night. You freeze and die peacefully in your sleep.",
  "In your sleep, a boat spots the smoke in the distance and heads towards your island. You are shaken awake by the search party that was called when you tripped and fell off a boat. Turns out you won a raffle for a new iPad and were so drunkenly excited that you tripped over yourself and fell into the ocean during your company's work party. When you eventually return to work a few weeks later the company (partially worried about lawsuits) gives you a raise, a new Hydro Flask® and asks you not drink so much at the next company outing.",
  "What would you like to consume?"
]
actionNodes = [
  "Eat the granola bars", "Drink from the Hydro Flask®", "Explore the island",
  "Drop the granola bars and run", "Finish the granola bars",
  "Eatt teh granolla bers", "Go fer a niice strol round the beeach",
  "Yes, that was a boat party", "No, that was not a boat party",
  "Dropp grranloa nd run", "Finsh grranola bers", "Eat the granola",
  "Look for food", "Pick some mysterious berries", "Try to fish",
  "Eat it raw, fresh sashimi is great!", "Try to start a fire",
  "Put out the fire. There might be someone (or something) strange that kills you in your sleep so its best not to be spotted",
  "Keep the fire going, it's getting pretty chilly",
  "Maybe have something to eat or drink?"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


class Node():

  def __init__(self, scenario):
    self.act1 = None
    self.act2 = None
    self.scenario = scenario


# 0
root = Node(scenarioNodes[0] + line + line + "Action 1: " + actionNodes[19] +
            line + "Action 2: " + actionNodes[2])
# 18
root.act1 = Node(scenarioNodes[18] + line + line + "Action 1: " +
                 actionNodes[0] + line + "Action 2: " + actionNodes[1])
# 3
root.act2 = Node(scenarioNodes[3] + line + line + "Action 1: " +
                 actionNodes[7] + line + "Action 2: " + actionNodes[8])
# 1
root.act1.act1 = Node(scenarioNodes[1] + line + line + "Action 1: " +
                      actionNodes[3] + line + "Action 2: " + actionNodes[4])
# 2
root.act1.act2 = Node(scenarioNodes[2] + line + line + "Action 1: " +
                      actionNodes[5] + line + "Action 2: " + actionNodes[6])
# 8
root.act2.act1 = Node(scenarioNodes[8] + line + line + "Action 1: " +
                      actionNodes[11] + line + "Action 2: " + actionNodes[12])
root.act2.act2 = Node(scenarioNodes[8] + line + line + "Action 1: " +
                      actionNodes[11] + line + "Action 2: " + actionNodes[12])
# 6
root.act1.act2.act1 = Node(scenarioNodes[6] + line + line + "Action 1: " +
                           actionNodes[9] + line + "Action 2: " +
                           actionNodes[10])
# 7
root.act1.act2.act2 = Node(scenarioNodes[7] + line + line + "Action 1: " +
                           actionNodes[7] + line + "Action 2: " +
                           actionNodes[8])
root.act1.act2.act2.act1 = root.act2.act1
root.act1.act2.act2.act2 = root.act2.act1
# 4
root.act1.act1.act1 = Node(scenarioNodes[4])
# 5
root.act1.act1.act2 = Node(scenarioNodes[5])
# 9
root.act1.act2.act1.act1 = Node(scenarioNodes[9])
# 10
root.act1.act2.act1.act2 = Node(scenarioNodes[10])
# 11
root.act2.act1.act1 = root.act1.act1
root.act2.act2.act1 = root.act1.act1
root.act2.act1.act2 = Node(scenarioNodes[11] + line + line + "Action 1: " +
                           actionNodes[14] + line + "Action 2: " +
                           actionNodes[13])
root.act2.act2.act2 = root.act2.act1.act2
# 13
root.act2.act1.act2.act1 = Node(scenarioNodes[13] + line + line +
                                "Action 1: " + actionNodes[16] + line +
                                "Action 2: " + actionNodes[15])
# 12
root.act2.act1.act2.act2 = Node(scenarioNodes[12])
# 15
root.act2.act1.act2.act1.act1 = Node(scenarioNodes[15] + line + line +
                                     "Action 1: " + actionNodes[17] + line +
                                     "Action 2: " + actionNodes[18])
# 14
root.act2.act1.act2.act1.act2 = Node(scenarioNodes[14])
# 16
root.act2.act1.act2.act1.act1.act1 = Node(scenarioNodes[16])
# 17
root.act2.act1.act2.act1.act1.act2 = Node(scenarioNodes[17] + line + line +
                                          "Action 1: " + actionNodes[19] +
                                          line + "Action 2: " + actionNodes[0])


class ActionView(View):

  def __init__(self, act1, act2):
    super().__init__()
    self.act1Node = act1
    self.act2Node = act2

  buttonPressed = False

  @discord.ui.button(label='Action 1', style=discord.ButtonStyle.primary)
  async def act1_callback(self, interaction, button):
    print(*self.children, sep=",")
    # for btn in self.children:
    #   btn.disabled = True
    # await interaction.edit_original_message(view=self)
    await askQuestion(self.act1Node, interaction.response)

  @discord.ui.button(label="Action 2", style=discord.ButtonStyle.primary)
  async def act2_callback(self, interaction, button):
    # for btn in self.children:
    #   btn.disabled = True
    await askQuestion(self.act2Node, interaction.response)


class CorrectOrNot(View):

  @discord.ui.button(label="This was a Good Ending",
                     style=discord.ButtonStyle.green)
  async def act1_callback(self, interaction, button):
    await interaction.response.send_message('Glad you enjoyed')

  @discord.ui.button(label="This was a Bad Ending",
                     style=discord.ButtonStyle.green)
  async def act2_callback(self, interaction, button):
    await interaction.response.send_message(
      'Ah sorry about that. `@StoryBot story` to play again')


async def askQuestion(node, ctx):
  if (node.act1 or node.act2):
    view = ActionView(node.act1, node.act2)
    await ctx.send_message(node.scenario, view=view)
  else:
    view = CorrectOrNot()
    await ctx.send_message(node.scenario, view=view)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if client.user in message.mentions and 'story' in message.content.lower():
    view = ActionView(root.act1, root.act2)
    await message.channel.send(root.scenario, view=view)

  if client.user in message.mentions and 'help' in message.content.lower():
    await message.channel.send("help")


token = "insertTokenHere"
client.run(token)
