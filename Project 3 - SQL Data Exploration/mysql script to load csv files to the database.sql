use PortofolioProject;
show tables;
select count(*) from covidvaccinations;
select * from covidvaccinations;

-- Remember, before you execute this script, make sure the csv file doesn't contain blank cell, 
-- replace blank cells with NULL instead, and for last column, replace blank cells with zero. that worked. don't ask me why. hahahaha smile.

-- Also, remember to reformat date field to be in mysql accepted format yyyy-mm-dd

LOAD DATA INFILE "F:\\Library\\Engineering\\computer science\\Data Science\\portfolio projects\\Project 4 - SQL Data Exploration - part 1\\datasets\\CovidVaccinationCleaned.csv" 
INTO TABLE covidvaccinations
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
ignore 1 lines;