from lib.account_repository import *

"""
When we call AccountRepository#all
We get a list of Account objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = AccountRepository(db_connection) 

    accounts = repository.all()

    # Assert on the results
    assert accounts == [
        Account(1, 'ann_person@email.com', 'ann_person' ),
        Account(2, 'john_doe@fakemail.com', 'john_doe'),
    ]

"""
When we call AccountRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = AccountRepository(db_connection)

    repository.create(Account(None, "tom.test@gmail.com", "tom_test"))

    accounts = repository.all()

    # Assert on the results
    assert accounts == [
        Account(1, 'ann_person@email.com', 'ann_person' ),
        Account(2, 'john_doe@fakemail.com', 'john_doe'),
        Account(3, "tom.test@gmail.com", "tom_test"),
    ]

"""
When we call AccountRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_media.sql")
    repository = AccountRepository(db_connection)
    repository.delete(2)

    result = repository.all()
    assert result == [
        Account(1, 'ann_person@email.com', 'ann_person' ),]
