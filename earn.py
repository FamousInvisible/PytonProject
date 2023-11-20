import random
import time

def earn(player):
    money = random.randint(300, 600)
    print(f"Грабим караваны - 0%")
    time.sleep(1)
    print(f"Продаем помидоры на рынке - 25%")
    time.sleep(1)
    print(f"Помогаем кузнецу - 50%")
    time.sleep(1)
    print(f"Копаем на шахте - 75%")
    time.sleep(1)
    print(f"Раздаем газеты - 100%\n")
    time.sleep(1)
    player["money"] += money
    print(f"Ты заработал {money} золотых!")
    print("\n")
    return