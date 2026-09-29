# Secure Code Assessment Report

## 1. Project Overview

This project is a simple Login Application developed for
Secure Code Assessment.

The application allows a user to enter a username and password
and checks whether the credentials are valid.

## 2. Objective

The objective of this project is to review the application for
common security weaknesses and suggest secure coding practices.

## 3. Identified Vulnerabilities

### 3.1 Hard-coded Credentials

The username and password are directly written inside the
JavaScript source code.

**Risk:**  
Anyone who can inspect the source code may discover the credentials.

**Recommended Fix:**  
Do not store authentication credentials directly in client-side code.
Use secure server-side authentication.

---

### 3.2 Weak Password

The demonstration application uses a simple password such as
`admin123`.

**Risk:**  
Weak passwords can be easily guessed or attacked.

**Recommended Fix:**  
Use strong passwords containing a combination of uppercase letters,
lowercase letters, numbers and special characters.

---

### 3.3 Client-side Authentication

The username and password are checked directly using JavaScript
running in the browser.

**Risk:**  
Client-side code can be inspected and modified by users.

**Recommended Fix:**  
Perform authentication and validation on a secure server.

## 4. Security Recommendations

- Avoid hard-coded credentials.
- Use strong passwords.
- Perform authentication on the server side.
- Use secure password hashing for stored passwords.
- Validate user input.
- Never expose sensitive credentials in client-side code.

## 5. Testing

### Test 1: Correct Credentials

**Username:** admin  
**Password:** admin123

**Result:** Login Successful

### Test 2: Incorrect Credentials

**Username:** admin  
**Password:** wrong password

**Result:** Invalid username or password

## 6. Conclusion

The application was reviewed for common security weaknesses.
Three main issues were identified: hard-coded credentials,
weak password usage and client-side authentication.

Recommended secure coding practices were documented to improve
the security of the application.