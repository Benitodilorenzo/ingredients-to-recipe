import json

#dictionary with a number corresponding to a fruit or vegetable

int_to_EN_dict = {"1": "Raspberry", "2": "Avocado", "3": "Apple Red 2", "4": "Potato Sweet", "5": "Lemon Meyer", "6": "Grapefruit White", "7": "Apple Golden 3",
                  "8": "Potato Red", "9": "Plum 2", "10": "Mango", "11": "Kiwi", "12": "Passion Fruit", "13": "Eggplant", "14": "Pear 2", "15": "Tomato 2",
                  "16": "Rambutan", "17": "Plum", "18": "Pineapple", "19": "Cucumber Ripe", "20": "Pear", "21": "Lychee", "22": "Tomato 1", "23": "Maracuja",
                  "24": "Pepper Yellow", "25": "Tangelo", "26": "Grape White 2", "27": "Potato Red Washed", "28": "Mandarine", "29": "Melon Piel de Sapo",
                  "30": "Dates", "31": "Fig", "32": "Granadilla", "33": "Nectarine Flat", "34": "Blueberry", "35": "Cherry Rainier", "36": "Grape Blue",
                  "37": "Cherry 1", "38": "Tomato 3", "39": "Mango Red", "40": "Chestnut", "41": "Quince", "42": "Pomegranate", "43": "Orange",
                  "44": "Grape Pink", "45": "Apple Golden 1", "46": "Corn Husk", "47": "Grapefruit Pink", "48": "Pepper Orange", "49": "Guava",
                  "50": "Banana Lady Finger", "51": "Mulberry", "52": "Nectarine", "53": "Cactus fruit", "54": "Cauliflower", "55": "Strawberry",
                  "56": "Apple Pink Lady", "57": "Plum 3", "58": "Limes", "59": "Peach", "60": "Pear Stone", "61": "Tomato Yellow", "62": "Tomato Heart",
                  "63": "Grape White", "64": "Banana", "65": "Pear Kaiser", "66": "Grape White 4", "67": "Pear Red", "68": "Mangostan", "69": "Walnut",
                  "70": "Peach 2", "71": "Papaya", "72": "Apple Braeburn", "73": "Beetroot", "74": "Cantaloupe 1", "75": "Cucumber Ripe 2",
                  "76": "Apple Red Yellow 1", "77": "Ginger Root", "78": "Tomato 4", "79": "Pear Monster", "80": "Kohlrabi", "81": "Peach Flat",
                  "82": "Tomato not Ripened", "83": "Nut Pecan", "84": "Pomelo Sweetie", "85": "Carambula", "86": "Apple Red 3", "87": "Cherry Wax Yellow",
                  "88": "Tamarillo", "89": "Clementine", "90": "Huckleberry", "91": "Nut Forest", "92": "Pitahaya Red", "93": "Apple Red Yellow 2",
                  "94": "Apple Red Delicious", "95": "Salak", "96": "Pineapple Mini", "97": "Banana Red", "98": "Apple Crimson Snow", "99": "Pepper Green",
                  "100": "Apple Granny Smith", "101": "Pepino", "102": "Strawberry Wedge", "103": "Avocado ripe", "104": "Pear Abate", "105": "Cantaloupe 2",
                  "106": "Cherry 2", "107": "Cherry Wax Black", "108": "Physalis", "109": "Redcurrant", "110": "Kumquats", "111": "Tomato Maroon",
                  "112": "Cherry Wax Red", "113": "Pepper Red", "114": "Watermelon", "115": "Apple Golden 2", "116": "Physalis with Husk",
                  "117": "Onion Red Peeled", "118": "Hazelnut", "119": "Grape White 3", "120": "Kaki", "121": "Onion Red", "122": "Corn", "123": "Apple Red 1",
                  "124": "Potato White", "125": "Pear Forelle", "126": "Pear Williams", "127": "Tomato Cherry Red", "128": "Onion White", "129": "Apricot",
                  "130": "Cocos"}


#dictonary where keys are ingredients in EN, values are DE ingredients in DE, sorted based on DE name so easy to see what has been translated to the same word
EN_DE_dict = {
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

#dictionary to create numbers as key with the name of the fruit or vegetable as value

int_to_EN_dict = {1: 'Raspberry', 2: 'Avocado', 3: 'Apple Red 2', 4: 'Potato Sweet', 5: 'Lemon Meyer', 6: 'Grapefruit White', 7: 'Apple Golden 3',
                  8: 'Potato Red', 9: 'Plum 2', 10: 'Mango', 11: 'Kiwi', 12: 'Passion Fruit', 13: 'Eggplant', 14: 'Pear 2', 15: 'Tomato 2', 16: 'Rambutan',
                  17: 'Plum', 18: 'Pineapple', 19: 'Cucumber Ripe', 20: 'Pear', 21: 'Lychee', 22: 'Tomato 1', 23: 'Maracuja', 24: 'Pepper Yellow',
                  25: 'Tangelo', 26: 'Grape White 2', 27: 'Potato Red Washed', 28: 'Mandarine', 29: 'Melon Piel de Sapo', 30: 'Dates', 31: 'Fig',
                  32: 'Granadilla', 33: 'Nectarine Flat', 34: 'Blueberry', 35: 'Cherry Rainier', 36: 'Grape Blue', 37: 'Cherry 1', 38: 'Tomato 3',
                  39: 'Mango Red', 40: 'Chestnut', 41: 'Quince', 42: 'Pomegranate', 43: 'Orange', 44: 'Grape Pink', 45: 'Apple Golden 1', 46: 'Corn Husk',
                  47: 'Grapefruit Pink', 48: 'Pepper Orange', 49: 'Guava', 50: 'Banana Lady Finger', 51: 'Mulberry', 52: 'Nectarine', 53: 'Cactus fruit',
                  54: 'Cauliflower', 55: 'Strawberry', 56: 'Apple Pink Lady', 57: 'Plum 3', 58: 'Limes', 59: 'Peach', 60: 'Pear Stone', 61: 'Tomato Yellow',
                  62: 'Tomato Heart', 63: 'Grape White', 64: 'Banana', 65: 'Pear Kaiser', 66: 'Grape White 4', 67: 'Pear Red', 68: 'Mangostan', 69: 'Walnut',
                  70: 'Peach 2', 71: 'Papaya', 72: 'Apple Braeburn', 73: 'Beetroot', 74: 'Cantaloupe 1', 75: 'Cucumber Ripe 2', 76: 'Apple Red Yellow 1',
                  77: 'Ginger Root', 78: 'Tomato 4', 79: 'Pear Monster', 80: 'Kohlrabi', 81: 'Peach Flat', 82: 'Tomato not Ripened', 83: 'Nut Pecan',
                  84: 'Pomelo Sweetie', 85: 'Carambula', 86: 'Apple Red 3', 87: 'Cherry Wax Yellow', 88: 'Tamarillo', 89: 'Clementine', 90: 'Huckleberry',
                  91: 'Nut Forest', 92: 'Pitahaya Red', 93: 'Apple Red Yellow 2', 94: 'Apple Red Delicious', 95: 'Salak', 96: 'Pineapple Mini',
                  97: 'Banana Red', 98: 'Apple Crimson Snow', 99: 'Pepper Green', 100: 'Apple Granny Smith', 101: 'Pepino', 102: 'Strawberry Wedge',
                  103: 'Avocado ripe', 104: 'Pear Abate', 105: 'Cantaloupe 2', 106: 'Cherry 2', 107: 'Cherry Wax Black', 108: 'Physalis', 109: 'Redcurrant',
                  110: 'Kumquats', 111: 'Tomato Maroon', 112: 'Cherry Wax Red', 113: 'Pepper Red', 114: 'Watermelon', 115: 'Apple Golden 2',
                  116: 'Physalis with Husk', 117: 'Onion Red Peeled', 118: 'Hazelnut', 119: 'Grape White 3', 120: 'Kaki', 121: 'Onion Red',
                  122: 'Corn', 123: 'Apple Red 1', 124: 'Potato White', 125: 'Pear Forelle', 126: 'Pear Williams', 127: 'Tomato Cherry Red',
                  128: 'Onion White', 129: 'Apricot', 130: 'Cocos'}

#creating a class that puts double quotation marks on the key and value pairs
class mydict(dict):
        def __str__(self):
            return json.dumps(self)

EN_dict = mydict(int_to_EN_dict)

print(EN_dict)

EN_dict = {"1": "Raspberry", "2": "Avocado", "3": "Apple Red 2", "4": "Potato Sweet", "5": "Lemon Meyer", "6": "Grapefruit White", "7": "Apple Golden 3",
 "8": "Potato Red", "9": "Plum 2", "10": "Mango", "11": "Kiwi", "12": "Passion Fruit", "13": "Eggplant", "14": "Pear 2", "15": "Tomato 2", "16": "Rambutan",
 "17": "Plum", "18": "Pineapple", "19": "Cucumber Ripe", "20": "Pear", "21": "Lychee", "22": "Tomato 1", "23": "Maracuja", "24": "Pepper Yellow",
 "25": "Tangelo", "26": "Grape White 2", "27": "Potato Red Washed", "28": "Mandarine", "29": "Melon Piel de Sapo", "30": "Dates", "31": "Fig",
 "32": "Granadilla", "33": "Nectarine Flat", "34": "Blueberry", "35": "Cherry Rainier", "36": "Grape Blue", "37": "Cherry 1", "38": "Tomato 3",
 "39": "Mango Red", "40": "Chestnut", "41": "Quince", "42": "Pomegranate", "43": "Orange", "44": "Grape Pink", "45": "Apple Golden 1", "46": "Corn Husk",
 "47": "Grapefruit Pink", "48": "Pepper Orange", "49": "Guava", "50": "Banana Lady Finger", "51": "Mulberry", "52": "Nectarine", "53": "Cactus fruit",
 "54": "Cauliflower", "55": "Strawberry", "56": "Apple Pink Lady", "57": "Plum 3", "58": "Limes", "59": "Peach", "60": "Pear Stone", "61": "Tomato Yellow",
 "62": "Tomato Heart", "63": "Grape White", "64": "Banana", "65": "Pear Kaiser", "66": "Grape White 4", "67": "Pear Red", "68": "Mangostan", "69": "Walnut",
 "70": "Peach 2", "71": "Papaya", "72": "Apple Braeburn", "73": "Beetroot", "74": "Cantaloupe 1", "75": "Cucumber Ripe 2", "76": "Apple Red Yellow 1",
 "77": "Ginger Root", "78": "Tomato 4", "79": "Pear Monster", "80": "Kohlrabi", "81": "Peach Flat", "82": "Tomato not Ripened", "83": "Nut Pecan",
 "84": "Pomelo Sweetie", "85": "Carambula", "86": "Apple Red 3", "87": "Cherry Wax Yellow", "88": "Tamarillo", "89": "Clementine", "90": "Huckleberry",
 "91": "Nut Forest", "92": "Pitahaya Red", "93": "Apple Red Yellow 2", "94": "Apple Red Delicious", "95": "Salak", "96": "Pineapple Mini", "97": "Banana Red",
 "98": "Apple Crimson Snow", "99": "Pepper Green", "100": "Apple Granny Smith", "101": "Pepino", "102": "Strawberry Wedge", "103": "Avocado ripe",
 "104": "Pear Abate", "105": "Cantaloupe 2", "106": "Cherry 2", "107": "Cherry Wax Black", "108": "Physalis", "109": "Redcurrant", "110": "Kumquats",
 "111": "Tomato Maroon", "112": "Cherry Wax Red", "113": "Pepper Red", "114": "Watermelon", "115": "Apple Golden 2", "116": "Physalis with Husk",
 "117": "Onion Red Peeled", "118": "Hazelnut", "119": "Grape White 3", "120": "Kaki", "121": "Onion Red", "122": "Corn", "123": "Apple Red 1",
 "124": "Potato White", "125": "Pear Forelle", "126": "Pear Williams", "127": "Tomato Cherry Red", "128": "Onion White", "129": "Apricot", "130": "Cocos"}

#returns a list of ingredients from the number given in a list
def filter_list_by_dict_keys(input_list, input_dict):
    """
    Filters a list by the keys of a dictionary.
    """
    result_list = []
    for item in input_list:
        if item in input_dict:
            result_list.append(input_dict[item])
        else:
            pass
    return result_list
