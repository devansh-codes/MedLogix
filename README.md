# 🚀 **MedLogix: Medical Supply Management System** 🏥

**MedLogix** is an intuitive and robust medical supply management system built to simplify the tracking and management of medical supplies in healthcare facilities. The system is crafted with Python, Flask, and SQLAlchemy, offering users a seamless experience to manage inventory, register shops, and track supply orders.

## **✨ Features**

- 🏪 **Shop Registration**: Effortlessly register shops and manage shop-related data.
- 📦 **Inventory Management**: Keep track of your medical supplies and manage inventory effectively.
- 📈 **Order Tracking**: Monitor the status of supply orders in real-time.
- 🔐 **User Authentication**: Secure login and registration for authorized users.
- 🔄 **Database Migrations**: Easily manage database schema changes with Flask-Migrate.

---

## **🔧 Technologies Used**
- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite (can be easily switched to other databases)
- **Frontend**: HTML, CSS, Bootstrap (optional for UI styling)
- **Version Control**: Git

## **🚀 Getting Started**

### **📋 Prerequisites**

- 🐍 Python 3.12+
- 📦 pip (Python package manager)
- 🧰 Git

## **✨ Deployment**


```bash
git clone https://github.com/devansh-codes/MedLogix.git
cd MedLogix

2. Create a Virtual Environment

bash
Copy code
python3 -m venv venv

3. Activate the Virtual Environment

On macOS/Linux:
bash
Copy code
source venv/bin/activate

On Windows:
bash
Copy code
venv\Scripts\activate

4. Install Project Dependencies

bash
Copy code
pip install -r requirements.txt

5. Set Up the Database

# Initialize Migrations:
bash
Copy code
flask db init

#Create Migration Scripts:
bash
Copy code
flask db migrate

#Apply Migrations:
bash
Copy code
flask db upgrade

6. Run the Application

bash
Copy code
flask run

The application will be running at http://127.0.0.1:5000. You can access it in your web browser.
