select contest_id,round(count(user_id)*100/(select count(user_id) from Users),2) as percentage from Register as r
#left join Register as r
#on u.user_id=r.user_id
group by contest_id
order by percentage desc, contest_id asc