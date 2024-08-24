# Web Test Automation Framework

This is a web test automation framework using Python and Playwright, structured with the Page Object Model (POM).

## Project Structure

- `po/`: Contains page objects representing the web pages.
- `reports/`: Contains a report.html file.
- `tests/`: Contains test scripts that execute the test cases.
- `setup.bat`: A batch file to set up the environment.
- `requirements.txt`: A file listing the Python dependencies.

## Setup Instructions

1. Clone the repository.
2. Run `setup.bat` to install dependencies and set up the virtual environment.


## Running Tests
- Make sure that the virtual environment is opened
- run this script on the terminal -> pytest --html=reports/report.html --self-contained-html


