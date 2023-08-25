from datetime import datetime
from typing import Dict, List
from inventory_report.inventory import Inventory
from inventory_report.reports.report import Report


class SimpleReport(Report):
    def __init__(self) -> None:
        self.inventories: List[Inventory] = []
        self.oldest_manuf_date = datetime.now()
        self.closest_exp_date = datetime.strptime("2500-09-30", "%Y-%m-%d")
        self.largest_inventory_company = ''

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def generate(self) -> str:
        self.get_oldest()
        oldest = self.oldest_manuf_date
        self.get_closest()
        closet = self.closest_exp_date
        self.get_largest()
        company = self.largest_inventory_company

        result = (
            f"Oldest manufacturing date: {oldest.strftime('%Y-%m-%d')}\n"
            f"Closest expiration date: {closet.strftime('%Y-%m-%d')}\n"
            f"Company with the largest inventory: {company}"
        )

        return result

    def get_largest(self) -> None:
        company: Dict[str, int] = dict()

        for inventory in self.inventories:
            for product in inventory.data:
                company_name = product.company_name
                if company_name in company:
                    company[company_name] += 1
                else:
                    company[company_name] = 1

                self.largest_inventory_company = max(company)

    def get_oldest(self) -> None:
        for inventory in self.inventories:
            for product in inventory.data:
                manufacturing_date = datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                )
                if manufacturing_date < self.oldest_manuf_date:
                    self.oldest_manuf_date = manufacturing_date

    def get_closest(self) -> None:
        for inventory in self.inventories:
            for product in inventory.data:
                expiration_date = datetime.strptime(
                    product.expiration_date, "%Y-%m-%d"
                )
                if (
                    expiration_date >= datetime.now()
                    and expiration_date < self.closest_exp_date
                ):
                    self.closest_exp_date = expiration_date
