# Map My World

**Version:** 1.0.0  
**Author:** eduinaf1980  

## **Overview**

**Map My World** is a REST API designed to help users explore and review various locations and categories. This project aims to provide a backend solution for managing locations, categories, and reviews while offering recommendations for exploration.

---

## **Features**

- **Manage Locations and Categories**: Add new locations and categories via endpoints.
- **Exploration Recommender**: Get 10 location-category combinations that:
  - Have not been reviewed in the past 30 days.
  - Are prioritized if they’ve never been reviewed.
- **Well-structured and Optimized Backend**:
  - Python and FastAPI ensure speed and maintainability.
  - Implements a clean, hexagonal architecture.
  - Efficient database operations with Tortoise ORM.

---

## **Technologies**

- **Programming Language**: Python (v3.9+)
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: Tortoise ORM
- **Containerization**: Docker + Docker Compose
- **Testing**: Pytest
- **Documentation**: Swagger (built into FastAPI)

---

## **Installation**

### **Requirements**
- Python 3.9+
- Docker
- Docker Compose

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/eduinaf1980/map-my-world.git
   cd map-my-world
2. Set up the environment:
  ```bash
    Create a .env file with the following variables:
    env
    Copiar código
    DATABASE_URL=postgres://<username>:<password>@<host>:<port>/<database>
    ENVIRONMENT=development

3. Build and run the Docker containers:
  ```bash
    Copiar código
    docker-compose up --build

4. Access the API documentation at: http://localhost:8000/docs
