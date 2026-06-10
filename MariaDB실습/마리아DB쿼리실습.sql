# MariaDB

/*
MariaDB에서 새로운 데이터베이스와 계정 생성하기 
: 오라클에서는 계정만 생성하면 되지만 MySQL(MariaDB)에서는 
새로운 DB와 User(사용자계정)을 동시에 생성한 후 권한설정을 해야한다. 
*/ 
 
## 아래 작업은 root 계정으로 접속한 후 실행해야 한다. ## 

# DB와 user 동시에 생성> mysql DB에서 root로 로그인한 후 실행
# 1.새로운 데이더 베이스 생성
CREATE DATABASE sample_db;
#2. 새로운 계정 생성 (로컬만 접척할 수 있는 계정)
CREATE USER 'sample_user'@'localhost' IDENTIFIED BY '1234';
# 사용할 권한을 부여한다
GRANT ALL PRIVILEGES ON sample_db.* TO 'sample_user'@'localhost';
# 확인한다
FLUSH PRIVILEGES;

/*실행방법(3) F9, F9+ctrl, F9+ ctrl+Shift */

/*
실행방법
F9 : 현재 문서의 전체 쿼리문을 실행한다. 
Ctrl + F9 : 블럭으로 지정한 쿼리문만 실행한다. 
	만약 쿼리문의 절반 정도만 선택한 후 실행하면 에러가 발생된다. 
Ctrl + Shift + F9 : 현재 쿼리를 실행한다. 단 마지막에 작성한
	세미콜론 안으로 커서를 옮긴 후 실행해야한다. 
*/

## 여기부터는 sample_user 계정으로 접속한 후 작성해주세요. ##

/*
AUTO_INCREMENT
	: 자동증가 컬럼으로 지정한다. 1씩 증가하는 순차적인 정수값이
	자동으로 입력된다. 오라클의 sequence(시퀀스)와 동일한 역할을
	한다. 
UNSIGNED
	: 정수형 컬럼으로 지정하는 경우 음수는 사용하지 않고, 양수의 
	범위만 사용한다. 이때 양의 범위가 2배로 늘어나게된다. 
*/


SELECT * FROM board;

SELECT * FROM books;

SELECT * FROM guestbook;

CREATE TABLE tb_int(
	#일련번호
	idx INT PRIMARY KEY AUTO_INCREMENT,
	#원래 -127~ 127 unsdigned경우 0~ 256
	num1 tinyint UNSIGNED NOT NULL,
	num2 SMALLINT NOT NULL,
	num3 MEDIUMINT DEFAULT '100',
	num4 BIGINT,
	
	fnum1 FLOAT(10,5) not null,
	fnum2 DOUBLE(20,10)
	
);
DESC tb_int;


INSERT INTO tb_int values
	(9, 123, 12345, 1234567, 1234567890,
	12345.12345, 1234567890.1234567890);
SELECT * FROM tb_int;


CREATE TABLE tb_date(
	idx INT PRIMARY KEY AUTO_INCREMENT,
	
	DATE1 DATE NOT NULL,
	DATE2 DATETIME DEFAULT current_timestamp
);
DESC tb_date;

INSERT INTO tb_date (DATE1, DATE2) values
('2023-04-22', NOW());

INSERT INTO tb_date (DATE1) VALUES ('2023-04-23');
select * FROM tb_date;

CREATE TABLE TB_STRING (
	IDX INT PRIMARY KEY AUTO_INCREMENT,
	
	STR1 VARCHAR(30) NOT NULL,
	STR2 TEXT
);
DESC TB_STRING;

INSERT INTO TB_STRING (STR1, STR2) VALUES
	('난 짧은글', '나는 엄청난 긴글이다');
#INSERT INTO TB_STRING (STR1, STR2) VALUES
#	('난 짧은글1', '나는 엄청난 긴글이다1');	
SELECT * FROM TB_STRING;
SELECT * FROM TB_STRING WHERE IDX=1;
SELECT * FROM TB_STRING WHERE IDX=1 STR1='난 짧은글';	
SELECT * FROM TB_STRING WHERE IDX=1 STR1 LIKE '%짧은%';

CREATE TABLE TB_SPEC(
	IDX INT AUTO_INCREMENT,
	SPEC1 ENUM('M', 'W', 'T'),
	SPEC2 SET('A','B','C','D'),
	PRIMARY KEY(IDX)
);
DESC TB_SPEC;

INSERT INTO tb_spec (spec1, spec2) VALUES ('W', 'A,B,C');
INSERT INTO tb_spec (spec1, spec2) VALUES 
	('X', 'A,B,C'); #에러발생
INSERT INTO tb_spec (spec1, spec2) VALUES 
	('W', 'X,B,C'); #에러발생 

SELECT * FROM tb_spec;	


CREATE TABLE board(
	num INT NOT NULL auto_increment,
	title VARCHAR(200) NOT NULL,
	content  TEXT  NOT NULL,
	id VARCHAR (20) NOT NULL,
	postdate DATETIME DEFAULT CURRENT_TIMESTAMP,
	visitcount MEDIUMINT,
	PRIMARY KEY (num)
);

INSERT INTO board (title, content, id, visitcount) VALUES
('안녕하세요, 첫 방문입니다!', '가입 인사드립니다. 앞으로 자주 소통해요.', 'user01', 5),
('공지사항 필독 부탁드립니다.', '게시판 이용 규칙 및 권장 사항 안내입니다.', 'admin', 120),
('오늘 점심 메뉴 추천받아요', '날씨도 꿀꿀한데 뜨끈한 국물이 당기네요. 추천 부탁드립니다.', 'foodie_99', 24),
('최신 IT 트렌드 공유', '인공지능과 데이터 분석 시장의 최근 변화에 대한 글입니다.', 'tech_dev', 42),
('주말에 가볼 만한 곳 추천', '가족들과 함께 가기 좋은 근교 드라이브 코스 공유합니다.', 'traveler', 15);

SELECT * FROM board;

CREATE TABLE phonebook
(
	idx INT NOT NULL AUTO_INCREMENT,
	name VARCHAR (30) NOT NULL,
   phone VARCHAR (20) NOT NULL,
   addr VARCHAR (50),
   PRIMARY KEY (idx)
   );
	