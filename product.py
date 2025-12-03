def format_product_info(product_id: str, name: str, quantity: int, price: float) -> str:
    return (
        f"Product Information:\n"
        f"ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ${price:.2f}"
    )


if __name__ == "__main__":
    
    print(format_product_info("P1001", "Laptop", 5, 999.99))
