import json

from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        config = json.load(config)
        for customer in config["customers"]:
            res = {}
            print(f"{customer['name']} has {customer['money']} dollars")

            for shop in config["shops"]:

                car = Car(
                    config["FUEL_PRICE"],
                    customer["car"]["fuel_consumption"],
                    customer["location"], shop["location"]
                ).calculate_trip_cost()

                sh = Shop(
                    customer["name"],
                    customer["product_cart"],
                    shop["products"]
                ).calculate_total_price()

                res[car + sh] = [
                    customer["name"],
                    customer["product_cart"],
                    shop["products"], shop["name"]
                ]

                print(f"{customer['name']}'s trip to the "
                      f"{shop['name']} costs {car + sh}")

            if customer["money"] < min(res.keys()):
                print(f"{customer['name']} doesn't have enough "
                      f"money to make a purchase in any shop")
                break

            print(f"{customer['name']} rides to {res[min(res)][-1]}\n")

            Shop(
                res[min(res)][0],
                res[min(res)][1],
                res[min(res)][2]
            ).print_account()

            print(f"{customer['name']} rides home")
            print(f"{customer['name']} now has "
                  f"{customer['money'] - min(res.keys())} dollars\n")
