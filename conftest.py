"""Pytest のフック
"""
import subprocess


def pytest_unconfigure(config):
    """pytest の実行時に一度だけ実行される

    """
    print('subprocess')
    print('manage.py check')
    subprocess.run(['python', '-Wd', 'manage.py', 'check'], shell=True)
    print('subprocess done')
