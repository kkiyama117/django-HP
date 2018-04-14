from environ import environ


def get_data_from_env(filename="production"):
    env = environ.Env()
    env_base = environ.Path(__file__) - 2
    env_file = str(env_base.path("{}{}".format(".env/", filename)))
    env.read_env(env_file)
    return env
