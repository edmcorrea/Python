from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    jobsDecoded = read(path)
    jobs = set()
    for job in jobsDecoded:
        jobs.add(job['job_type'])
    print(jobs)
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_list = [elem for elem in jobs if elem["job_type"] == job_type]
    return filtered_list
