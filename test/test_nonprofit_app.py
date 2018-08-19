import responses

from nonprofit_app import nonprofit_config, collect_html_content, collect_needs_from_html


def test_nonprofit_config_keys():
    for config in nonprofit_config:
        assert all(key in config for key in ('name', 'host', 'need_endpoint', 'css_selector'))


@responses.activate
def test_collect_html_content():
    sample_url = 'https://www.example.com/mostneededfoods'

    responses.add(responses.GET, sample_url,
                  body='<h1>captured html</h1>', status=200)

    html_content = collect_html_content(sample_url)
    assert html_content == '<h1>captured html</h1>'


def test_collect_needs_from_html():
    sample_html = """<div id="colTwoContent"><ul>
    <li>Canned tuna, chicken or salmon</li>
    <li>Peanut butter</li>
    <li>Meals in a can (soup, stew, chili)</li>
    <li>Low-sodium canned vegetables</li>
    <li>Canned fruit in its own juice or water</li>
    <li>Olive or canola oil</li>
    <li>Spices (cinnamon, chili powder, cumin, salt-free spice blends)</li>
    <li>Canned foods with pop-top lids</li>
    <li>Low-sugar whole grain cereals</li>
    <li>Healthy snacks (granola bars, nuts, dried fruit)</li>
    </ul>
    </div>
    """

    css_selector = 'div#colTwoContent li'

    collected_needs = collect_needs_from_html(sample_html, css_selector)
    assert len(collected_needs) == 10
    assert collected_needs[0] == 'Canned tuna, chicken or salmon'




