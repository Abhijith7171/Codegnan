import random

story_starters = [
    "Once upon a time",
    "In a land far away",
    "Long ago",
    "In the beginning",
    "It all started when",
    "One day",
    "At the crack of dawn",
    "In a quiet town",
    "In the heart of the city",
    "Amidst the chaos",
    "Underneath the starry sky",
    "In a small village",
    "In the dead of night",
    "In a distant galaxy",
    "In a magical forest",
    "In a world where",
    "From the moment",
    "As the clock struck midnight",
    "Deep in the mountains"
]

n=input("share your story randomly the beggining of the story is generated ")

c=random.choice(story_starters)

print(c+" "+n)