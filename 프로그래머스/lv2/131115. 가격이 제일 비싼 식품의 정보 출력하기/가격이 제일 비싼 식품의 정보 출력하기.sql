-- 코드를 입력하세요
#select max(price) from food_product
SELECT * from food_product where price = (select max(price) from food_product)