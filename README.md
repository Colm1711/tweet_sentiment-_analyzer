# Contents
* [**Project Goals**](<#project-goals>)
    *  [User Goals](#user-goals)
    *  [Site Owner Goals](#site-owner-goals)
* [**User Experience UX**](<#user-experience-ux>)
    *  [User Stories](<#user-stories>)
    * [Design](<#design>)
    * [Wireframes](<#wireframes>)
* [**Features**](<#features>)
    * [Current Features](<#current-features>)
    * [Future Features](<#future-features>)
* [**Technologies Used**](<#technologies-used>)
    * [Languages Used](<#languages-used>)
    * [Frameworks Libraries & Programs Used](<#frameworks-libraries-programs-used>)
    * [Libraries](<#libraries>)
* [**Testing**](<#testing>)
    * [Validation](<#validation>)
    * [Testing User Stories from User Experience](<#testing-user-experienece>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
*  [**Acknowledgements**](<#acknowledgements>)

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Project Goals
* The Tweet Analyzer application is the beginning of a real world application to allow users retrieve live stock data and get numerical representation of how that company is trending with real
world users of twitter. To help give stock traders a competitive advantage.
* The application enables user to retrieve live stock information and have it represented back to them in the terminal from the SP500 list.
* Application also looks to provide weekly data for a given stock.


## User Experience (UX)

-   ### Target Audience
1. Users looking to retrieve live data from stock market and are looking for sentiment score of company to help with decisions.

## User stories

-   ### User

1.    I want a clear menu with options that are clear on intention.
2.    I want to able to log in and know that my details are secure and no one has access to my account.
3.    I want to be able to register my information and have it stored so I can log in again.
4.    I want to get real time data through the app.
5.    I want to be able to have data sheet to view in more organised way in the application.
6.    I want to be able to access single stock data showing weekly treending information.
7.    I want to be able to get sentiment data on my query of information.
8.    I want to be able to understand data that is being presented to me.
    
-   ### Site Owner

9.    I want users to have positive experience when using the app.
10.   I want users to understand and easily use the menu screen.
11.   I want to have record of users email and password and retrieve information for validation
12.   I want to provide user with clear message if incorrect information is entered.
13.   I want validation on data entry points such as user email and password.
14.   I want to be able to update the users list by remongin from registration application.

-   ### Scope

1. For first release, the scope is to rpovide users ability to register, login and retrieve live data.
2. Future scope includes adding ability for user to email or downloiad live data offline. Search multiple parameters and filtering of data.

*   ### Wireframes

    The flow for how the application operates was mapped out on lucidcharts

    * Highlevel overview wireframe image  
     ![Highlevel](assets/images/sentiment%20data%20from%20twitter.jpeg)

    * Login/Registration wireframe  
    ![lower](assets/images/tweet_sentiment_login_registration.jpeg)  

    * Micro 
    ![micro](assets/images)

[Back to top](<#contents>)

## Features

### Current Features



### Future Features



[Back to top](<#contents>)

## Technologies Used

### Languages Used

-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks Libraries & Programs Used
1. [Git](https://git-scm.com/) - Git was used for version control.
2. [GitHub](https://github.com/) - Github was used as a remote repository to store project code.
3. [Gitpod](https://gitpod.io/) - Gitpod was the IDE user to write the code of the project code.
4. [Lucidcharts](https://www.lucidchart.com/) - Lucidcharts was used to map out the flowcharts for the project.
5. [Googlesheets](https://www.google.com/sheets/about/) -  Googlesheets was used to act as the backend database to store snesitive information to be queried.
6. [Google Cloud Platform](https://cloud.google.com/) - Google cloud is iused to manage the access to the google services, google authorization, google sheets.
7. [Twitter](https://developer.twitter.com/en) -  Twitter developer was used to access the Twitter API. With use of OAUthandler to access live tweets from timeline.
8. [Yahoo finance](https://finance.yahoo.com/) -  Yahoo finance was used to access the Yahoo Stock API, this gives appliction access to live data.

#### Libraries

1. time - Facilitate waits in application between operations such as database writes and prints.
2. os -  allow screen refersh between prints to not have terminal 'clogged' with information.
3. getpass - hide password on terminal screen for user protection.
4. json - reading of JSON files and data for API.
5. re - regualr expression was used to help with email verfication and to remove emoji's from tweets.
6. strings - used in validation to search for uppercase, lowercase, punctuation and digits.
7. datetime - to help finance stock queries to ensure it is realtime.

##### 3rd Party Libraries

1. [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.
2. [Textblob](https://textblob.readthedocs.io/en/dev/) -  JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.
3. [tweepy](https://www.tweepy.org/) - JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.
4. [yahoo_fin](https://pypi.org/project/yahoo-finance/) -  JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.
5. [yfinance](https://pypi.org/project/yfinance/) - JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.
6. [pandas](https://pandas.pydata.org/) - JUSTIFICATION: Efforts to source native python library available that gives access to add, update, remove or return data from googlesheets and to interact with the google cloud platform API. Based on this it was imported to facilate google sheet operations to provide external database.

[Back to top](<#contents>)

## Testing

### Validation



### Testing User Stories from User Experience (UX) Section

### Testing User Experienece

-   #### First Time Visitor Goals

-   #### Returning Visitor Goals

-   #### Frequent User Goals


### Further Testing


### Known Bugs

- when attempting to hook up smtplib to tweet sentiment gmail account to send user registration froms. Recieved '[Errno 101] Network is unreachable' error
  message. Data online points to firewall issues. No known solution.

- There is a bug when the incorrect option is selected in login and rehgistration in the welcome function. SOLVED: Removing additonal elif from validaiton.

- with gspread there is an API limit of 500 requests per 100 seconds per project and 100 requests per 100 seconds per user. Due to this when writing the 
  company name and ticker name to stock data sheet gfor user was getting 429 error code. SOLVED: added 2 second wait btween writes to sheet.

- pandas append is being depreciated for concat. This leads to print out to terminal of warning message 

- heroku deployement with twitter API keys. Tutor support resolved.

[Back to top](<#contents>)

## Deployment

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

[Back to top](<#contents>)

## Credits

### Code

- Email validation and password validation information on use of regular expression was sourced here[GeeksforGeeks](https://www.geeksforgeeks.org/password-validation-in-python/)

- Regular expressions were taken from cheetsheet[MyGreatLearning](https://www.mygreatlearning.com/blog/regular-expression-in-python/)

- Regualr expressions of emojis was sourced from this cheatsheet[Github](https://gist.github.com/Alex-Just/e86110836f3f93fe7932290526529cd1)

- Dataframes information was sourced from [w3schools](https://www.w3schools.com/python/pandas/pandas_dataframes.asp)

- Manipulation of spreadhseets was sourced from here[gspread](https://docs.gspread.org/en/latest/user-guide.html)

- how to set dates for stock look back was sourced here[python.org](https://docs.python.org/3/library/datetime.html#timedelta-objects)

- Yahoo finance reference (https://algotrading101.com/learn/yahoo-finance-api-guide/)

- Gspread formating (https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells)

#### Libraries

- Imported Tweepy library to help extend this project and to connect with the Twitter API [Tweepy](https://docs.tweepy.org/en/stable/)

- Gspread

- re - regualr expressions

- JSON

- getpass this is to hide password for user from terminal output to ensure their data is protected

- TextBlob is imported to help woth polarity analysis of tweets[TextBlob](https://textblob.readthedocs.io/en/dev/)

- yfinance 

- yahoo_fin.stock_info

### Content

-   All content was written by the developer.

### Acknowledgements

The app was completed as a Portfolio 3 Project for the Full Stack Software Developer (e-Commerce) Diploma at the [Code Institute](https://codeinstitute.net/). I would like to thank my mentor Mo Shami, both tutors Gemma and Scott, my class mates, the Slack community, and all at the Code Institute for their help and support. 

Also to my friends and family who helped test site & provide feedback and most importantly patient with me during this time!

[Back to top](<#contents>)