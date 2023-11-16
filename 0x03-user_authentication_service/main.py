#!/usr/bin/env python3
"""
End to end integration testing
"""
import requests

domain: str = "http://0.0.0.0:5000/%s"


def register_user(email: str, password: str) -> None:
    """Test registeration endpoint
    """
    url = domain % "users"
    payload = [("email", email), ("password", password)]
    expected = {"email": email, "message": "user created"}
    res = requests.post(url, data=payload)
    assert res.status_code == 200
    assert res.json() == expected

    expected = {"message": "email already registered"}
    res = requests.post(url, data=payload)
    assert res.status_code == 400
    assert res.json() == expected


def log_in_wrong_password(email: str, password: str) -> None:
    """Test login endpoint with wrong password
    """
    url = domain % "sessions"
    payload = [("email", email), ("password", password)]
    expected = {"error": "Unauthorized"}
    res = requests.post(url, data=payload)
    assert res.status_code == 401
    assert res.json() == expected
    assert res.cookies == {}
    return res.cookies.get("session_id", None)


def profile_unlogged() -> None:
    """Test profile route with unlogged user
    """
    url = domain % "profile"
    expected = {"error": "Forbidden"}
    res = requests.get(url, cookies=dict())
    assert res.status_code == 403
    assert res.json() == expected


def log_in(email: str, password: str) -> str:
    """Test login with valid credentials
    """
    url = domain % "sessions"
    payload = [("email", email), ("password", password)]
    expected = {"email": "%s" % email, "message": "logged in"}
    res = requests.post(url, data=payload)
    session_id = res.cookies.get("session_id", None)
    assert res.status_code == 200
    assert res.json() == expected
    assert session_id is not None
    return session_id


def profile_logged(session_id: str) -> None:
    """Test profile route for a valid logged in user
    """
    url = domain % "profile"
    res = requests.get(url, cookies=dict(session_id=session_id))
    assert res.status_code == 200
    assert res.json().get("email") is not None


def log_out(session_id: str) -> None:
    """Test logout call
    """
    url = domain % "sessions"
    res = requests.delete(url, cookies=dict(session_id=session_id))
    print(res.status_code)
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email: str) -> str:
    """Test reset token route
    """
    url = domain % "reset_password"
    res = requests.post(url, data={"email": email})
    assert res.status_code == 200
    reset_token = res.json().get("reset_token")
    assert type(reset_token) == str
    assert len(reset_token) > 0
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test passward update route
    """
    url = domain % "reset_password"
    payload = [
        ("email", email),
        ("reset_token", reset_token), ("new_password", new_password)]
    expected = {"email": "%s" % email, "message": "Password updated"}
    res = requests.put(url, data=payload)
    assert res.status_code == 200
    assert res.json() == expected


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
