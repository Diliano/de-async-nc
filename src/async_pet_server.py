import src.utils.server as server
import asyncio


async def fetch_banner_content():
    banner_content = await server.get_banner_content()
    return banner_content

async def get_lower_owners():
    owners = await server.get_owners()
    return [owner.lower() for owner in owners]

async def get_pets_by_owner(owner):
    try:
        cats = await server.get_cats_by_owner(owner)
        return {"pets": cats}
    except KeyError:
        return {"pets": [], "message": f"{owner} not found"}
    
async def get_all_pets():
    owners = await get_lower_owners()
    tasks = [get_pets_by_owner(owner) for owner in owners]
    all_pets = await asyncio.gather(*tasks)

    return [{"owner": owner, **pets} for owner, pets in zip(owners, all_pets)]

async def get_pet_pics(file_names):
    tasks = [server.get_pic(file_name) for file_name in file_names]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return ["placeholder_cat.png" if isinstance(result, Exception) else result for result in results]