def test_import():
    import cli  # type: ignore
    assert hasattr(cli, "main")
