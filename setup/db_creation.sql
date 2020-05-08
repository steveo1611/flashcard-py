-- for creating the db schema

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
