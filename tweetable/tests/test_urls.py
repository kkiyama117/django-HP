import pytest

from django.urls import Resolver404, resolve

urls: str = 'tweetable.urls'


@pytest.mark.tweetable
@pytest.mark.tweetable_urls
@pytest.mark.urls(urls)
class TestUrl:
    @pytest.mark.parametrize(('url', 'expected'), [
        ('/api/users/', {'func_name': 'UserViewSet', 'kwargs': {}}),
        ('/api/statuses/',
         {'func_name': 'TweetViewSet', 'kwargs': {}}),
        # {'func_name': 'TweetViewSet', 'kwargs': {'user_id': '0000-0000'}}),
    ])
    def test_valid(self, url, expected):
        func, args, kwargs = resolve(url)
        assert func.__name__ == expected['func_name']
        for k, v in expected['kwargs'].items():
            assert kwargs[k] == v

# @pytest.mark.parametrize(('url',), [
#     # ('/api/',),
#     ('/api/statues/',),
# ])
# def test_invalid(self, url):
#     u"""404 になるケース"""
#     with pytest.raises(Resolver404):
#         func, args, kwargs = resolve(url)
