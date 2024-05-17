from main import delete_spaces


def test_smthing():
    actual_result = delete_spaces("Welcome to New York")
    expected_result = "toNewYork"
    assert actual_result == expected_result
