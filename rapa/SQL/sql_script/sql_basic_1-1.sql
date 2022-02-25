CREATE TABLE users_t(id INTEGER PRIMARY KEY,
username TEXT, email TEXT, phone TEXT,
website TEXT, regdate TEXT)

CREATE TABLE users_t2(id INTEGER PRIMARY KEY,
username TEXT, email TEXT, phone TEXT,
website TEXT, regdate TEXT)

DROP TABLE users_t2 ;

insert into users_t(id, username, email, phone, website, regdate) values(1, 'kim', 'kim@cozlab.com', '010-1234-5678','cozlab.com','20201024');
insert into users_t values(2, 'lee', 'lee@naver.com', '010-1234-5678','naver.com','20201024');
insert into users_t values(3, 'hwang', 'hwang@cozlab.com', '010-2356-0978','cozlab.com','20201024');
insert into users_t values(4, 'oh', 'oh@naver.com', '010-1234-5678','naver.com','20201024');

SELECT * from users_t ut where username='oh';
SELECT * from users_t ut;
SELECT username, phone from users_t ut ;

update users_t set email ='kim@google.com', phone ='010-2356-3245'
WHERE id=1;

DELETE FROM users_t WHERE id=3;
DELETE FROM users_t ;

DROP table users_t ;

CREATE table post(id integer not null primary key, 
title text not null, content text not null);

CREATE table usersd(id integer not null primary key,
username text not null, phone text not null, address text not null
);
drop table usersd;
-- 데이터 추가
INSERT into post(id, title, content) values(1, 'java','객체지향 언어');
INSERT into post(id, title, content) values(2, 'html','웹 표준 언어');
INSERT into post(id, title, content) values(3, 'javascript','잘하면 좋겠네');
INSERT into post(id, title, content) values(4, 'django','풀스텍 개발 프레임워크');
INSERT into post(id, title, content) values(5, '코딩','재미있어요!');

SELECT count(*) cnt from post;

SELECT * from post where title like '%java%';

SELECT * from post where title like '%코%';

-- post 테이블에서 content 끝부분이 '~언어'인 레코드 조회
SELECT * from post where content like '%언어';

insert into usersd (id, username , phone, address) values(1, 'kim', '010-1111-1111','seoul');
insert into usersd (id, username, phone, address) values(2, 'lee', '010-2111-1111','daegu');
insert into usersd (id, username, phone, address) values(3, 'song', '010-3111-1111','pusan');
insert into usersd (id, username, phone, address) values(4, 'park', '010-4111-1111','newyork');
insert into usersd (id, username, phone, address) values(5, 'lee', '010-5111-1111','jeju');

SELECT * from post order by title asc;
SELECT * from usersd u order by address desc;














