-- for creating the db schema
/*
USE mysql;
CREATE DATABASE IF NOT EXISTS flashcards DEFAULT CHARACTER SET utf8 ;

USE flashcards;
DROP TABLE IF EXISTS flashcards.Cards;

-- Create the table in the specified schema
CREATE TABLE IF NOT EXISTS flashcards.Cards
(
    CardId INT NOT NULL AUTO_INCREMENT, -- primary key column
    mainsubject NVARCHAR(50) NOT NULL,
    catagory NVARCHAR(50) NOT NULL,
    question NVARCHAR(200) NOT NULL,
    answer NVARCHAR(200) NOT NULL,
    additional_info NVARCHAR(200),
    PRIMARY KEY (CardId)
    -- specify more columns here
);
*/

/*  -- for adding test cards
USE flashcards;
INSERT INTO cards(mainsubject, catagory, question, answer, additional_info) 
VALUES
    ('aws', 's3', 'testq1', 'testa1', 'http://test'),
    ('aws', 's3', 'testq2', 'testa2', 'http://test2'),
    ('aws', 's3', 'testq3', 'testa3', 'http://test3'),
    ('aws', 's3', 'testq4', 'testa4', 'http://test4'),
    ('aws', 's3', 'testq5', 'testa5', 'http://test5'),
    ('aws', 's3', 'testq6', 'testa6', 'http://test6'),
    ('aws', 's3', 'testq7', 'testa7', 'http://test7'),
    ('aws', 's3', 'testq8', 'testa8', 'http://test8'),
    ('aws', 's3', 'testq9', 'testa9', 'http://test9'),
    ('aws', 's3', 'testq10', 'testa10', 'http://test10'),
    ('aws', 's3', 'testq11', 'testa11', 'http://test11'),
    ('aws', 's3', 'testq12', 'testa12', 'http://test12');

*/