from __future__ import annotations
from typing import List
from converter import EXCHANGE_RATES, available_currencies, convert_multiple

def get_amount() -> float:
    # Prompt user for a valid positive amount
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return amount
        except ValueError:
            print("Invalid amount. Please enter a positive number.")

def get_currency(label: str, currencies: tuple[str, ...]) -> str:
    # prompt user to enter a valid currency code
    while True:
        currency = input(f"{label} currency {currencies}: ").upper().strip()
        if currency not in currencies:
            print("Invalid currency. Try again.")
        else:
            return currency

def get_target_currencies(currencies: tuple[str, ...], source_currency: str) -> List[str]:
    # Prompt user to enter multiple target currencies separated by commas
    while True:
        raw = input("Enter target currencies separated by commas (Example: EUR, CAD, GBP): ").upper().strip()
        targets = [c.strip() for c in raw.split(",") if c.strip()]

        # Remove duplicates
        targets = list(dict.fromkeys(targets))

        if not targets:
            print("Please enter at least one currency.")
            continue

        # Validate currencies
        invalid = [c for c in targets if c not in currencies]
        if invalid:
            print(f"Invalid currencies: {invalid}. Allowed currencies: {currencies}")
            continue

        # Prevent same currency conversion
        targets = [c for c in targets if c != source_currency]
        if not targets:
            print("Target currencies must be different from source currency.")
            continue

        return targets

def print_history(history: List[str]) -> None:
    # Print session conversion history
    print("\nConversion history [Current session]:")
    print("-" * 40)

    if not history:
        print("No conversions history.")
        return

    for i, record in enumerate(history, start = 1):
        print(f"{i}. {record}")

def main():
    currencies = available_currencies(EXCHANGE_RATES)
    history: List[str] = []

    print("Currency Converter")
    print(f"Available currencies: {currencies}")

    while True:
        amount = get_amount()
        source = get_currency("Source", currencies)
        targets = get_target_currencies(currencies, source)

        results = convert_multiple(amount, source, targets, EXCHANGE_RATES)

        print("Conversion Results")
        print("-" * 40)
        for currency, value in results.items():
            record = f"{amount:.2f} {source} is equal to {value:.2f} {currency}"
            print(record)

            # Save history
            history.append(record)

        # Continue?
        again = input("Would you like to convert again? [y/n]: ").lower().strip()
        if again != "y":
            break

    # Print history
    print_history(history)
    print("Thank you for using the currency converter.")

if __name__ == "__main__":
    main()
