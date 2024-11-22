def area_rect(len, wid):
    """ Use the area of a rectangle formula and returns the area

    Args:
        len: the length of the rectangle
        wid: the width of the rectangle

    Returns:
        The area of the rectangle
    """
    return len * wid

def area_tri(base, hei):
     """ Use the area of a circle formula and returns the area

    Args:
        base: the base of the 
        hei: the width of the rectangle

    Returns:
        The area of the rectangle
    """
     return (base * hei) / 2

def test_should_return_24_for_6_and_4():
    assert area_rect(6, 4) == 24

def test_should_return_12_for_6_and_4():
    assert area_tri(6, 4) == 12