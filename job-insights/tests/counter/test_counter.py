from src.pre_built.counter import count_ocurrences


def test_counter():
    lower_case = count_ocurrences('data/jobs.csv', 'python')
    upper_case = count_ocurrences('data/jobs.csv', 'PYTHON')
    all_case = count_ocurrences('data/jobs.csv', 'PyThOn')
    assert lower_case == 1639
    assert upper_case == 1639
    assert all_case == 1639
