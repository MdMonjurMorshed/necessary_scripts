/*
Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

There are a total of [occupation_count] [occupation]s.
where [occupation_count] is the number of occurrences of an occupation in OCCUPATIONS and [occupation] is the lowercase occupation name. If more than one Occupation has the same [occupation_count], they should be ordered alphabetically.
*/

select 
concat(Name,'(',left(Occupation,1),')') as Name
-- case


 -- when Occupation = 'Actor' Then concat(Name,'(A)')
 -- when Occupation = 'Doctor' Then concat(Name,'(D)')
 -- when Occupation = 'Singer' Then concat(Name,'(S)')
 -- when Occupation = 'Professor' Then concat(Name,'(P)')
-- end as Name
 
from OCCUPATIONS

union all

select 
concat('There are a total of',' ',st.oc,' ',lower(st.Occupation),'s.')
from(select Occupation,count(*) as oc
    from OCCUPATIONS
    group by Occupation
   ) as st 
order by Name 