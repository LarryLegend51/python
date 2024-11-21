import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.power()
    assert str(tv) == "Power: Off, Channel: 0, Volume: 0"

def test_mute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"  # Volume doesn't show muted state
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"  # Unmutes automatically

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 1, Volume: 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"  # Wraps back to min channel

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power: On, Channel: 3, Volume: 0"  # Wraps to max channel

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 1"
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"  # Max volume
    tv.volume_up()
    assert str(tv) == "Power: On, Channel: 0, Volume: 2"  # Stays at max

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"
    tv.volume_down()
    assert str(tv) == "Power: On, Channel: 0, Volume: 0"  # Stays at min
