
#dictonary where keys are ingredients in EN, values are DE ingredients in DE, sorted based on DE name so easy to see what has been translated to the same word
translations = {
    "pineapple": "ananas",
    "pineapple mini": "ananas",
    "apple red 2": "apfel",
    "apple golden 3": "apfel",
    "apple golden 1": "apfel",
    "apple pink lady": "apfel",
    "apple braeburn": "apfel",
    "apple red yellow 1": "apfel",
    "apple red 3": "apfel",
    "apple red yellow 2": "apfel",
    "apple red delicious": "apfel",
    "apple crimson snow": "apfel",
    "apple granny smith": "apfel",
    "apple golden 2": "apfel",
    "apple red 1": "apfel",
    "apricot": "aprikosen",
    "eggplant": "aubergine",
    "avocado": "avocado",
    "avocado ripe": "avocado",
    "banana red": "banana",
    "banana lady finger": "banane",
    "banana": "banane",
    "pear 2": "birne",
    "pear": "birne",
    "pear stone": "birne",
    "pear kaiser": "birne",
    "pear red": "birne",
    "pear monster": "birne",
    "pear abate": "birne",
    "pear forelle": "birne",
    "pear williams": "birne",
    "cauliflower": "blumenkohl",
    "cantaloupe 1": "cantaloupe-melone",
    "cantaloupe 2": "cantaloupe-melone",
    "clementine": "clementinen",
    "dates": "datteln",
    "strawberry": "erdbeeren",
    "strawberry wedge": "erdbeeren",
    "chestnut": "esskastanien",
    "fig": "feigen",
    "pomegranate": "granatapfel",
    "grapefruit white": "grapefruit",
    "grapefruit pink": "grapefruit",
    "guava": "guave",
    "cucumber ripe": "gurke",
    "cucumber ripe 2": "gurke",
    "nut forest": "haselnusse",
    "hazelnut": "haselnusse",
    "huckleberry": "heidelbeere",
    "blueberry": "heidelbeeren",
    "raspberry": "himbeere",
    "mulberry": "himbeere",
    "ginger root": "ingwer",
    "redcurrant": "johannisbeeren",
    "kaki": "kaki",
    "cactus fruit": "kaktusfeige",
    "potato red": "kartoffeln",
    "potato red washed": "kartoffeln",
    "potato white": "kartoffeln",
    "cherry wax yellow": "kirsche",
    "cherry 2": "kirsche",
    "cherry wax black": "kirsche",
    "cherry wax red": "kirsche",
    "cherry rainier": "kirschen",
    "cherry 1": "kirschen",
    "kiwi": "kiwi",
    "kohlrabi": "kohlrabi",
    "cocos": "kokosnuss",
    "kumquats": "kumquats",
    "limes": "limette",
    "salak": "litschi",
    "lychee": "lychees",
    "corn": "mais",
    "corn husk": "maisschale",
    "mandarine": "mandarine",
    "tangelo": "mandarinen",
    "mango": "mango",
    "mango red": "mango",
    "mangostan": "mangostane",
    "maracuja": "maracuja",
    "melon piel de sapo": "melonen",
    "nectarine": "nektarine",
    "nectarine flat": "nektarine ",
    "orange": "orange",
    "papaya": "papaya",
    "pepper yellow": "paprika",
    "pepper orange": "paprika",
    "pepper green": "paprika",
    "pepper red": "paprika",
    "passion fruit": "passionsfrucht",
    "granadilla": "passionsfrucht",
    "nut pecan": "pecannuss",
    "pepino": "pepino",
    "peach": "pfirsich",
    "peach 2": "pfirsich",
    "peach flat": "pfirsich",
    "plum 2": "pflaumen",
    "plum": "pflaumen",
    "plum 3": "pflaumen",
    "physalis": "physalis",
    "physalis with husk": "physalis",
    "pitahaya red": "pitahaya",
    "pomelo sweetie": "pomelo",
    "quince": "quitten",
    "rambutan": "rambutan",
    "beetroot": "rote-bete",
    "onion red peeled": "rote-zwiebel",
    "carambula": "sternfrucht",
    "potato sweet": "süßkartoffeln",
    "tamarillo": "tamarillo",
    "tomato 2": "tomaten",
    "tomato 1": "tomaten",
    "tomato 3": "tomaten",
    "tomato yellow": "tomaten",
    "tomato heart": "tomaten",
    "tomato 4": "tomaten",
    "tomato not ripened": "tomaten",
    "tomato maroon": "tomaten",
    "tomato cherry red": "tomaten",
    "grape white 2": "trauben",
    "grape blue": "trauben",
    "grape pink": "trauben",
    "grape white": "trauben",
    "grape white 4": "trauben",
    "grape white 3": "trauben",
    "walnut": "walnusse",
    "watermelon": "wassermelone",
    "lemon meyer": "zitrone",
    "lemon": "zitrone",
    "onion red": "zwiebeln",
    "onion white": "zwiebeln",
}


#translate ingredients in EN to DE based on a dictionary
def EN2DE(ingredients_EN, dictionary):
    ingredients_DE = set()  # use set to ensure unique elements
    looked_up = set()  # keep track of already looked up items
    for item in ingredients_EN:
        item = item.lower()  # convert item to lowercase
        if item in dictionary and item not in looked_up:
            ingredients_DE.add(dictionary[item])
            looked_up.add(item)  # add item to the set of looked up items
        else:
            pass
    return list(ingredients_DE)  # convert set to list and return

def generate_restegourmet_url(mylist):
    # Convert the list to a comma-separated string
    list_str = ",".join(mylist)
    # Construct the URL string
    url = f"https://restegourmet.de/rezeptsuche/_/{list_str}/_"
    return url


#to test, uncomment these
#ingredients_EN = ["tomato yellow","hjkkjh","cactus fruit","grape white","grape white 3","redcurrant"]
#my_ingredients = EN2DE(ingredients_EN,translations)
#print(my_ingredients)
#print(generate_restegourmet_url(my_ingredients))
