import requests
import urllib.parse
import json


class character:
    name: str = ""
    realm: str = ""
    WOWHEAD = "https://worldofwarcraft.com/en-us/character/us/"
    def __init__(self, name: str, realm: str) -> None:
        self.name = name
        self.realm = realm

    @property
    def armoryUrl(self) -> str:
        quotedName = urllib.parse.quote(self.name)
        return f"{self.WOWHEAD}{self.realm}/{quotedName}"

    @property
    def characterJson(self) -> dict:
        try:
            r = requests.get(self.armoryUrl)
            r.raise_for_status()
        except:
            return {self.name: "?"}

        charJson = {}
        for line in r.text.split("\n"):
            if 'characterProfileInitialState = ' in line:
                charJson = json.loads(line.partition('characterProfileInitialState = ')[2].rstrip(";"))
                break

        if not charJson:
            raise Exception("Character information not found.")

        return charJson

    @property
    def itemLevel(self) -> str:
        if 'character' not in self.characterJson:
            return "Average Item Level Unknown."

        return self.characterJson['character']['averageItemLevel']


    def tierBonuses(self) -> dict:
        if 'character' not in self.characterJson:
            return {self.name: "?"}


        TIER_SLOTS = [
            "chest",
            "head",
            "shoulder",
            "hand",
            "leg"
        ]


        setCount = 0
        for slot in TIER_SLOTS:
            if setCount > 0:
                break
            if "set" in self.characterJson['character']['gear'][slot]:
                for index in range(len(self.characterJson['character']['gear'][slot]['set']['effects'])):
                    if "is_active" in self.characterJson['character']['gear'][slot]['set']['effects'][index]:
                        setCount = self.characterJson['character']['gear'][slot]['set']['effects'][index]['required_count']
                #out = self.characterJson['character']['gear'][slot]['set']['effects'][0]
                #print(json.dumps(out, indent=4))

        #print("{}: {}".format(self.name, setCount))
        return {self.name: {"Tier Set Bonus": setCount, "Average Item Level": self.itemLevel}}


    def tierBonuses101(self) -> dict:
        if 'character' not in self.characterJson:
            return {self.name: "?"}


        TIER_SLOTS = [
            "chest",
            "head",
            "shoulder",
            "hand",
            "leg"
        ]

        TIER_SET_IDS = [
            1540,
            1541,
            1542,
            1543,
            1544,
            1545,
            1546,
            1547,
            1548,
            1549,
            1550,
            1551,
            1552
        ]


        setCount = 0
        for slot in TIER_SLOTS:
            if setCount > 0:
                break
            if "set" in self.characterJson['character']['gear'][slot]:
                if self.characterJson['character']['gear'][slot]['set']['item_set']['id'] in TIER_SET_IDS:
                    for index in range(len(self.characterJson['character']['gear'][slot]['set']['effects'])):
                        if "is_active" in self.characterJson['character']['gear'][slot]['set']['effects'][index]:
                            setCount = self.characterJson['character']['gear'][slot]['set']['effects'][index]['required_count']

        return {self.name: {"Tier Set Bonus": setCount, "Average Item Level": self.itemLevel}}


#pitza = character(name="pitza", realm="elune")

#print(pitza.name)
#print(pitza.realm)
#print(pitza.armoryUrl)
#print(json.dumps(pitza.characterJson, sort_keys=True, indent=4))
#print(pitza.tierBonuses())

