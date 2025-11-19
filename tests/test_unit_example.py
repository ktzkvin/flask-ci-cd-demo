from app.app import count_items

def test_count_items():
    assert count_items(["a","b"]) == 2