def apply_transactions(balance: dict, transactions: list) -> dict:
    for transaction in transactions:
        for k, v in transaction.items():
            print(f'k is: {k}')
            print(f'balance[k] before is: {balance[k]}')
            balance[k] += v
            print(f'balance[k] after is: {balance[k]}')
    return balance
