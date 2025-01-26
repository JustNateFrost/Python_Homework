from address import Address
from mailing import Mailing


from_address = Address(654321, "Moscow", "Pushkin", 30, 21)
to_address = Address(659876, "Moscow", "Lermontova", 50, 98)

my_mailing = Mailing(to_address, from_address, "350", "A87T432OPB7")

print(f"Отправление {my_mailing.track} из {my_mailing.from_address}"
      f"в {my_mailing.to_address}. Стоимость {my_mailing.cost} рублей.")
