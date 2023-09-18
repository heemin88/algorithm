-- 상반기 주문 정보 - first_half , 아이스크림 성분 - icecream_info
-- 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문 량 (총 주문량이 작은 순서대로)
SELECT ingredient_type, sum(total_order) as total_order from icecream_info,first_half where icecream_info.flavor = first_half.flavor group by ingredient_type 