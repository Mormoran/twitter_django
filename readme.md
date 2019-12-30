# [Tweet Dash](https://mytweetdash.herokuapp.com/):
A Twitter dashboard analysis tool with filterable graphs that convey usage trends for any single user.

[Deployed website link.](https://mytweetdash.herokuapp.com/)

## UX
#### Scope

Scope 1 - Beta version.

The website will allow users to analyze and gather usage trends and statistics for any Twitter user account over time.

The site will fetch and parse data from the user’s timeline up to 3,200 tweets (which is the limit imposed by Twitter’s API), providing insights displayed using data visualisation tools for easier understanding.

The initial or beta version of the site will showcase the following information to users:
- Detailed view of individual tweets in a scatter plot, showing all tweets over a historical timeline divided in 24 hour segments with the tweet's text body included in the point tooltip.
- A bar chart comparing daily tweets and retweets.
- A series of pie charts that show original tweets and retweets, tweets using hashtags and without them, and tweets by day of the week, and tweets sent over different times of the day.
- A bar chart showing the number of tweets per day.


Scope 2 - Commercial dashboard.

A host of in-depth charts and scheduled retrieval of any user's timeline will ensure the latest trends and tweets are always accessible. More advanced charts will also show much more detailed usage data and statistics and allow the customer to spot potential revenue streams, weaknesses in their campaigns or opportunities to engage different audiences.

It is also planned that the dashboard will offer real time updates, changing as a user continues to tweet.

##### User stories:

- As a social media influencer, I want to make sure I maintain my ratio of original content higher than my retweets, so I can establish a name as a content creator and not just a sharer.
- As a small business owner, I want to monitor that the shop’s assistant manager is tweeting on behalf of our business at the right times, so we can reach our audience more effectively.
- As a marketing agency executive, I want to confirm a potential collaborator is active and consistent on Twitter, so I can make an informed decision before offering them a contract.
- As a journalist, I want to see what is the period of the day when I am more frequently tweeting, so I can adjust it to those times where my readers are more likely to be online.
- As a blogger, I want to see my proportion of tweets per day of the week, so I can make sure I am remembering to tweet evenly and not only when I’ve spare time.

##### Mockups and wireframes

The mockup for this project was created with Balsamiq.

All of the key pages were included in the mockup.

Alternatively, you can find the mockup uploaded as a PNG within the folder ASSETS/MOCKUP.

## Features

##### Existing features

A homepage that prompts the user to login or create an account.

An account's system that allows the site to remember all of a user’s Twitter user searches and enables them to use the dashboard.

A dashboard in which logged in users can enter a public Twitter account’s profile name to get analytics regarding usage trends.

A crossfilter allows the filtering of tweet data by clicking on the pie chart wedges that provide users with key information about their tweeting habits (for example, original versus retweeted content, tweets with and without the use of hashtags, etc).

A dropdown menu that allows users to change from one dataset to another, fetching the analytics of different accounts they’ve searched before.


##### Desired features

We plan to include real time updates in a future version by polling the currently selected Twitter user’s timeline every 10 seconds with a [setInterval’ed](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval) [$.ajax GET request](https://api.jquery.com/jquery.ajax/), and comparing the last fetched tweet with the last tweet in our database (using Django’s filters to fetch `.last()` from our tweets table). If they are different we push the tweet’s JSON body to our data array, and use the DC.js methods to update and redraw the charts [without trashing the current charts](https://dc-js.github.io/dc.js/examples/replacing-data.html).

We also plan to include more graphs types that help us give further details about a Twitter user’s own trends such as

- Average tweets per day
- Average tweets per day of the week
- Most interactions VS time of the day
- Most favourites VS day of the week
- Most retweets VS day of the week
- Top 10 most liked tweets
- Top 10 most retweeted tweets
- Top 10 users by interaction

A feature allowing us to separate free accounts and paid accounts will allow the site to become a revenue stream and also, to offer some premium features to users who need or want further data about the accounts they search. Some examples of premium features would include side by side Twitter users comparisson, email notifications for certain thresholds (certain amount of tweets in a day, a tweet reaching a certain amount of retweets/favourites, etc).

## Technologies Used

- [Datas Driven Documents (D3.js)](https://d3js.org/)
    - Basis library for our graphs

- [DC.js](https://dc-js.github.io/dc.js/)
    - Wrapper library for D3.js that simplifies chart creation and filtering

- [Crossfilter.js](https://square.github.io/crossfilter/)
    - Allows dynamic dataset shifting and filtering by providing chart bin methods

- [JQuery](https://jquery.com)
    - For DOM manipulation.

- [Font Awesome](https://fontawesome.com/)
    - For better design and styling.

- [Whitenoise](http://whitenoise.evans.io/en/stable/)
    - Simple yet powerful static file serving for WSGI.

- [Tweepy](https://www.tweepy.org/)
    - Python library to interact with the Twitter public API

- [Twitter API](https://developer.twitter.com/en/docs)
    - RESTful API that allows us to fetch any public Twitter user's timeline

- [PostgreSQL Database](https://www.postgresql.org/)
    - Allows certain special field types for Django databases we need (array field and JSON field)

- [Python Decouple](https://pypi.org/project/python-decouple/)
    - To separate dev and production environment variables

- [Python Celery](http://www.celeryproject.org/)
    - To perform background tasks on server side on a different thread and consume tasks asynchronously

- [Redis](https://redis.io/)
    - To act as a task queue manager and distributor


### Testing

Revisiting the user stories given above, followed by an explanation of how the site fulfills these needs:

- As a social media influencer, I want to make sure I maintain my ratio of original content higher than my retweets, so I can establish a name as a content creator and not just a sharer.
- The dashboard allows a user searching themselves to see their proportion of original tweets versus retweets in a simple and easy to understand pie chart. They can also have a visual representation of their original versus retweet ratio by looking at the purple versus yellow dots on the scatter plot on top of the dashboard.

- As a small business owner, I want to monitor that the shop’s assistant manager is tweeting on behalf of our business at the right times, so we can reach our audience more effectively.
- The scatter plot by period of the day at the beginning of the dashboard shows all tweets visualised over the time of the day they were sent, allowing for a clear view on when is content being sent.

- As a marketing agency executive, I want to confirm a potential collaborator is active and consistent on Twitter, so I can make an informed decision before offering them a contract.
- The user can search the potential collaborator’s profile and get insights on their frequency of tweets (time of day, day of week) as well as check whether they are simply retweeting or are creating original content.

- As a journalist, I want to see what is the period of the day when I am more frequently tweeting, so I can adjust it to those times where my readers are more likely to be online.
- The user can have a general overview of this by seeing the scatterplot, but also, they can see the pie chart section where a graph titled Tweets by Period for the Day displays the share of content divided by Morning, Afternoon, Evening, and Late Night.

- As a blogger, I want to see my proportion of tweets per day of the week, so I can make sure I am remembering to tweet evenly and not only when I’ve spare time.
- The user can have a general overview of this by seeing the scatterplot, but also, they can see the pie chart section where a graph titled Tweets by Day of the Week displays the share of content divided by each of the seven days of the week.

#### Manual Testing

1. Logging in:
    1. Open site: Homepage prompts user to sign-in or sign-up.
    2. Click on “sign-in”: user is taken to a login page asking for username and password.
    3. Input wrong password: User can’t login.
    4. Input correct password and username: User logs in successfully.

    - (Feedback: In future versions, it will be ideal to offer users more intuitive ways to offer better feedback when a login is unsuccessful.)

2. Searching a Twitter account to get the analytics:
    1. Input a non-existing account name: Message saying USER NOT FOUND is displayed.
    2. Input an existing account name: Dashboard loads and tweets are retrieved.

3. Going from the dashboard currently displayed to one from a different Twitter user:
Changing the name on the dataset selector: site refreshes and retrieves information on the selected account.
Opening the selector but keeping the same dataset as currently being displayed: nothing changes, the site continues to display current dataset.

4. Different screen sizes:
    - The site is mobile friendly, and it uses Bootstrap grids to provide a flexible and appealing structure that looks well both on desktop sizes and smartphones.
    - The style and colour palette remains consistent throughout different screen sizes and the text becomes smaller, but at no point it becomes so small that it impairs readability.

- We choose to use yellow and purple for the scatter plot due to the fact that these two colours offer a high contrast when facing against one another.


### Bugs and Issues

- While most of the content is responsive, some unusual and especially smaller screen sizes might crop a portion of the feature charts.
- The current implementation shows all of a user's tweets. While this is currently desirable, as the number of stored tweets starts to grow large, reponsiveness on the site will be impacted. [Streaming tweets from the database in chunks](https://www.pubnub.com/blog/stream-data-to-create-realtime-charts-w-d3js-and-rickshaw/) is a possible solution though as of yet untested, although even then, large numbers of tweets become an issue for the browser to handle.

## Deployment

- Download or pull the repository.
- Install all required packages with `pip install -r requirements.txt`.
- Create a new Heroku project.
- [Follow the great guide from Vitor Freitas on how to deploy Django projects on Heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)
- [Provision a Redis backend server](https://devcenter.heroku.com/articles/heroku-redis)
- Ensure a Celery worker is included in your Procfile (add “worker: celery worker --app=mytweetdash -B -l info” in a new line without quotes, where mytweetdash is your Heroku project name). We have included a default Procfile for this project but if you must use your own or are trying to deploy to your own WSGI server you must include at least one Celery background worker that is needed for the project to function.
    - `-B` to start the Beat Scheduler, which we don't use at the moment but will in a future release for scheduled tasks.
    - `-l info` will provide verbose logs to the Heroku (or your own) log console. It can be removed after production is stable.
- Start the Celery worker Heroku Dyno with the Heroku CLI with “heroku ps:scale worker=1:Standard-1X -a mytweetdash” (without the quotes)
    - If deploying to your own server start the worker with `python manage.py celery -A twitter_django worker -B -l info -n worker1@myserver`
        - (Where `twitter_django` is the Django project name, not the Heroku app name)
        - `-l info` will provide verbose logs to the Heroku (or your own) log console. It can be removed after production is stable.

### Credits and acknowledgements

- [Change Django’s default SQLite database to a PostgreSQL database](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/)
- [Implement user accounts system](https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/)
- [Workaround to have celery tasks in windows](https://github.com/celery/celery/issues/4081) (Used only for local development)
- [Footer fix](https://medium.com/@zerox/keep-that-damn-footer-at-the-bottom-c7a921cb9551)
- [Login dialog help](https://bootsnipp.com/snippets/R5rn4)
- [Tweeter getter script obtained from](https://gist.github.com/MihaiTabara/631ecb98f93046a9a454) (Modified by Andres Correa with help from Richard Dalton)

### Acknowledgements

Code Institute Tutor Niel McEwen
Mentors Richard Dalton and Matt Rudge
Code Institute room on Slack
Code Institute Alumni Gabriela Guedez
Software Developer Vitor Freitas