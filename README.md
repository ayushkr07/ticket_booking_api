# ticket_booking_api

## Prerequisite..
 - Python-3
 - Django(Backend Framework)
 - Django Restframework(Rest Framework)
 - Pytest(Testing Framework)
 
## Database
  - Sqlite
 
 ## Basic SetUp
1. Install VirtualEnvironment setup : *pip install virtualenvwrapper-win*
2. Create VirtualEnvironment and activating: *mkvirtualenv project*
3. Create new folder : *mkdir pro*
4. clone the repo inside folder(pro): *git clone https://github.com/ayushkr07/ticket_booking_api.git*
5. Install all the dependencies: *pip install -r requirements.txt*
6. Run the project: *python manage.py runserver*

## Testing
  - Write in terminal : *py.test*

## Admin Panel
  - username : test
  - password : Test@123

## Output

#### An endpoint to view all the tickets.
![](images/get_all_ticket.png)

#### An endpoint to book a ticket using a user’s name, phone number, and timings.
![](images/1(a).png)
![](images/1(b).png)

#### An endpoint to update a ticket timing.
![](images/2.png)

#### An endpoint to view all the tickets for a particular time.
![](images/3.png)

#### An endpoint to delete a particular ticket.
![](images/4.png)

#### An endpoint to view the user’s details based on the ticket id.
![](images/5.png)

#### Auto Expire ticket code.
![](images/expire_ticket_code.png)
