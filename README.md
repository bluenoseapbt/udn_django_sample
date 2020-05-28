# UDN Particpants Sample Application - Part 1 Web Application using Django

This project contains two views, a form that gathers information on a participant and a list of all participants with 
their data in a table. It also has the ability to edit entries in the table by double clicking on a cell. In addition to
that, there is also an Update button that can also be used to update participant information. 

The table contains a pulldown menu that contains the Review Status. Clicking on the pulldown and selecting a value will 
automatically update the participant data by using ajax and sending the request to the server.

The form contains the following data:
● Participant Name 
● Participant Age 
● Does Participant have any siblings? 
● Known environmental exposures 
● Known genetic mutations 

After submitting information a list view is displayed where each participant and the values they entered are present. 
There is an additional dropdown box for each participant that contains 3 values (Not Reviewed, Reviewed - Accepted, 
Reviewed - Not Accepted). Changing dropdown should saves this field alongside the participant data. 


# Please Note: 
A sample user has been created that can be used to login into the application. The user credentials are:
* username: test
* password: password123$


# Part 2
1. What are some measures that can be taken to secure the application and to only show data for the user logging in?
    a. There are several ways that this can be accomplished. One way is to use ldap where the application access can be
    defined in a realm. 
    b. Another way to isolate user data is to use the Oauth 2.0 protocol. The data would be retrieved for the user
    logging in. A good explanation of how this works is https://medium.com/@darutk/the-simplest-guide-to-oauth-2-0-8c71bd9a15bb

2. What are some ways in which the above mentioned workflow could be made more dynamic from a UI/UX perspective?
    a. A new user interface would need to be created that would show only the data for the authorized user. The current
    implementation shows all participant data and in order to show data for an authorized user, the data would need to be
    partitioned per user. That is, the data model would need to be updated so that each authorized user has their own database
    tables which could be based off an authorization token.
    
Development
---

To setup the environment

    $ ./dev-setup.sh

To run the script

    $ ./run.sh
    
Launch a web browser and enter the url: http://localhost:8000
You will be directed to a login screen where you can enter the default user specified above.

