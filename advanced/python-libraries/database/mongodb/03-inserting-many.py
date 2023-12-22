from config.main import client

# Creating a new database
forest = client.forest

# Creating a new collection
animals = forest.animals

animal_names = [
    "Lion",
    "Elephant",
    "Giraffe",
    "Monkey",
    "Penguin",
    "Kangaroo",
    "Dolphin",
    "Tiger",
    "Zebra",
    "Koala",
]
animal_sounds = [
    "Roar",
    "Trumpet",
    "Necking sounds",
    "Chatter",
    "Honk",
    "Chirp",
    "Clicks",
    "Roar",
    "Bray",
    "Squeak",
]
animal_habitats = [
    "Grasslands",
    "Savannah",
    "Savannah",
    "Rainforest",
    "Antarctica",
    "Australia",
    "Oceans",
    "Jungle",
    "Grasslands",
    "Eucalyptus Forest",
]
animal_weights = [200, 5000, 1200, 5, 40, 70, 300, 250, 400, 12]


docs = []
for name, sound, habitat, weight in zip(
    animal_names, animal_sounds, animal_habitats, animal_weights
):
    doc = {"name": name, "sound": sound, "habitat": habitat, "weight": weight}
    docs.append(doc)

animals.insert_many(docs)
