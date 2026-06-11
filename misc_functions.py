'''Miscellaneous functions that the bot uses to perform some commands'''

import discord

from random import sample
from datetime import datetime, timedelta

def generate_warmup(exer: int) -> str:
    '''
    Credits to Ronik Bhaskar for the code!
    Creates a random taekwondo warmup containing 'exer' exercises.
    Returns a string containing each exercise on a new line.
    There should be at least 216 different warmups that can be generated.
    No exercise can be used more than once in a warmup.
    
    ## Parameters:
        exer: int
        The number of exercises to be completed in the warmup. This must be a positive number.
    
    ## Returns:
        str
        The warmup of 'exer' random exercises neatly formatted in 'exer' new lines.
    '''

    if exer == 1:
        return "You can do more than just one warmup exercise. Try again. PIL SUNG!"
    elif exer <= 2:
        return f"You can do more than just {exer} warmup exercises. Try again. PIL SUNG!"
    
    exercises = [
        "Tuck Jumps",
        "High Knees",
        "Butt Kicks",
        "Side Shuffle",
        "Grape Vines",
        "Duck Walk",
        "Bunny Hops",
        "Mario Jumps",
        "Spiderman Push-Ups",
        "Side-to-Side Lunges",
        "Lunge Twists",
        "Squat Jumps",
        "Elephant Walks (Scoops)",
        "Open the gate, Close the gate",
        "Cross-Body Monster Walks",
        "Same Side Monster Walks",
        "Roundhouse Kick Chambers",
        "Push-Ups",
        "Diamond Push-Ups",
        "Sit Ups (feet on the ground)",
        "Sit Ups (feet off the ground)",
        "Toe Reaches/Lemon Squeezes (Lying on back, legs pointing straight up, reach up)"
        "Ladder: In-In-Out-Out",
        "Ladder: 1-2-1-2",
        "Ladder: Forward-Back in a Sparring Stance",
        "Ladder: Side-to-Side Crossover Steps, Twisting your Hips",
        "Crab Walks",
        "Up-and-Down Plank (Plank position, Hands -> Elbows -> Hands -> Elbows)",
        "360 Jumps",
        "Lying Leg Raises (on your side)",
        "Lying Leg Raises (on your back)",
        "Russian Twists",
        "Wheelbarrow",
        "Suicides/Wind Sprints",
        "Skipping (for height)",
        "Hop on 1 Leg",
        "Army Crawl",
        "Knee-Up Rhythm Hops (typically up-up-side-side)",
        "Pil Sung Tag (or any variation of tag)",
        "Quick Feet! (some variation of an inplace footwork drill)"
    ]

    sampled_exercises = sample(exercises, exer)

    return "\n".join((f"{i+1}. {e}" for i, e in enumerate(sampled_exercises)))


def prune_counts(counts_dict, days=30):
    '''Takes a dictionary-like object whose keys are dates and deletes any
    key-value pairs whose date is more than `days` days in the past.

    ## Args:
    counts_dict (dict, collections.defaultdict): the dictionary whose keys are dates
    days (int): The number of days in the past that we set the cutoff for pruning. Defaults to 30.
    '''
    cutoff = datetime.now().date() - timedelta(days=days)
    for date_key in list(counts_dict.keys()):
        if date_key < cutoff:
            del counts_dict[date_key]

def has_image(msg: discord.Message):
    '''Checks to see if a message has an image in it.
    
    Args:

    msg (discord.Message): the message to check for attachments
    '''
    for attachment in msg.attachments:
        if attachment.content_type and attachment.content_type.startswith("image/"):
            return True
    for embed in msg.embeds:
        if embed.type == "image" or embed.thumbnail:
            return True
    return False

