# Basic Join

### Population Census 

```mysql
SELECT SUM(CITY.POPULATION) 
FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'ASIA';
```



### African Cities

```mysql
SELECT CITY.NAME
FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE CONTINENT = 'Africa';
```



### Average Population of Each Continent

```mysql
SELECT COUNTRY.CONTINENT, TRUNCATE(AVG(CITY.POPULATION),0)
FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;
```

- TRUNCATE(숫자, 버릴자리수)



### The Report

>GRADE 8 이상만 이름, 아래는 NULL로 변경
>
>성적 오름차순 정렬, 같으면 이름순

```mysql
SELECT IF(GRADE<8, NULL, NAME) AS 'NAME', GRADE, MARKS
FROM STUDENTS JOIN GRADES
WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC, NAME;
```

- COLUMN 겹치는게 없어서 그냥 사용해도 된다.



### Top Competitors

```mysql
```



### Ollivander's Inventory

```mysql

```



### Challenges

```mysql

```