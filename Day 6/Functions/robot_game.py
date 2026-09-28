import random

def create_robot(name, health=100):
    return {"name": name, "health": health, "position": [0, 0]}

def move_robot(robot, direction):
    moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    if direction in moves:
        robot["position"][0] += moves[direction][0]
        robot["position"][1] += moves[direction][1]
        print(f"{robot['name']} moved {direction} to {robot['position']}")
    else:
        print("Invalid direction! Use: up, down, left, right")

def attack(robot, target):
    damage = random.randint(10, 30)
    target["health"] -= damage
    print(f"{robot['name']} attacks {target['name']} for {damage} damage!")
    if target["health"] <= 0:
        print(f"{target['name']} has been destroyed!")
        return True
    return False

def display_status(robot):
    print(f"Robot: {robot['name']} | Health: {robot['health']} | Position: {robot['position']}")

def main():
    print("=== Robot Battle ===")
    player = create_robot("PlayerBot", 100)
    enemy = create_robot("EnemyBot", 80)
    
    while player["health"] > 0 and enemy["health"] > 0:
        display_status(player)
        display_status(enemy)
        print("\n1. Move")
        print("2. Attack")
        choice = input("Choose action: ")
        
        if choice == "1":
            direction = input("Direction (up/down/left/right): ")
            move_robot(player, direction)
        elif choice == "2":
            if attack(player, enemy):
                break
        
        if enemy["health"] > 0:
            attack(enemy, player)
    
    print("\nGame Over!")

if __name__ == "__main__":
    main()
