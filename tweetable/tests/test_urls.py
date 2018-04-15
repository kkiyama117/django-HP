import pytest

from django.urls import Resolver404, resolve

urls: str = 'tweetable.urls'


@pytest.mark.tweetable
@pytest.mark.tweetable_urls
@pytest.mark.urls(urls)
class TestUrl(object):
    pass

# @pytest.mark.parametrize(('url', 'expected'), [
#     ('/', {'func_name': 'TemplateView', 'kwargs': {}}),
#     ('/tweets/api/',
#      {'func_name': 'HelloView', 'kwargs': {'user_id': '0000-0000'}}),
# ])
# def test_valid(self, url, expected):
#     func, args, kwargs = resolve(url)
#     assert func.__name__ == expected['func_name']
#     for k, v in expected['kwargs'].items():
#         assert kwargs[k] == v

# @pytest.mark.parametrize(('url',), [
#     # ('/api/',),
#     ('/api/statues/',),
# ])
# def test_invalid(self, url):
#     u"""404 になるケース"""
#     with pytest.raises(Resolver404):
#         func, args, kwargs = resolve(url)
