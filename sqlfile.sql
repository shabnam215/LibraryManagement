create database library;
use library;
create table student
(
ID int,
NAME varchar(50),
COURSE varchar(100),
CONTACTNUMBER varchar(20)
);
drop  table student;
create table student
(
ID int,
SNAME varchar(50),
COURSE varchar(100),
CONTACTNUMBER varchar(20)
);
create table teacher
(
ID int,
TNAME varchar(50),
TQUAL varchar(100),
TCONTACT varchar(30)
);
drop table teacher;
create table teacher
(
ID int PRIMARY KEY,
TNAME varchar(50),
TQUAL varchar(100),
TCONTACT varchar(30)
);
create table book
(
BID int PRIMARY KEY,
BNAME VARCHAR(100),
BSUB VARCHAR(100),
BPUB VARCHAR(100),
BAUT VARCHAR(100),
BPRICE VARCHAR(100)
);
select * from student;
create table issuereturn
(
BOOKID int,
BORRID int,
ISSUEDATE date,
RETURNDATE date,
CATEGORY varchar(50),
STAT varchar(50),
fine int
);
select * from issuereturn;
select curdate();
alter table issuereturn add column ACTUALRETURNDATE date after RETURNDATE;
select * from issuereturn;
alter table issuereturn add column EXPECTEDRETURNDATE date after ISSUEDATE;
desc issuereturn;
set sql_safe_updates=0;
delete from issuereturn where expectedreturndate is null;
create table admin
(
login int,
pass varchar(100)
);
alter table admin modify login varchar(40);
insert into admin (login,pass) values('root','root');
alter table admin rename column pass to passwords;

