# 要求三
### 1. 在 `member` 資料表中新增 5 筆資料。
* 先新增一筆 `username` 和 `password` 欄位都是 test 的資料。
  * 指令：
    ```sql
    INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');
    ```
  * 指令執行畫面：
    ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(1).JPG)
* 接著新增 4 筆隨意的資料
  * 指令：
    ```sql
    INSERT INTO member(name, username, password) VALUES('ben', 'benn', 'nneb');
    INSERT INTO member(name, username, password) VALUES('carl', 'carll', 'llrac');
    INSERT INTO member(name, username, password) VALUES('daisy', 'daisyy', 'yysiad');
    INSERT INTO member(name, username, password) VALUES('emma', 'emmaa', 'aamme');
    ```
  * 指令執行畫面：
    ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(2).JPG)
### 2. 取得所有在 `member` 資料表中的會員資料。
* 指令：
  ```sql
  SELECT * FROM member;
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(3).JPG)
### 3. 取得所有在 `member` 資料表中的會員資料，並按照 `time` 欄位，由近到遠排序。
* 指令：
  ```sql
  SELECT * FROM member ORDER BY time DESC;
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(4).JPG)
### 4. 取得 `member` 資料表中第 2 到第 4 筆共三筆資料，並按照 `time` 欄位，由近到遠排序。
* 指令：
  ```sql
  SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(5).JPG)
### 5. 取得欄位 `username` 是 test 的會員資料。
* 指令：
  ```sql
  SELECT * FROM member WHERE username='test';
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(6).JPG)
### 6. 取得欄位 `username` 是 test 且欄位 `password` 也是 test 的資料。
* 指令：
  ```sql
  SELECT * FROM member WHERE username='test' and password='test';
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(7).JPG)
### 7. 更新欄位 `username` 是 test 的會員資料，將資料中的 `name` 欄位改成 test2。
* 指令：
  ```sql
  UPDATE member SET name='test2' WHERE username='test';
  
  --用SELECT指令檢查更新的結果
  SELECT * FROM member;  
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(8).JPG)
# 要求四
### 0. 更新 `member` 資料表中，所有會員 `follower_count` 欄位的值
* 更新後的資料表：
   ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/4%20(1).JPG)
### 1. 取得 `member` 資料表中，總共有幾筆資料、所有會員 `follower_count` 欄位的總和與的平均數。
* 指令：
  ```sql
  SELECT COUNT(*) AS 總共有幾位會員, SUM(follower_count) AS 追蹤人數總和, AVG(follower_count) AS 追蹤人數平均
  FROM member;
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/4%20(2).JPG)
# 要求五
### 1. 在資料庫中，建立新資料表紀錄留⾔資訊
* 指令：
  ```sql
  CREATE TABLE message(
   id BIGINT PRIMARY KEY AUTO_INCREMENT,
   member_id BIGINT NOT NULL,
   content VARCHAR(255) NOT NULL,
   like_count INT UNSIGNED NOT NULL DEFAULT 0,
   time DATETIME NOT NULL DEFAULT NOW(),
   FOREIGN KEY(member_id) REFERENCES member(id)
  );
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/5%20(1).JPG)
### 2. 取得所有留⾔，結果須包含留⾔者的姓名
* 指令：
  ```sql
  SELECT message.id, message.member_id, member.name, message.content, message.like_count, message.time FROM message INNER JOIN member ON message.member_id=member.id;
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/5%20(5).JPG)
### 3. 取得 `member` 資料表中欄位 `username` 是 test 的所有留⾔，資料中須包含留⾔者的姓名。
* 指令：
  ```sql
  SELECT message.id, message.member_id, member.name, message.content, message.like_count, message.time FROM message INNER JOIN member ON message.member_id=member.id and member.username='test';
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/5%20(6).JPG)
### 4. 取得 `member` 資料表中欄位 `username` 是 test 的所有留⾔平均按讚數。
* 指令：
  ```sql
  SELECT AVG(like_count) AS test留言的平均按讚數 FROM message INNER JOIN member ON message.member_id=member.id and member.username='test';
  ```
* 指令執行畫面：
  ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/5%20(7).JPG)
