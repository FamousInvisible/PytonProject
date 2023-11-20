import random
import time

def battle_game(player, enemy):
    print("У тебя сейчас: ", player["hp"],"здоровья.")
    
    while True:
        
        player_damage_now = random.randint(player["damage"] // 3, player["damage"])
        enemy_damage_now = random.randint(enemy["damage"] // 3, enemy["damage"])
        
        time.sleep(1)
        print("Наносит удар", player["name"],"\n")
        time.sleep(1)
        
        player_damage_now = player_damage_now - random.randint(enemy["armor"] // 2, enemy["armor"])  
        enemy["hp"] = enemy["hp"] - player_damage_now
        print(player["name"], f"Нанес: {player_damage_now}", "Противнику")
        print("У противника - ", enemy["hp"],"\n")
        
        if enemy["hp"] <= 0:
            print("Ты победил!")
            player["level"] = player["level"] + enemy["level"]
            break
        
        time.sleep(1)
        print("Наносит удар Противник!\n")
        time.sleep(1)
        
        enemy_damage_now = enemy_damage_now - random.randint(player["armor"] // 2, player["armor"])
        player["hp"] = player["hp"] - enemy_damage_now
        print("Противник", f"Нанес: {enemy_damage_now}", player["name"])
        print("У", player["name"], "-", player["hp"],"\n")
        
        if player["hp"] <= 0:
            print("Ты проиграл! Но ничего страшного у тебя есть ещё одно попытка\n")
            print("Здоровье восстановлено!", "У тебя 100 hp")
            player["hp"] = 100
            break

    return