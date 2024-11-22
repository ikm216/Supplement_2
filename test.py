def area_rect(len, wid):
    return len * wid

def test_should_return_24_for_6_and_4():
    assert area_rect(6, 4) == 24