use ml_cia2;
create table USER_PSWD(
   user_name varchar(30) NOT NULL,
   passwords varchar(10)
   );

insert into USER_PSWD (user_name,passwords) values
('Sam_15','snubatch25'),
('Muthu_26','Topper@snu'),
('Raveesh_05','trivandrum'),
('Raaghav09','guitar!'),
('Surya_04','weeknd_op'),
('Shreya003','blahblah'),
('Akshay10','bablooo'),
('Aneesha1','aprilfool'),
('Nandy11','nonsense'),
('Smruthi21','Padips101'),
('Adithi28','abcdefgh'),
('Vatsan1','Terror');
delete from USER_PSWD where user_name='Sam_15';
