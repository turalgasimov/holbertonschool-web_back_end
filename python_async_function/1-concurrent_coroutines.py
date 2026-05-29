#!/usr/bin/env python3
"""Module 1-concurrent_coroutines.py"""
import asyncio
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """wait_n"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)
