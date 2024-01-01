def pytest_configure():
    from addok import hooks
    import addok_es
    hooks.register(addok_es)
