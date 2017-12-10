# LogMyRow
A Django app that can log indoor rowing workouts.

## Local Environment Setup
1. Make sure your local machine is set up with: Python, Django & Virtualenv
  - [Max OS Instructions](https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux/)
  - [Windows Instructions](https://www.codingforentrepreneurs.com/blog/install-python-django-on-windows/)

2. Clone the project ```git clone https://github.com/ashleyelaine/LogMyRow``` or download zip

3. Navigate to the root directory of the project and run ```virtualenv -p python3 .```

4. Run ```source bin/activate``` on Mac/Linux or ```.\Scripts\activate``` on Windows

5. Navigate to the ```src``` directory and run ```pip install -r requirements.txt```

6. Run ```python manage.py runserver``` and you should be able to view the app locally at: http://127.0.0.1:8000/


## Future Plans
1. Add ability to have multiple users with logins
2. Add charts to visually represent data & be able to show improvements over time
3. Calculate & display average Meters/Hour
4. Be able to input a baseline goal of Meters/Hour and visually track whether meeting the goal or not
5. Add seconds to Total Time field
