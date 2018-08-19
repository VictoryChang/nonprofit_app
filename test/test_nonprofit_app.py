import responses

from nonprofit_app import nonprofit_config, collect_html_content


def test_nonprofit_config_keys():
    for config in nonprofit_config:
        assert all(key in config for key in ('name', 'host', 'need_endpoint'))


@responses.activate
def test_collect_html_content():
    sample_url = 'https://www.example.com/mostneededfoods'

    responses.add(responses.GET, sample_url,
                  body='<h1>captured html</h1>', status=200)

    html_content = collect_html_content(sample_url)
    assert html_content == '<h1>captured html</h1>'
