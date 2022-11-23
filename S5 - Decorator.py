import functools



def cache_function(func):
    """Keep a cache of previous function calls"""
    
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    
    wrapper_cache.cache = dict()
    return wrapper_cache






@cache_function
def fibonnacci(number):
    if number <= 1:
        return 1
    else:
        return fibonnacci(number-1) + fibonnacci(number-2)