import random

def get_numbers_ticket(min:int, max:int, quantity:int) -> list:
    
    if (min < 1) or (max > 1000) or (quantity - 1 > (max - min)):
        print("""Формат чисел не вірний. 
              Діапазон не може перевищувати значення від 1 до 1000. 
              Кількість рандомно обраних елементів не може перевищувати 
              кількість елементів заданого діапазону!""")
        return []
    else:
        total_elements = 0
        set_of_quantity = set()
        while total_elements < quantity:
            set_of_quantity.add(random.randint(min, max))
            total_elements = len(set_of_quantity)
        # list_of_quantity = sorted(set_of_quantity)
        return sorted(set_of_quantity)

lottery_numbers = get_numbers_ticket(1, 49, 7)
print("Ваші лотерейні числа: ", lottery_numbers)