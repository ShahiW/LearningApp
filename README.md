# LearningApp - Django Project

The idea behind the app is for children to have fun repeating and practicing what they have learned at school. 

Both pupils and teachers get their own accounts. The teachers can track the progress of their students and the children have the opportunity to collect medals and master increasingly difficult tasks (levels). 

The app will also be expandable so that other subjects can be practiced - at the moment it is only one subject: math.

One idea for the future would be to introduce a student chat that is monitored by the teachers.


## Setup

Clone this repo, setup a venv and install django:

``` bash
python3 -m venv .venv
source/.venv/bin/activate
pip install --upgrade pip wheel setuptools
pip install django
```

Apply default migrations from Django:

```bash
python manage.py migrate
```

Install Bootstrap:

```bash
```
