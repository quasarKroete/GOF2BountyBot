from .. import bbAliasable
from ...bbConfig import bbData

class bbWeapon(bbAliasable.Aliasable):
    dps = 0.0
    value = 0
    wiki = ""
    hasWiki = False
    manufacturer = ""

    icon = ""
    hasIcon = False
    shopSpawnRate = 0
    emoji = ""
    hasEmoji = False

    def __init__(self, name, aliases, dps=0.0, value=0, wiki="", manufacturer="", icon="", emoji=""):
        super(bbWeapon, self).__init__(name, aliases)
        self.dps = dps
        self.value = value
        self.wiki = wiki
        self.hasWiki = wiki != ""
        self.manufacturer = ""
        self.icon = icon
        self.hasIcon = icon != ""
        self.emoji = emoji
        self.hasEmoji = emoji != ""
        self.shopSpawnRate = 0

    
    def getValue(self):
        return self.value


    def toDict(self):
        return {"name": self.name, "builtIn": True}

    
    def statsStringShort(self):
        return "*Dps: " + str(self.dps) + "*"


    def getType(self):
        return bbWeapon


def fromDict(weaponDict):
    if weaponDict["builtIn"]:
        return bbData.builtInWeaponObjs[weaponDict["name"]]
    else:
        return bbWeapon(weaponDict["name"], weaponDict["aliases"], dps=weaponDict["dps"], value=weaponDict["value"], wiki=weaponDict["wiki"] if "wiki" in weaponDict else "", manufacturer=weaponDict["manufacturer"] if "manufacturer" in weaponDict else "", icon=weaponDict["icon"] if "icon" in weaponDict else bbData.rocketIcon, emoji=weaponDict["emoji"] if "emoji" in weaponDict else "")
