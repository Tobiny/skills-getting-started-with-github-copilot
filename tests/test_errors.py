import pytest


def test_signup_missing_email(client):
    """Test signup with missing email parameter."""
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.post(f"/activities/{activity_name}/signup")

    # Assert
    assert response.status_code == 422  # Unprocessable Entity for missing required param
    data = response.json()
    assert "detail" in data


def test_unregister_missing_email(client):
    """Test unregister with missing email parameter."""
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup")

    # Assert
    assert response.status_code == 422  # Unprocessable Entity for missing required param
    data = response.json()
    assert "detail" in data