
-- SELECT id, title, created_at, updated_at,
-- CASE 
-- 	WHEN box_office > 300000000 THEN "Less_Than" 
--     WHEN box_office < 1000000000 THEN "Greater_Than"
-- END AS box_office
-- FROM movies
-- ORDER BY box_office

select title as "Movie Title" from movies;


SELECT *,
CASE 
    WHEN box_office > 300000000 THEN "Less_Than" 
    WHEN box_office < 1000000000 THEN "Greater_Than"
END AS box_office_checker
FROM movies
ORDER BY box_office;



SELECT 
id, title, box_office, CAST(number1 + 0.99 AS FLOAT) as float_number1, number2, 
table_1.number1*table_1.number2 as "Inflated Box Office Price" FROM (
SELECT `movies`.`id`,
    `movies`.`title`,
    movies.box_office,
    `movies`.`box_office` as number1,
	ceiling(movies.box_office - 7000000) as number2,
    `movies`.`created_at`,
    `movies`.`updated_at`,
    `movies`.`director_id`
FROM `directors_movies`.`movies`) AS table_1;



select directors_movies.title FROM (
select movies.title, directors.first_name from movies
left join directors on directors.id = movies.director_id) as directors_movies;


select * from directors;

