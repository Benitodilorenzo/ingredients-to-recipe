#functions used on FE

#dictionary with a number corresponding to a fruit or vegetable
int_EN_dict = {
    "0": "Apple",
    "1": "Avocado",
    "2": "Banana",
    "3": "Beetroot",
    "4": "Broccoli",
    "5": "Cauliflower",
    "6": "Eggplant",
    "7": "Granadilla",
    "8": "Kiwi",
    "9": "Kohlrabi",
    "10": "Lemon",
    "11": "Limes",
    "12": "Mango",
    "13": "Melon",
    "14": "Onion",
    "15": "Orange",
    "16": "Pear",
    "17": "Pepper",
    "18": "Pineapple",
    "19": "Pomegranate",
    "20": "Potato",
    "21": "Strawberry",
    "22": "Tomato",
    "23": "Watermelon",
}

"""
olddict={
    "0": "Raspberry",
    "1": "Avocado",
    "2": "Apple Red 2",
    "3": "Potato Sweet",
    "4": "Lemon Meyer",
    "5": "Grapefruit White",
    "6": "Apple Golden 3",
    "7": "Potato Red",
    "8": "Plum 2",
    "9": "Mango",
    "10": "Kiwi",
    "11": "Passion Fruit",
    "12": "Eggplant",
    "13": "Pear 2",
    "14": "Tomato 2",
    "15": "Rambutan",
    "16": "Plum",
    "17": "Pineapple",
    "18": "Cucumber Ripe",
    "19": "Pear",
    "20": "Lychee",
    "21": "Tomato 1",
    "22": "Maracuja",
    "23": "Pepper Yellow",
    "24": "Tangelo",
    "25": "Grape White 2",
    "26": "Potato Red Washed",
    "27": "Mandarine",
    "28": "Melon Piel de Sapo",
    "29": "Dates",
    "30": "Fig",
    "31": "Granadilla",
    "32": "Nectarine Flat",
    "33": "Blueberry",
    "34": "Cherry Rainier",
    "35": "Grape Blue",
    "36": "Cherry 1",
    "37": "Tomato 3",
    "38": "Mango Red",
    "39": "Chestnut",
    "40": "Quince",
    "41": "Pomegranate",
    "42": "Orange",
    "43": "Grape Pink",
    "44": "Apple Golden 1",
    "45": "Corn Husk",
    "46": "Grapefruit Pink",
    "47": "Pepper Orange",
    "48": "Guava",
    "49": "Banana Lady Finger",
    "50": "Mulberry",
    "51": "Nectarine",
    "52": "Cactus fruit",
    "53": "Cauliflower",
    "54": "Strawberry",
    "55": "Apple Pink Lady",
    "56": "Plum 3",
    "57": "Limes",
    "58": "Peach",
    "59": "Pear Stone",
    "60": "Tomato Yellow",
    "61": "Tomato Heart",
    "62": "Grape White",
    "63": "Banana",
    "64": "Pear Kaiser",
    "65": "Grape White 4",
    "66": "Pear Red",
    "67": "Mangostan",
    "68": "Walnut",
    "69": "Peach 2",
    "70": "Papaya",
    "71": "Apple Braeburn",
    "72": "Beetroot",
    "73": "Cantaloupe 1",
    "74": "Cucumber Ripe 2",
    "75": "Apple Red Yellow 1",
    "76": "Ginger Root",
    "77": "Tomato 4",
    "78": "Pear Monster",
    "79": "Kohlrabi",
    "80": "Peach Flat",
    "81": "Tomato not Ripened",
    "82": "Nut Pecan",
    "83": "Pomelo Sweetie",
    "84": "Carambula",
    "85": "Apple Red 3",
    "86": "Cherry Wax Yellow",
    "87": "Tamarillo",
    "88": "Clementine",
    "89": "Huckleberry",
    "90": "Nut Forest",
    "91": "Pitahaya Red",
    "92": "Apple Red Yellow 2",
    "93": "Apple Red Delicious",
    "94": "Salak",
    "95": "Pineapple Mini",
    "96": "Banana Red",
    "97": "Apple Crimson Snow",
    "98": "Pepper Green",
    "99": "Apple Granny Smith",
    "100": "Pepino",
    "101": "Strawberry Wedge",
    "102": "Avocado ripe",
    "103": "Pear Abate",
    "104": "Cantaloupe 2",
    "105": "Cherry 2",
    "106": "Cherry Wax Black",
    "107": "Physalis",
    "108": "Redcurrant",
    "109": "Kumquats",
    "110": "Tomato Maroon",
    "111": "Cherry Wax Red",
    "112": "Pepper Red",
    "113": "Watermelon",
    "114": "Apple Golden 2",
    "115": "Physalis with Husk",
    "116": "Onion Red Peeled",
    "117": "Hazelnut",
    "118": "Grape White 3",
    "119": "Kaki",
    "120": "Onion Red",
    "121": "Corn",
    "122": "Apple Red 1",
    "123": "Potato White",
    "124": "Pear Forelle",
    "125": "Pear Williams",
    "126": "Tomato Cherry Red",
    "127": "Onion White",
    "128": "Apricot",
    "129": "Cocos",
    "130": "Lemon",
}
"""

#dictonary where keys are ingredients in EN, values are DE ingredients in DE, sorted based on DE name so easy to see what has been translated to the same word
EN_DE_dict = {
    "pineapple": "ananas",
    "pineapple mini": "ananas",
    "apple": "apfel",
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
    "broccoli": "broccoli",
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
    "Hokaido": "hokkaido-kurbis",
    "ginger root": "ingwer",
    "redcurrant": "johannisbeeren",
    "kaki": "kaki",
    "cactus fruit": "kaktusfeige",
    "potato": "kartoffeln",
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
    "pepper": "paprika",
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
    "potato sweet": "susskartoffeln",
    "tamarillo": "tamarillo",
    "tomato": "tomaten",
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
    "meatcow": "rindfleisch",
    "walnut": "walnusse",
    "watermelon": "wassermelone",
    "lemon meyer": "zitrone",
    "lemon": "zitrone",
    "onion red": "zwiebeln",
    "onion white": "zwiebeln",
    "onion": "zwiebeln",
}

#function that takes a dictionary and returns a list of its unique values
def unique_values(dictionary):
    return list(set(dictionary.values()))


#create list out of dict based on threshold
def filter_dict_by_value(input_dict,threshold):
    """
    Filters a dictionary by the value of its items.
    """
    result_list = []
    for key, value in input_dict.items():
        if value >= threshold:
            result_list.append(key)
    return result_list

#returns a list of ingredients from the number given in a list
def get_values_from_dict(input_list, input_dict):
    """
     Returns a list of values from the input dictionary that correspond to keys in the input list.
    """
    result_list = []
    for item in input_list:
        if item in input_dict:
            result_list.append(input_dict[item])
        else:
            pass
    return result_list

#translate ingredients in EN to DE based on a dictionary
def EN2DE(ingredients_EN, dictionary):
    """
    Translates a list of English ingredient names to German using a given dictionary.
    """
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

#hard coded URL link to visit
def generate_restegourmet_url(mylist):
    """ Convert the list to a comma-separated string and Construct the URL string"""
    list_str = ",".join(mylist)
    url = f"https://restegourmet.de/rezeptsuche/_/{list_str}/_"
    return url

#to convert ingredients into code
def lookup_keys(lst, dct):
    """Look up values in dictionary and return a list of corresponding keys."""
    return [list(dct.keys())[list(dct.values()).index(value)] for value in lst]



#print(lookup_keys(["33","22"],int_EN_dict))

# def generate_shell_command(shell_command):
#     """
#     Convert a list of command line arguments into a string that can be run as a shell command.
#     """
#     command_string = " ".join(shell_command)
#     return command_string

#if needed, uncomment these
#ingredients_EN = ["tomato yellow","hjkkjh","cactus fruit","grape white","grape white 3","redcurrant"]
#my_ingredients = EN2DE(ingredients_EN,translations)
#print(my_ingredients)
#print(generate_restegourmet_url(my_ingredients))

#import json
#creating a class that puts double quotation marks on the key and value pairs
#class mydict(dict):
#        def __str__(self):
#            return json.dumps(self)
#EN_dict = mydict(int_to_EN_dict)
#print(EN_dict)
