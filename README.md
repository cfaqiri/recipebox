# RecipeBox

Those who learned to cook with grandparents will recognize the old school recipe boxes used to store family recipes passed down from generations prior. Nowadays, it seems that any recipe one's heart could desire can be found with a quick google search, and keeping track of the links can get messy! Enter RecipeBox - a simple webapp that allows the modern day online recipe loving cook to store their beloved urls in a safe, organized place.

## Description and Files

RecipeBox is built on the Django Framework and uses Bootstrap + Javascript on the front-end. Its main two features include a user authentication system and a recipe storing system; nothing fancy, just what you'd need to save those sweet, sweet urls.

Beyond the standard files that come built into a Django app and the html templates, I created a number of new files for this project:
- app.js stores the javascript I wrote for the search functionality
- forms.py stores my forms 
- style.css stores some styling elements 
- files required for deployment to Heroku which include those in the static and staticfiles folder, as well as the Procfile
- requirements.txt which list which dependencies and packages are required
- .gitignore for the files that I want the version control system to ignore


### Distinctiveness and Complexity

This project is not a social network (the primary goal is not to connect about something with other users), an it is not an ecommerce site either (no one is buying or selling anything). This project is about information storage. As a result, the project satisfies the distinctiveness requirement. 

As for complexity, I've included a number features in this project that we had either not learned or not been required to include in previous projects. For example:
- Learning about and implementing some of Django's built-in features, such as those that allow users to register, log in, log out, change password, and reset password. Whereas in the past, some of these were built for us (like the login/logout), I structured these features myself in order to ensure that the user would have more stringent criteria to meet (more complicated passwords, for example). And so that they could change their password or reset it if they forgot. Super useful!
- Using Django's messages framework to pass messages to the user, and this is supplemented by Bootstrap's alert framework to make them pretty
- Using environment variables to keep secrets safe. For instance, for the password reset feature, I had to use my own email address as the sender and needed to give Django permission to log into my account. This username and password is kept safe from the source code. 
- Leveraging bootstrap further (and on my own) to implement and customize a navbar, forms, and modals 
- Deploying on Heroku. Now anyone in the world can access my app - none of that ./manage.py runserver for them, yay! This was arguably the most difficult and unique aspect of my project and what sets it aside in terms of distinctiveness AND complexity. 

## Getting Started

### Dependencies

Make sure to install the requirements.txt file if using this project locally. 

### Installing

Fork the project and enjoy.

### Executing program

You can either use the version deployed on Heroku at http://myrecipeboxapp.herokuapp.com/ or you can run this locally using python. Just a heads up though: since the password reset function uses environment variables, you won't have access to that if you run it locally. 

## Authors

Contributors names and contact info

ex. Crystal Faqiri - cfaqiri@gmail.com