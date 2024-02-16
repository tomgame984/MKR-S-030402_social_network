# Two Tables Design Recipe | Social Network

## 1. Extract nouns from the user stories

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

```
```
Nouns:
account, email address, username
posts, title, content, user_id, views
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record    | Properties                     |
| --------- | ------------------------------ |
| account   | email address, username        |
| posts     | title, content, user_id, views |

1. TABLE ONE: `accounts` 

    Column names: `email address`, `username`

2. TABLE TWO: `posts` 

    Column names: `title`, `content`, `user_id`, `views`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
table one: accounts
id: SERIAL PRIMARY KEY,
email_address: VARCHAR(255),
username: VARCHAR(255),

table two: posts
id: SERIAL PRIMARY KEY,
title: VARCHAR(255)
content: VARCHAR(255)
views: INT

```

## 4. The Tables Relationship

1. **ACCOUNTS** have many **POSTS**.
2. **POSTS** belong to **ACCOUNTS**.
3. Foreign key is in the table **POSTS**.


## 5. Write the SQL

```sql
-- file: social_network.sql

-- Table without the foreign key:
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255),
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
    id: SERIAL PRIMARY KEY,
    title: VARCHAR(255)
    content: VARCHAR(255)
    views: INT
-- The foreign key name is always {other_table_singular}_id
    account_id INT,
    CONSTRAINT fk_account FOREIGN KEY (account_id)
    references accounts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
createdb -h 127.0.0.1 -U tomgame social_network
```