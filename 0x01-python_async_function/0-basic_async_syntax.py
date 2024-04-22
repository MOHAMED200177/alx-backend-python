#!/usr/bin/env python3
"""task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float :
    """wait for a random delay"""
    randomDaley = random.random() * max_delay
    awit asyncio.sleep(randomDaley)
    return randomDaley
