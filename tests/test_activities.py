import pytest


def test_get_activities_success(client):
    """Test GET /activities returns all activities successfully."""
    # Arrange - No specific setup needed as data is in-memory

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) == 9  # Based on current activities in app.py
    # Check structure of one activity
    activity = data["Chess Club"]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)