DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;
DROP TABLE IF EXISTS accounts;
DROP SEQUENCE IF EXISTS accounts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    email_address VARCHAR(255),
    username VARCHAR(255)
    );

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    views INT,
    account_id INT,
    CONSTRAINT fk_account FOREIGN KEY (account_id)
    references accounts(id)
    on delete cascade
    );

-- accounts table entries
INSERT INTO accounts (email_address, username) VALUES ('ann_person@email.com', 'ann_person' );
INSERT INTO accounts (email_address, username) VALUES ('john_doe@fakemail.com', 'john_doe');

-- posts table entries
INSERT INTO posts (title, content, views, account_id) VALUES ('Title I', 'content alpha', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title II', 'content bravo', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title III', 'content charlie', 0, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title IV', 'content delta', 0, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title V', 'content echo', 0, 1);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title VII', 'content foxtrot', 0, 2);
INSERT INTO posts (title, content, views, account_id) VALUES ('Title VIII', 'content golf', 0, 1);