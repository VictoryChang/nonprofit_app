
from bs4 import BeautifulSoup
from flask import Flask, render_template
app = Flask(__name__)

import requests


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', nonprofits=nonprofits, food_list=food_list)


nonprofits = [
    {
        'name': 'Second Harvest Food Bank',
        'host': 'https://www.shfb.org/',
        'need_endpoint': '/mostneededfoods',
        'css_selector': 'div#colTwoContent li'
    }
]

food_items = {}

def collect_html_content(url):
    """
    Collect the html context for a specific url
    :param url: [str] Url of source to be extracted
    """
    response = requests.get(url)
    assert response.status_code == 200
    return response.text


def collect_needs_from_html(html_content, css_selector):
    """
    Collect a list of items from html text block via a css-selector
    :param html_content: [str] Block of html text
    :param css_selector: [str] Corresponding CSS selector
    """
    beautiful_soup = BeautifulSoup(html_content, 'html.parser')
    elements = beautiful_soup.select(css_selector)
    return [element.get_text() for element in elements]


if __name__ == '__main__':
    test_data = nonprofits[0]
    name = test_data['name']
    host = test_data['host']
    endpoint = test_data['need_endpoint']
    html_content = collect_html_content(host + endpoint)
    print(html_content)

    css_selector = test_data['css_selector']
    food_list = collect_needs_from_html(html_content, css_selector)

    print(food_list)

    app.run(debug=True)
