def pytest_addoption(parser):
    parser.addoption("--url", action="store")
    parser.addoption("--token", action="store")
    parser.addoption("--space", action="store")
    parser.addoption("--parent", action="store")

def pytest_generate_tests(metafunc):
    url_value = metafunc.config.option.url
    if 'url' in metafunc.fixturenames and url_value is not None:
        metafunc.parametrize("url", [url_value])

    token_value = metafunc.config.option.token
    if 'token' in metafunc.fixturenames and token_value is not None:
        metafunc.parametrize("token", [token_value])

    space_value = metafunc.config.option.space
    if 'space' in metafunc.fixturenames and space_value is not None:
        metafunc.parametrize("space", [space_value])
    
    parent_value = metafunc.config.option.parent
    if 'parent' in metafunc.fixturenames and parent_value is not None:
        metafunc.parametrize("parent", [parent_value])
