def deprecated(alt):
    def decorator(f):
        def deprecated_func(*args, **kwargs):
            print("\nDEPRECATION WARNING:")
            print(f"    The '{f.__name__}' function is deprecated.\n")
            print(f"You should use the '{alt.__name__}' function instead.\n")
            return f(*args, **kwargs)
        return deprecated_func
    return decorator


def some_better_function():
    pass


@deprecated(some_better_function)
def some_deprecated_function(*args, **kwargs):
    print(args, kwargs)
