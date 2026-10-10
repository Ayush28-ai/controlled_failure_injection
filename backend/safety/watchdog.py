
import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar


T = TypeVar("T")


async def run_with_timeout(
    operation: Callable[[], Awaitable[T]],
    timeout_seconds: int,
) -> T:
    if timeout_seconds < 1:
        raise ValueError("Timeout must be positive")

    return await asyncio.wait_for(
        operation(),
        timeout=timeout_seconds,
    )
