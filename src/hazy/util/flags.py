import os

def should_open_browser():
    return bool(os.environ.get('HAZY_OPEN_BROWSER', False))

def is_testing():
    return bool(os.environ.get('HAZY_TESTING', False))
