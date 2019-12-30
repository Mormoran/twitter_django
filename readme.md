- Change SQLite3 to PostgreSQL - https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation/
- Implement user accounts system - https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
- Workaround to have celery tasks in windows - https://github.com/celery/celery/issues/4081
- Footer fix - https://medium.com/@zerox/keep-that-damn-footer-at-the-bottom-c7a921cb9551
- Login dialog help - https://bootsnipp.com/snippets/R5rn4
- Tweeter getter script obtained from https://gist.github.com/MihaiTabara/631ecb98f93046a9a454
- Modified by Andres Correa with help from Richard Dalton

- Python Decouple to separate dev and production environment variables
- Celery to perform background tasks on server side on a different thread and consume tasks
- Redis to act as a task queue manager and distributor


# [Tweet Dash](https://mytweetdash.herokuapp.com/):
A Twitter dashboard analysis tool with filterable graphs that convey usage trends for any single user.

[Deployed website link.](https://mytweetdash.herokuapp.com/)

## UX
#### Scope

Scope 1 - Beta version.

The website will allow users to analyze and gather usage trends and statistics for any Twitter user account over time.

Scope 2 - Commercial dashboard.

A host of in-depth charts and scheduled retrieval of any user's timeline will ensure the latest trends and tweets are always accessible. More advanced charts will also show much more detailed usage data and statistics and allow the customer to spot potential revenue streams, weaknesses in their campaigns or opportunities to engage different audiences.

##### User stories:

- As a People Operations Coordinator, I want to find and hire a team of performers, so I can give a special touch to my office’s Christmas party.
- As a bridesmaid, I want to find an illusionist that will perform at my friend’s engagement party, so I can surprise her and her family.
- As a cocktail bar owner, I want to have a list of reliable performers I can call and book on semi-regular basis, so I can throw themed events for my customers.
- As a mother of a 7 year old, I want to see images and descriptions of the performers, so I can get a sense of whether their show will be suitable for a children’s party.

##### Mockups and wireframes

See the mockup

The mockup for this project was created with Balsamiq.

All of the key pages were included in the mockup.

Alternatively, you can find the mockup uploaded as a PNG within the folder ASSETS/MOCKUP.

## Features

##### Existing features

A homepage that shows a group photo of some of the company’s main performers, as well as a description of what they do and a call to action to facilitate users going to the contact us page.

A rotating carousel of images with professional photography of the Kadabra Entertainment acts.

A section with more information and a feature image of each performer, and allows them to move up or down with the mouse or the arrows.

An image gallery with professional headshots and action shots, which opens in a  modal when users click on a photo, and allows them to move forwards or backwards with the mouse or the arrows.

A contact form that allows users to get in touch. To facilitate separating leads, support and general queries, users can select the most relevant between different possible subjects. The Kadabra Entertainment team will receive an email when a form is submitted (this is the desired feature, however, as part of a static, front-end initial project, the email functionality is not yet implemented on the back end).

The website features a gallery with a wide variety of images showcasing acts that might be suitable for different types of events. Some of the acts include descriptors such as “spooky” or “scary”, which provides information to parents looking for acts that might scare smaller children.

##### Desired features

We would like to include a page with reviews where they can show positive testimonials from former customers.

Eventually, it would be ideal to feature a calendar showing available dates, filtering by performer or type of act.

## Technologies Used

- [JQuery](https://jquery.com)
    - For DOM manipulation.

- [JQuery Flip](http://lab.smashup.it/flip/)
    - For the flip on the gallery and homepage.

- [JQuery/UI](https://jqueryui.com/)
    - For the the gallery and homepage.

- [Masonry PACKAGED](https://masonry.desandro.com/)
    - For the pictures gallery.

- [Font Awesome](https://fontawesome.com/)
    - For better design and styling.

### Testing

- As a People Operations Coordinator, I want to find and hire a team of performers, so I can give a special touch to my office’s Christmas party.

- Users can go to a landing page with information about each performer and their act, and then go to the contact us page in order to get in touch about booking their desired act or acts.

- As a bridesmaid, I want to find an illusionist that will perform at my friend’s engagement party, so I can surprise her and her family.

- Users can navigate the gallery to get an idea of the different acts, and they can read the descriptions on the performers page.

- As a cocktail bar owner, I want to have a list of reliable performers I can call and book on semi-regular basis, so I can throw themed events for my customers.

- Users can reach out directly to the company via the form on the contact us page, or call to their phone number. The different performers are listed by name or stage name, so users can inquiry about a particular artist if preferred.

- As a mother of a 7 year old, I want to see images and descriptions of the performers, so I can get a sense of whether their show will be suitable for a children’s party.

#### Manual Testing

1. Browse the gallery:
    1. Click on hamburger button: Menu opens.
    2. Click on “Gallery”: Gallery opens.
    3. Click on an image: Modal with the desired image opens.
    4. Click on the arrows left and right: images move left or right respectively.
    5. Click “esc” to exit: modal closes.

    - (Feedback: In future versions, it will be ideal to offer users more intuitive ways to close the modal, but at least the given option is highlighted, readable and functioning.)

2. Visit “About Us” section:
    1. Click on hamburger button: Menu opens.
    2. Click on “About us”: About us page opens.

3. Fill up the form:
    1. Click on hamburger button: Menu opens.
    2. Click on “Contact us”: Contact us page opens.
    3. Write name under “Name” field: Text is accepted and stays on field.
    4. Write email under “email” field: Text stays put. Suggested email appears when using Google Chrome.
    5. Choose a subject: Drop down menu opens allowing user to choose a subject for their email.
    6. Write message: The message field allows users to input paragraphs of over 500 words. This is desired, as some inquiries might be very detailed.
    7. Tried to submit the form without a name: User is not allowed to submit, a message pointing out to the required field appears. This happens for every required field when empty.
    8. Click submit when all fields are filled correctly: The front end side of the form works as expected. It is possible to see in the URL that the form is capable of passing the message to the backend (please note that this part of the project involved setting up the frontend and it took place before the backend lessons, therefore it was considered satisfactory if it would make it this far).

4. Different screen sizes:
    - The site is best seen on desktop sizes, however, media queries are in place to make it functional on smaller and bigger devices.
    - The style and colour palette remains consistent throughout different screen sizes and the text becomes smaller, but at no point it becomes so small that it impairs readability.
    - The hamburger menu was decided for cleanliness and design more than mobile functionality. The curtain effect was requested by the owner of the website as a hint of his company style.

### Bugs and Issues

- While most of the content is responsive, some unusual and especially smaller screen sizes might crop a portion of the feature images.
- On the entertainers landing page, smaller screen sizes cause the secondary (smaller) image of the artist to move, and it ends up partially covering some of the text describing what the act is about.
- As a starter website (Stream 1 final project) finished in early 2017, my general knowledge of modern libraries and practicality of maintenance was still in develpment. When creating the website, I wanted to try something other than just a static page, and I chose "flashier" effects. As such, some of the addon help libraries are nearly a decade old at this point, and attempting to update them to modern standards would require a complete rewrite of the entire project. I have decided to keep the website nearly "as is" while only updating some glaring issues. Possibly in the future I may rewrite this under a whole different project repository. This being my very first completed website holds some significance in showcasing how much I could accomplish in 1 month of learning HTML and JS techniques.

## Deployment

I deployed this project on GitHub Pages.
There is no difference between the development and the deployed version of the site.

### Credits and acknowledgements

All images were courtesy of Kadabra Entertainers.

### Acknowledgements

Code Institute Tutor Niel McEwen
Mentors Richard Dalton and Matt Rudge
Code Institute room on Slack
Code Institute Alumni Gabriela Guedez
