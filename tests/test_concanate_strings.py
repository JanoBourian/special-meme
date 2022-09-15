from concatenate_strings import concatenate_strings

def test_concanate_happy_path():
    items = ["     hello", 5, "martin   ", "@  "]
    assert concatenate_strings(items) == "hello 5 martin    @"

def test_concatenate_all_types():
    items = [" ", "aex", False, 0.0, "   ", "darkooooo ", [1,2, "name"]]
    assert concatenate_strings(items) == "aex False 0.0     darkooooo  [1, 2, 'name']"