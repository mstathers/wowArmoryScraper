#!/usr/bin/env python3

import multiprocessing
from character import character

"""
WHO HAS THE FIRE RING
https://www.wowhead.com/item=195480/seal-of-diurnas-chosen
"""


def main() -> None:
    roster = [
        {"name":"Pitza", "realm":"elune"},
        {"name":"Phorcefull", "realm":"elune"},
        {"name":"Aknologia", "realm":"elune"},
        {"name":"Callippe", "realm":"elune"},
        {"name":"Fog", "realm":"elune"},
        {"name":"Halîk", "realm":"nathrezim"},
        {"name":"Citra", "realm":"gilneas"},
        {"name":"Mayday", "realm":"gilneas"},
        {"name":"Murfwyrm", "realm":"elune"},
        {"name":"Murfbot", "realm":"elune"},
        {"name":"Shale", "realm":"gilneas"},
        {"name":"Duero", "realm":"sargeras"},
        {"name":"Dochollidày", "realm":"elune"},
        {"name":"Aya", "realm":"elune"},
        {"name":"Rhenin", "realm":"elune"},
        {"name":"Dehvii", "realm":"elune"},
        {"name":"Strozzoun", "realm":"elune"},
        {"name":"Astartes", "realm":"elune"},
        {"name":"Comelywhite", "realm":"elune"},
        {"name":"Zordiak", "realm":"elune"},
        {"name":"Mockra", "realm":"elune"},
        {"name":"Danabell", "realm":"elune"},
        {"name":"Baryll", "realm":"elune"},
        {"name":"Beansupplier", "realm":"illidan"},
        {"name":"Chamanita", "realm":"elune"},
        {"name":"Haralda", "realm":"elune"},
        {"name":"Fira", "realm":"elune"},
    ]

    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(pool_size)
    fireRingPlayers = pool.map(worker, roster)
    pool.close()
    pool.join()

    for player in sorted(fireRingPlayers, key=lambda d: list(d.keys())):
        if "NA" not in player.values():
            print(player)



def worker(player: dict) -> dict:
    toon = character(name=player['name'], realm=player['realm'])
    charInfo = toon.characterJson
    FIRE_RING_ID = 195480
    for slot in ['rightFinger', 'leftFinger']:
        if charInfo['character']['gear'][slot]['id'] == FIRE_RING_ID:
            ringName=charInfo['character']['gear'][slot]['name']
            ringIlvl=charInfo['character']['gear'][slot]['level']['value']

            return {player['name']: [ringName, ringIlvl]}

    return {player['name']: "NA"}
    

if __name__ == "__main__":
    main()
