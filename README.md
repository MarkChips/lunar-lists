# Lunar Lists
### A to-do list website
Lunar lists allows users to create to-do lists for any task with the addition of a fun and friendly space theme. Whether you are a busy person, or a forgetful one, you can use lunar lists to log all your tasks, set their due date, and mark them as completed when they're done. Your lunar lists are only available to you, so don't worry about people tampering with your lists.

![Responsive Mockup](documentation/screenshots/amiresponsive.png)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Agile](#agile)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Testing
### Responsiveness
I used dev tools on firefox and set the responsive design mode to iPhone 11 pro (as it had the thinnest display). During development I focused on mobile first design to support the majority of web users. The important thing was to prevent the need to scroll horizontally on mobile view. Occassionally I had to remove the bootstrap class 'container' to prevent horizontal scrolling.
- The navbar turns into a burger bar on small screen sizes.
- The task entries take up the full width on small screen sizes, while only taking up a third on large screens.

Below are displayed screenshots of all the pages as they would appear on an iphone 11 pro:

![index page mobile view](documentation/screenshots/index.png)
![register page mobile view](documentation/screenshots/register.png)
![login page mobile view](documentation/screenshots/login.png)
![logout page mobile view](documentation/screenshots/logout.png)
![account settings page mobile view](documentation/screenshots/account-settings.png)
![change password page mobile view](documentation/screenshots/change-password.png)
![saved lists page mobile view](documentation/screenshots/saved-lists.png)
![task view page mobile view](documentation/screenshots/task-view.png)
![create tasks page mobile view](documentation/screenshots/create-task.png)
![edit task page mobile view](documentation/screenshots/edit-task.png)

### Validation
#### HTML
I tested all HTML templates via text input on [W3 HTML validator](https://validator.w3.org/). There were no errors found except for a parse error relating to the `</html>` closing tag in the base.html file:
![html validator error message](documentation/validator/html/html-error.png)

I was unable to diagnose the cause of this error. I checked it against the following possible causes and found that it did not violate any of them:
- Premature closing of the HTML document: The `</html>` tag should be the last element in an HTML document. If it appears earlier, it can cause parsing errors.
- Missing opening `<html>` tag: If the document lacks an opening` <html>` tag, the closing tag may be considered out of place.
- Nesting issues: There might be unclosed tags or improperly nested elements before the `</html>` tag.
- Extra content after `</html>`: Any content after the closing HTML tag can trigger parsing errors.

Since the error does not relate to any of these problems, and causes no issues with running the website, I have chosen to ignore this one error. The table below was ticked off for each page tested, disregarding the previously mentioned error.

| HTML page       | Pass? |
|-----------------|-------|
| index           | ✅     |
| logout          | ✅     |
| signup          | ✅     |
| login           | ✅     |
| saved_lists     | ✅     |
| task_view       | ✅     |
| create_task     | ✅     |
| edit_task       | ✅     |
| account_settings| ✅     |
| password_change | ✅     |

**When using the HTML validator with urls of the deployed website, the django template language caused errors.** It looks as though these are due to the indentation, and `<p>` element used by the django form insertion. Interestingly the parse error did not show up in these instances.

#### CSS
I tested the CSS using [W3 CSS validator](https://jigsaw.w3.org/css-validator/). Two parse errors were found relating to a nested media query. The errors were resolved by moving the media query to a new line. Bootstrap was the cause behind all 434 warnings; these relate to vendor extensions and variables not being statically checked.
- Validator before and after fixing:

![css before](documentation/validator/css/css-before.png)
![css after](documentation/validator/css/css-after.png)

#### Python pep8
I tested every python file using [CI Python Linter](https://pep8ci.herokuapp.com/). Not many violations were found, except for the ocasional whitespace and line length.
- urls.py before and after amendments:

![urls.py before](documentation/validator/pep8/urls-before.png)
![urls.py after](documentation/validator/pep8/urls-after.png)

- I left the following pep8 violations in the settings.py as the code could not be made shorter for the AUTH_PASSWORD_VALIDATORS:

![settings.py leftovers pep8 violations](documentation/validator/pep8/settings-after.png)

### Manual Testing

## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:
  1. Install the gunicorn python package and create a file called 'Procfile' in the repo's root directory
  2. In the Procfile write 'web: gunicorn lunar_lists.wsgi'
  3. In settings.py add ".herokuapp.com" to the ALLOWED_HOSTS list
  4. In settings.py add 'https://*.herokuapp.com' to CSRF_TRUSTED_ORIGINS list
  5. git add, commit and push to github
  6. Navigate to the Heroku dashboard
  7. Create a new Heroku app
  8. Give it a name and select the region 'Europe'
  9. Navigate to settings tab and scroll down to Config Vars
  10. Click 'Reveal Config Vars'
  11. Add the following keys:
      - key = DATABASE_URL | value = (my secret database url)
      - key = SECRET_KEY | value = (my secret key)
  12. Navigate to Deploy tab
  13. Connect to GitHub and select the repo 'lunar-lists'
  14. Scroll down to 'Manual deploy' and select the 'main' branch
  15. Click 'Deploy Branch'
 
The live link can be found here - https://lunar-lists-658001c5b8b7.herokuapp.com/

## Credits
### Images
- The moon background image was downloaded from https://unsplash.com/.
### Code
- The following were adjusted from bootstrap 5.3:
  - The navbar
  - The modal delete warning
- The following were adjusted from django allauth:
  - login.html
  - logout.html
  - password_change.html
  - signup.html
- The following were adjusted from the code institute tutorial project 'Django Blog':
  - Django message notifications
  - User login status