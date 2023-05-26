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
        {"name":"Dochollidày", "realm":"elune"},
        {"name":"Murfi", "realm":"elune"},
        {"name":"Callippe", "realm":"elune"},
        {"name":"Aknologia", "realm":"elune"},
        {"name":"Astartes", "realm":"elune"},
        {"name":"Aya", "realm":"elune"},
        {"name":"Comelywhite", "realm":"elune"},
        {"name":"Gauntlet", "realm":"elune"},
        {"name":"Haralda", "realm":"elune"},
        {"name":"Kofie", "realm":"elune"},
        {"name":"Mockra", "realm":"elune"},
        {"name":"Phorceful", "realm":"elune"},
        {"name":"Pitza", "realm":"elune"},
        {"name":"Relifus", "realm":"elune"},
        {"name":"Shale", "realm":"gilneas"},
        {"name":"Strozzoun", "realm":"elune"},
        {"name":"Tasty", "realm":"elune"},
        {"name":"Valkkar", "realm":"elune"},
        {"name":"Virusgt", "realm":"elune"},
        {"name":"Zordiak", "realm":"elune"},
        {"name":"Sumscales", "realm":"elune"},
        {"name":"Duero", "realm":"sargeras"},
        {"name":"Tyraxis", "realm":"elune"},
        {"name":"Beansupplier", "realm":"illidan"},
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
    return toon.tierBonuses101()


if __name__ == "__main__":
    main()
