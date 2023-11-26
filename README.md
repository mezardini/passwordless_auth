# Passwordless_auth Django Email Verification API

## Overview

This Django API provides functionality for email verification, including validation, sending verification codes, and session management.

## Features

1. **Email Validation and Sending**
   - **Endpoint**: `/api/validate-email/` (POST)
   - **Request Payload**:
     ```json
     {
       "email": "user@example.com"
     }
     ```
   - **Response**:
     - 200 OK: Email is valid, and a verification code is sent.
     - 400 Bad Request: Invalid email format.

2. **Code Verification**
   - **Endpoint**: `/api/verify-code/` (POST)
   - **Request Payload**:
     ```json
     {
       "code": "abcde"
     }
     ```
   - **Response**:
     - 200 OK: User is verified.
     - 400 Bad Request: Incorrect verification code.

3. **Session Management**
   - **Get Session**
     - **Endpoint**: `/api/session/` (GET)
     - **Response**:
       ```json
       {
         "fav_color": "default_color"
       }
       ```
   - **Set Session**
     - **Endpoint**: `/api/session/` (POST)
     - **Request Payload**:
       ```json
       {
         "fav_color": "blue"
       }
       ```
     - **Response**: Session data.
   - **Clear Session**
     - **Endpoint**: `/api/session/` (DELETE)
     - **Response**:
       ```json
       {
         "message": "Session cleared."
       }
       ```

## Usage

1. **Validate Email**: Send a POST request to `/api/validate-email/` with the email address to receive a verification code.

2. **Verify Code**: Send a POST request to `/api/verify-code/` with the verification code to confirm the user.

3. **Session Management**:
   - **Get Session**: Send a GET request to `/api/session/` to retrieve the current session data.
   - **Set Session**: Send a POST request to `/api/session/` to set the session variable.
   - **Clear Session**: Send a DELETE request to `/api/session/` to clear the session.

## Note

This API is a barebones implementation and should be extended for production use. It lacks proper security measures and additional functionalities.
