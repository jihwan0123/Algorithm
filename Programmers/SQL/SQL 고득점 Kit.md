## SQL 고득점 Kit

## SELECT

### 모든 레코드 조회하기

```mysql
SELECT * FROM ANIMAL_INS 
ORDER_BY ANIMAL_ID
```



### 역순 정렬하기

```mysql
SELECT NAME, DATETIM
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC
```



### 아픈 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
```



### 어린 동물 찾기

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
```



### 동물의 아이디와 이름

```mysql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```



### 여러 기준으로 정렬하기

```mysql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```



### 상위 n개 레코드

```mysql
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```



## SUM, MAX, MIN

### 최댓값 구하기

```mysql
SELECT MAX(DATETIME) AS 시간
FROM ANIMAL_INS;
```



### 최솟값 구하기

```mysql
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS;
```



### 중복 제거하기

```mysql
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
```



## GROUP BY

### 고양이와 개는 몇마리 있을까

```mysql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```



### 동명 동물 수 찾기

```mysql
SELECT NAME, COUNT(NAME) AS 'COUNT'
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```



### 입양 시각 구하기1

```mysql
SELECT HOUR(DATETIME) AS 'HOUR', COUNT(HOUR(DATETIME)) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME);
```



### 입양 시각 구하기2

```mysql
```



## IS NULL

### 이름이 없는 동물의 아이디

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL;
```



### 이름이 있는 동물의 아이디

```mysql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL;
```



### NULL 처리하기

```mysql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```





## JOIN

### 없어진 기록 찾기

```mysql
SELECT OUTS.ANIMAL_ID, OUTS.NAME
FROM ANIMAL_INS INS
RIGHT JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL
```



### 있었는데요 없었습니다.

```mysql
SELECT INS.ANIMAL_ID, INS.NAME
FROM ANIMAL_INS INS INNER JOIN ANIMAL_OUTS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID AND INS.DATETIME > OUTS.DATETIME
ORDER BY INS.DATETIME
```



### 오랜 기간 보호한 동물(1)

```mysql
```



### 보호소에서 중성화한 동물

```mysql
```



## String, Date

### 루시와 엘라 찾기

```mysql

```



### 이름에 el이 들어가는 동물 찾기

```mysql

```



### 중성화 여부 파악하기

```mysql

```



### 오랜 기간 보호한 동물(2)

```mysql
```



### DATETIME에서 DATE로 형 변환

```mysql

```
