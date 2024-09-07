
# E-commerce Backend Documentation

## Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Local Development and Deployment](#local-development-and-deployment)
4. [API Endpoints](#api-endpoints)
5. [cURL Examples](#curl-examples)

## Overview

This project is a simple e-commerce backend built with Python and Flask, following clean architecture principles. It allows for basic user management, product management, cart functionality, and order placement. JWT-based authentication is implemented to ensure that users can only view and manipulate their own data.

## Architecture

The project is structured following **clean architecture**, separating concerns between different layers and maintaining a clear distinction between business logic and infrastructure:

```
ecommerce-backend/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── product_controller.py
│   │   ├── user_controller.py
│   │   └── order_controller.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   ├── cart.py
│   │   │   ├── order.py
│   │   │   ├── product.py
│   │   │   └── user.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── database.py  # Handles SQLite connections
│   │   ├── hashing.py  # Handles password hashing
│   │   ├── jwt_handler.py  # Manages JWT creation and validation
│   │   └── auth_middleware.py  # JWT-based route protection
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── product_repository.py
│   │   ├── user_repository.py
│   │   └── order_repository.py
│   └── use_cases/
│       ├── __init__.py
│       ├── user_use_cases.py
│       ├── product_use_cases.py
│       └── order_use_cases.py
├── tests/
│   ├── test_user.py
│   ├── test_product.py
│   └── test_order.py
├── Dockerfile
├── requirements.txt
├── main.py  # Flask app entry point
└── README.md
```

### Key Components

- **Domain Layer (Entities)**: Contains the core business logic (User, Product, Cart, Order).
- **Repository Layer (Persistence)**: Manages interactions with the SQLite database.
- **Use Cases (Service Layer)**: Handles the application-specific business rules.
- **API (Presentation Layer)**: Provides RESTful API endpoints via Flask.
- **Infrastructure**: Handles external dependencies like JWT tokens and password hashing.

---

## Local Development and Deployment

### Prerequisites
- Python 3.9+
- Docker
- `pip` for package management

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/datagopher/ecommerce-backend.git
   cd ecommerce-backend
   ```

2. **Install dependencies**:
   You can install dependencies in a virtual environment or with Docker.
   
   #### Option 1: Install Locally
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   #### Option 2: Docker Setup
   You can also use Docker to run the app in a container. This ensures a consistent environment.

3. **Run Locally (Without Docker)**:
   ```bash
   python main.py
   ```
3.1 **Run Tests**:
   ```bash
   python3 -m unittest discover -s tests
   ```

   The application will be accessible at `http://localhost:8080`.

4. **Run with Docker**:
   To run the application locally using Docker:

   1. **Build the Docker Image**:
      ```bash
      docker build -t ecommerce-backend .
      ```

   2. **Run the Docker Container**:
      ```bash
      docker run -p 8080:8080 ecommerce-backend
      ```

   3. **Or Run the Docker Script**:
      ```bash
      sh build_local.sh
      ```

   Your application will now be accessible at `http://localhost:8080`.

---

## API Endpoints

### User Management
- **Register a User**: `POST /user/register`
- **Login a User**: `POST /user/login`

### Product Management
- **Add a Product (Admin Only)**: `POST /product/products`
- **Get All Products**: `GET /product/products`

### Cart and Order Management
- **Place an Order**: `POST /order/order`

### JWT Protected Routes
- **Authorization**: All order-related routes are protected via JWT tokens. Users need to log in and provide a valid token in the `Authorization` header.

---

## cURL Examples

### 1. **Register a User**
```bash
curl -X POST http://localhost:8080/user/register \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser",
  "password": "testpassword"
}'
```

### 2. **Login and Receive JWT Token**
```bash
curl -X POST http://localhost:8080/user/login \
-H "Content-Type: application/json" \
-d '{
  "username": "testuser",
  "password": "testpassword"
}'
```

This returns a JWT token:
```json
{
  "token": "your.jwt.token.here"
}
```

### 3. **Add a Product (Admin Only)**
```bash
curl -X POST http://localhost:8080/product/products \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your.jwt.token.here" \
-d '{
  "name": "Gaming Mouse",
  "description": "High precision gaming mouse",
  "price": 49.99,
  "stock": 100
}'
```

### 4. **Get All Products**
```bash
curl -X GET http://localhost:8080/product/products \
-H "Content-Type: application/json"
```

### 5. **Place an Order (Authenticated User)**
```bash
curl -X POST http://localhost:8080/order/order \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your.jwt.token.here" \
-d '{
  "cart_items": [
    {"product_id": 1, "quantity": 2},
    {"product_id": 2, "quantity": 1}
  ]
}'
```

### 6. **Access Protected Endpoints (Without Token)**
```bash
curl -X GET http://localhost:8080/order/order \
-H "Content-Type: application/json"
```

This will return an error since the token is missing:
```json
{
  "message": "Token is missing!"
}
```

---

## Notes

- **JWT Authentication**: Each user receives a token upon successful login. This token is required for accessing protected endpoints.
- **SQLite Database**: Data is stored in an SQLite database. Each request establishes a new connection and the connection is closed after each request.
- **Token Security**: The secret key for JWT (`SECRET_KEY`) should be stored securely in production environments (e.g., environment variables).

