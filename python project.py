currencies = {
    'USD': {'EUR': 0.88, 'GBP': 0.76, 'JPY': 114.74, 'AUD': 1.48},
    'EUR': {'USD': 1.13, 'GBP': 0.86, 'JPY': 130.26, 'AUD': 1.67},
    'GBP': {'USD': 1.32, 'EUR': 1.16, 'JPY': 151.45, 'AUD': 1.94},
    'JPY': {'USD': 0.0087, 'EUR': 0.0077, 'GBP': 0.0066, 'AUD': 0.013},
    'AUD': {'USD': 0.68, 'EUR': 0.6, 'GBP': 0.52, 'JPY': 76.87},
}

def convert_currency(from_currency, to_currency, amount):
    if from_currency in currencies and to_currency in currencies[from_currency]:
        rate = currencies[from_currency][to_currency]
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

def main():
    print("Currency Converter")
    print("Available currencies: USD, EUR, GBP, JPY, AUD")
    
    from_currency = input("From currency: ").strip().upper()
    to_currency = input("To currency: ").strip().upper()
    
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    
    result = convert_currency(from_currency, to_currency, amount)
    
    if result is not None:
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    else:
         print("Invalid currency selected.")

if _name_ == "_main_":
    main()'''

