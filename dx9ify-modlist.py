# If this file is in your GAMMA/profile folder, you fucked up. Go reread the instructions.

# Takes the default GAMMA (DX11) modlist from Github source and edits it to be DX8/9 compatible.
# Outputs as a text file named modlist.txt in a subfolder called G.A.M.M.A. DX8 and DX9 - 0.9.4


from datetime import date
from urllib.request import urlopen

today = str(date.today()) #for date stamps

# Read in the DX11 modlist from the GAMMA Github
with urlopen("https://raw.githubusercontent.com/Grokitach/Stalker_GAMMA/refs/heads/main/G.A.M.M.A/modpack_data/modlist.txt") as f:
    data = f.read().decode("utf-8")
    modlist = data.split("\n")

# Create list of mods that need to be enabled or disabled
enable_mods = [
    "DX9 Compatibility Patch",
    "No BNVG FDDA Redone Patch",
    "439- The Covenant Weapon Pack for DX9 - TCWP Team"
]

disable_mods = [
    # 3DSS and dependencies
    "428- Authentic Reticle for 3DSS - Napolemon",
    "441- HOWA20 Makeover - Andtheherois & Phant0m",
    "427- IWP SV98 3DSS - Andtheherois & IWP Team",
    "434- 3DSS M4A1 Siber Reanimation - Andtheherois",
    "431- 3DSS ISG AK Makeover - Andtheherois & BAS Team",
    "429- The Covenant Weapon Pack 3DSS - Andtheherois & TCWP Team",
    "430- M98B 3DSS Update - Andtheherois & frostychun",
    "410- 3DSS for GAMMA - Redotix99 & Andtheherois & party50",
    "409- Mark Switch - party50 & meowie",
    "461- GAMMA Immaculate Munitions Pack GIMP - andtheherois",

    #Shaders
    "388- Aydins Grass Tweaks SSS Terrain LOD Compatibility - aytabag",
    "290- Atmospherics Shaders Weathers and Reshade Latest - Hippobot",
    "190- Screen Space Shaders 23 - Ascii1457",
    "189- Beef's NVG - theRealBeef",
    "188- Enhanced Shaders - KennShade",
    "LVutner's Shader Corner Shadow Fix",
    "G.A.M.M.A. Weathers",

    #Others
    "356- Lurker HD Remodel - KeatonB_08 & KynesPeace",
    "Teivaz's Gunslinger Exo Animations Port"
]

# Iterate through DX11 modlist and enable/disable as appropriate
for i in range(len(modlist)):
    for mod in enable_mods:
        if mod in modlist[i] and modlist[i].startswith("-"):
            modlist[i] = "+" + modlist[i][1:]
    for mod in disable_mods:
        if mod in modlist[i] and modlist[i].startswith("+"):
            modlist[i] = "-" + modlist[i][1:]

# Change topline comment with timestamp
modlist[0] = "# GAMMA modlist for DX8 and DX9, last edited " + today + "\n"

# Print to file
with open("./G.A.M.M.A. DX8 and DX9 - 0.9.4/modlist.txt", "w") as output:
    for i in range(len(modlist)):
        output.write(modlist[i] + "\n")
