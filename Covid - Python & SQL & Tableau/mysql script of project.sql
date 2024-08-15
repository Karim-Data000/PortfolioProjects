/*
Covid 19 Data Exploration 

Skills used: Joins, CTE's, Temp Tables, Windows Functions, Aggregate Functions, Creating Views, Converting Data Types

*/

use portofolioproject;
select * from portofolioproject.coviddeaths 
where continent is not null
order by 3, 4;
-- Select data we are starting with.

select location, date, total_cases, new_cases, total_deaths, population
from portofolioproject.coviddeaths
where continent is not null
order by 1, 2;

-- Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country

select location, date, total_cases, total_deaths, (total_deaths / total_cases)*100 as DeathPercentage
from portofolioproject.coviddeaths
where location like 'Egypt'
order by 1, 2;

-- Total Cases vs Population
-- Shows what percentage of population infected with Covid

select location, date, population, total_cases, (total_cases / population)*100 as PercentPopulationInfected
from portofolioproject.coviddeaths
where location like 'Egypt'
order by 1, 2;

-- Countries with highest infection rate compared to population

select location, population, max(total_cases) as HighestInfectionCount, max(total_cases / population)*100 as PercentPopulationInfected
from portofolioproject.coviddeaths
GROUP BY location, population
order by PercentPopulationInfected DESC;

-- Countries with highest Death Count per population

select location, max(total_deaths) as HighestDeathCount, max(total_deaths / population)*100 as PercentPopulationDied
from portofolioproject.coviddeaths
where continent is not null
GROUP BY location
order by HighestDeathCount DESC;

---------------------------------
-- BREAKING THINGS DOWN BY CONTINENT
-- Showing contintents with the highest death count per population
-- Using CTE (common table expression) to solve this problem.
-- the problem : get the total number of deaths for each continent

with DeathCountByCountry as (
    select location,continent, max(total_deaths) as HighestDeathCountByCountry, max(total_deaths / population)*100 as PercentPopulationDied
from portofolioproject.coviddeaths
where  continent is not NULL
GROUP BY location, continent
order by HighestDeathCountByCountry DESC
)
select continent, sum(HighestDeathCountByCountry) as HighestDeathCountByContinent from DeathCountByCountry
GROUP BY continent
order by HighestDeathCountByContinent desc;

-- same as the query above but contain unwanted records like world and High-income countries records

-- Showing contintents with the highest death count per population

select location, max(total_deaths) as HighestDeathCount, max(total_deaths / population)*100 as PercentPopulationDied
from portofolioproject.coviddeaths
where continent is null
GROUP BY location
order by HighestDeathCount DESC;

-- There are many countries in each continent so be careful, using max function will only get you highest deaths
-- of a single country in the continent

select location,continent, max(total_deaths) as HighestDeathCount, max(total_deaths / population)*100 as PercentPopulationDied
from portofolioproject.coviddeaths
where  continent ='North America'
GROUP BY location, continent
order by HighestDeathCount DESC;

-----------------------------------
-- Global Numbers

select sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths) / sum(new_cases))*100 as DeathPercentage
from portofolioproject.coviddeaths
where continent is not NULL;

-- this result give same results as above query
select sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths) / sum(new_cases))*100 as DeathPercentage
from portofolioproject.coviddeaths
where location = 'World';

--------------------------

select count(*) from covidvaccinations;

select count(*) from coviddeaths;

select * from coviddeaths 
NATURAL join covidvaccinations;

select * from coviddeaths dea 
join covidvaccinations vac
    on dea.`date` = vac.`date`
    and dea.location = vac.location;


-- Total Population vs Vaccinations
-- Show percentage of population who have received at least one Covid Vaccine

select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
sum(vac.new_vaccinations) OVER (PARTITION BY location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
from coviddeaths dea 
join covidvaccinations vac
    on dea.`date` = vac.`date`
    and dea.location = vac.location
where dea.continent is not null
order by 2, 3
limit 1000;

-- Using CTE to perform Percent Calculation on Partition By in previous query

with PopvsVac as (
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
sum(vac.new_people_vaccinated_smoothed) OVER (PARTITION BY location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
from coviddeaths dea 
join covidvaccinations vac
    on dea.`date` = vac.`date`
    and dea.location = vac.location
where dea.continent is not null
-- order by 2, 3
-- limit 1000;
)
select *, ((RollingPeopleVaccinated / population) * 100) as PercentPopulationVaccinated
from PopvsVac
limit 100000;


-- Using Temporary table to perform Percent Calculation on Partition By in previous query

drop TABLE if EXISTS PercentPopulationVaccinated;
create TEMPORARY TABLE PercentPopulationVaccinated 
select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
sum(vac.new_vaccinations) OVER (PARTITION BY location ORDER BY dea.location, dea.date) as RollingPeopleVaccinated
from coviddeaths dea 
join covidvaccinations vac
    on dea.`date` = vac.`date`
    and dea.location = vac.location
where dea.continent is not null;
-- order by 2, 3
-- limit 1000;

select *, ((RollingPeopleVaccinated / population) * 100) as RollingPercentPopulationVaccinated
from PercentPopulationVaccinated
limit 1000;


-- Creating View to store data for later visualizations

Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations,
SUM(vac.new_vaccinations) OVER (Partition by dea.Location Order by dea.location, dea.Date) as RollingPeopleVaccinated
From CovidDeaths dea
Join CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null;


SELECT * from percentpopulationvaccinated;