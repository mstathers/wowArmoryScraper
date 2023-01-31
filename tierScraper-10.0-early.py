#!/usr/bin/env python3
import argparse
import requests
import json
import urllib.parse
import multiprocessing
from multiprocessing.pool import ThreadPool

http = requests.Session()

def main(args):
    if args.url:
        rosterTier = queryArmory(args.url)
    else:
        # TODO: We could scrape for the raid roster here. Raider.io requires
        # javascript for all this unfortunately so a better source will be
        # needed.
        #
        # Instead, we'll just create a manual list of urls and loop through
        # them.
        roster = [
            "https://worldofwarcraft.com/en-us/character/us/elune/Baryll",
            "https://worldofwarcraft.com/en-us/character/us/elune/Chamanita",
            "https://worldofwarcraft.com/en-us/character/us/gilneas/Citra",
            "https://worldofwarcraft.com/en-us/character/us/elune/Haralda",
            "https://worldofwarcraft.com/en-us/character/us/elune/Murfwyrm",
            "https://worldofwarcraft.com/en-us/character/us/elune/Marlonus",
            "https://worldofwarcraft.com/en-us/character/us/elune/Phorcefull",
            "https://worldofwarcraft.com/en-us/character/us/elune/Pitza",
            "https://worldofwarcraft.com/en-us/character/us/gilneas/Shale",
            "https://worldofwarcraft.com/en-us/character/us/elune/Stumpyfoot",
            "https://worldofwarcraft.com/en-us/character/us/elune/Tyraxis",
            "https://worldofwarcraft.com/en-us/character/us/elune/Vancleef",
            "https://worldofwarcraft.com/en-us/character/us/elune/Virusgt",
            "https://worldofwarcraft.com/en-us/character/us/elune/Wangchi",
        ]
        roster.sort()


        rosterTier={}

        pool_size = multiprocessing.cpu_count()
        pool = ThreadPool(pool_size)
        for url in roster:
            output = pool.apply_async(queryArmory, args=(url,)).get()
            rosterTier.update(output)
        pool.close()
        pool.join()


    # Output
    sortedTier = {k: rosterTier[k] for k in sorted(rosterTier)}
    for key, value in sortedTier.items():
        print("{} {}".format(key, value))



def queryArmory(url):
    encodedCharName = urllib.parse.urlparse(url).path.split('/')[-1]
    charName = urllib.parse.unquote(encodedCharName)
    r = http.request('GET', url)
    if r.raise_for_status():
        print(r.raise_for_status())
        return 1

    for line in r.text.split("\n"):
        if 'characterProfileInitialState = ' in line:
            charJson = json.loads(line.partition('characterProfileInitialState = ')[2].rstrip(";"))
            break

#    print(json.dumps(charJson['character'], indent=4))
    averageItemLevel = charJson['character']['averageItemLevel']

    tierSlots = [
        "chest",
        "head",
        "shoulder",
        "hand",
        "leg"
    ]

    setCount = 0
    for slot in tierSlots:
        if setCount > 0:
            break
        if "set" in charJson['character']['gear'][slot]:
            for index in range(len(charJson['character']['gear'][slot]['set']['effects'])):
                if "is_active" in charJson['character']['gear'][slot]['set']['effects'][index]:
                    setCount = charJson['character']['gear'][slot]['set']['effects'][index]['required_count']
            #out = charJson['character']['gear'][slot]['set']['effects'][0]
            #print(json.dumps(out, indent=4))

    #print("{}: {}".format(charName, setCount))
    return {charName: {"Tier Set Bonus": setCount, "Average Item Level": averageItemLevel}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="wow armory url for character. Skip to scan Collusion raiders.", nargs="?")
    args = parser.parse_args()
    main(args)
