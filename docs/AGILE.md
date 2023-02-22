
# Agile

## Overview

The Agile planning methodology was used during the development of Sensical.ie. GitHub Projects, Boards, Milestones and Issues were utilised to Organise the development into Sprints, Kanban Boards, Epics, and User Stories respectively.

<img src="../docs/agile_images/agile_placeholder.png">

<br>

This was just my second time approaching a project using Agile, and I applied many of the lessons I learned during my first experience to the Sensical project.

These include:

* Creating More Sprints/Cycles

During the last project, I struggled initially with the planning of sprints due to my unfamiliarity with the Django Framework.
This time around, I feel I gave much more thought to the development tasks and planning phase at the beginning of the project,
including them in the overall Agile process. As the codebase and scope of this project was larger than the last, 
I doubled the amount of sprints to more effectively separate and manage the units of work.

* Using a waterfall approach when creating Epics

As I will explain, during the first Agile project I managed, I made the mistake of slipping into the traditional 'Waterfall' project management method the further I progressed into the project. I attributed this to the fact that the Agile process is usually followed by a team of people, enfusing multiple work units together simultaniously.

With this project, I decided not to worry too much on the sequence of the process and instead embrace a psuedo-waterfall approach, as by working alone some sort of linear pattern to the development was always going to manifest itself. I am aware that this is not what will happen in real world situations, and that the reason agile cycles, meetings and backlogs etc are essential to modern development, is the ability to adapt and change the project quickly and efficiently from any rigid plan or structure.

So the Epics I created were designed using a linear approach and organised in order of the importance of the features they contributed to the project.

* Add more user stories during development

In essence, using the Agile tool when working alone on a project of this size is far more beneficial than not, regardless of its real-world, practical use.
One of the absolutely essential benefits of creating Epics, User Stories and boards is the ability to focus soley on one particualar area of the project code at a time. During the last project however, I was too rigid in my approach to adding and removing user stories as the project started to develop.

During this project, I was much more forthright in my actions and pushed many items from each cycle to the project backlog and added user stories to add value to the project as I went along. I felt like this was a true reflection of the Agile approach.

<br>


## MoSCoW

<img src="../docs/agile_images/agile2.png">

When utilising MoSCow prioritisation I felt I had a good mix of 'Must Have', 'Could Have', 'Should Have' and 'Wont Have This Time' cards. I re-organised many of the 'Should Have' priority cards by creating time and space to address the project backlog in the final development cycle.

<br>

## Epics

Eight Epics in total were created for reference during the agile process and used GitHub 'Milestones' to link the 'User Stories' created during the User Experience Design phase of the project planning. 

<img src="../docs/agile_images/agile1.png">

<br>

The Eight Epics were:

1. [Sensical Epic 1: Setup Development environment, install packages, dependencies and early deployment.](https://github.com/davidcalikes/sensical.ie/milestone/1)

Developer tasks include setting up dev environment, installing packages, setting up the skeleton project, and Early deployment to Heroku.

<img src="../docs/agile_images/agile_epic1.png">

<br>

2. [Create Signup/Login Feature](https://github.com/davidcalikes/mypse.ie/milestone/2?closed=1)

Create functionality for users to securely log in and out of the app.

User stories include: "Create Superuser", "Implement Allauth Adapter" and "Login and redirect users"

<img src="../docs/agile_images/agile_epic2.png">

<br>

3. [Create, View, Update and Delete Pupil Records](https://github.com/davidcalikes/mypse.ie/milestone/4?closed=1)

For security purposes, in order for passports to be created, pupils must have a pupil record that contains their unique Pupil ID.

User stories include: "View List of Pupil Records", "Create Enrolled Pupil Record view and template" and "Style and format the delete pupil record confirmation page"

<img src="../docs/agile_images/agile_epic3.png">

<br>

4. [Create, View, Update and Delete Pupil Passports](https://github.com/davidcalikes/mypse.ie/milestone/3?closed=1)

Authenticated users have the ability to create passports for SEN pupils. 

Only users with the role of pupil or parent are authorised to create passport documents. Passports can only be created for users in possession of a school-issued Pupil ID, which will be required before any information is collected to improve UX. Users can only create one passport at a time. If a passport already exists for a pupil, users cannot create a new passport without deleting the old one first.

User stories include: "Create Passport", "Create Passport List" and "Add Passport Form Customisation"

<img src="../docs/agile_images/agile_epic4.png">

<br>

5. [Create Passport views with Restricted Functionality](https://github.com/davidcalikes/mypse.ie/milestone/6?closed=1)

Create restricted access views where pupils only have access to one passport(their own) and teachers can only view passports assigned to them.

User stories include: "Create a list of pupils assigned to a teacher" and "Create a Passport as a Pupil"

<img src="../docs/agile_images/agile_epic5.png">

<br>

6. [Add Media, Style and Tertiary Features To Enhance User Experience](https://github.com/davidcalikes/mypse.ie/milestone/5?closed=1)

Adding features to the site including the about page. Index page information, background images, custom fonts, styling and formatting.

User stories include: "Style and format base template to improve user experience" and Style and format passport page layout to improve user experience"

<img src="../docs/agile_images/agile_epic6.png">

<br>

## Agile User Stories

<br>

The User Stories created for reference within the Agile framework were derived from both the Epics created and also the empathetic User Stories I created as a result of planning research during the 'User Experience Design' phase of the project. I used GitHub Issues to create cards for Agile User Stories, Development Tasks, and Bugs.

The structure of a MyPSE.ie Agile User Story can be seen below.

<img src="../docs/agile_images/agile_us1.png">_Agile User Story_

As evidenced above, the title of Each Agile User Story Issue can be more accurately thought of as a descriptive overview of the tasks within the Issue. The actual User Story this issue will address is written at the top part of each Issue Card.

Each Issue Card contains:

* A Title: Descriptive overview of the issue/ticket

* The User Story the issue addresses

* Acceptance Criteria for each issue/ticket

* Tasks required to satisfy the acceptance criteria

* A label that determines the priority of each issue

* An assigned Kanban board

* An assigned Epic

<br>

I made a few errors when creating some of the user stories and had to remove some issues during development due to overlap. As I mentioned before this was down to my lack of experience working with Agile. I do feel however that my knowledge of how to implement the methodology and my understanding of its manifold benefits greatly increased during the development of MyPSE.ie.

The final amount of issues created totalled 44, of which 29  Agile user stories were created, 5 were bugs that I added during development and the remainder (7) were added as Developer Tasks.

<img src="../docs/agile_images/agile_us2.png">_Agile Issues_

The full list of issues for the project is available [here](https://github.com/davidcalikes/mypse.ie/issues?q=is%3Aissue+is%3Aclosed)

<br>

## Sprints

### Sprints Duration

Due to my inexperience with the Agile methodology and Django as a framework, I had few reference points that could inform my decision making when it came to allowing sufficient time for each sprint, whilst setting a realistic, achievable deadlines. 

### [MyPSE.ie Sprint 1 -- Overview](https://github.com/users/davidcalikes/projects/7)

I thought the best way forward as I began to become more comfortable working with Django was to base the timeframe given to the last three sprints on how long it took me to complete Sprint 1. As mentioned before, I had already set up part of the development environment before creating the first Kanban board so I had to factor this, as well as the fact that I was familiar with some elements of Django Account Authorisation due to the course content of the Code Institute's 'I think therfore I blog' walkthrough project.

<br>

### Developer Tasks and User Stories Completed During Sprint 1
<br>

* [Developer Task: Setup Django in Development Environment #1](https://github.com/davidcalikes/mypse.ie/issues/1)

* [Developer Task: Setup Skeleton Project and Start apps #2](https://github.com/davidcalikes/mypse.ie/issues/2)

* [Developer Task: Fix issue with S****_KEY variable #3](https://github.com/davidcalikes/mypse.ie/issues/3)

* [Developer Task: Deploy to Heroku #4](https://github.com/davidcalikes/mypse.ie/issues/4)

* [User Story: Create Landing Page & Base Template #5](https://github.com/davidcalikes/mypse.ie/issues/5)

* [User Story: Style landing page to improve user experience #6](https://github.com/davidcalikes/mypse.ie/issues/6)

* [Developer Task: Create Superuser#7](https://github.com/davidcalikes/mypse.ie/issues/7)

* [Developer Task: Add Dependencies for custom user model #8](https://github.com/davidcalikes/mypse.ie/issues/8)

* [Developer Task: Implement Allauth Account adapter #9](https://github.com/davidcalikes/mypse.ie/issues/9)

* [User Story: Custom User Signup #10](https://github.com/davidcalikes/mypse.ie/issues/10)

* [User Story: Login and redirect users #11](https://github.com/davidcalikes/mypse.ie/issues/11)

* [User Story: Create Pupil Records #16](https://github.com/davidcalikes/mypse.ie/issues/16)

* [Developer Task: Records and Passports Forms Dependencies #17](https://github.com/davidcalikes/mypse.ie/issues/17)

* [User Story: View List of Pupil Records #18](https://github.com/davidcalikes/mypse.ie/issues/18)

* [User Story: Provide Update and delete functionality to Pupil Records #19](https://github.com/davidcalikes/mypse.ie/issues/19)

* [User Story: Style and format delete confirmation page #20](https://github.com/davidcalikes/mypse.ie/issues/20)

* [User Story: Style and format base template to improve user experience #35](https://github.com/davidcalikes/mypse.ie/issues/35)

* [User Story: Redirect 'school' user to list page direct from login #36](https://github.com/davidcalikes/mypse.ie/issues/36)

* [User Story: Create Enrolled Pupil Record view and template #37](https://github.com/davidcalikes/mypse.ie/issues/37)

<br>

### Sprint 1 Evaluation

Development time -- 8 days.

The obvious  first conclusion reached here is that sprint 1 had far too many issues. A project with the scope of MyPSE.ie should have had at least one more sprint focusing on development tasks and initialising the project. 

Another observation I made was during the initial development. As the sole developer of this project, I felt I had to remain conscious of including all aspects of the development project during each sprint in order to replicate the true synergetic nature of an agile development.

I used the time it took to complete the issues from sprint one to make a general time rule of 1 week per sprint for the remainder of the project.

<br>

### [MyPSE.ie Sprint 2 -- Overview](https://github.com/users/davidcalikes/projects/8/views/1)

Sprint 2 focused on the creation of the passport functionality. Each user story explicitly laid out tasks and assessment criteria. The Second sprint benefitted from the newly set time parameters inherited from Sprint 1.  I also felt more confident moving the items across the columns of the Kanban board and could feel the benefits of the methodology as my understanding grew.  

<br>

### User Stories Completed During Sprint 2
<br>

* [User Story: Restrict ability to create passport unless authorised #12](https://github.com/davidcalikes/mypse.ie/issues/12)

* [User Story: Restrict access to Pupil Passports #13](https://github.com/davidcalikes/mypse.ie/issues/13)

* [User Story: Add Passport Form customisation #23](https://github.com/davidcalikes/mypse.ie/issues/23)

* [User Story: Create Passport #31](https://github.com/davidcalikes/mypse.ie/issues/31)

* [User Story: Create Passport List #33](https://github.com/davidcalikes/mypse.ie/issues/33)

* [User Story: Create Passport Edit Feature #38](https://github.com/davidcalikes/mypse.ie/issues/38)

* [User Story: Add Pupil Passport #39](https://github.com/davidcalikes/mypse.ie/issues/39)

* [User Story: Delete passport #40](https://github.com/davidcalikes/mypse.ie/issues/40)

* [User Story: Return to passports list page from other areas of the site #41](https://github.com/davidcalikes/mypse.ie/issues/41)

<br>

### Sprint 2 Evaluation

Development time -- 6 days.

The Second sprint was completed ahead of schedule and I found that following each issue in turn to be extremely productive. Focusing on the passport functionality of the application, the core model, views and templates came together with little difficulty as I became more proficient using the Django and Bootstrap frameworks.

<br>

### [MyPSE.ie Sprint 3 -- Overview](https://github.com/users/davidcalikes/projects/9/views/1)

Sprint 3 focused on providing teacher access to created passports. Each user story explicitly laid out tasks and assessment criteria. Similar to sprint 2, the third sprint benefitted from the newly set time parameters inherited from Sprint 1.  

<br>

### User Stories and Bugs Completed During Sprint 3
<br>

* [User Story: Create list of students assigned to Teacher #27](https://github.com/davidcalikes/mypse.ie/issues/27)

* [BUG! : Unacceptable risk of unauthorised access #42](https://github.com/davidcalikes/mypse.ie/issues/42)

* [User Story: Allow teacher to view passports #26](https://github.com/davidcalikes/mypse.ie/issues/26)

* [User Story: Create Passport as a pupil #25](https://github.com/davidcalikes/mypse.ie/issues/25)

* [User Story: View passport as a pupil #24](https://github.com/davidcalikes/mypse.ie/issues/24)

<br>

### Sprint 3 Evaluation

Development time -- 6 days.

The third sprint was completed on schedule and again I found following each issue in turn to be extremely productive. This sprint focused on restricting aspects of passport functionality to certain user types. The first bugs started to appear at this point during the project and I began to add the errors and issues to the Kanban board that took more than a few hours to correct. What was helpful using the Agile methodology here was the habit of referring to the end user at the beginning of every unit of work. This allowed for a much more robust program and caught logic errors such as in issue 42. I think that the solving the logic error during this sprint proved my sprint time estimations to be close to optimal. 

<br>

### [MyPSE.ie Sprint 4 -- Overview](https://github.com/users/davidcalikes/projects/10/views/1)

Sprint 4 focused on the tertiary features of the application and contained the most 'should have' and 'could have' priority issues. Multiple bugs and errors were also added to this sprint during development.

<br>

### User Stories and Bugs Completed During Sprint 4

<br>

* [User Story: Create About page #21](https://github.com/davidcalikes/mypse.ie/issues/21)

* [User Story: Style and format passport page layout to improve user experience #43](https://github.com/davidcalikes/mypse.ie/issues/43)

* [User Story: Provide additional feedback after user actions #44](https://github.com/davidcalikes/mypse.ie/issues/43)

* [Bug: Add code to prohibit access to restricted pages by way of direct URL #45](https://github.com/davidcalikes/mypse.ie/issues/45)

* [Bug: Users can change pupil id after id check #46](https://github.com/davidcalikes/mypse.ie/issues/46)

* [Bug: Referer code no longer blocking users from navigating direct to passport form from url #47](https://github.com/davidcalikes/mypse.ie/issues/47)

* [User Story: Page Titles & Favicon #48](https://github.com/davidcalikes/mypse.ie/issues/48)

* [Bug: Loading modal firing on click and covering incorrect id alert!#50](https://github.com/davidcalikes/mypse.ie/issues/50)

* [User Story: Pagination of lists #49](https://github.com/davidcalikes/mypse.ie/issues/50)

<br>

### User Stories Not Completed

The following issues were marked as 'wont have' and moved to the 'Future Features' column on the Sprint 4 Kanban board.

* [User Story: Create Print function for passports #22](https://github.com/davidcalikes/mypse.ie/issues/50)

* [User Story: Automatically delete passports for pupils no longer in school #15](https://github.com/davidcalikes/mypse.ie/issues/50)

<img src="../docs/agile_images/agile_us3.png">_Agile Issues_

<br>


### Sprint 4 Evaluation

Development time -- 11 days.

The final sprint of the Agile process was far less organised and ran far beyond the week-long time-frame I had originally set.  I allowed myself some flexibilty during this Sprint as this was my first attempt at using the methodology and I had made excellent progress during the initial three cycles. I feel the problem with sprint three was that some of the user story's were not fully defined and left too much to the subjectivity of the developer. For example the two 'must have' user stories 21 and 43 were not specific enough with respect to unit tasks. This is something I will be conscious of moving forward when utilising the Agile approach in future projects. 


## Agile Summary

The resulting minimum viable product, of the first iteration of MyPSE.ie would not have been possible without the myriad benefits of Agile. These include, the rapid development of a marketable MVP, the simple prioritisation and implementation of features, focus on individual tasks and the continuous feeling of improvement and delivery of tangible progress moving through the tasks.

From the perspective of a junior developer there are key aspects of Agile I will pay closer attention to in forthcomimg projects. 

* I will use Agile much earlier in development and make the process even more prominent during the planning stages while developing Epics and User Stories. This was difficult to implement as a solo developer, as I had to wear different 'hats' (Client, Owner, Developer(s) user(s) etc.).

* Given how much I have learned about creating Kanban boards, Issues etc, I think I will be more confident in my ability moving forward to predict the time it will take to complete each unit of work. This is especially applicable for future Django projects as my skill with the framework has grown significantly.

* Prioritisation is another area I feel I have a much better understanding of. With an app like MyPSE.ie it was very difficult to prioritise say accessibility features over security features. If pupil's could not use the app to create a passport in the first place then the security features would be redundant yet to create an app where a vulnerable users information is insecure would make the app unsafe for use. I aim to improve my ability prioritising issues in these cases as I continue my coding journey.

Return to main [README](https://github.com/davidcalikes/mypse.ie#agile) document.