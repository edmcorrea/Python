from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    # A função abre o arquivo e ler seu conteúdo
    with open(path, encoding="utf-8") as file:
        # A função trata o arquivo como CSV
        # E ela retorna uma lista de dicionarios, onde
        # as chaves são cabecalhos de coluna e os valores são as linhas
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(jobs_reader)


def get_unique_job_types(path: str) -> List[str]:
    # A função invoca a função "read" usando o path recebido para obter dados
    jobsDecoded = read(path)
    # A função deve retornar uma lista
    # de valores únicos presentes na coluna "job_type"
    jobs = set()
    for job in jobsDecoded:
        jobs.add(job['job_type'])
    print(jobs)
    return jobs


# A função retorna uma lista com todos os empregos
# onde a coluna "job_type" corresponde ao parâmetro "job_type"
def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_list = [elem for elem in jobs if elem["job_type"] == job_type]
    return filtered_list
