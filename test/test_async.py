from time import time

import pytest

from src.async_cat_server import fetch_banner_content


@pytest.mark.asyncio
@pytest.mark.describe("fetch_banner_content")
@pytest.mark.it("returns the banner_content from the server")
async def test_fetch_banner_content_value():
    banner = await fetch_banner_content()
    assert banner == {
        "title": "Kitty Litter",
        "bannerImg": "https://riotfest.org/wp-content/uploads/2017/10/AcT9YIL.jpg",
        "copyrightYear": 2006,
    }


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_lower_owners")
@pytest.mark.it("returns the list of owners from the server in lower case")
async def test_get_lower_owners_value():
    lower_owners = await get_lower_owners()
    assert lower_owners == ["pavlov", "schrodinger", "foucault", "vel", "calvin"]


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_pets_by_owner")
@pytest.mark.it("returns a dict with the requested owners pets")
async def test_get_pets_by_owner_value():
    pets = await get_pets_by_owner("pavlov")
    assert pets == {"pets": ["Belle", "Dribbles", "Nibbles"]}

    pets = await get_pets_by_owner("schrodinger")
    assert pets == {"pets": ["Leben", "Tot"]}


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_pets_by_owner")
@pytest.mark.it(
    "returns a dict with an empty list and a message when the owner isn't found"
)
async def test_get_pets_by_owner_errors():
    res = await get_pets_by_owner("missing")
    assert res == {"pets": [], "message": "missing not found"}


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_all_cats")
@pytest.mark.it("returns a dict with both owners and cats in the correct order")
async def test_get_pets_return():
    res = await get_all_cats()
    assert res == [
        {"owner": "pavlov", "cats": ["Belle", "Dribbles", "Nibbles"]},
        {"owner": "schrodinger", "cats": ["Leben", "Tot"]},
        {"owner": "foucault", "cats": ["M. Fang"]},
        {"owner": "vel", "cats": ["Opal"]},
        {"owner": "calvin", "cats": ["Hobbes"]},
    ]


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_all_cats")
@pytest.mark.it("runs multiple requests for pets at the same time")
async def test_get_pets_time():
    start_time = time()
    await get_all_cats()
    execution_time = time() - start_time
    allowed_time = 7
    # up to 3 for owners and up to 3 for cats and 1 for leeway
    assert execution_time < allowed_time


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_cat_pics")
@pytest.mark.it("returns cat_pics from the server")
async def test_get_cat_pics_return_cat():
    cat_pics = await get_cat_pics(["cute_cat"])
    assert cat_pics == ["cute_cat.png"]


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_cat_pics")
@pytest.mark.it("non-cats are replaced with placeholder_cat.png")
async def test_get_cat_pics_return_placeholder():
    cat_pics = await get_cat_pics(["sausage_dog"])
    assert cat_pics == [
        "placeholder_cat.png",
    ]


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_cat_pics")
@pytest.mark.it("handles placeholders and regular images at the same time")
async def test_get_cat_pics_return_multiple():
    cat_pics = await get_cat_pics(
        ["cute_cat", "grumpy_cat", "smelly_cat", "sausage_dog"]
    )
    assert cat_pics == [
        "cute_cat.png",
        "grumpy_cat.png",
        "smelly_cat.png",
        "placeholder_cat.png",
    ]


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("get_cat_pics")
@pytest.mark.it("runs multiple requests for pics at the same time")
async def test_get_cat_pics_time():
    start_time = time()
    res = await get_cat_pics(["cute_cat", "grumpy_cat", "smelly_cat", "sausage_dog"])
    execution_time = time() - start_time
    # up to 3 seconds to request pics and 1 for leeway
    assert execution_time < 4


@pytest.mark.skip
@pytest.mark.asyncio
@pytest.mark.describe("retry_server")
@pytest.mark.it("(eventually) returns the message from the legacy server")
async def test_retry_legacy_server_return():
    message = await retry_legacy_server()
    assert message == "Legacy Server up and running"
