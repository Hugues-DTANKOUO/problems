import asyncio
import concurrent.futures
import functools
import inspect

from typing import Any, Callable, Coroutine, TypeVar


F = TypeVar("F", bound=Callable[..., Any])


def async_timeout(timeout: int = 1000) -> Callable[[F], Callable[..., Coroutine[Any, Any, Any]]]:
    """
    A decorator that adds a timeout to an asynchronous function.

    :param timeout: The timeout in milliseconds
    :return: The wrapper function
    """

    def decorator(func: F) -> Callable[..., Coroutine[Any, Any, Any]]:
        """
        The actual decorator that adds a timeout to an asynchronous function.

        :param func: The function to decorate
        :return: The wrapper function
        """

        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if inspect.iscoroutinefunction(func):
                    return await asyncio.wait_for(func(*args, **kwargs), timeout / 1000)
                loop = asyncio.get_event_loop()
                with concurrent.futures.ThreadPoolExecutor() as pool:
                    return await asyncio.wait_for(
                        loop.run_in_executor(pool, functools.partial(func, *args, **kwargs)), timeout / 1000
                    )
            except asyncio.TimeoutError as error:
                raise AssertionError(f"Function timed out after {timeout} milliseconds") from error

        return wrapper

    return decorator
