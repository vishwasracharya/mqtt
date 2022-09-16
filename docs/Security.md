# MQTT Security
Security Topics are as followed:

## Authentication
It is a part of Appllication and Transport Level Security.
- Application Level: MQTT protocal provides username (UTF-8 encoded) and password (binary data with a maximum of 65535 bytes) for authentication. (Provided during CONNECT message)
- Transport Level: client certificate is used for authentication.

### Response Codes:
- 0: Connection accepted
- 1: Connection refused, unacceptable protocol version
- 2: Connection refused, identifier rejected
- 3: Connection refused, server unavailable
- 4: Connection refused, bad user name or password
- 5: Connection refused, not authorized

## Transport Security: TLS
- TLS and SSL provide a secure communication between client and a server.
- It uses a handshake mechanism to establish a secure connection.

## Payload Encryption & Payload Signing:
- MQTT payload encrypition is of application level. Which usually is of MQTT Publish or CONNECT LWT payload.
- This Encryption can be used when you don't want to use TLS but still want to encrypt the payload.

### Scenarios:
- End-to-end (E2E) encryption
- Client-to-broker

### Mechanisms:
- Asymmetric encryption (public/private key encryption)
- Symmetric encryption (shared secret key encryption)

## Authentication protocols oAuth, JWT:

<strong>oAuth 2.0</strong>

- OAuth 2.0 is an authorization framework that allows a client to access a resource that is owned by a resource owner without giving unencrypted credentials to the client. 

<em>Flow</em>
Resource Owner --> Client --> Authorization Server --> Resource Server --> Authorization Server --> Client --> Resource Server

<strong>JWT</strong>

- JWT is a compact, URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is digitally signed using JSON Web Signature (JWS).
- JWT has a base64 encoded header, payload and signature. 

<em>Types:</em>

- Access Tokens
- Refresh Tokens

## Authorization / Topic Permissions:
- Authorization specifies access rights to a resource.

Essential Parts of Authorization:
- Subject or user who wants to access a resource.
- Resource, object, or service that need to be protected from unauthorized access.
- Policy that specifies if a subject or user has access to a resource. 

###  Authorization Policies:
- Access Control List (ACL)
    - E.G., Unix file permissions
- Role Based Access Control (RBAC)
    - E.G., Active Directory, SELinux, PostgreSQL
