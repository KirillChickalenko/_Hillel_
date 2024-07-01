def filter_type(type_to_filter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, list):
                return [item for item in result if not isinstance(item, type_to_filter)]
            return result

        return wrapper

    return decorator


@filter_type(str)
def generate_list_with_strings() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_type(int)
def generate_list_with_integers() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_type(float)
def generate_list_with_floats() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_type(type(None))
def generate_list_with_none() -> list:
    return ["hello", 123, "world", 456, 78.9]


@filter_type(str)
def return_non_list() -> any:
    return "This is not a list"


print(generate_list_with_strings())
print(generate_list_with_integers())
print(generate_list_with_floats())
print(generate_list_with_none())
print(return_non_list())
