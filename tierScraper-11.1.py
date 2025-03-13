#!/usr/bin/env python3

# python3 character.py | jq '.character.gear.head.set.item_set | "\(.id) \(.name)"'

import multiprocessing
from character import character

"""
10.1 tier set
https://www.wowhead.com/guide/raids/vault-of-the-incarnates/tier-sets
"""


def main() -> None:
    roster = [
        {"name":"Aknologia", "realm":"elune"},
        {"name":"Hoj", "realm":"elune"},
        {"name":"Ark", "realm":"elune"},
        {"name":"Kerogen", "realm":"gilneas"},
        {"name":"Bermy", "realm":"gilneas"},
        {"name":"Murfie", "realm":"gilneas"},
        {"name":"Danabell", "realm":"elune"},
        {"name":"Valkkar", "realm":"elune"},
        {"name":"Haralda", "realm":"elune"},
        {"name":"Virusgt", "realm":"elune"},
        {"name":"Cait", "realm":"elune"},
        {"name":"Talial", "realm":"elune"},
        {"name":"Relifus", "realm":"elune"},
        {"name":"Stumpyfoot", "realm":"elune"},
        {"name":"Mockradin", "realm":"elune"},
        {"name":"Fax", "realm":"elune"},
        {"name":"Duero", "realm":"sargeras"},
        {"name":"Dranaldo", "realm":"zuljin"},
        {"name":"Vinni", "realm":"nathrezim"},
    ]

    pool_size = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(pool_size)
    rosterTier = pool.map(worker, roster)
    pool.close()
    pool.join()

    for player in sorted(rosterTier, key=lambda d: list(d.keys())):
        if "NA" not in player.values():
            print(player)


def worker(player: dict) -> dict:
    toon = character(name=player['name'], realm=player['realm'])
    return toon.tierBonuses111()


if __name__ == "__main__":
    main()
