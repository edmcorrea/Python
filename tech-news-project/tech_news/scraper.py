import time
import requests
from parsel import Selector
from tech_news.database import create_news


# 1
def fetch(url):
    # A função deve respeitar um Rate Limit de 1 requisição por segundo.
    time.sleep(1)
    try:
        # A função faz uma requisição HTTP para o parâmetro (url) de entrada.
        response = requests.get(
            url,
            # O header "user-agent" é usado para que a raspagem funcione certo.
            headers={"user-agent": "Fake user-agent"},
            # O "timeout" é o tempo de espera da Requisição (3 segundos).
            timeout=3
        )
 
        if response.status_code == 200:
            return response.text

    # O "timeout" abandona a Requisição caso não receba resposta.
    except requests.ReadTimeout:
        return None

    return None


# 2
def scrape_updates(html_content):
    # O "Selector" importado do "parsel" é responsável por extrair os textos
    selector = Selector(text=html_content)
    # Utilizado o ".css" para buscar um atributo específico
    # Utilizado o ".getall()" para trazer todos
    titles = selector.css('.entry-title a::attr(href)').getall()
    return titles


# 3
def scrape_next_page_link(html_content):
    # Mesma lógica do #2
    selector = Selector(html_content)
    # Pega o hiperlink da página seguinte
    # ".get()" pega o primeiro elemento
    nxt_page = selector.css("a.next::attr(href)").get()
    return nxt_page


# 4
def scrape_news(html_content):
    selector = Selector(html_content)
    # Mesma lógica do #2
    url = selector.css('link[rel="canonical"]::attr(href)').get()

    title = selector.css('h1.entry-title::text').get().strip()
    timestamp = selector.css('li.meta-date::text').get()
    writer = selector.css('span.author > a::text').get()
    reading_time = selector.css('li.meta-reading-time::text').get().split()
    summary = ''.join(
        selector.css('.entry-content > p:first-of-type *::text').getall()
    ).strip()
    category = selector.css('span.label::text').get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time[0]),
        "summary": summary,
        "category": category,
    }


# 5
def get_tech_news(amount):
    url_base = 'https://blog.betrybe.com/'
    all_news = []
    # print('NEWS', url_base)
    while len(all_news) < amount:
        response = fetch(url_base)
        titles = scrape_updates(response)
        url_base = scrape_next_page_link(response)

        for new in titles:
            if len(all_news) < amount:
                data = scrape_news(fetch(new))
                all_news.append(data)

    create_news(all_news)
    return all_news
