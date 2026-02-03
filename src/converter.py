from __future__ import annotations
from typing import List, Dict, Tuple

EXCHANGE_RATES: Dict[str, Dict[str, float]] = {
        "USD": {"EUR": 0.85, "CAD": 1.25, "GBP": 0.73, "INR": 83.10, "JPY": 147.20, "AUD": 1.53},
        "EUR": {"USD": 1.18, "CAD": 1.47, "GBP": 0.86, "INR": 97.80, "JPY": 173.00, "AUD": 1.80},
        "CAD": {"USD": 0.80, "EUR": 0.68, "GBP": 0.59, "INR": 66.40, "JPY": 117.70, "AUD": 1.23},
        "GBP": {"USD": 1.37, "EUR": 1.16, "CAD": 1.70, "INR": 114.00, "JPY": 201.20, "AUD": 2.10},
        "INR": {"USD": 0.012, "EUR": 0.010, "CAD": 0.015, "GBP": 0.0088, "JPY": 1.77, "AUD": 0.018},
        "JPY": {"USD": 0.0068, "EUR": 0.0058, "CAD": 0.0085, "GBP": 0.0050, "INR": 0.56, "AUD": 0.010},
        "AUD": {"USD": 0.65, "EUR": 0.56, "CAD": 0.81, "GBP": 0.48, "INR": 55.00, "JPY": 98.00},
    }

def available_currencies(rates: Dict[str, Dict[str, float]] = EXCHANGE_RATES) -> Tuple[str, ...]:
    # Return list of supported currencies
    return tuple(rates.keys())

def validate_currency(currency: str, rates: Dict[str, Dict[str, float]] = EXCHANGE_RATES) -> bool:
    # Check if currency exists in supported list
    return currency in rates

def convert(amount: float, source: str, target: str, rates: Dict[str, Dict[str, float]] = EXCHANGE_RATES) -> float:
    # Convert amount from source currency to target currency using fixed exchange rates.
    # Raises ValueError for invalid currencies
    if amount <= 0:
        raise ValueError("Amount must be positive")

    if source not in rates:
        raise ValueError(f"Unsupported source currency: {source}")

    if target not in rates:
        raise ValueError(f"Unsupported target currency: {target}")

    if source == target:
        return amount

    return amount * rates[source][target]

def convert_multiple(amount: float, source: str, targets: str, rates: Dict[str, Dict[str, float]] = EXCHANGE_RATES) -> Dict[str, float]:
    # Convert amount from source to multiple target currencies
    # Returns dict like: {"EUR": 85.0, "CAD": 125.0}
    results: Dict[str, float] = {}
    for t in targets:
        if t != source:
            results[t] = convert(amount, source, t, rates)

    return results
