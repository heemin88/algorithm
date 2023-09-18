 -- 동물 보호소에 가장 먼저 들어온 동물
#select * from animal_ins
SELECT min(DATETIME) as 시간 from animal_ins