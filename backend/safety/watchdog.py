
import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

T = TypeVar("T")


async def run_with_timeout(
    operation: Callable[[], Awaitable[T]],
    timeout_seconds: float,
) -> T:
    if timeout_seconds <= 0:
        raise ValueError("Timeout must be positive")

    try:
        return await asyncio.wait_for(
            operation(),
            timeout=timeout_seconds,
        )
    except asyncio.TimeoutError as exc:
        raise TimeoutError(
            f"Operation exceeded {timeout_seconds} seconds"
        ) from exc
