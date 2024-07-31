## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

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
      - key = DISABLE_COLLECTSTATIC | value = 1
      - key = DATABASE_URL | value = (my secret database url)
      - key = SECRET_KEY | value = (my secret key)
  12. Navigate to Deploy tab
  13. Connect to GitHub and select the repo 'lunar-lists'
  14. Scroll down to 'Manual deploy' and select the 'main' branch
  15. Click 'Deploy Branch'
 
The live link can be found here - https://lunar-lists-658001c5b8b7.herokuapp.com/
