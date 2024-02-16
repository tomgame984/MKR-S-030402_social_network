from lib.account import *

"""
Account constructs with an id, email_address and username
"""
def test_account_constructs():
    account = Account(1, "test@test.com", "test_test")
    assert account.id == 1
    assert account.email_address == "test@test.com"
    assert account.username == "test_test"

def test_account_formats():
    account = Account(1, "test@test.com", "test_test")
    assert str(account) == 'Account(1, test@test.com, test_test)'