import requests

nonprofit_config = [
    {
        'name': 'Second Harvest Food Bank',
        'host': 'https://www.shfb.org/',
        'need_endpoint': '/mostneededfoods'
    }
]


def collect_html_content(url):
    """
    Collect the html context for a specific url
    :param url: [str] Url of source to be extracted
    """
    response = requests.get(url)
    assert response.status_code == 200
    return response.text


if __name__ == '__main__':
    test_data = nonprofit_config[0]
    host = test_data['host']
    endpoint = test_data['need_endpoint']
    content = collect_html_content(host + endpoint)
    print(content)