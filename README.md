# CAR PRICE PREDICTION SITE:
This Machine Learning model aims to predict the price of a car (in $) upon providing necessary parameters as inputs. It takes in values like the length, width and height of the car, size of the engine, peak RPM, horsepower, etc., to predict it's price.

This model has been implemented using modules like Pandas, HTML, CSS, Flask and SQL.

### This repository contains the following files:
* login.html: This is a login page that authenticates the user.
* recommend.html: This is the main page that gets input from the user and upon clicking "submit", predicts and displays the output.
* model.pkl: This pickle file contains the ML model.
* app.py: This is the main Flask file that integrates all the files.
  
The login page:

<img width="853" alt="image" src="https://user-images.githubusercontent.com/118250546/229409550-4ffd2925-00dd-4243-ae5d-8cf5984768aa.png">

The main webpage:

<img width="878" alt="image" src="https://user-images.githubusercontent.com/118250546/229410356-eccf22ab-c71e-402c-8298-0a2c36f6f5bb.png">
The values are entered in the above page.

The result:

<img width="392" alt="image" src="https://user-images.githubusercontent.com/118250546/229410521-de85b355-02cd-4df3-9ee6-12efd5aefaed.png">

  
### How to run this application:
* To run this application,clone this repository to your local system.
* Check and install necessary libraries required for running the application.
* Run app.py.
* On your web browser, copy and paste the following link: http://localhost:5000/.
* Enter your login credentials.
* Enter the details of a car you want to predict the price for.


