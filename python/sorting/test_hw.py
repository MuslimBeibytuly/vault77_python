from hw import apply_transactions

def test_apply_transactions():
    balance = {'user1': 100, 'user2': 500}
    transactions = [
        {'user1': -10}, 
        {'user2': -20}, 
        {'user1': 50}, 
        {'user2': -20}, 
        {'user2': -100}
    ]
    result = apply_transactions(
        balance=balance,
        transactions=transactions
    )
    expected = {'user1': 140, 'user2': 360}
    assert result == expected