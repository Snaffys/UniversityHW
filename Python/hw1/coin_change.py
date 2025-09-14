NAME = "Danil"
SURNAME = "Grezin"
PATRONYMIC = "Maximovich"
NAME_LEN = len(NAME)
SURNAME_LEN = len(SURNAME)
PATRONYMIC_LEN = len(PATRONYMIC)

def coin_change(value):
    try:
        coin_nominal = int(value)
    except(ValueError, TypeError):
        return -1, -1, -1

    for i in range(coin_nominal // PATRONYMIC_LEN + 1):
        for j in range(coin_nominal // SURNAME_LEN + 1):
            for k in range(coin_nominal // NAME_LEN + 1):
                if((i * PATRONYMIC_LEN + j * SURNAME_LEN + k * NAME_LEN) == coin_nominal):
                    return i, j, k
    return -1, -1, -1

def main():
    coin_nominal = input("Write down a value for change: ")
    max_change, mid_change, min_change = coin_change(coin_nominal)
    if(max_change == mid_change == min_change == -1):
        print("-42!")
    else:
        print(f"Name value ({NAME}): {min_change}\nSurname value ({SURNAME}): {mid_change}\nPatronymic value ({PATRONYMIC}): {max_change}")
    
if __name__ == "__main__":
    main()