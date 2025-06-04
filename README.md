# Work Schedule

![Work Schedule](documentation/README/work-schedule.png)

Do you write the schedule for your coworkers in a usual spreadsheet? Are you missing specified features fir schedule writing and the existing features are just too time consuming to implement them. Here is the solution to your problem. Work Schedule gives you a clean site with build in feathers, what makes scheduling easier and faster. Implement in your company as well. Check the live app [here](https://work-schedule-fb81687f20a4.herokuapp.com/)!

## Contents

* [User Stories](#user-stories)
  * [Welcome Page](#welcome-page)
  * [Authentication](#authentication)
  * [General](#general)
  * [Staff](#staff)
  * [Admin](#admin)
  * [Admin Page](#admin-page) 
* [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [Favicon](#favicon)
  * [Wireframe](#wireframe)
  * [ERD](#erd)
* [Feathers](#feathers)
  * [Authentication Pages](#authentication-pages)
    * [Welcome](#welcome)
    * [Sign Up](#sign-up)
    * [User is not Authenticated](#user-is-not-authenticated)
    * [Sign In](#sign-in)
    * [Sign Out](#sign-out)
  * [Admin Rights](#admin-rights)
    * [Accept User Application](#accept-user-application)
    * [Add Admin Rights](#add-admin-rights)
    * [Groups](#groups)
    * [Delete User](#delete-user)
    * [Other Django Admin Options](#other-django-admin-options)
  * [Sign Out Button](#sign-out-button)
  * [Schedule](#schedule)
    * [Previous-and-Next](#previous-and-next)
    * [Edit Schedule](#edit-schedule)
    * [Shift Types](#shift-types)
    * [Quick Fill](#quick-fill)
    * [Check Shift Correctness](#check-shift-correctness)
  * [Chat](#chat)
  * [Logged In User](#logged-in-user)
  * [Future Implementations](#future-implementations)
* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Used Programs](#used-programs)
* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
* [Testing](#testing)
  * [Detailed Testing](#detailed-testing)
  * [Fixed Bugs](#fixed-bugs)
  * [Test With Software](#test-with-software)
    * [HTML Validator](#html-validator)
    * [CSS Validator](#css-validator)
    * [JS Validator](#js-validator)
    * [PEP 8 Style Checker](#pep-8-style-checker)
    * [Google Lighthouse](#google-lighthouse)
* [Credits](#credits)
  * [Code Sources](#code-sources)
    * [Convert Datetime](#convert-datetime)
    * [Find Existing Record](#find-existing-record)
    * [Return JSON](#return-json)
  * [Acknowledgements](#acknowledgements)

## User Stories

Githubs projects and issues were used for agil programing. 29 user stories were created for this project. 

### Welcome Page

- User Story - As a not logged in user I can open the website so that I see the welcome page
- User Story - As a user I can click the sign in button on welcome page so that I can navigate to sign in page
- User Story - As a user I can click on the sign up button so that I can navigate to the sign up page

### Authentication

- User Story - As a user I can click a hypertext on sign up page so that I can navigate to sign in page
- User Story - As a user I can sign up so that I enter the app
- User Story - As a logged in user I can sign out so that I exit the app
- User Story - As a user I can click on go back button on sign out page so that I go back to the content

### General

- User Story - As a logged in user I can click on the sign out button so that I can navigate to sign out page
- User Story - As a logged in user I can see the text "You are logged in as ..." with the user's username

### Staff

- User Story - As a staff I can see the schedule so that I see my shifts
- User Story - As a staff I can push the next button so that I can see the next week's shifts
- User Story - As a staff I can see the chat so that I can read the messages
- User Story - As a staff I can write a new message so that my message appears on the chat-board

### Admin

- User Story - As a Superuser I can click on a shift on the schedule table so that the date and the employee regarding of the cell loads on the edit section
- User Story - As a superuser I can select employee on the edit-board so that I can change that employee's shift
- User Story - As a superuser I can select a date on schedule editing so that I can modify a shift in that day
- User Story - As a superuser I can enter times for the shift so that I can set starting and ending for shifts
- User Story - As a superuser I can click on vacation radio button so that I can set a vacation
- User Story - As a Superuser I can select the sick radio button so that I can set a shift too sick leave
- User Story - As a superuser I can click on the edit so that I can modify the schedule
- User Story - As a superuser I can push the delete button so that the chosen shift will be deleted
- User Story - As a superuser I can get a feedback if I incorrectly filled the form so that I can correct myself

### Admin Page

- User Story - As a superuser I can enter the django admin page so that I can reach more admin options
- User Story - As a superuser I can create groups so that employees can be assign to groups
- User Story - As a superuser I can modify user properties so that I can give privileges, change password, add groups, delete users
- User Story - As a superuser I can delete messages

## Design

### Color Scheme

* #EEEEFF was used for the main background and for text color when the background has an other color.
* #5AAEFF is the secondary background. It is used at Hader, Footer, buttons.
* #FFAB5A is the color for side panels, for #edit-schedule on every screen size, for buttons and also used in the table.
* #FFC093 was used in the table to differentiate the groups.
* #EEEEFFAA is the color for the author and the date for messages.
* #000000 is the main text color on white background, also used for drawing the table.

![Color Codes](documentation/README/color-scheme.png)

### Typography

Lexend Giga was used as font-family from Google Fonts.

![Lexend Giga](documentation/README/lexend-giga.png)


### Favicon

The favicon is a calendar from [flaticon.com](https://www.flaticon.com/free-icon/schedule_3652191?term=schedule&page=1&position=1&origin=search&related_id=3652191).

![favicon](documentation/README/favicon.png)

### Wireframe

There are two kinds of pages on the site one is the authentication the other is the schedule.

![Auth Mobile](documentation/README/auth-mobile.png)
![Schedule Mobile](documentation/README/schedule-mobile.png)
![Auth Screen](documentation/README/auth-screen.png)
![Schedule Screen](documentation/README/schedule-screen.png)

### ERD

![ERD](documentation/README/erd.png)

## Feathers

### Authentication Pages

Authentication pages are where the user haven't reached the main content jet. They have the same layout.

#### Welcome

If the user isn't logged in, then as he loads the home page a welcome message appears. The user has two options. Either go to log in or to sign in.

![Welcome](documentation/README/welcome.png)

#### Sign Up

Here the user has the possibility to Sign Up with name, password and email optionally. Other option is to go to sign in page.

![Sign Up](documentation/README/sign-up.png)

An error message pop up if the user incorrectly filled the form.

![Sign Up Alerts](documentation/README/sign-up-alerts.png)

#### User is not Authenticated

When the user signs up, or sign in but isn't approved yet, then a message appear that the user isn't approved yet. 

#### Sign In

The user can enter on the sign in page with a username and a password. 

![Sign In](documentation/README/sign-in.png)

And here is the possible error messages.

![Sign In Alerts](documentation/README/sign-in-alerts.png)

#### Sign Out

If the user clicks on the sign out button then the sign out page appears, where the user can confirm the action or go back to the content.

![Sign Out](documentation/README/sign-out.png)

### Admin Rights

Superusers/ chiefs have the possibility to use the django admin page. The necessary functions are below.

#### Accept User Application

Superusers can give staff status. That means the chief approve that the user really works for the company and after the approval the user as an employee can access the schedule.

![Staff Status](documentation/README/staff-status.png)

#### Add Admin Rights

Superuser can give superuser status in case of the boss is leaving the company and a new one comes or in case of bigger companies it is possible that there are more employee in higher position, who need the right to write the schedule.

![Superuser Status](documentation/README/superuser-status.png)

#### Groups

Superuser can create, delete groups, and add group for users. The groups symbolize the position of the employee. In the schedule they are grouped by their positions, so that easier for the schedule writer to compare the employees' schedule in the same or in similar position.

![Groups](documentation/README/groups.png)

#### Delete User

User can be deleted. It is equant that, that the employee leaves the company.

![Delete User](documentation/README/delete-user.png)

#### Other Django Admin Options

The superusers have some other options in case but normally they should be able to work without them. Some of them most of the time just not that useful, some of them just supposed to do from the main page. But in some special cases can be still useful.
* Create user
* Edit user data, password
* List users with filter
* Add different rights for users
* Create, edit, delete messages
* Create, edit, delete schedule

![Other Django Admin Options](documentation/README/other-django-admin-options.png)

### Sign Out Button

If the user is signed in, then a sign out button is available in the header. It leads to sign out page.

![Sign Out Button](documentation/README/sign-out-button.png)

### Schedule

The schedule appears when a user a user signs in with staff status. It displays a week. There are the days with dates in the first row, employees' name in the first column grouped by positions. And the shift in the table. What can be empty, sick, vacation or a shift time, maybe two if there is a split shift.

![Schedule](documentation/README/schedule.png)

#### Previous and Next

Clicking these buttons other weeks are accessible.

### Edit Schedule

This section is only available for superusers. They can add or edit shift with the edit button and delete with the delete button.

![Edit Schedule](documentation/README/edit-schedule.png)

#### Shift Types

Clicking shit a shift input, sick or vacation sets back the other two types.

#### Quick Fill

If the superuser clicks a cell on the schedule, then the date and the employee’s name will be automatically copied from there to edit schedule.

#### Check Shift Correctness

The JavaScript checks if the shifts startings and endings in an appropriate order. If the shift still has no sense, then it drops an error message. Only by split shift.

![Edit Alerts](documentation/README/edit-alerts.png)

#### Delete Check

The app checks if the shift is exist.

![Delete Alerts](documentation/README/delete-alerts.png)

### Chat

It appears for every user with staff status. It is possible only to read and write new messages. Every message is marked with a date and the sender.

![Chat](documentation/README/chat.png)

### Logged In User

If the user is logged in, then the name of the user appears on the footer.

![Logged In User](documentation/README/loged-in-user.png)

### Future Implementations

Depending the future feedbacks and development different implementations can be.

* A setting page will be created, so that the superuser will be able to select from the features.
* If the chat happened to be not useful then it will be optional or deleted.
* The chat may get its own page, when the home page gets too crowded.
* If the chat will be used by the companies, then editing and deleting functions will be added.
* Template will be savable for employees, so that will be automatically or with a button loaded for the next week.
* Other type of template will be accessible for the most used shift.
* Shift correctness checking will be updated according the law and the company policy.
* Schedule policy for the different positions will be possible to set in another page.

## Technologies Used

### Languages Used

HTML, CSS, JavaScript, Python

### Used Programs

| Program | Purpose |
| --- | --- |
| Figma | To create wireframe. |
| Github | To save project. |
| Heroku | To deploy project. |
| Sublime Text | To coding. |
| Git | To manage versions. |
| Paint | To edit readme images. |
| tinypng.com | To tinify images. |
| Firefox Developer Tools | To find CSS and JavaScript bugs and to check responsiveness. |
| ChatGTP | To search coding keywords and solutions. |
| Ms Office Word | To correct spelling. |
| draw.io | Draw ERD diagram. |

## Deployment & Local Development

### Deployment

The site is deployed using GitHub Pages - [Work Schedule](https://zoltannyaradi.github.io/work-schedule/).

To Deploy the site using GitHub Pages:

1. Login (or signup) to Github.
2. Go to the repository for this project, [ZoltanNyaradi/work-schedule](https://github.com/ZoltanNyaradi/work-schedule/deployments).
3. Click the settings button.
4. Select pages in the left hand navigation menu.
5. From the source dropdown select main branch and press save.
6. The site has now been deployed, please note that this process may take a few minutes before the site goes live.

### Local Development

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [ZoltanNyaradi/work-schedule](https://github.com/ZoltanNyaradi/work-schedule/deployments).
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [ZoltanNyaradi/work-schedule](https://github.com/ZoltanNyaradi/work-schedule/deployments).
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

## Testing

### Detailed Testing

Manual testing can be found in the [TESTING.md](TESTING.md) file.

### Fixed Bugs

| Bug | Cause | Solution |
| --- | --- | --- |
| WSGI didn't work | WSGI's name was misspelled | Change "-" to "_" |
| Code failed to find out if a shift was already in the database | Code logic was bad | Use correct method to do |
| Post request from scheduleForm and messageForm were the same | Couldn’t get form name  | Add a hidden element for scheduleForm |
| Js error at checking shift times | Code iterated over an array | Fix the conditions of the loop |
| H2 element had wrong text color | H20 was in the ccs | Delete the 0 |
| Changing week buttons didn't work| Monday cell got a class | Cutting data from Monday cell's html was adjusted |
| Rendering data didn't work | rendering schedule form caused a bug | Delete this line of code |
| Form disappeared | Js delete the form | Add another form to delete that instead |

### Test With Software

#### HTML Validator

[validator.w3.org](https://validator.w3.org/) was used to validate HTML code. After correcting a few error, it doesn't show more error.

#### CSS Validator

[Jigsaw](https://jigsaw.w3.org/css-validator/) found no error in the CSS file.

#### JS Validator

[JSHint](https://jshint.com/) found some missing semicolons and declarations. After these were corrected only 3 warnings remained.

17	Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (klickToShift)

134	Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (fillForm, datesOfTheWeek, j, employees, i)

330	Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (employees, i, datesOfTheWeek, j, shiftExist, shift)

But these don't cause any issue.

#### PEP 8 Style Checker

To check and upgrade code style [code:wof](https://www.codewof.co.nz/style/python3/) was used.

#### Google Lighthouse 

Google Lighthouse was used to check performance, accessibility, best practices and search engine optimization. All test passed.

![Lighthouse](documentation/README/lighthouse.png)

## Credits

### Code Sources

#### Convert Datetime

It was necessary to convert datetime values to pass them for JS.

![Convert Datetime](documentation/README/convert-datetime.png)

#### Find Existing Record

With this code I could find existing recods in the database, so the code can differentiate if it should edit or create this record.

![Find Existing Record](documentation/README/find-existing-recod.png)

#### Return JSON

With this solution possible to send a list from the backend to the frontend.

![Return JSON](documentation/README/render-json.png)

### Acknowledgements

I would like to thank for
 - my mentor Jubril Akolade who helped me with his valuable views,
 - my friends Puska Richard and Sisa Bence who tired the site and gave me usefull feedbacks.
