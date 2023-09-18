-- 코드를 입력하세요
#select * from online_sale order by USER_ID ASC,PRODUCT_ID DESC
SELECT USER_ID , PRODUCT_ID from online_sale group by user_id,product_id having count(*)>=2 order by USER_ID ASC,PRODUCT_ID DESC