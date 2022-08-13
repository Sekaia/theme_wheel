import random
import storage


p1 = []
p2 = []
closet = [storage.color, storage.place, storage.emotion, storage.character,
          storage.focus_point, storage.style, storage.items, storage.accessories,
          storage.clothes]
shelves = ["Color", "Location", "Theme", "Base", "Type", "Style", "Item", "Accessory", "Clothes"]


def spin():
    for shelf in closet:
        get_random_from_list(shelf)
    print_result(p1)
    print_result(p2)


def get_random_from_list(storage_list):
    result = []
    random_choice = random.choice(storage_list)
    result.append(random_choice)
    while random_choice == result[0]:
        random_choice = random.choice(storage_list)
    result.append(random_choice)
    add_to_list(result)


def add_to_list(random_items):
    p1.append(random_items[0])
    p2.append(random_items[1])


def print_result(p):
    print("------------------------------")
    for count, shelf in enumerate(shelves):
        print(f"{shelf}: {p[count]}")


spin()
