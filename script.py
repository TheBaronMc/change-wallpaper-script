import os
import sys

# Path to wallpapers
WALLPAPER_FOLDER = '/Path/to/wallpapers/'

number = int()              # indentation number
wallpapers = list()         # list of wallpaper
selectedWallpaper = str()   

def chooseNumber(mode):
    if (mode == "RANDOM"):
        pass
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

try:
    number = chooseNumber(sys.argv[1])
except:
    raise ValueError("You haven't selected a mode !")

# Select a picture
wallpapers = os.listdir(WALLPAPER_FOLDER)
selectedWallpaper = wallpapers[ number % len(wallpapers) ]

# Change wallpaper
try:
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + WALLPAPER_FOLDER + selectedWallpaper)
except:
    ValueError("Your path is wrong ! Try to name folders in one word.")
