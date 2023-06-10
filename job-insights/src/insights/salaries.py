from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    salaries = filter_salary(path, "max_salary")
    return max(salaries)
    

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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("'max_salary' or 'min_salary' does Not Exist")
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        if min > max:
            raise ValueError("'min_salary' can't be bigger than 'max_salary'")
        return min <= int(salary) <= max
    except TypeError:
        raise ValueError('some input is not a number')


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    match_jobs = []
    for job in jobs:
        try:
            min = int(job["min_salary"])
            max = int(job["max_salary"])
            bool = min <= int(salary) <= max
            if bool:
                match_jobs.append(job)
        except Exception as exp:
            print(exp)
    return match_jobs

