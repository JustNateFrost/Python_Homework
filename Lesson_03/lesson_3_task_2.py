from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy A16", "79028590802"),
    Smartphone("HUAWEI", "Pura 70", "79066254800"),
    Smartphone("Xiaomi", "Redmi A3", "79089603265"),
    Smartphone("HONOR", "X6b", "79066243397"),
    Smartphone("ASUS", "Zenfone 11 Ultra", "78002342506")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - "
          f"{smartphone.phone_model} - {smartphone.phone_number}")
