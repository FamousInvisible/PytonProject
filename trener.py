import random
import time

def workout(num, player):
    if num == 1:
        power_up = random.randint(20, 50)
        print(f"Прокачака персонажа - 0%")
        time.sleep(1)
        print(f"Прокачака персонажа - 25%")
        time.sleep(1)
        print(f"Прокачака персонажа - 50%")
        time.sleep(1)
        print(f"Прокачака персонажа - 75%")
        time.sleep(1)
        print(f"Прокачака персонажа - 100%\n")
        time.sleep(1)
        player["damage"] = player["damage"] + power_up
        print(f"Атака увеличена на {power_up} пунктов")
        print("\n")
        return
    elif num == 2:
        power_up = random.randint(20, 50)
        print(f"Прокачака персонажа - 0%")
        time.sleep(2)
        print(f"Прокачака персонажа - 25%")
        time.sleep(2)
        print(f"Прокачака персонажа - 50%")
        time.sleep(2)
        print(f"Прокачака персонажа - 75%")
        time.sleep(2)
        print(f"Прокачака персонажа - 100%\n")
        time.sleep(1)
        player["hp"] = player["hp"] + power_up
        print(f"Здоровье увеличено на {power_up} пунктов")
        print("\n")
        return
    else:
        return "Такого числа нет"
        