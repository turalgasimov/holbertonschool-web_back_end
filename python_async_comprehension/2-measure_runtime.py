#!/usr/bin/env python3
'''Async Comprehension'''
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measure runtime'''
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end = asyncio.get_event_loop().time()
    return end - start
