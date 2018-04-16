import pytest
from django.urls import resolve, Resolver404

urls: str = 'account.urls'


@pytest.mark.tweetable
@pytest.mark.tweetable_urls
@pytest.mark.urls(urls)
class TestUrls(object):
    @pytest.mark.parametrize(('url', 'expected'), [
        ('/', {'func_name': 'index', 'kwargs': {}}),
        ('/profile/', {'func_name': 'profile', 'kwargs': {}}),
    ])
    def test_valid(self, url, expected):
        func, args, kwargs = resolve(url)
        assert func.__name__ == expected['func_name']
        for k, v in expected['kwargs'].items():
            assert kwargs[k] == v

    @pytest.mark.parametrize(('url',), [
        # ('/api/',),
        ('/api/statues/',),
    ])
    def test_invalid(self, url):
        """404 になるケース"""
        with pytest.raises(Resolver404):
            func, args, kwargs = resolve(url)
