# Currency Converter (Python)

A **Currency Converter** project built with Python.

It supports:
- Convert to **multiple currencies at once**
- Expanded list of currencies (USD, EUR, CAD, GBP, INR, JPY, AUD)
- Keeps **conversion history** during the session
- Unit tests using **pytest**

## 📌 Features

✅ Multi-currency conversion in one run  
✅ Session conversion history  
✅ Input validation  
✅ Testable modular code structure  

## 🚀 Run the app

```bash
python src/app.py
```

## 🧪 Run tests

Install dependencies:
```bash
pip install -r requirements.txt
```
Run tests:
```bash
pytest -v
```

## 📝 Example
Input:
```bash
Enter amount to convert: 100
Source currency ('USD', 'EUR', 'CAD', 'GBP', 'INR', 'JPY', 'AUD'): USD
Enter target currencies separated by commas: EUR,CAD,GBP
Output:

100.00 USD = 85.00 EUR
100.00 USD = 125.00 CAD
100.00 USD = 73.00 GBP
```

## 📄 License

MIT
