
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

The Eight Epics Created:

1. [Sensical Epic 1: Setup Development environment, install packages, dependencies and early deployment.](https://github.com/davidcalikes/sensical.ie/milestone/1)

This Epic contains the initial development tasks including setting up the dev environment, installing packages, setting up the skeleton project, and Early deployment to Heroku.

<img src="../docs/agile_images/agile3.png">

<br>

2. [Sensical Epic 2: Add Login/registration functionality utilising Django AllAuth](https://github.com/davidcalikes/sensical.ie/milestone/2)

This Epic helps users to login/register to use the app and recieve benifits, such as the ability to save their purchase history and delivery details and also access the user wishlist feature. 

<img src="../docs/agile_images/agile4.png">

<br>

3. [Epic 3: Create general site structure and navigation elements referencing planning stage wireframes.](https://github.com/davidcalikes/sensical.ie/milestone/3)

The user stories associated with Epic 3 create the skeleton of the site that will allow most users to navigate through its contents. Add placeholder styles and content.

<img src="../docs/agile_images/agile5.png">

<br>

4. [Epic 4: Create Site Admin Functionality allowing site owner to CRUD products for sale.](https://github.com/davidcalikes/sensical.ie/milestone/5)

This Epic focuses on providing the site owner with the ability to upload and edit products for sale on the e-Commerce Webstore.

<img src="../docs/agile_images/agile6.png">

<br>

5. [Epic 5: Implement organisation of items and provide user search functionality.](https://github.com/davidcalikes/sensical.ie/milestone/7)

This Epic provides the users with search functionality and product categorisation features. Making it easier for users to find products they might like to purchase.

<img src="../docs/agile_images/agile7.png">

<br>

6. [Epic 6: Add Shopping Basket and toast messages functionality.](https://github.com/davidcalikes/sensical.ie/milestone/6)

The user stories and work units associated with Epic 6 Focus on helping users add items to a virtual shopping basket and providing visual feedback in the form of toast messages.
<img src="../docs/agile_images/agile8.png">

<br>

6. [Epic 7: Create Checkout and payment functionality utilising stripe.](https://github.com/davidcalikes/sensical.ie/milestone/8)

By far the most time-consuming and complex series of user stories where derived from Epic 7 and largely focused on adding payment functionality with Stripe.
<img src="../docs/agile_images/agile9.png">

<br>

6. [Epic 8: Tertiary features and backlogged bugs/issues. Finalise styling and formatting.](https://github.com/davidcalikes/sensical.ie/milestone/4)

Epic 8 implimented the tiertiary features of the application like hire packages and testimonials. There was also a significant project backlog of incomplete issues from earlier user stories that were addressed here.
<img src="../docs/agile_images/agile10.png">

<br>

## Agile User Stories

<br>

The User Stories created for reference within the Agile framework were derived from both the Epics created and also the empathetic User Stories I created as a result of planning research during the 'User Experience Design' phase of the project. I used GitHub Issues to create cards for Agile User Stories, Development Tasks, and Bugs.

The structure of a Sensical.ie Agile User Story can be seen below.

<img src="../docs/agile_images/us1.png"> _Agile User Story_

As evidenced above, the title of Each Agile User Story Issue can be more accurately thought of as a descriptive overview of the tasks within the Issue. The actual UX design User Story or Multiple Stories this issue will address is written at the top part of each Issue Card.

Each Issue Card contains:

* A Title: Descriptive overview of the issue/ticket

* The User Story the issue addresses

* Acceptance Criteria for each issue/ticket

* Tasks required to satisfy the acceptance criteria

* A label that determines the priority of each issue

* An assigned Kanban board

* An assigned Epic

<br>

The final amount of issues created totalled 55, of which 24 had the 'Developer Tasks' label, 18 had the 'Must Have' user story label 14 were labelled 'Should Have' 4 were tagged 'Could Have' and one was re-badged to a 'Won't have'. 5 were labelled as 'bugs' that I added during development. Some issues were given more than one label.

<img src="../docs/agile_images/us2.png">_Agile Issues_

The full list of issues for the project is available [here](https://github.com/davidcalikes/sensical.ie/issues?q=is%3Aissue+is%3Aclosed)

<br>

## Sprints

### Sprints Duration

Although I had a little experience working with the Agile methodology and Django as a framework from my previous project, I still felt I had few reference points that could inform my decision making when it came to allowing sufficient time for each sprint, whilst setting a realistic, achievable deadlines. Tackling unfamiliar API's like Stripe and Mailchimp meant that timeboxing for this project was always going to be more fluid than it would be for a more experienced developer or development team. 

### [Sensical.ie Sprint 1 -- Overview](https://github.com/users/davidcalikes/projects/12/views/1)

Learning from my last encounter with the Agile process I attributed significant amounnt of time just to get my development environment set up and th proper packages installed. This Sprint was very short and I included parts of project planning and creating the referance wireframes during this cycle.

<br>

### Developer Tasks and User Stories Completed During Sprint 1
<br>

* [Install Django and Gunicorn HTTP Server](https://github.com/davidcalikes/sensical.ie/issues/1)

* [Install Cloudinary storage and add requirements.txt file](https://github.com/davidcalikes/sensical.ie/issues/2)

* [Start Django Project and create Heroku App](https://github.com/davidcalikes/sensical.ie/issues/3)

<br>

### Sprint 1 Evaluation

Development time -- 3 days.

Sprint one was relatively straight forward as mentioned befor, I used time attributed to this cycle plan outside of the development environment. 

<br>

### [Sensical.ie Sprint 2 -- Overview](https://github.com/users/davidcalikes/projects/13)

Sprint 2 focused on adding Django Allauth user authentication functionality. 

<br>

### User Stories Completed During Sprint 2
<br>

* [Install Django Allauth](https://github.com/davidcalikes/sensical.ie/issues/4)

* [Add authentication and Email backends for Email account verification](https://github.com/davidcalikes/sensical.ie/issues/5)

* [User Story: Add Passport Form customisation #23](https://github.com/davidcalikes/mypse.ie/issues/23)

* [Developer Task: Import allauth templates for customisation](https://github.com/davidcalikes/sensical.ie/issues/7)

<br>

### Sprint 2 Evaluation

Development time -- 2 days.

The Second sprint was completed ahead of schedule and I found that my relative lack of experience in using both Django and Agile had caused me to create sprints with less work units than required. I think this was a reaction to my last project using Django where I tended to add to many user stories and tasks to each sprint. I compensated here by increasing the level of work units in sprint three.

<br>

### [Sensical.ie Sprint 3 -- Overview](https://github.com/users/davidcalikes/projects/14/views/1)

Sprint 3 focused on creating the skeleton structure for the front-end of the application. 

<br>

### User Stories Completed During Sprint 3
<br>

* [Developer Task: Create Home App for Landing page](https://github.com/davidcalikes/sensical.ie/issues/11)

* [User Story: Add base template and header content.](https://github.com/davidcalikes/sensical.ie/issues/8)

* [User Story: Add fontawesome Icons and create default Icon style rules.](https://github.com/davidcalikes/sensical.ie/issues/9)

* [Bug! Content overlapping in smaller screen widths](https://github.com/davidcalikes/sensical.ie/issues/12)

* [User Story: Add main navigation bar to base template.](https://github.com/davidcalikes/sensical.ie/issues/13)

* [User Story: Add footer with developer links.](https://github.com/davidcalikes/sensical.ie/issues/14)

<br>

### Sprint 3 Evaluation

Development time -- 5 days.

The third sprint was completed on schedule and again I found following each issue in turn to be extremely productive. This sprint focused on the creating the basic site structure and implimenting all of the main navigation functionality. I feel the amount of user stories and tasks in this sprint was close to optimal for a project of this scope.

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