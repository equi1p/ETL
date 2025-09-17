import pandas as pd

def transform(data):
    data = data.rename(columns = {'fNAME':'first_name',
                                  'lNAME':'second_name',
                                   'Age':'age',
                                   'country':'country_born',
                                   'entryEXAM':'result_exam',
                                   'prevEducation':'education',
                                   'studyHOURS':'study_hours',
                                   'Python':'python_score',
                                   'DB':'DB_score'})
    
    data = data.dropna()
    data = data.drop_duplicates()
    
    data.gender = data.gender.apply(lambda x: 'F' if x.startswith('F') or x.startswith('f') else 'M')
    data.residence = data.residence.apply(lambda x: 'BI_Residence' if x.startswith('BI') else x)
    data.country_born = data.country_born.apply(lambda x: 'Norway' if x.startswith('No') or x.startswith('no') else x )
    data.python_score = data.python_score.apply(int)
    
    data.education = data.education.replace({'HighSchool': 'High School',
                                             'diploma':'Diploma',
                                             'Diplomaaa': 'Diploma',
                                             'DIPLOMA':'Diploma',
                                             'Barrrchelors': 'Bachelors'})
    return data