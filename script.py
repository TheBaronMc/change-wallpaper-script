import os
import sys
import random

# Path to wallpapers
WALLPAPER_FOLDER = '/Path/to/wallpapers/'

number = int()              # indentation number
wallpapers = list()         # list of wallpaper
selectedWallpaper = str()   

def chooseNumber(mode):
    if (mode == "RANDOM"):
        return random.randint(0, len(wallpapers))
    elif (mode == "CYCLIC"): 
        nb = int()
        try:
            with open(".wallpaperNumber", 'r') as fichier:
                nb = (int(fichier.readline()) + 1) 
        except:
            nb = 0

        with open(".wallpaperNumber", 'w') as fichier:
            fichier.write(str(nb))

        return nb

    else:
        raise ValueError("You have selected a wrong mode ! (RANDOM | CYCLIC)")

def changeWallpaper(WALLPAPER_FOLDER, selectedWallpaper):
    pltf = sys.platform
    if (pltf == "linux"): # if you are using linux
        try:
            # The next command will exit execute a correct command if you are using Gnome
            # if for example you are using Cinnamon you have to change org.gnome.desktop.background to org.cinnamon.desktop.background 
            os.system("gsettings set org.gnome.desktop.background picture-uri file://" + WALLPAPER_FOLDER + selectedWallpaper)
        except:
            ValueError("Your path is wrong ! Try to name folders in one word.")
    else:
        Exception("Your are using an unsupported system.")

# Select a picture
wallpapers = os.listdir(WALLPAPER_FOLDER)

try:
    number = chooseNumber(sys.argv[1])
except:
    raise ValueError("You haven't selected a mode !")

selectedWallpaper = wallpapers[ number % len(wallpapers) ]

changeWallpaper(WALLPAPER_FOLDER, selectedWallpaper)


