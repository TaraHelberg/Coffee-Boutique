# Coffee Boutique 

![amiresponsive]()

Live App link : [Coffee Boutique]()

Git Hub Repository : [Coffee Boutique Repository]()


# Contents

- [User Experience(UX)](#user-experience-ux)
   * [User Stories](#user-stories)
        * [Agile Method](#agile-method-git-projects)
        * [Future Features](#future-features) 
   * [Design](#design)
      * [Colour Scheme](#colour-scheme)
      * [Images](#images)
      * [Font](#fonts)
      * [Wireframes(Balsamiq Wireframes)](#balsamiq-wireframes)
      * [Data Modal](#data-modal)
   * [Security Features and Defensive Design](#security-features-and-defensive-design)
      * [User Authentication](#user-authentication)
      * [Form Validation](#form-validation)
      * [Database Security](#database-security)
      * [Custom error pages:](#custom-error-pages)


- [Features](#features)
   * [HomePage](#home-page)
   * [UserAccountPages](#user-account-pages)
   

- [AdminControl](#admin-control)
   * [AdminControlPanel](#admin-control-panel)
   * [AdminLogin](#admin-login)
   

- [Technologies](#technologies)
   * [Programming Languages](#programming-languages)
   * [Support Programs & Libraries](#support-programs--libraries)

- [Testing](#testing)
   * [Bugs](#bugs)
   * [ManualTesting](#manual-testing)
        * [NavigationHeader](#navigation-header)
        * [NavigationFooter](#navigation-footer)
      * [SignUpManualTesting](#sign-up-manual-testing)
      * [SignInManualTesting](#sign-in-manual-testing)
      * [SignOutManualTesting](#sign-out-manual-testing)  
      * [AdminControlMaualTesting](#admin-control-maual-testing)          
          * [AdminLoginMaualTest](#admin-login-maual-test)
          * [AdminControlPanelMaualTesting](#admin-control-panel-maual-testing)
                         
    * [Validation](#validator-testing)

- [Deployment](#deployment)
   * [Github](#github)
   * [Django and Heroku](#django-and-heroku)   
   * [Clone Project](#clone-project)

- [Acknowledgments](#acknowledgments)
    * [Credits](#credits)
    * [CopiedCode&CodeAssistance](#copied-code--code-assistance)
    * [Note](#note)

## User Experience UX


## User Stories


[Back to top ⇧](#contents)

## Agile Method Git Projects

GitHub projects was used to manage the development process using an agile approach. Please see link to project [Kanban Board]()

Not all Epics have made it into the project using the MSCW Method you will find on the Kanban Must have’s, Should Have’s, Could Have's and Won’t have labels. 

## Future Features


[Back to top ⇧](#contents)

# Design


## Colour Scheme

## Images

### Images Credit for Project

 <details><summary></summary>
    
* [Images obtained via ....]()
    
 </details>


## Fonts

[Back to top ⇧](#contents)

# Balsamiq Wireframes

Wireframes are extremely basic and did not incorporate all App pages. Wireframes were used as boiler plates to start the app design many updates and alterations made after the basic Wireframes were used to get started on the App.

<details><summary>Balsamiq Wireframes</summary>

Home Page ![ Home Page ]()

Register ![ Register ]()

Login ![ Login ]()

LogOut ![ LogOut ]()


</details>

[Back to top ⇧](#contents)

# Data Modal

I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.
User Modal with the User_Id as the Primary Key


The diagram below details the <details><summary>Database Flow Chart:</summary>
![Database Flow Chart ]()
</details>

[Back to top ⇧](#contents)

# Security Features and Defensive Design

## User Authentication

    
## Form Validation
    

## Database Security

The Database URL and secret key are stored in the env.py file to prevent unwanted connections to the Database and this was done at the beginning of the App set up and pushed to GitHub.

Cross-Site Request Forgery (CSRF) Tokens are used on all Forms within the App.
    
## Custom error pages:

Custom Error Pages have been created to give the User / Author more information and help redirect them when an should an Error occur. These pages are provided with Redirect Buttons to appropriate areas of the App.

403 Error page shown as an Example of what the Error pages present to the User / Author.

<details><summary>Error Page Example Imagery</summary>

![403]()

</details>


   ### 400 Error - Bad Request
   
   ### 403 Error - Access Forbidden Image 
        
   ### 404 Error - Page Not Found
   
   ### 500 Error - Server Error
   
[Back to top ⇧](#contents)

# Features

## Home Page 

<details><summary>Full Home Page Image :</summary>

![HomePage]()

</details> 


The Home Page of the App incorporates the Following :



### Image of Header and Navigation when User is not Logged In
![]()

### Image of Header and Navigation when User is Logged In
![Naviagtion Logged In]()



### Footer Image

![Footer]()

[Back to top ⇧](#contents)

# User Account Pages

<details><summary>Full Sign Up Page Image :</summary>

![SignUpPage]()

</details> 


<details><summary>Full Sign In Page Image :</summary>

![SignInPage]()

</details> 


<details><summary>Full Sign Out Page Image :</summary>

![SignOutPage]()

</details>


[Back to top ⇧](#contents)



[Back to top ⇧](#contents)

#  Page

<details><summary> Page Image :</summary>

![]()

</details> 


### Image

![]()



### Image

![]()

###  Image

![]()


### Image

![]()


### Image

![]()

[Back to top ⇧](#contents)

## 


### Image  

![]()

[Back to top ⇧](#contents)

#  

<details><summary> :</summary>

![]()

</details> 


[Back to top ⇧](#contents)

# 

<details><summary> :</summary>

![]()

</details> 


[Back to top ⇧](#contents)

# 

<details><summary> :</summary>

![]()

</details> 


[Back to top ⇧](#contents)

# 

<details><summary> :</summary>

![]()

</details> 


[Back to top ⇧](#contents)

# 

<details><summary> :</summary>

![]()

</details> 

[Back to top ⇧](#contents)

#  Admin 


## Admin Control Panel

<details><summary>Full Admin Control Panel Page Image :</summary>

![AdminControlPanel]()

</details> 

The Admin Control Panel is part of the Django Framework and assists the Admin in Controlling the Content of the App.
The Control panel welcomes the Admin with options to View Site / Change Password and Logo Out of the Control Panel.
From this area you are able to see Accounts , Authentication & Authorization , The setups you have used for you sight such as Django Summernote as well as having access to in the Case of our App ,Recipes section for Approval of Comments & Recipes that the User has uploaded to the App.

## Admin Login

As the Admin a Login Page was required in order to access the Admin Control Panel Area.
This is part of the Django Framework and supplies a simple form area requesting the Admin Username and Password with a Log In button.

[Admin Login link]()

### Image of Admin Login 

![AdminLogin]()


## 

<details><summary> :</summary>

![]()

</details> 




[Back to top ⇧](#contents)


# Technologies

## Programming Languages 

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)
   
## Support Programs & Libraries

- [Git](https://git-scm.com/)
    - Version control.
- [GitHub](https://github.com/)
    - For storing code and deploying the site.
- [Gitpod](https://www.gitpod.io/)
    - Used for building and editing my code.
- [Django](https://www.djangoproject.com/)
    - A python based framework that was used to develop the site.
- [Bootstrap](https://getbootstrap.com/)
    - For help designing the html templates.
- [Google Fonts](https://fonts.google.com/)
    - Used to add style the website's font.
- [Font Awesome](https://fontawesome.com/)
    - Used to obtain the icons used.
- [Favicon.io]()
    - Used to generate the site's favicon.   
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used to help fix problem areas and identify bugs.
- []()
    - Used to store static files and images.
- [SQlite](https://www.sqlite.org/index.html)
    - Used when performing unit tests.
- [ElephantSQL](https://www.elephantsql.com/)  
- []()
    - To draw out the database schema.
- [Balsamiq](https://balsamiq.com/)
    - To create the wireframes.
- [W3C Markup Validation Service](https://validator.w3.org/) 
    - Used to validate HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - Used to validate CSS code.
- [Pep8ci](https://pep8ci.herokuapp.com/) - Thank you Code Institute
    - Used to validate Python code found on slack #announcements
- [JSHint](https://jshint.com/)
    - Used to validate JS code.
- [Summernote](https://summernote.org/)
    - Used to add a WYSIWYG text box to the add recipe page.
- [Heroku](https://www.heroku.com/)
    - To deploy the project.


[Back to top ⇧](#contents)

# Testing 

* Testing During development of the App was done through the project in order to Test for Bugs, Manual Testing was constantly done on all aspects of the App and Constant testing was done for the Responsiveness of the app via Dev Tools. Keeping an eye on the Look and Feel of the App.
  
## Bugs

Debug was kept on True in order to make use of Django's error page which came in use more often than not as a new Django Developer.
I as a new Django User & Developer encountered a great many Bugs . Solving them through many different means.

Bug Errors solved via :

1 :  

2 : Stack Overflow 

3 : Djano Documentation

4 : CI Tutor support

Find below a few images of errors encountered and solved through the making of this App.

<details><summary>Images of Bugs / Errors</summary>

![1]()

![2]()

![3]()

![4]()

![5]()
</details>


## Manual Testing

* User Testing

  * Expectations
     As a user I wanted the App to 
    1.  
    2. 

  * Result
     As a user I was able to  
    1. 
    2.        


### Navigation Header


| Feature            |  Expect                       | Action   | Result    |
| ------------------ | ----------------------------- | -------- | ----------|
|                    |                               | Click On |   ✔       | 


### Navigation Footer


| Feature           |  Expect                       | Action   | Result    |
| ------------------| ----------------------------- | -------- | ----------|
|  Icon Facebook    | Navigation Link - external Tab| Click On |   ✔       |
|  Icon Twitter     | Navigation Link - external Tab| Click On |   ✔       | 
|  Icon YouTube     | Navigation Link - external Tab| Click On |   ✔       |
|  Icon  Instagram  | Navigation Link - external Tab| Click On |   ✔       |
|  Icon  Linkedin   | Navigation Link - external Tab| Click On |   ✔       |
|  Icon  GitHub     | Navigation Link - external Tab| Click On |   ✔       |


###  Maual Testing

####  Manual Test 


| Feature           |  Expect                           | Action   | Result    |
| ------------------| --------------------------------- | -------- | ----------|
|                   |                                   | N/A      |   ✔       |
|  Sign Up Button   | Navigation Link                   | Click On |   ✔       |
|  Sign Out Button  | Navigation Link                   | Click On |   ✔       | 


## Admin Control Maual Testing


### Admin Login Maual Test


| Feature                        |  Expect                        | Action    | Result    |
| -------------------------------| ------------------------------ | --------- | ----------|
|  Input Fields                  | Access to & Fill In            |  Type     |   ✔       |
|  Log In Button                 | Log Into Django Admin          | Click On  |   ✔       |


### Admin Control Panel Maual Testing


| Feature                        |  Expect                        | Action    | Result    |
| -------------------------------| ------------------------------ | --------- | ----------|
|  Django Administration Panel   | Access to full Panel           |  N/A      |   ✔       |
|  Access via selection          | Access to Selections           |  Click On |   ✔       |

* From this panel the Admin has full C R U D functionality .

## Validator Testing

   ### HTML - W3C Html Validator 
   
   <details><summary>No Errors Found Html</summary>

   ![W3CHtml]()
    
   </details>

   ### CSS - W3C CSS Validator

   <details><summary>No Errors Found Css</summary>

   ![W3Ccss]()
    
   </details>

   ### Python - Pep8ci CI Python Linter
   
      
   <details><summary>No Errors Found Python Example Image</summary>

   ![Python]()
    
   </details> 
    
   ### Javascript - Jshint Validator
   
   <details><summary>No Errors Found JavaScript</summary>

   ![Jshint]()
    
   </details> 
    
   ### Responsiveness 

   * Responsiveness tested via Google Dev Tools & Imagery checked Via Am I Responsive

   <details><summary>Responsiveness Image</summary>

   ![amiresponsive]()
    
   </details> 
    
   ### Lighthouse - Website tested for Performance, Accessibility, Best Practice and SEO as seen below.
   <details><summary>LightHouse Test Results</summary>

   ![Lighthouse]()
    
   </details> 

[Back to top ⇧](#contents)

# Deployment

This project was deployed using Github and Heroku.

- ## Github 

    * To create a new repository, I took the following steps:

        + Logged into GitHub.
        + Click the ‘repositories’ section.
        + Click the green ‘new’ button to create new repository.
        + Choose ‘repository template’ Used the code institute template as recommended from the dropdown menu.
        + Add repository name then clicked the green ‘create repository button’ at the bottom of the page.
        + Open the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

- ## Django and Heroku

    To get the Django framework installed and set up I followed the Code institutes [Django I Think Therefore I Blog cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit). & Revisited the Walkthrough to assist.
    However due to changes made by Heroku changes were made when this occurred & information received from Code Institute.
    
    #### Final Deployment 
    DEBUG = False

    X_FRAME_OPTIONS = 'SAMEORIGIN' 

    In Heroku go to Reveal Congfig Vars  
    Remove Disbable_Collectstatic

    Go to Deploy Tab & Deploy Branch
   
- ## Clone Project 

    * Cloning of Project was made possible by GitHub
        + Go to Git Hub
        + Go to the repository 
        + Click on it to go to main repository site 
        + Click on the Code drop down button menu next to the greeen Gippod button
        + Click on HTTP section you will see the http of the repository click on the window next to it it will say copied
        + Clikced on Download and Zip
        + Clicked on Open with GitHubDesktop
 
 [Back to top ⇧](#contents)

# Acknowledgments

I would like to take the time to Acknowledge & give credit to all the main assistances that I used whilst making my App.

## Credits

   * Code Institute without who I would have had no base to begin a project & Readme.md Template .https://codeinstitute.net/ie/
   * GitHub for my workspace and saving all my work as well as my deployed project . https://github.com/
   * Heroku for hosting my App . https://www.heroku.com/ 
   * Reuben Ferrante my mentor without all his great guidance I would be lost. A Huge Thanks. https://github.com/arex18
   * The Slack community - for someone always been there no matter the time and with advice or direction. https://slack.com
   * Code Institute Tutoring ......
   * Balsamiq used to build the wireframes for my project. https://balsamiq.com   
   * Stack Overflow  for all the information to assist with my project .https://stackoverflow.com
   * Django Documentation for all the invaluable information on how to use the features .https://docs.djangoproject.com/en/4.1/
   * I am Responsive for a fantastic spot to see a visual of responsiveness. https://ui.dev/amiresponsive?msclkid=400b1adabe5b11ecbc48938198bb87b4
   * Lighthouse testing system whom I can't find a webpage link for but am grateful for been able to use.


## Copied Code / Code assistance  

Code Institutes walkthrough: ........ paid a big part in the structure of my App as well as certain parts that are directly used and referred to in the code via comments. 


 ### Note

All Recipes and information in this App are for Education purpose only.

[Back to top ⇧](#contents)
  
 