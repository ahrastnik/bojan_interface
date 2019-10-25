# Bojan interface
Interface software for the 2-axis drawing CNC, named Bojan

## Installation instructions
- Install Python: https://www.python.org/downloads/release/python-375/
- Install Git: https://git-scm.com/
- Clone the repository in a directory of your choice: *git clone git@github.com:ahrastnik/bojan_interface.git*
- Install the python virtual environment manager: *pip install virtualenv virtualenvwrapper-win*
- Setup the project virtual environment:
    - Create the project virtual environment: *mkvirtualenv bojan*
    - Make sure you are located in the root project directory
    - Set the virtual environment project directory: *setprojectdir .*
    - Install all project-required modules: *pip install -r requirements.txt*

## Development instructions
### Installing a new module
After running *pip install "module"*, update the project requirements list, by running *pip freeze > requirements.txt*
