from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "Nicotine Polacrilex",
        "Target Corporation",
        "2021-02-18",
        "2023-09-17",
        "CR25 1551 4467 2549 4402 1",
        "instrucao 1",
    )
    assert product.id == '1'
    assert product.product_name == 'Nicotine Polacrilex'
    assert product.company_name == 'Target Corporation'
    assert product.manufacturing_date == '2021-02-18'
    assert product.expiration_date == '2023-09-17'
    assert product.serial_number == 'CR25 1551 4467 2549 4402 1'
    assert product.storage_instructions == 'instrucao 1'
