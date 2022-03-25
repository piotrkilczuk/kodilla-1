def is_palindrome(data):
    if type(data) is not str:
        raise ValueError("Input must be a string!")

    if len(data) == 0:
        raise ValueError("Input is empty!")

    clean_data = "".join(data.lower().strip().split())

    if len(clean_data) < 2:
        return False

    return clean_data == clean_data[::-1]


dataset = {
    None: ValueError,
    123: ValueError,
    "": ValueError,
    "    ": False,
    "a    ": False,
    "a b": False,
    "test": False,
    "a": False,
    "bb": True,
    "Bb": True,
    "abba": True,
    "ABba": True,
    "Do geese see God": True,
    "do geese see God": True,
    "  do geese see God    ": True,
    "12345": False,
    "11311": True
}


for data, expected_result in dataset.items():
    print("Test start: ", data)
    try:
        actual_result = is_palindrome(data)
    except ValueError as ex:
        if issubclass(expected_result, ValueError):
            print("Test passed", data)
        else:
            print(f"{data} should return {expected_result}, got ValueError")
    except Exception as ex:
        print(f"{data} should return {expected_result}, got exception: {ex}")
    else:
        assert actual_result == expected_result, f"{data} should return {expected_result}, got {actual_result}!"
        print("Test passed", data)
