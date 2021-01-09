import os
import sys
import random

import argparse
import json

def chooseNumber(mode):
    """
        choose a number in function of the selected mode

        :param mode (str): "RANDOM" or "CYCLIC"

        :return (int): Chosen number 
    """
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
            os.system("gsettings set org.gnome.desktop.background picture-uri file://{}{}".format(WALLPAPER_FOLDER, selectedWallpaper))
        except:
            raise ValueError("Your path is wrong ! Try to name folders in one word.")
    else:
        raise Exception("Your are using an unsupported system.")

def argumentsParser():
    """
        Parse arguments from command line

        :return: (argparse.Namespace) a namespace who contains parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", "-m", help="execution mode (RANDOM|CYCLIC)")
    parser.add_argument("--path", "-p", help="path to wallpapers directory")
    parser.add_argument("--config", "-c", help="path to configuration file")
    return parser

def getParameters(parsedArguments):
    """
        Get parameters from the parsed arguments

        :param parsedArguments (argparse.Namespace): parsed arguments

        :return: dict who contain the mode and the path

        :raise: ValueError 
    """
    args = {"mode": "", "path": ""}

    # If there is a configuration file
    if parsedArguments.config is None:
        if not ((parsedArguments.mode == "RANDOM") or (parsedArguments.mode == "CYCLIC")):
            raise ValueError("mode has to be RANDOM or CYCLIC")
        else:
            args["mode"] = parsedArguments.mode

        if parsedArguments.path is None:
            raise ValueError("You have to set a wallpaper directory")
        else:
            if os.path.exists(parsedArguments.path):
                if os.path.isdir(parsedArguments.path):
                    args["path"] = parsedArguments.path
                else:
                    raise ValueError("Your path to your wallpaper directory is not pointing on a directory")
            else:
                raise ValueError("The path to your wallpaper directory doesn't exist")

        return args

    # If there isn't a configu    
    else:
        if os.path.exists(parsedArguments.config):
            if os.path.isfile(parsedArguments.config):
                with open(parsedArguments.config, 'r') as configFile:
                    decodeConfigFile = json.load(configFile)
                    for key in decodeConfigFile.keys():
                        if key == "mode":
                            parsedArguments.mode = decodeConfigFile["mode"]
                        if key == "path":
                            parsedArguments.path = decodeConfigFile["path"]

                    parsedArguments.config = None

                    return getParameters(parsedArguments)
            else:
                raise ValueError("Your to your configuration file is not pointing on a file")
        else:
            raise ValueError("The path to your configuration file doesn't exist")

def main():
    
    parser = argumentsParser()
    parsedArguments = parser.parse_args()
    try:
        args = getParameters(parsedArguments)
    
        # Select a picture
        wallpapers = os.listdir(args["path"])

        number = chooseNumber(args["mode"])

        selectedWallpaper = wallpapers[ number % len(wallpapers) ]

        changeWallpaper(args["path"], selectedWallpaper)

    except ValueError as err:
        print(err)
        parser.print_help()
        exit(-1)

if __name__ == "__main__":
    main()