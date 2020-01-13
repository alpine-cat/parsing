import lxml.html as html
import requests


def get_all_links(pages:int, domain):
    links = list()
    for i in range(1, pages+1):
        current_domain = domain + '/page/%s' % i
        response = requests.get(current_domain)
        page = html.fromstring(response.content)
        links += page.xpath("//div[@id='main_columns']/article/a/@href")

    return links


def get_page_info(link):
    response = requests.get(link)
    page = html.fromstring(response.content)

    return {
        'title': page.xpath("//div[contains(@class, 'post-title')]/h1/text()"),
        'body': page.xpath("//div[@itemprop='articleBody']//text()"),
        'images': page.xpath("//img/@src"),
        'datePublished': page.xpath("//time[@itemprop='datePublished']/text()")
    }


def run():
    main_domain = 'https://tproger.ru/'
    links = get_all_links(3, main_domain)
    for x in links:
        info = get_page_info(x)
        print('\n')
        print(x+'\n')
        for k in info:
            print(k, info.get(k))


if __name__ == '__main__':
    run()
