def main():
    fruit = str(input("what fruit would you like to know the nutrition info about?: ")).lower().strip()
    print(nutrition(fruit))

def nutrition(fruit):
    calories = {
        'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'grapefruit': 60,
        'grapes': 90, 'honeydew melon': 50, 'kiwifruit': 90, 'lemon': 15, 'lime': 20,
        'nectarine': 60, 'orange': 80, 'peach': 60, 'pear': 100, 'pineapple': 50, 'plums': 70, 
        'strawberries': 50, 'sweet cherries': 100, 'tangering': 50, 'watermelon': 80, 
    }

    if fruit in calories:
        return(calories[fruit])
    else:
        return ""

main()