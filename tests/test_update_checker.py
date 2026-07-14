from study.update_checker import is_newer_version, version_tuple


def test_version_tuple_accepts_v_prefix():
    assert version_tuple("v1.2.3") == (1, 2, 3)


def test_newer_version_is_detected():
    assert is_newer_version("v1.2.0") is True


def test_same_version_is_not_newer():
    assert is_newer_version("v1.1.0") is False


def test_older_version_is_not_newer():
    assert is_newer_version("v1.0.9") is False
