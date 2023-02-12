

class TestFailure(Exception): pass


def tests(*args_result_pairs):
    def wrapper(f):
        errors = []
        for args, result in args_result_pairs:
            actual_result = f(*args)
            if actual_result != result:
                errors.append(
                    f"\nExpected {f.__name__}({', '.join(repr(x) for x in args)}) "\
                    f"\n    to be: {repr(result)}\n   but is: {repr(actual_result)}"
                )
        if errors:
            raise TestFailure("\n" + "\n".join(errors) + "\n")
        return lambda *args, **kwargs: f(*args, **kwargs)
    return wrapper
