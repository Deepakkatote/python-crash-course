import city_function # type: ignore

def test_city_country():
    long_name = city_function.city_country("tokyo", "japan", 50000)
    assert long_name == 'Tokyo, Japan -50000'