import random

# maximum number of lines that can users can bet on
MAX_LINES = 300
# maximum amount that users can bet
MAX_BET = 1000
# minimum amount that users can bet
MIN_BET = 5
ROWS = 3
COLS = 3

# the symbol count decides the function to hold the value true.
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [[], [], []]
    for col in range(cols):
        columns = []
        for row in range(rows):
            value = random.choice(all_symbols)








# This function is responsible for getting the user input that gets the deposit form the user
def deposit():
    # while loop runs until the user gives a valid amount for the deposit to be made
    while True:
        amount = input("Please enter the amount you would like to deposit: $")
        # checks for the type of input entered by the user
        # amount is the variable that stores the
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount


def get_number_of_lines():
    # while loop runs until the user gives a valid amount for the deposit to be made
    while True:
        amount = input("Please enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # checks for the type of input entered by the user
        # amount is the variable that stores the
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_LINES:
                break
            else:
                print(f"Amount must be between 1 and ${MAX_LINES} (inclusive)")
        else:
            print("Please enter a valid number.")

    return amount


def get_bet():
    # while loop runs until the user gives a valid amount for the deposit to be made
    while True:
        amount = input("Please enter the amount you would like to bet on each line: $")
        # checks for the type of input entered by the user
        # amount is the variable that stores the
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

    return amount

if __name__ == '__main__':
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount. Your current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Here the total bet is equal to ${total_bet}")
