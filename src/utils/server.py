import asyncio
from random import randint
from time import time


async def get_banner_content():
    await asyncio.sleep(randint(1, 3))
    return {
        "title": "Kitty Litter",
        "bannerImg": "https://riotfest.org/wp-content/uploads/2017/10/AcT9YIL.jpg",
        "copyrightYear": 2006,
    }


async def get_owners():
    await asyncio.sleep(randint(1, 3))
    owners = ["Pavlov", "Schrodinger", "Foucault", "Vel", "Calvin"]
    return owners


async def get_cats_by_owner(owner):
    await asyncio.sleep(randint(1, 3))
    cats_by_owner = {
        "schrodinger": ["Leben", "Tot"],
        "pavlov": ["Belle", "Dribbles", "Nibbles"],
        "foucault": ["M. Fang"],
        "vel": ["Opal"],
        "calvin": ["Hobbes"],
    }
    return cats_by_owner[owner]


async def get_pic(file_name):
    await asyncio.sleep(randint(1, 3))

    if "cat" not in file_name:
        raise Exception("not a cat")

    return f"{file_name}.png"


async def get_legacy_status():
    await asyncio.sleep(randint(1, 3))
    if randint(0, 2) < 2:
        return {"status": 500, "message": "Internal Server Error"}

    return {"status": 200, "message": "Legacy Server up and running"}
