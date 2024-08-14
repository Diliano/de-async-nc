from time import time

from src.async_cat_server import fetch_banner_content

async def test_fetch_banner_content_returns_value_from_server():
    banner = await fetch_banner_content()
    assert banner == {
        "title": "Kitty Litter",
        "bannerImg": "https://riotfest.org/wp-content/uploads/2017/10/AcT9YIL.jpg",
        "copyrightYear": 2006,
    }

async def test_get_lower_owners_returns_list_of_owners_in_lower_case():
    lower_owners = await get_lower_owners()
    assert lower_owners == ["pavlov", "schrodinger", "foucault", "vel", "calvin"]

async def test_get_pets_by_owner_returns_dict_with_requested_owners_pets():
    pets = await get_pets_by_owner("pavlov")
    assert pets == {"pets": ["Belle", "Dribbles", "Nibbles"]}

    pets = await get_pets_by_owner("schrodinger")
    assert pets == {"pets": ["Leben", "Tot"]}

async def test_get_pets_by_owner_returns_dict_with_empty_list_when_no_owner():
    res = await get_pets_by_owner("missing")
    assert res == {"pets": [], "message": "missing not found"}

async def test_get_all_cats_returns_dict_with_correct_ordered_owners_and_cats():
    res = await get_all_cats()
    assert res == [
        {"owner": "pavlov", "cats": ["Belle", "Dribbles", "Nibbles"]},
        {"owner": "schrodinger", "cats": ["Leben", "Tot"]},
        {"owner": "foucault", "cats": ["M. Fang"]},
        {"owner": "vel", "cats": ["Opal"]},
        {"owner": "calvin", "cats": ["Hobbes"]},
    ]

async def test_get_all_cats_runs_multiple_requests_for_pets_at_the_same_time():
    start_time = time()
    await get_all_cats()
    execution_time = time() - start_time
    allowed_time = 7
    # up to 3 for owners and up to 3 for cats and 1 for leeway
    assert execution_time < allowed_time

async def test_get_cat_pics_returns_cat_pics_from_servedr():
    cat_pics = await get_cat_pics(["cute_cat"])
    assert cat_pics == ["cute_cat.png"]

async def test_get_cat_pics_returns_placeholder():
    cat_pics = await get_cat_pics(["sausage_dog"])
    assert cat_pics == [
        "placeholder_cat.png",
    ]

async def test_get_cat_pics_handles_placeholders_and_regular_images():
    cat_pics = await get_cat_pics(
        ["cute_cat", "grumpy_cat", "smelly_cat", "sausage_dog"]
    )
    assert cat_pics == [
        "cute_cat.png",
        "grumpy_cat.png",
        "smelly_cat.png",
        "placeholder_cat.png",
    ]

async def test_get_cat_pics_runs_multiple_requests_for_pics_at_the_same_time():
    start_time = time()
    res = await get_cat_pics(["cute_cat", "grumpy_cat", "smelly_cat", "sausage_dog"])
    execution_time = time() - start_time
    # up to 3 seconds to request pics and 1 for leeway
    assert execution_time < 4

async def test_retry_legacy_server_returns_message_from_legacy_server():
    message = await retry_legacy_server()
    assert message == "Legacy Server up and running"
