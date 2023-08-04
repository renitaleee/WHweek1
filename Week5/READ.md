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
    ![image](https://github.com/ysirene/WeHelpAssignment/blob/main/Week5/pic/3%20(1).JPG)
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
