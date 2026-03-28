import pytest


def test_unregister_success(client):
    """Test successful unregister from an activity."""
    # Arrange
    activity_name = "Basketball Team"
    email = "student@example.com"

    # First signup
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]

    # Verify the student was removed
    activities_response = client.get("/activities")
    activities = activities_response.json()
    basketball = activities[activity_name]
    assert email not in basketball["participants"]


def test_unregister_not_signed_up(client):
    """Test unregister when student is not signed up."""
    # Arrange
    activity_name = "Basketball Team"
    email = "notsigned@example.com"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "not signed up" in data["detail"].lower()


def test_unregister_activity_not_found(client):
    """Test unregister from non-existent activity."""
    # Arrange
    activity_name = "NonExistent Activity"
    email = "student@example.com"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()