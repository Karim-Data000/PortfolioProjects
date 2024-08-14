/*

 Views created for tableau visualizations of the covid project 

*/


-- View 1

CREATE VIEW view_Death_Percentage_Globally AS 
select sum(new_cases) as total_cases, sum(new_deaths) as total_deaths, (sum(new_deaths) / sum(new_cases))*100 as DeathPercentage
from portofolioproject.coviddeaths
where continent is not NULL;


-------------------------------------------------------
-- View 2
-- BREAKING THINGS DOWN BY CONTINENT
-- Showing contintents with the highest death count per population
-- Using CTE (common table expression) to solve this problem.
-- the problem : get the total number of deaths for each continent

CREATE VIEW view_death_count_by_continent AS
with DeathCountByCountry as (
    select location,continent, max(total_deaths) as HighestDeathCountByCountry
from portofolioproject.coviddeaths
where  continent is not NULL
GROUP BY location, continent
order by HighestDeathCountByCountry DESC
)
select continent, sum(HighestDeathCountByCountry) as HighestDeathCountByContinent from DeathCountByCountry
GROUP BY continent
order by HighestDeathCountByContinent desc;



-------------------------------------------------------
-- View 3

-- Countries with highest infection rate compared to population
CREATE VIEW view_Percent_Population_Infected_by_country as
select location, population, max(total_cases) as HighestInfectionCount, max(total_cases / population)*100 as PercentPopulationInfected
from portofolioproject.coviddeaths
where continent is not null
GROUP BY location, population
order by PercentPopulationInfected DESC;


-------------------------------------------------------
-- View 4

-- Countries with highest infection rate compared to population
CREATE VIEW view_rolling_Percent_Population_Infected_daily as
select location, population, date, max(total_cases) as HighestInfectionCount, max(total_cases / population)*100 as PercentPopulationInfected
from portofolioproject.coviddeaths
where continent is not null
GROUP BY location, population, DATE
order by PercentPopulationInfected DESC;


-------------------------------------------------------
-- View 5

create view view_Rolling_People_Vaccinated_daily as
Select dea.continent, dea.location, dea.date, dea.population
, MAX(vac.people_fully_vaccinated) as RollingPeopleVaccinated
-- , (RollingPeopleVaccinated/population)*100
From CovidDeaths dea
Join CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
where dea.continent is not null 
group by dea.continent, dea.location, dea.date, dea.population
order by 1,2,3;


-------------------------------------------------------
-- View 6

create view view_rolling_percent_population_vaccinated_daily as 
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
from PopvsVac;






