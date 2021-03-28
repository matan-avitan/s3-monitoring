import os


def try_get_env(key, not_found_key):
    """
    Try to get environment key - if not found use the conf file
    """
    return os.environ[key] if key in os.environ else not_found_key
