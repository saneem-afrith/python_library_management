use book_db;
create table book_details(
			id int primary key auto_increment,
            book_name varchar(100),
            author_name varchar(40),
            price int,
            type varchar(100),
            published_year date
            
);