# Secure File Sharing System - Security Report

## 1. Project Overview

This project is a Secure File Sharing System developed using Python Flask.

The application allows authenticated users to securely download files, while authorized administrators can upload files. Uploaded files are encrypted before being stored on the server.

## 2. Technologies Used

- Python
- Flask
- Cryptography
- Fernet Encryption
- HTML
- CSS

## 3. Security Features

### 3.1 Authentication

Users must log in with valid credentials before accessing the file-sharing system.

Demo users:

- Admin: admin
- User: user

### 3.2 File Encryption

Uploaded files are encrypted using Fernet symmetric encryption before being stored on the server.

The stored file is saved with the `.enc` extension.

### 3.3 Secure Download

Only authenticated users can access the download function.

During download, the encrypted file is decrypted and the original file is provided to the authenticated user.

### 3.4 Role-Based Access Control

The system implements two roles:

- Admin
- User

Admin users can upload and download files.

Normal users can download files but cannot upload files.

### 3.5 Session Management

Flask sessions are used to maintain the authenticated user's login state and role.

### 3.6 Access Protection

Unauthenticated users cannot access protected upload and download operations.

The upload route also checks whether the logged-in user has the Admin role.

## 4. Security Testing

### Test 1: Valid Login

Result: Login successful with valid credentials.

### Test 2: Invalid Login

Result: Invalid username or password is rejected.

### Test 3: File Encryption

Result: Uploaded files are stored in encrypted `.enc` format.

### Test 4: File Download

Result: Authenticated users can download and decrypt stored files.

### Test 5: User Role Restriction

Result: Normal users cannot see or use the file upload feature.

### Test 6: Admin Role

Result: Admin users can upload and download files.

## 5. Security Recommendations

- Use strong password policies.
- Store passwords using secure password hashing.
- Do not hard-code credentials in a production application.
- Store encryption keys securely.
- Use HTTPS for network communication.
- Validate uploaded file types and file sizes.
- Use secure temporary files for downloads.
- Use expiring download links for sensitive files.
- Disable Flask debug mode in production.
- Use a production WSGI server for deployment.

## 6. Conclusion

The Secure File Sharing System demonstrates important security practices including authentication, file encryption, session management and role-based access control.

The project provides a practical demonstration of secure file upload, storage and download.
