import pytest

from functions import format_ip_address


def test_format_ip_address():
    assert format_ip_address('192.168.0.1') == '192[.]168[.]0[.]1'

def test_none_ip_address():
    assert format_ip_address(None) == ''

def test_empty_ip_address():
    assert format_ip_address('') == ''


def test_cidr_ip_address():
    assert format_ip_address('192.168.0.1/24') == '192[.]168[.]0[.]1/24'


def test_invalid_ip_address():
    with pytest.raises(ValueError):
        format_ip_address('300.4.0.1')
