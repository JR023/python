set sql_safe_updates =0;
-- Create 3 dojos
SELECT * FROM dojos_and_ninjas.dojos;
insert into dojos (name) values('Red Dojo');
insert into dojos (name) values('Black Dojo');
insert into dojos (name) values ('White Dojo');
SELECT * FROM dojos_and_ninjas.dojos;
-- Delete dojos
delete from dojos;
-- Create 3 new dojos
insert into dojos (name) values ('Green Dojo');
insert into dojos (name) values ('Yellow Dojo');
insert into dojos (name) values ('Pink Dojo');
SELECT * FROM dojos_and_ninjas.dojos;
-- Create 3 new ninjas in first dojo
SELECT * FROM dojos_and_ninjas.ninjas;
insert into ninjas (first_name, last_name, age, dojo_id) values ('Jordan', 'Romero', 10, 31);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Tyler', 'Gali', 22, 31);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Taylor', 'Swift', 22, 31);
SELECT * FROM ninjas;
-- create 3 new ninjas in second dojo
SELECT * FROM ninjas;
insert into ninjas (first_name, last_name, age, dojo_id) values ('Bob', 'Marley', 23, 32);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Michael', 'Jordan', 22, 32);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Stephen', 'Curry', 26, 32);
-- create 3 new ninjas in third dojo
select * from ninjas;
insert into ninjas (first_name, last_name, age, dojo_id) values ('Bobby', 'Khaems', 24, 33);
insert into ninjas (first_name, last_name, age, dojo_id) values ('Draymond', 'Green', 28, 33);
insert into ninjas (first_name, last_name, age, dojo_id) values ('John', 'Smith', 34, 33);
select *from ninjas;
-- retrieve ninjas from first dojo
select name, first_name, last_name, age from dojos
JOIN ninjas on ninjas.dojo_id = dojos.id where dojos.id=31;
-- retrieve ninjas from last dojo
select name, first_name, last_name, age from dojos
JOIN ninjas on ninjas.dojo_id = dojos.id where dojos.id=33;
-- retrieve last ninja dojo
select name, first_name, last_name, age from dojos
JOIN ninjas on ninjas.dojo_id = dojos.id 
order by ninjas.id desc limit 1;