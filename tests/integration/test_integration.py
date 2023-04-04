"""
    This module contains integration tests for the rock-paper-scissors game.
"""
import requests
import pytest
import os

app_url = os.environ.get("APP_URL")


@pytest.mark.integration
def test_health_endpoint():
    """
    Test the health endpoint of the application.

    :param app_url: The URL of the running application.
    :type app_url: str
    """
    health_endpoint = app_url + "/health"
    response = requests.get(health_endpoint)
    assert response.status_code == 200


@pytest.mark.integration
def test_rps_endpoint():
    """
    Test the RPS endpoint of the application while the server is running.

    :param app_url: The URL of the running application.
    :type app_url: str
    """
    rps_endpoint = app_url + "/rps"
    response = requests.post(rps_endpoint, json={"move": "rock"})
    assert response.status_code == 200
