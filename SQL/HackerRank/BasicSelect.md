# Basic Select

### Revising the Select Query I

```mysql
SELECT * FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION > 100000;
```



### Revising the Select Query II

```mysql
SELECT NAME FROM CITY
WHERE COUNTRYCODE='USA' AND POPULATION > 120000;
```



### Select All

```mysql
SELECT * FROM CITY;
```



### Select By ID

```mysql
SELECT * FROM CITY
WHERE ID=1661;
```



###  Japanese Cities' Attributes

```mysql
SELECT * FROM CITY
WHERE COUNTRYCODE='JPN';
```



###  Japanese Cities' Names

```mysql
SELECT NAME FROM CITY
WHERE COUNTRYCODE='JPN';
```



### Weather Observation Station 1

```mysql
SELECT CITY, STATE FROM STATION;
```



### Weather Observation Station 3

```mysql
SELECT DISTINCT CITY FROM STATION
WHERE ID%2 = 0;
```



### Weather Observation Station 4

```mysql
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) AS COUNT
FROM STATION;
```



### Weather Observation Station 5

```mysql
(
    SELECT CONCAT(CITY,' ',LENGTH(CITY)) FROM STATION
	ORDER BY LENGTH(CITY),CITY
	LIMIT 1
)
UNION
(
    SELECT CONCAT(CITY,' ',LENGTH(CITY)) FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
    LIMIT 1
)
```



### Weather Observation Station 6

```mysql
SELECT DISTINCT CITY FROM STATION
WHERE CITY LIKE 'a%'
OR CITY LIKE 'e%'
OR CITY LIKE 'i%'
OR CITY LIKE 'o%'
OR CITY LIKE 'u%';
```

```mysql
SELECT DISTINCT CITY FROM STATION
WHERE LEFT(CITY,1) IN ('a','e','i','o','u');
```



