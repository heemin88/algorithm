-- animal_ins : 동물 보호소에 들어온 동물의 정보, animal_outs : 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름 조회
SELECT animal_ins.animal_id ,animal_ins.name from animal_outs,animal_ins where animal_ins.animal_id = animal_outs.animal_id and animal_ins.datetime >animal_outs.datetime order by animal_ins.datetime