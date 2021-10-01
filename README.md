# Beyond Earth Ecommerce Website With Django + React

E-commerce is the buying and selling of good or services via the internet, 
and the transfer of money and data to complete the sales. 
The website has created implements all of these options in which you can buy tickets to the moon and beyond. 
The whole ideal was to create a fictional website that would be focused in the future when space travel is possible. 
Using an E-commerce website to reflect the buying of the most exclusive tickets
Also can get which will make it possible for anyone with enough money to be able to visit the moon and beyond. 

## Prerequisites
- Python & Django installed
- You can follow this guide line how to install Python for macOS <a href=https://www.python.org/downloads/macos/>Python for MacOS</a> or <a href=https://www.python.org/downloads/windows/>Python for Windows</a>
- You can follow this guide line how to install Django <a href=https://docs.djangoproject.com/en/3.2/topics/install/>How to install Django</a> or "pip3 install django"
- You can check python&django version on your computer by this command: 
```
# Linux/macOS
python3 -m django --version

# Windows
py -3 -m django --version
```

## Download & Setup Instructions
- Clone project: git clone https://github.com/tharitar8/beyond_earthAPI
- cd beyond_earthAPI
- Setup the virtual environment: "pipenv install"
- Activate the virtual environment: "pipenv shell"
- Install gunicorn to your pip environment with "pipenv install gunicorn"
- Run "pipenv install django-rest-auth django-cors-headers python-dotenv dj-database-url"
- Create a .env file
- Generate a secret key using this https://djecrety.ir/ and add it to the .env file using the key SECRET.
- The .env file should look something like the following replace secret_key with your secret key.
```
ENV=development
DB_NAME_DEV=beyond_earthAPI
SECRET=secret_key 
```
- python manage.py runserver

## Important Links
- <a href="https://tharitar8.github.io/beyond_earthClient/">Deployed Client </a>
- <a href="https://github.com/tharitar8/beyond_earthClient">Client Repo </a>
- <a href="https://earthpluto.herokuapp.com/"> Deployed API </a>

## Technologies USED
- Python
- Django
- PostgresSQL

## Unsolved Problem
- [ ] images for product

## Wireframes

<img src="https://i.imgur.com/EKZACOj.png" />

## User Stories

- [x] As an unregistered user, I would like to sign up with email and password.
- [x] As a registered user, I would like to sign in with email and password.
- [x] As a signed in user, I would like to change password.
- [x] As a signed in user, I would like to sign out.
- [x] As an unregistered user, I would like to see all of the products.
- [x] As a signed in user, I would like to add and remove products from a shopping cart.

## ERD

<img src="https://i.imgur.com/lSrYWeV.jpg" />

## USER PATHS & METHODS
<table>
  <tr>
    <th>Endpoint</th>
    <th>Method</th>
  </tr>
  <tr>
    <td>/sign-up</td>
    <td>POST</td>
  </tr>
  <tr>
    <td>/sign-in</td>
    <td>POST</td>
  </tr>
  <tr>
    <td>/change-password</td>
    <td>PATCH</td>
  </tr>
  <tr>
    <td>/sign-out</td>
    <td>DELETE</td>
  </tr>
</table>

## WEBSITE PATHS & METHODS
<table>
  <tr>
    <th>Endpoint</th>
    <th>Method</th>
    <th>Response</th>
  </tr>
  <tr>
    <td>/products</td>
    <td>GET</td>
    <td>show all tickets</td>
  </tr>
  <tr>
    <td>/orders</td>
    <td>POST</td>
    <td>create an orderId when sign-in</td>
  </tr>
  <tr>
    <td>/product/:id</td>
    <td>GET</td>
    <td>Show Info for single ticket</td>
  </tr>
  <tr>
    <td> `/order/${order.id}/product/${product.id}/`</td>
    <td>PATCH</td>
    <td>Update an order when add to cart</td>
  </tr>
  <tr>
    <td> /order/:id</td>
    <td>GET</td>
    <td>Show all tickets been add to cart</td>
  </tr>
   <tr>
    <td> /order/:id</td>
    <td>PATCH</td>
    <td>Update an order by remove each</td>
  </tr>
  <tr>
    <td> /order/:id</td>
    <td>DELETE</td>
    <td>Delete all in order</td>
  </tr>
</table>
