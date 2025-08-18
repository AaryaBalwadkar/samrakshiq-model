def track_latency(func):
    """Decorator for timing functions."""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Latency: {time.time() - start}s")
        return result
    return wrapper