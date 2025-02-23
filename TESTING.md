# Testing

## Welcome Page

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Sign in button | Click | Sign in page opens | Pass |
| Sign up button | Click | Sign up page opens | Pass |

## Sign In Page

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Sign in with missing or wrong data | Click to sign in | Stay in sign in page | Pass |
| Superuser signs in | Fill the form with superuser's data and click to sign in | Schedule opens with edit-schedule | Pass |
| Staff signs in | Fill the form with staff's data and click to sign in | Schedule opens without edit-schedule | Pass |
| Unauthorised user signs in | Fill the form with unauthorised user's data and click to sign in | Waiting for authorised message opens | Pass |
| Sign out button | Succesfull sign in | Sing out button appears | Pass |
| Logged in | Succesfull sign in | In the footer we can see who is logged in | Pass |
| Sign up link | Click onto the link | Sign up page opens | Pass |
| Remember me | Check remeber me | Users stays longer signed in | Pass |

## Sign Up Page

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Sign up with missing data | Click to sign up with missing data | Signing up fails | Pass |
| Sign up | Fill the form and click to sign up | Unauthorised message opens | Pass |
| Sign in link | Click to the link | Sign in page opens | Pass |

## Sign Out Page

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Sign Out | Click to sign out | User signs out | Pass |
| Go back | Click to go back | Last page opens | Pass |

## Schedule Page

### Sign Out Button

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Sign out button | Click to sign out button | Sign out page opens | Pass |

### Schedule

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| First row | Load the page | This weeks with days and dates load in the first row | Pass |
| First coulmn | Load the page | Employees load in the first row | Pass |
| Groups | Load the page | Employees with different positions have different background | Pass |
| Shifts | Load the page | Shifts load in the schedule | Pass |
| Previous | Click to the previous button | Previous week loads | Pass |
| Next | Click to next page | Next week loads | Pass |

### Chat

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Messages | Load the page | Messages load in the chat | Pass |
| Scroll | Scroll in the chat | Scrolling is working | Pass |
| Send message | Write and send a message | Message will be saved | Pass |

### Edit Schedule

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Employees | Click on dropdown list | List of employees opens | Pass |
| Date | Load page | Current day in the date imput | Pass |
| Shift | Click on shift | Vacation or shift will be checked out, in case shifts got a lighter background again | Pass |
| Vacation | Click on vacation | Sick checks off, Shifts become empty and get a darker background | Pass |
| Sick | Click on sick | Vacation checks off, Shifts become empty and get a darker background | Pass |
| Missing shift | Click on edit with a missing shift start or begin | Shift doesn't save | Pass |
| Shifts aren't in order | Click on edit with ambigous shifts | Error message appears | Pass |
| Shifts in order again | Click on edit with correct shifts, when error message is there | Error message disappears | Pass |
| Auto fill | Click on schedule | The relevant employee and date load into edit schedule | Pass |
| Edit | Click on edit with a correctly filled form | Create or edit a record in the database | Pass |
| Delete | Click on delete | Delete the relevant shift | Pass |

## Admin page

| Feature | Action | Expected Result | Result |
|---|---|---|---|
| Create group | Create group | New group appears | Pass |
| Add group | Add group for user | User get the group | Pass |
| Staff | Add staff for user | User will be staff | Pass |
| Superuser | Add superuser for user | User will be superuser | Pass |