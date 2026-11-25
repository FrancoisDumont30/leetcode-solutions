import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:


    df = students.merge(subjects, how='cross')

    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')

    df = df.merge(exam_counts, on=['student_id', 'subject_name'], how='left')
    df = df[['student_id','student_name','subject_name', 'attended_exams']]
    df['attended_exams'] = df['attended_exams'].fillna(0)

    return df.sort_values(['student_id', 'subject_name'])
