select 
student_id as user_id, 
unix_timestamp(update_time) as submit_time, 
question_id,
five as skill_id, 
right_or_wrong as answer_result,
(end_time - start_time) as duration,
answer as student_answer
from answer_question_detail;

select 
question_id,
difficulty,
stem as question_content
from question_info;

select
lk_id as skill_id,
lk_name as skill_name
from knowledge_structure;