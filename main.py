from src.mask import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

# 7000 7922 8960 6361
print(get_mask_card_number("7000792289606361"))
# 7365 4108 4301 3587 4305
print(get_mask_account("73654108430135874305"))
# Visa Platinum 7000792289606361
print(mask_account_card("Visa Platinum 7000792289606361"))
# Счет 73654108430135874305
print(mask_account_card("Счет 73654108430135874305"))