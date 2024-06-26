import os
import pyfiglet
from colorama import init, Fore, Style

init(autoreset=True)

beyblades = {
    "Storm Pegasus": ("Attack", "Pegasus Starblast Attack", "Rubber Flat (RF)", "Storm", "105RF", "Gingka Hagane"),
    "Lightning L-Drago": ("Attack", "Lightning Destructor", "Right Rubber Flat (R2F)", "L-Drago", "100HF", "Ryuga"),
    "Rock Leone": ("Defense", "Lion Gale Force Wall", "Wide Ball (WB)", "Leone", "145WB", "Kyoya Tategami"),
    "Flame Sagittario": ("Stamina", "Sagittario Flame Claw", "Claw Sharp (CS)", "Sagittario", "C145S", "Kenta Yumiya"),
    "Earth Eagle": ("Defense", "Eagle Counter Attack", "Wide Defense (WD)", "Eagle", "145WD", "Tsubasa Otori"),
    "Dark Bull": ("Balance", "Bull Upper", "Heavy Sharp Defense (H145SD)", "Bull", "H145SD", "Benkei Hanawa"),
    "Thermal Pisces": ("Stamina", "Pisces Tornado Wing", "Wide Defense (WD)", "Pisces", "145WD", "Tetsuya Watarigani"),
    "Rock Aries": ("Stamina", "Aries Spin Track", "Defense Sharp (DS)", "Aries", "145D", "Damian Hart"),
    "Dark Gasher": ("Stamina", "Gasher Reverse Wind Strike", "Semi Defense (SD)", "Gasher", "CH120SF", "Yu Tendo"),
    "Storm Aquario": ("Attack", "Aquario Infinite Assault", "Metal Semi Defense (M145Q)", "Aquario", "M145Q", "Masamune Kadoya"),
    "Storm Capricorn": ("Stamina", "Capricorn Heavy Fusion", "Metal Semi Defense (M145Q)", "Capricorn", "M145Q", "Toby"),
    "Storm Serpent": ("Stamina", "Serpent Gravity Destroyer Attack", "Semi Defense (SD)", "Serpent", "S130MB", "Jack"),
    "Poison Serpent": ("Stamina", "Serpent Venom Strike", "Semi Defense (SD)", "Serpent", "SW145SD", "Julian Konzern"),
    "Burn Fireblaze (Phoenix)": ("Attack", "Fireblaze Crimson Flash", "Wide Defense (WD)", "Fireblaze", "135MS", "Phoenix"),
    "Cyber Pegasus (Cyber Aquario)": ("Attack", "Pegasus Jumper", "Rubber Sharp (RS)", "Pegasus", "105F", "Sora Akatsuki"),
    "Counter Leone": ("Defense", "Leone's Roar Blast", "Defense 125 Ball (D125B)", "Leone", "D125B", "Kyoya Tategami"),
    "Rock Scorpio": ("Stamina", "Scorpio Energy Drain", "Triple Change Semi Defense (T125JB)", "Scorpio", "T125JB", "Toby"),
    "Evil Gemios": ("Stamina", "Gemios Counter", "Defense Flat Spike (DF145FS)", "Gemios", "DF145FS", "Demure"),
    "Ray Striker": ("Attack", "Striker Flash", "Defense 125 Rubber Semi Flat (D125CS)", "Striker", "D125CS", "Masa Kinomiya"),
    "Flame Libra": ("Stamina", "Libra Inferno Blast", "Defense 125 Rubber Semi Flat (T125ES)", "Libra", "T125ES", "Yu Tendo"),
    "Thermal Lacerta": ("Stamina", "Lacerta's Bite Strike", "Wide Attack (WA130HF)", "Lacerta", "WA130HF", "Lena"),
    "Galaxy Pegasus": ("Attack", "Pegasus Starbooster Attack", "Defense 125 Rubber Defense Flat (D125RDF)", "Pegasus", "D125RDF", "Gingka Hagane"),
    "Flame Gasher": ("Stamina", "Gasher Shield Attack", "Semi Wide Semi Flat (SW145SF)", "Gasher", "SW145SF", "Yu Tendo"),
    "Grand Capricorn": ("Stamina", "Capricorn Jumbo Cannon", "Rubber 145 Wide Ball (R145WB)", "Capricorn", "R145WB", "Nowaguma"),
    "Hell Kerbecs": ("Stamina", "Kerbecs Centipede Blast", "Defense Sharp (145DS)", "Kerbecs", "145DS", "Demure"),
    "Gravity Destroyer": ("Attack", "Destroyer Force Strike", "Attack 85 Flat (85F)", "Destroyer", "85F", "Johannes"),
    "Vulcan Horuseus": ("Stamina", "Horuseus Crimson Flash", "Defense 130 Ball (130D)", "Horuseus", "130D", "Julian Konzern"),
    "Twisted Tempo": ("Defense", "Tempo Hammer Hit", "Defense 145 Rubber Semi Flat (BD145RS)", "Tempo", "BD145RS", "Nowaguma"),
    "Spiral Capricorn": ("Attack", "Capricorn Spin Attack", "Triple Change Wide Semi Flat (T125HF)", "Capricorn", "T125HF", "Nowaguma"),
    "Storm Northern Cross": ("Stamina", "Northern Cross Beam", "Attack 85 Extra Flat (85XF)", "Northern Cross", "85XF", "Daidoji"),
    "Fang Leone": ("Defense", "Leone's Fang Blast", "Defense 130 Wide 2 Defense (130W2D)", "Leone", "130W2D", "Kyoya Tategami"),
    "Storm Leone": ("Stamina", "Leone's Roar", "Defense 145 (145D)", "Leone", "145D", "Kyoya Tategami"),
    "Ray Gil": ("Attack", "Gil Flash", "Defense 125 Rubber Semi Flat (D125CS)", "Gil", "D125CS", "Beylin Fist"),
    "Meteor L-Drago": ("Attack", "L-Drago Destructor Assault", "Left Rubber Flat (LRF)", "L-Drago", "LRF", "Ryuga"),
    "Diablo Nemesis": ("Balance", "Nemesis Ultimate Balance", "Xtreme: Drive (X:D)", "Nemesis", "X:D", "Rago"),
    "Big Bang Pegasus": ("Attack", "Pegasus Starbooster Attack", "Final Drive (F:D)", "Pegasus", "F:D", "Gingka Hagane"),
    "Variares": ("Attack", "Variares Super Assault", "Defense: Drive (D:D)", "Variares", "D:D", "King"),
    "Jade Jupiter": ("Stamina", "Jupiter Gravity Destroyer Attack", "Defense 130 Ball (130B)", "Jupiter", "130B", "Aguma"),
    "Death Quetzalcoatl": ("Stamina", "Quetzalcoatl Assault", "Defense Flat Spike (DF145FS)", "Quetzalcoatl", "DF145FS", "Dylan")
}

def display_stats(beyblade):
    stats = beyblades.get(beyblade)
    if stats:
        beyblade_type, power, tip, wheel, spintrack, owner = stats
        print(f"\n{Fore.YELLOW}Beyblade: {beyblade}")
        print(f"{Fore.CYAN}Type: {beyblade_type}")
        print(f"{Fore.GREEN}Power: {power}")
        print(f"{Fore.MAGENTA}Tip: {tip}")
        print(f"{Fore.BLUE}Wheel: {wheel}")
        print(f"{Fore.RED}Spintrack: {spintrack}")
        print(f"{Fore.YELLOW}Owner: {owner}")
    else:
        print(f"{Fore.RED}Beyblade '{beyblade}' not found.")

if __name__ == "__main__":

    while True:
        title = pyfiglet.figlet_format("BeyBlade: Metal Fuzion")
        print(Fore.RED + title)

        print("\n" + Fore.GREEN + "Choose a Beyblade to see its stats (or type 'exit' to quit):")
        for index, beyblade in enumerate(sorted(beyblades.keys())):
            print(f"{index + 1}. {beyblade}")

        choice = input("\nEnter your choice: ")
        if choice.lower() == 'exit':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(beyblades):
            os.system('cls' if os.name == 'nt' else 'clear')
            beyblade = sorted(beyblades.keys())[int(choice) - 1]
            display_stats(beyblade)
            input("\nPress Enter to continue...")
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print(Fore.RED + "Invalid choice. Please enter a number from the menu.")
