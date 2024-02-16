from lib.account import *

class AccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts')
        return [Account(row["id"],
                        row["email_address"],
                        row["username"])
                        for row in rows]

    def create(self, account):
        self._connection.execute('INSERT INTO accounts (email_address, username) VALUES (%s, %s)', [
                                 account.email_address, account.username])
        return None

    def delete(self, account_id):
        self._connection.execute(
            'DELETE FROM accounts WHERE id = %s', [account_id])
        return None