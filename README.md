### Software Shopping Web Application Introduction:
Welcome to our App Store website! We are an online platform that integrates a variety of quality apps and aims to provide you with the best app download experience.

Our store features a rich and diverse range of apps, including social media, games, productivity, education, healthcare, music, video and many more. Our team carefully selects each app to ensure that they are all high quality, useful, safe and secure.

In our store, you can easily find the apps you need through categories, leaderboards and search. We also regularly update the latest apps with professional reviews and introductions so you can better understand the functions and features of each app.

### The web application consists of three tables. These are:
1，Software list: all the apps in the shopping site, you can click on the details to enter the details page, you can display the information about the software: price, rating, number of reviews
2，Shopping cart: displays price, quantity, and delete and checkout
3，My orders: displays price, quantity

### Main features
1,Show all applications list
2,Pagination
3,Search
4,Detail page
5,Add to cart
6,Checkout

## 4 - Installation

### 4.1 If you are using Codio:

#### 4.1.1 Create a virtual environment and activate it in the terminal of Codio
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.1.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:grace-lliu/CS551Q-solo-assessment.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.1.3 Changed the site details in **ALLOWED_HOSTS** of ```mysite/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','milanpolo-buffalorapid-8000.codio-box.uk/']
```

#### 4.1.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.1.5 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 3.1.3

### 4.2 If you are using a local editor, such as Visual Studio Code, or Mac Terminal:

#### 4.2.1 Create a virtual environment and activate it in the terminal
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.2.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:grace-lliu/CS551Q-solo-assessment.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.2.3 Changed the site details in **ALLOWED_HOSTS** of ```mysite/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','localhost']
```

#### 4.2.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.2.5 Run the website application

``` shell
    python3 manage.py runserver
```

## 5 - Test

Besides the disaster table app, we have done unit testing for other apps. The table app does not need us to test inside the app, but we have their related testing in other apps. 

## 6 - Details of deploying the website application

The website application has been deployed to Render, here is its URL: https://ali-cs551q-assignment.onrender.com .

Build command:

``` shell
    pip install --upgrade pip && pip install -r requirements.txt
```

Start command:

``` shell
    gunicorn AppStoreShopping.wsgi:application --worker-class=gevent --worker-connections=1000 --workers=4 --bind=0.0.0.0:$PORT
```
