# Passwordless_auth Django Email Verification API

## Overview

This Django API provides functionality for email verification, sending verification codes and JWT authentication.

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
     - 200 OK: A 'User is verified' message and User Token.
     - 400 Bad Request: Incorrect verification code.


## Usage

1. **Validate Email**: Send a POST request to `/api/validate-email/` with the email address to receive a verification code.

2. **Verify Code**: Send a POST request to `/api/verify-code/` with the verification code to confirm the user.


## Note

This API is a barebones implementation and should be extended for production use. It lacks proper security measures and additional functionalities.
