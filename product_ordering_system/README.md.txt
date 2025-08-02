# 🛒 Django REST Product Ordering System

A basic product ordering system built using Python, Django, and Django REST Framework.

---

## ✅ Features Implemented

1. **User Signup & Login**
   - Signup & Login with username/password (Session-based).
   - `is_admin` flag for admin privileges.

2. **Product Management**
   - Admins can add new products (name, price, stock).
   - All users can view products and filter by name.

3. **Order Placement**
   - Users can place orders with selected product quantities.
   - Validates stock and auto-updates stock on order placement.

4. **Order History**
   - View all previous orders with items, quantities, total, and date.

5. **Frontend (Bonus)**
   - HTML page for product browsing.
   - Day/Night mode, cart drawer, toast notifications.

---

## 🧪 API Endpoints (Tested via Postman)

| Endpoint            | Method | Auth Required | Description                        |
|---------------------|--------|---------------|------------------------------------|
| `/api/signup/`      | POST   | No            | Register a new user                |
| `/api/login/`       | POST   | No            | Log in a user                      |
| `/api/logout/`      | GET    | Yes           | Log out the current user           |
| `/api/products/`    | GET    | No            | List all products (filterable)     |
| `/api/products/`    | POST   | Admin Only    | Add new product                    |
| `/api/place-order/` | POST   | Yes           | Place an order                     |
| `/api/orders/`      | GET    | Yes           | View logged-in user's order history|

---

## 🧪 Postman Collection

A Postman collection is included here:  
📁 `Product Store.postman_collection`

**Tests Included:**
- Signup ✅
- Login ✅
- Add Product (admin) ✅
- View Products ✅
- Place Order ✅
- View Orders ✅

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2.Create & Activate Virtual Environment

bash

python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

3.Install Dependencies

bash

pip install -r requirements.txt

4.Run Migrations

bash

python manage.py makemigrations
python manage.py migrate

5.Create Superuser (for admin access)

bash

python manage.py createsuperuser

6.Run the Server

bash

python manage.py runserver

7.Open in browser:
👉 http://127.0.0.1:8000/
✅ Redirects to the login page.

🧪 API Testing (via Postman)
Import the provided Postman Collection:
 Product Store.postman_collection(included in repo)

Testable APIs:
Endpoint	Method	Access	Description
/signup/	POST	Public	User registration
/login/	POST	Public	User login (session-based)
/logout/	GET	Authenticated	Logout current user
/products/	GET	All users	List all products (optionally filter by name)
/products/	POST	Admin only	Add a new product
/place-order/	POST	Authenticated	Place an order with selected products
/orders/	GET	Authenticated	View order history for the logged-in user

📝 Notes

-Admins can add products from /products/ (POST)

*Non-admin users can only view products and place orders.

#Orders automatically reduce stock.

+All HTML pages include login protection.

!No token auth — session-based login used.

📁 Project Structure

core/
├── models.py         # User, Product, Order, OrderItem
├── serializers.py    # DRF Serializers
├── views.py          # Function-based Views (API + HTML)
├── urls.py           # Route mappings
templates/
├── login.html
├── signup.html
├── product_list.html
├── order_history.html
static/
├── custom JS/CSS/assets
├── AOS, NProgress, Animate.css integrations

🧾 Postman Test Collection

The Postman collection includes the following API tests:

✅ Signup

✅ Login

✅ Logout

✅ Add Product (Admin)

✅ Get Products (with/without filter)

✅ Place Order (with quantity and validation)

✅ View Order History

File name:  Product Store.postman_collection

Import it into Postman for quick testing!

🔗 GitHub Repo
🔗 https://github.com/shibilee12/product_Store

👨‍💻 Author
 Muhammed Shibili


