from datetime import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name_customer: str
    products_cart: dict
    shop_products: dict

    def calculate_total_price(self) -> float | int:
        return sum(
            self.shop_products[product] * value
            for product, value in self.products_cart.items()
        )

    def print_account(self) -> None:
        print(f"Date: "
              f"{datetime(2021, 4, 1, 12, 33, 41).strftime('%m/%d/%Y %T')}")
        print(f"Thanks, {self.name_customer}, for your purchase!")
        print("You have bought:")
        for product, value in self.products_cart.items():
            product_s = self.shop_products[product]
            if product_s * value == int(product_s * value):
                print(
                    f"{value} {product}s for "
                    f"{int(product_s * value)} dollars"
                )
                continue
            print(
                f"{value} {product}s for "
                f"{product_s * value} dollars"
            )
        print(f"Total cost is {self.calculate_total_price()} dollars")
        print("See you again!\n")
