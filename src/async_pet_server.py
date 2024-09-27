import src.utils.server as server


async def fetch_banner_content():
    banner_content = await server.get_banner_content()
    return banner_content