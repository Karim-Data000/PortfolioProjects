
-- Remember, before you execute this script, make sure the csv file doesn't contain blank cell.

-- for text columns, replace blank cells with 'NULL'. For numeric column, replace blank cells with zero.
-- Also, remember to reformat date field to be in mysql accepted format yyyy-mm-dd

use sqlcleaningproject;
show tables;
select count(*) from nashvillehousing;
select * from nashvillehousing;


LOAD DATA INFILE "F:\\Library\\Engineering\\computer science\\Data Science\\portfolio projects\\Data Cleaning in SQL\\Nashville Housing Data - Cleaned for sql.csv" 
INTO TABLE nashvillehousing
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
ignore 1 lines;