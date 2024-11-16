# Chocolate House Management Application

A Django-based application to manage a fictional chocolate house's:
- **Seasonal Flavor Offerings**: Add, update, and delete flavors.
- **Ingredient Inventory**: Track and manage ingredient stock.
- **Customer Suggestions**: Record flavor ideas and allergy concerns.

This application uses **Docker**, **Gunicorn**, and **Nginx** for deployment, with **SQLite** as the database.

---

## **Features**
1. **Seasonal Flavor Offerings**
   - Add new flavors.
   - Update existing flavors.
   - Delete flavors.

2. **Ingredient Inventory**
   - View and manage ingredients.

3. **Customer Suggestions**
   - Add and review flavor suggestions and allergy concerns.

---

## **Requirements**
- **Docker** and **Docker Compose** installed on your system.

---

## **Setup and Run**

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Build and start
```bash
docker-compose up --build
```

### 3. Running the migrations
```bash
docker-compose exec django python manage.py migrate
```

### 4. Accessing the Application
```bash
Open your browser and go to: http://localhost
```

### 5. Stop the Application
```bash
To stop the application, press Ctrl+C in the terminal or run:
docker-compose down
```

## **Environment Configuration**

Static Files: Django static files are served by Nginx and collected at /app/static.
Database: The SQLite database is stored at /app/db/db.sqlite3 inside the container.

## **Testing the Application**

### 1. Functional Tests
Open the application at http://localhost.
Test the following functionalities:
#### Seasonal Flavors:
Add, edit, and delete flavors from the dashboard.
#### Ingredient Inventory:
View the list of ingredients and update stock levels.
#### Customer Suggestions:
Submit flavor ideas and allergy concerns through the form.
View the submitted entries in the admin panel.

### 2. Admin Panel
Access the Django admin panel at http://localhost/admin.
Login with:
Username: admin
Password: <admin-password> (Set during initial Django setup)

### 3. Validation Steps
#### 1. Seasonal Flavors:
Add a new flavor.
Verify the flavor appears in the list.
Update an existing flavor and confirm changes.
Delete a flavor and ensure it is removed.
#### 2. Ingredient Inventory:
Check ingredient details.
Update stock levels and confirm changes.
#### 3. Customer Suggestions:
Submit a new suggestion.
Validate it appears in the admin panel.
Static Files:
Confirm static assets (CSS/JS/images) load correctly.

