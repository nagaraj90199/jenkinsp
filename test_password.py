import pytest
from password import password_strength


def test_strong_password():
    output = password_strength("Pratham", "Strong@123")
    assert "Strength: STRONG" in output
    assert "Password is secure." in output

