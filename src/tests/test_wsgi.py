def test_wsgi():
    import {{ project_name }}.wsgi.development
    import {{ project_name }}.wsgi.docker
