import pytest
from password import password_strength


def test_strong_password():
    output = password_strength("Nagaraj", "Strong@123")
    assert "Strength: STRONG" in output
    assert "Password is secure." in output


def test_medium_password():
    output = password_strength("Ravi", "Password1")
    assert "Strength: MEDIUM" in output


def test_weak_password_common():
    output = password_strength("Arun", "password")
    assert "Password is too common and unsafe." in output
    assert "Strength: WEAK" in output


def test_missing_special_character():
    output = password_strength("Suresh", "Strong123")
    assert "Add at least one special character." in output
