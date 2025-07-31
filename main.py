import json
from rich import print, box
from rich.panel import Panel
from rich.prompt import Prompt

def create_account(username):
    return {
        "username": username,
        "level": 50,
        "silver": 2140000000,
        "gold": 2140000000,
        "maps_unlocked": ["mt_drive", "sunset"],
        "cars": []
    }

def add_premium_cars(account, count=12):
    for i in range(count):
        account["cars"].append({
            "car_id": f"car_{i+1}",
            "name": f"Premium Car {i+1}",
            "power": 9999,
            "tuned": True,
            "is_premium": True
        })
    return account

def save_account(account):
    with open("modded_save.json", "w") as f:
        json.dump(account, f, indent=4)
    print(f"[green]✔ Save file created: [bold]modded_save.json[/bold]")

def main():
    print(Panel("[bold cyan]CarX Street Mod Tool[/bold cyan]\n[white]Made for Termux", box=box.DOUBLE))
    username = Prompt.ask("[yellow]Enter your modded username")
    
    acc = create_account(username)
    acc = add_premium_cars(acc)
    save_account(acc)
    print(Panel("[bold green]Done![/bold green]\nUpload [italic]modded_save.json[/italic] to game folder if possible."))

if __name__ == "__main__":
    main()