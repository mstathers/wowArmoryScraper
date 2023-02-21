#!/usr/bin/env python3

import multiprocessing
from character import character


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
    rosterTier = pool.map(worker, roster)
    pool.close()
    pool.join()


    # Output
    sortedTier = sorted(rosterTier, key=lambda d: list(d.keys()))
    for i in sortedTier:
        for key, value in i.items():
            print(f"{key} {value}")


def worker(player: dict) -> dict:
    toon = character(name=player['name'], realm=player['realm'])
    return toon.tierBonuses()


if __name__ == "__main__":
    main()
