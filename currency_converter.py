
def currency_converter(amount, from_currency, to_currency):
    if amount > 0:
        conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
        }

        values = conversion_rate[from_currency]
        rate = values[to_currency]

        conversion = amount * rate
        return conversion
    return 0.0

# Submit only this file currency_converter.py with the completed function.
# Do not add additional code for calling the function, or code to get user input.