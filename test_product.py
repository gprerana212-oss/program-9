from product import format_product_info

def test_format_product_info():
    result = format_product_info("P1002", "Mouse", 10, 19.99)

    expected = (
        "Product Information:\n"
        "ID: P1002\n"
        "Name: Mouse\n"
        "Quantity: 10\n"
        "Price: $19.99"
    )

    assert result == expected
