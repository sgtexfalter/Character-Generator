import random

# Lists of fantasy first names, surnames, and D&D classes
FIRST_NAMES = [
    "Alaric", "Bryn", "Cedric", "Dara", "Elara", "Finnian", "Galen",
    "Halia", "Ilyas", "Jareth", "Kaelin", "Lira", "Mira", "Nim", "Orin",
    "Perrin", "Quill", "Rowan", "Sylas", "Theren", "Uriel", "Vesper", "Willow", "Xander", "Yara", "Zane"
]

SURNAMES = [
    "Amberhide", "Briarwood", "Cinderfell", "Duskbane", "Eaglecrest", "Frostbeard",
    "Glimmerstone", "Hawkridge", "Ironfoot", "Jadewhisper", "Keenblade", "Lightbringer",
    "Moonshadow", "Nightbreeze", "Oakenshield", "Proudmore", "Quickstep", "Ravenwood",
    "Stormrider", "Thornheart", "Umbermoor", "Valewind", "Wildheart", "Yewbranch", "Zephyr"
]

CLASSES = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter",
    "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
]

def generate_character():
    first = random.choice(FIRST_NAMES)
    last = random.choice(SURNAMES)
    char_class = random.choice(CLASSES)
    name = f"{first} {last}"
    return name, char_class

if __name__ == "__main__":
    name, char_class = generate_character()
    print(f"Your D&D character: {name}, the {char_class}")
