select
max(earning),count(employee_id)

from (
    select employee_id,(salary*months) as earning from Employee
    -- group by earning,employee_id
    -- order by earning desc
) as st
group by st.earning
order by st.earning desc
limit 1