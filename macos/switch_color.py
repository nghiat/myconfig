#!/usr/bin/env python3.7

import asyncio
import datetime
import iterm2

# Clock time to change colors.
LIGHT_TIME=(8, 0)
DARK_TIME=(19, 0)

# Color presets to use
LIGHT_PRESET_NAME="ez"
DARK_PRESET_NAME="ez_dark"

# Profiles to update
PROFILES=["Default"]

def datetime_after(t, time):
    today = datetime.datetime(t.year, t.month, t.day, time[0], time[1])
    if today > t:
        return today
    # Same time tomorrow
    return today + datetime.timedelta(1)


def next_deadline_after(t):
    light_deadline = datetime_after(t, LIGHT_TIME)
    dark_deadline = datetime_after(t, DARK_TIME)
    if light_deadline < dark_deadline:
        return (DARK_PRESET_NAME, LIGHT_PRESET_NAME, light_deadline)
    return (LIGHT_PRESET_NAME, DARK_PRESET_NAME, dark_deadline)

def get_duration():
    now = datetime.datetime.now()
    current_preset, next_preset, deadline = next_deadline_after(now)
    duration = (deadline - now).seconds
    print("Sleep for {} seconds until {}".format(duration, deadline))
    return duration, current_preset, next_preset

async def set_colors(connection, preset_name):
    print("Change to preset {}".format(preset_name))
    preset = await iterm2.ColorPreset.async_get(connection, preset_name)
    for partial in (await iterm2.PartialProfile.async_query(connection)):
        if partial.name in PROFILES:
            await partial.async_set_color_preset(preset)

async def main(connection):
    while True:
        duration, current_preset, next_preset = get_duration()
        await set_colors(connection, current_preset)
        await asyncio.sleep(duration)
        await set_colors(connection, next_preset)
        await asyncio.sleep(1)

iterm2.run_forever(main)
