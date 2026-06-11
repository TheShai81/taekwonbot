'''
Contains a dictionary with some of the bot commands or relevant variables
Key         : Value
Bot Command : Textual output
'''

from collections import defaultdict

# to read off all the fun facts from a text file
facts = []
with open('fun_facts.txt', 'r', encoding="utf-8") as factsfile:
    for line in factsfile.readlines():
        facts.append(line)

# sniping dictionary
snip_dict = defaultdict(int)

# all commands
bot_commands = {
    'dues': "This is a test command. HELLO!!!!!",
    'duesREAL': """
 ------------------------------
| **$ 30 per Quarter**             |
|       OR                     |
| **$ 75 per Year (Save $15!)**     |
 ------------------------------
Note: Dues are *not* required except for belt testing, but there are many 
benefits included for paying dues! Read Below.

__Why pay dues?__
Dues help with club logistics
""",
    'funfact': facts,
    'sniping_id': 1261144929128812617,  # currently activate-bot for testing
    'pil_sung_id': "<:ps:1065684391587762196>",
    'sniping_count': 0
}