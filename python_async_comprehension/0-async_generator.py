#!/usr/bin/env python3
"""Module 0-async_generator.py"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Loops 10 times, waits 1 sec each time, yields random float (0-10)"""
    for _ in range(10):
        # Must explicitly AWAIT the sleep so the loop actually pauses
        await asyncio.sleep(1)
        
        # uniform gives a random float within the specific 0 to 10 bounds
        yield random.uniform(0, 10)