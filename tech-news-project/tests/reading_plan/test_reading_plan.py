import pytest
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
# from unittest.mock import MagicMock
# from .mock_news import mock_news


mock_find_news_return = [
    {
        "title": "Antivírus Android: conheça os 10 melhores!",
        "reading_time": 10,
    },
    {
        "title": "Angular CLI: como usar a interface de linha de comando",
        "reading_time": 7,
    },
    {
        "title": "Operadores booleanos: 3 exemplos para usar em pesquisas",
        "reading_time": 4,
    },
    {
        "title": "O que é array, para que serve e como fazer?",
        "reading_time": 5,
    },
    {
        "title": "Usabilidade no Desenvolvimento de software e UX",
        "reading_time": 11,
    },
    {
        "title": "Conheça os 11 tipos de firewall e saiba qual usar",
        "reading_time": 8,
    },
    {
        "title": "Programação em Arduino para iniciantes em 11 passos!",
        "reading_time": 14,
    },
    {
        "title": "5 exemplos de algoritmos na vida real e na computação",
        "reading_time": 5,
    },
    {
        "title": "Next JS: o que é, para que serve e por que usar?",
        "reading_time": 13,
    },
]

mock_result_ten_min = {
    "readable": [
        {
            "unfilled_time": 0,
            "chosen_news": [
                ("Antivírus Android: conheça os 10 melhores!", 10)
            ],
        },
        {
            "unfilled_time": 3,
            "chosen_news": [
                ("Angular CLI: como usar a interface de linha de comando", 7)
            ],
        },
        {
            "unfilled_time": 1,
            "chosen_news": [
                ("Operadores booleanos: 3 exemplos para usar em pesquisas", 4),
                ("O que é array, para que serve e como fazer?", 5),
            ],
        },
        {
            "unfilled_time": 2,
            "chosen_news": [
                ("Conheça os 11 tipos de firewall e saiba qual usar", 8)
            ],
        },
        {
            "unfilled_time": 5,
            "chosen_news": [
                ("5 exemplos de algoritmos na vida real e na computação", 5)
            ],
        },
    ],
    "unreadable": [
        ("Usabilidade no Desenvolvimento de software e UX", 11),
        ("Programação em Arduino para iniciantes em 11 passos!", 14),
        ("Next JS: o que é, para que serve e por que usar?", 13),
    ],
}


def test_reading_plan_group_news(mocker):
    mocker.patch(
        "tech_news.analyzer.reading_plan.find_news",
        return_value=mock_find_news_return,
    )

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(0)

    assert (
        ReadingPlanService.group_news_for_available_time(10)
        == mock_result_ten_min
    )