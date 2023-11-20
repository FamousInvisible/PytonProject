from battle import battle_game
from trener import workout
from earn import earn
shop = {
    "Деревянный топор":{"price":100, "damage":10},
    "Железный меч":{"price":300, "damage":20},
    "Коса Возмездия":{"price":600, "damage":40}
}

player = {
    "name": "",
    "hp": 100,
    "damage": 55+shop["Деревянный топор"]["damage"],
    "armor": 10,
    "money": 1_000,
    "level": 1,
    "gun":"Деревянный топор",
    "status": "alive",
    "inventory":["Деревянный топор"]
}


enemy = {
    "Зомби": {
        "hp": 50,
        "damage": 20,
        "armor": 10,
        "money": 150,
        "level": 1},
    "Маг-некромант": {
        "hp": 150,
        "damage": 45,
        "armor": 15,
        "money": 650,
        "level": 5},
    "Ситх-зомби": {
        "hp": 400,
        "damage": 88,
        "armor": 50,
        "money": 15_000,
        "level": 25},
    "Дракон-зомби": {
        "hp": 1000,
        "damage": 200,
        "armor": 100,
        "money": 50_000,
        "level": 200}
}

player["name"] = input("Придумайте ник своего персонажа: ")

while player["hp"] > 0:
    print("Меню: ")
    print(f"1 - В бой\n"
          f"2 - Тренировка\n"
          f"3 - Информация о игроке\n"
          f"4 - Информация о противниках\n"
          f"5 - Магазин\n"
          f"6 - Выбрать оружие\n"
          f"7 - Заработать денег\n")
    action = int(input("Выберите действие: "))
    print("\n")
    if action == 1:
        
        print(f"У вас {player['level']} level")
        print("Зомби - 1 level\nМаг-некромант - 5 level\nСитх-зомби - 25 level\nДракон-зомби - 150 level")
        print("С кем будете сражаться?\n")
        print("1 - Зомби\n2 - Маг-некромант\n3 - Ситх-зомби\n4 - Дракон-зомби")
        action_enemy = int(input("Выберите действие: "))
        
        enemy_now = enemy["Зомби"]
        if action_enemy == 1:
            if player["level"] >= enemy_now["level"]:
                battle_game(player, enemy_now)
            else:
                print("У вас низкий уровень! Прокачайте свой level")
                continue
            continue
        
        enemy_now = enemy["Маг-некромант"]
        if action_enemy == 2:
            if player["level"] >= enemy_now["level"]:
                if enemy_now["hp"] >= player["hp"]:
                    if enemy_now["damage"] >= player["damage"]:
                        print("У Мага-некроманта больше hp и damage чем у вас. Прокачайте свое здоровье и урон")
                        print("Здоровье Мага-некроманта: ", enemy_now["hp"])
                        print("Урон Мага-некроманта: ", enemy_now["damage"])
                        continue
                    print("У Мага-некроманта больше hp чем у вас. Прокачайте свое здоровье ")
                    print("Здоровье Мага-некроманта: ", enemy_now["hp"])
                    continue
                battle_game(player, enemy_now)
            else:
                print("У вас низкий уровень! Прокачайте свой level")
                continue
            continue
        
        enemy_now = enemy["Ситх-зомби"]
        if action_enemy == 3:
            if player["level"] >= enemy_now["level"]:
                if enemy_now["hp"] >= player["hp"]:
                    if enemy_now["damage"] >= player["damage"]:
                        print("У Ситха-зомби больше hp и damage чем у вас. Прокачайте свое здоровье и урон")
                        print("Здоровье Ситха-зомби: ", enemy_now["hp"])
                        print("Урон Ситха-зомби: ", enemy_now["damage"])
                        continue
                    print("У Ситха-зомби больше hp чем у вас. Прокачайте свое здоровье ")
                    print("Здоровье Ситха-зомби: ", enemy_now["hp"])
                    continue
                battle_game(player, enemy_now)
            else:
                print("У вас низкий уровень! Прокачайте свой level")
                continue
            continue
            
        enemy_now = enemy["Дракон-зомби"]
        if action_enemy == 4:
            if player["level"] >= enemy_now["level"]:
                if enemy_now["hp"] >= player["hp"]:
                    if enemy_now["damage"] >= player["damage"]:
                        print("У Дракона-зомби больше hp и damage чем у вас. Прокачайте свое здоровье и урон")
                        print("Здоровье Дракона-зомби: ", enemy_now["hp"])
                        print("Урон Дракона-зомби: ", enemy_now["damage"])
                        continue
                    print("У Дракона-зомби больше hp чем у вас. Прокачайте свое здоровье ")
                    print("Здоровье Дракона-зомби: ", enemy_now["hp"])
                    continue
                battle_game(player, enemy_now)
            else:
                print("У вас низкий уровень! Прокачайте свой level")
                continue
            continue
        
    elif action == 2:
        print("Прокачать атаку - 1\nПрокачать здоровье - 2\n")
        action_t = int(input("Выберите действие: "))
        print("\n")
        workout(action_t, player)
        continue
        
    elif action == 3:
        print("Твои харктеристики: ")
        print(f"Здоровье: {player['hp']}\nМаксимальный наносимый урон: {player['damage']}\nlevel: {player['level']}\n")
        print("Твой инвентарь: ")
        for item in player["inventory"]:print(item)
        print(f"У тебя {player['money']} золотых")
        continue
    
    elif action == 4:
        print("Характеристики противников: \n")
        for key, items in enemy.items():
            print(f"{key}: \n"
                  f"Здоровье: {items['hp']}\n"
                  f"Урон: {items['damage']}\n"
                  f"Броня: {items['armor']}\n"
                  f"Денег может выпасть: {items['money']}\n")
            
    elif action == 5:
        shoping = True
        print(f"Приветствую, {player['name']}! Что ты желаешь приобрести?")
        print(f"У тебя сейчас {player['money']} золотых!")
        for key, items in shop.items():
            print(key, ", урон - ", items["damage"], ", цена - ", items["price"])
        print("Выйти")
        while shoping:

            item = input()

            if item in player['inventory']:
                print(f'У тебя уже есть {item}!')
            elif item in shop:
                if player['money'] >= shop[item]["price"]:
                    print(f'Ты успешно приобрёл {item}!')
                    player['inventory'].append(item)
                    player['money'] -= shop[item]["price"]
                    print(f"У тебя осталось {player['money']} золотых!")
                else:"Тебе не хватило денег :c"

            elif item=="Выйти":shoping=False

            else:
                print('У нас такого нет')
        print()
        print('Буду ждать тебя снова, путник!')
        print()
    elif action == 6:
        equip=True
        while equip:
            print("Твое оружие: ")
            for item in player["inventory"]:print(item)
            print("Выйти")
            print(f"Сейчас ты вооружен оружием: {player['gun']}")
            item = input()
            if item in player["inventory"]:
                player["gun"] = item
                player['damage'] = 55+shop[item]['damage']
                print(f"Ты взял {item}!")
            elif item == "Выйти":equip=False
            else:print("У тебя такого нет")
    elif action == 7:
        earn(player)
        continue