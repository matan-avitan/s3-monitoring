import os


def try_get_env(key, not_found_key):
    return os.environ[key] if key in os.environ else not_found_key
