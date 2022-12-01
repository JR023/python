-- Queries
-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)
select  world.countries.name as name, world.languages.language as language, world.languages.percentage from world.languages
join world.countries on world.languages.country_id = world.countries.id
where world.languages.language ="Slovene"
order by world.languages.percentage desc;

-- 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
select countries.name as name, count(cities.name) as cities from cities
join countries on cities.country_id = countries.id
group by countries.name
order by cities desc;
-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

select cities.name, cities.population, country_id from cities
join countries on cities.country_id = countries.id
where countries.name = "Mexico" and cities.population >500000
order by cities.population desc;
-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
select countries.name as country_name, langauges.language as language_name, languages.percentage from languages
left join countries on languages.country_id = countries.id
where languages.percentage > 89
order by languages.percentage desc;
-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
select countries.name, countries.surface_area, countries.population from countries
where countries.surface_area < 501 and countries.population >100000;
-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
select countries.name, countries.government_form, countries.capital, countries.life_expectancy from countries
where countries.government_form = "Constitutional Monarchy" and countries.capital >200 and countries.life_expectancy >75;
-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
select countries.name as country_name, cities.name as city_name, cities.district, cities.population from cities
join countries on countries.id = cities.country_id
where countries.name = "Argentina" and cities.district = "Buenos Aires" and cities.population >500000;
-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
select countries.region, count(countries.name) as countries from countries
group by countries.region
order by countries desc;