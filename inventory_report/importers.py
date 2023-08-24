from abc import ABC, abstractmethod
from inventory_report.product import Product
from typing import Dict, Type, List
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.list_products: List[Product] = []

    def import_data(self) -> List[Product]:
        with open(self.path, 'r') as file:
            content = file.read()
            products_json = json.loads(content)
        for product in products_json:
            object_product = Product(
                id=product["id"],
                product_name=product["product_name"],
                company_name=product["company_name"],
                manufacturing_date=product["manufacturing_date"],
                expiration_date=product["expiration_date"],
                serial_number=product["serial_number"],
                storage_instructions=product["storage_instructions"])
            self.list_products.append(object_product)
        return self.list_products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
