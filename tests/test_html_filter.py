from source.html_filter import HTMLFilter


def test_html_filter():
    HTMLFilter_instance = HTMLFilter(('div', 'second'))
    HTMLFilter_instance.feed('<div class="test"><span itemprop="description"><div class="first second"><h1>My First Heading<p>Banino</p></h1></div><p>My first <br/><br/>paragraph.</p></span></div>')
    actual = HTMLFilter_instance.get_data()
    expected = '<h1>My First Heading<p>Banino</p></h1>'
    assert expected in actual, f'Assertion Failed, actual = {actual}, expected = {expected}'


def test_html_filter_2():
    HTMLFilter_instance = HTMLFilter(('div', 'test'))
    HTMLFilter_instance.feed('<div class="test"><span itemprop="description"><h1>My First Heading</h1><p>My first <br/><br/>paragraph.</p></span></div>')
    actual = HTMLFilter_instance.get_data()
    expected = '<span itemprop="description"><h1>My First Heading</h1><p>My first <br/><br/>paragraph.</p></span>'
    assert expected in actual, f'Assertion Failed, actual = {actual}, expected = {expected}'


def test_save_to_file():

    HTMLFilter_instance = HTMLFilter(('div', 'test'))
    HTMLFilter_instance.feed('<div class="test"><span itemprop="description"><h1>My First Heading</h1><p>My first <br/><br/>paragraph.</p></span></div>')
    HTMLFilter_instance.save_data()
    assert True