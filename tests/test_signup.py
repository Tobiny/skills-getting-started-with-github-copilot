import pytest


def test_signup_success(client):
    """Test successful signup for an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert email in data["message"]

    # Verify the student was added
    activities_response = client.get("/activities")
    activities = activities_response.json()
    chess_club = activities[activity_name]
    assert email in chess_club["participants"]


def test_signup_already_signed_up(client):
    """Test signup when student is already signed up."""
    # Arrange
    activity_name = "Chess Club"
    email = "existing@example.com"

    # First signup
    client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Act - Second signup
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data
    assert "already signed up" in data["detail"].lower()


def test_signup_activity_not_found(client):
    """Test signup for non-existent activity."""
    # Arrange
    activity_name = "NonExistent Activity"
    email = "student@example.com"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()