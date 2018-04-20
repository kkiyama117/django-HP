import os

from environ import environ


# for django-environ
def get_data_from_env(filename):
    env = environ.Env()
    env_base = environ.Path(__file__) - 2
    env_file = str(env_base.path("{}{}".format(".env/", filename)))
    env.read_env(env_file)
    return env


def env_file_setting():
    env_name = os.environ.get("DJANGO_SETTINGS_MODULE","")
    if "staging" in env_name:
        return get_data_from_env("staging")
    elif "production" in env_name:
        return get_data_from_env("production")
    elif "test" in env_name:
        return get_data_from_env("test")
    else:
        return get_data_from_env("local")
