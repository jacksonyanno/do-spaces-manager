import os

def file_get_contents(filename):
    try:
        with open(filename) as f:
            return f.read()
    except:
        return ""

def env_get_contents(env_name, default="", cast=str):
    content = None
    if (env_name + '_FILE') in os.environ:
        content = file_get_contents(os.environ.get(env_name + '_FILE'))
    elif (env_name) in os.environ:
        content = os.environ.get(env_name)
    else:
        content = default
    if cast == bool:
        return str(content).lower() != 'false'
    return cast(content)
