import pytest
from banco_web.api.apps import ApiConfig
from banco_web.core.apps import CoreConfig


def test_apps():
    assert ApiConfig.name == 'api'
    assert CoreConfig.name == 'core'
