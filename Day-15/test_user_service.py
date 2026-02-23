# test_user_service.py
import pytest  # type:ignore
from unittest.mock import Mock, patch
from user_service import Database, EmailSender, UserService

# ----------------------------------------------------------------------
# Fixtures – provide reusable test components
# ----------------------------------------------------------------------


@pytest.fixture
def mock_db():
    """Fixture that returns a mocked Database instance."""
    # We create a Mock object that behaves like a Database
    db = Mock(spec=Database)
    # We'll also set up a simple in‑memory store for demonstration
    db.users = {}
    db.get_user.side_effect = lambda uid: db.users.get(uid)
    db.add_user.side_effect = lambda user: db.users.update({user["id"]: user}) or user
    db.update_user.side_effect = lambda uid, data: (
        db.users[uid].update(data) if uid in db.users else None
    )
    return db


@pytest.fixture
def mock_email_sender():
    """Fixture that returns a mocked EmailSender."""
    return Mock(spec=EmailSender)


@pytest.fixture
def user_service(mock_db, mock_email_sender):
    """Fixture that returns a UserService instance with mocked dependencies."""
    return UserService(db=mock_db, email_sender=mock_email_sender)


@pytest.fixture
def sample_user():
    """Fixture that provides sample user data."""
    return {"id": 1, "name": "Alice", "email": "alice@example.com"}


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------


def test_get_user(user_service, mock_db, sample_user):
    """Test retrieving a user."""
    # Arrange: manually add a user to the mock database
    mock_db.add_user(sample_user)

    # Act
    result = user_service.get_user(1)

    # Assert
    assert result == sample_user
    mock_db.get_user.assert_called_once_with(1)


def test_create_user(user_service, mock_db, mock_email_sender, sample_user):
    """Test creating a user and sending a welcome email."""
    # Act
    result = user_service.create_user(sample_user)

    # Assert
    assert result == sample_user
    # Verify database interaction
    mock_db.add_user.assert_called_once_with(sample_user)
    # Verify email sending
    mock_email_sender.send_welcome_email.assert_called_once_with("alice@example.com")


def test_create_user_missing_id_raises_error(user_service):
    """Test that creating a user without an id raises ValueError."""
    with pytest.raises(ValueError, match="User must have an id"):
        user_service.create_user({"name": "Bob", "email": "bob@example.com"})


def test_update_email(user_service, mock_db, sample_user):
    """Test updating a user's email."""
    # Arrange: pre‑add user
    mock_db.add_user(sample_user)

    # Act
    updated = user_service.update_email(1, "newalice@example.com")

    # Assert
    assert updated["email"] == "newalice@example.com"
    mock_db.get_user.assert_called_once_with(1)
    mock_db.update_user.assert_called_once_with(1, {"email": "newalice@example.com"})


def test_update_email_user_not_found(user_service, mock_db):
    """Test updating email for a non‑existent user."""
    mock_db.get_user.return_value = None  # user not found

    with pytest.raises(ValueError, match="User not found"):
        user_service.update_email(999, "nobody@example.com")
    mock_db.get_user.assert_called_once_with(999)
    mock_db.update_user.assert_not_called()


# ----------------------------------------------------------------------
# Using monkeypatch for environment variables (extra example)
# ----------------------------------------------------------------------


def test_database_connection_string(monkeypatch):
    """Example of monkeypatching an environment variable."""
    monkeypatch.setenv("DB_CONN", "sqlite:///test.db")
    from user_service import Database

    db = Database(connection_string="sqlite:///test.db")
    assert db.connection_string == "sqlite:///test.db"
