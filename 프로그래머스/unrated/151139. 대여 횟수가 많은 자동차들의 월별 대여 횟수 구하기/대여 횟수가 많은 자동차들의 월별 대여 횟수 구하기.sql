-- 코드를 입력하세요
#select * from CAR_RENTAL_COMPANY_RENTAL_HISTORY group by car_id
# id에 각 월마다 대여 횟수
SELECT month(start_date) as month, car_id, count(month(start_date)) as records from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in 
(select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE start_date BETWEEN "2022-08-01 00:00:00" AND "2022-10-31 23:59:59"
 group by car_id having count(*)>=5 )
 and start_date BETWEEN "2022-08-01 00:00:00" AND "2022-10-31 23:59:59"
 group by month(start_date),car_id 
 having count(*) >0
 order by month(start_date) asc, car_id desc 



# select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where month(start_date)=8 or month(start_date)=9 or month(start_date)=10 group by car_id having count(*)>=5
