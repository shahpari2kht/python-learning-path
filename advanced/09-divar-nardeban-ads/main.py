import requests
from bs4 import BeautifulSoup

def has_nardeban_tag(post):
    # تگ 'نردبان' معمولاً یک span یا div با متن یا کلاس خاص است (نیاز به آشنایی با ساختار دیوار)
    tag = post.find(lambda tag:
                    tag.name in ['span', 'div'] and
                    ('نردبان' in tag.get_text()))
    return tag is not None

def main():
    url = 'https://divar.ir/s/tehran'
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    posts = soup.find_all('div', class_='post-card-item')

    found = False
    for post in posts:
        if has_nardeban_tag(post):
            title_tag = post.find('span', attrs={"class": "kt-post-card__title"})
            title = title_tag.text.strip() if title_tag else '[بدون عنوان]'
            print(title)
            found = True
    if not found:
        print('هیچ آگهی دارای تگ نردبان یافت نشد.')

if __name__ == '__main__':
    main()
