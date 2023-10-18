from typing import Union, List, Dict
from src.insights.jobs import read


# A função funciona similar a função "get_unique_job_types" no file "./jobs"
def get_max_salary(path: str) -> int:
    salaries = filter_salary(path, "max_salary")
    return max(salaries)


# A função funciona similar a função "get_unique_job_types" no file "./jobs"
def get_min_salary(path: str) -> int:
    salaries = filter_salary(path, "min_salary")
    return min(salaries)


def filter_salary(path: str, search: str) -> List[int]:
    jobs_decoded = read(path)
    salaries = set()
    for job in jobs_decoded:
        if job[search] != '' and job[search] != 'invalid':
            salaries.add(int(job[search]))
    return salaries


# PRIMEIRO PARAMETRO
# A função recebe um dicionário "job" com as chaves "min_salary" e "max_salary"
# que podem ser números ou strings que representem números.
# SEGUNDO PARAMETRO
# A função recebe um número ou string que represente o número "salary"
def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("'max_salary' or 'min_salary' does Not Exist")
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        if min > max:
            raise ValueError("'min_salary' can't be bigger than 'max_salary'")
        # A func retorna "True" se o salário estiver dentro da faixa salarial
        # ou "False" se não estiver.
        return min <= int(salary) <= max
    except TypeError:
        raise ValueError('some input is not a number')


# PRIMEIRO PARAMETRO
# A função recebe uma lista de dicionários "jobs".
# SEGUNDO PARAMETRO
# A função recebe um número ou string que represente o número "salary"
def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    match_jobs = []
    for job in jobs:
        try:
            bool = matches_salary_range(job, salary)
            if bool:
                match_jobs.append(job)
        except Exception as exp:
            print(exp)
    # A função retorna uma lista com todos os empregos
    # onde o salário "salary" está entre
    # os valores da coluna "min_salary" e max_salary".
    return match_jobs
