--# Write your MySQL query statement below
select v.customer_id, count(*) as count_no_trans
from Visits as v
left join Transactions as t on t.visit_id = v.visit_id
where t.transaction_id is null
group by v.customer_id