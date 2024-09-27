import src.utils.server as server


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