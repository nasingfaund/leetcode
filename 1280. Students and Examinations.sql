select student.student_id, student.student_name, subject.subject_name, count(exam.subject_name) as attended_exams
FROM Students as student
         cross JOIN Subjects as subject
         left join Examinations as exam
                   on student.student_id = exam.student_id and subject.subject_name = exam.subject_name
group by student.student_id, student_name, subject.subject_name
order by student_id, subject_name;
