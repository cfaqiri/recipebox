# Introduction

Keeping track of the links to recipes can get messy! Enter RecipeBox - a simple webapp that allows the modern day online recipe loving cook to store their beloved urls in a safe, organized place. This project has been deployed and can be accessed at http://myrecipeboxapp.herokuapp.com/.

## Features

RecipeBox's main two features include a user authentication system and a recipe storing system -- nothing fancy. Users are able to register, log in, log out, change password, reset password, add recipe urls, and search recipes. 

## Getting Started

### Dependencies

Make sure to install the requirements.txt file if running this project locally. 

### Installing

1. Clone the repository
```
git clone https://github.com/cfaqiri/recipebox.git
```
2. Install the requirements (virtual environment recommended)
```
pip install -r requirements.txt
```

### Executing program locally

- Make all migrations 
```python manage.py migrate```
- Run your local server
```python manage.py runserver```

## Authors

Crystal Faqiri - cfaqiri@gmail.com
