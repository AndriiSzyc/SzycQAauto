# Modular-Based Testing Framework for Automated Testing

## Description
This framework was developed to automate API and UI testing on GitHub.com. Also contains a database testing module and test cases for HTTP responses.

In this Framework, the tester can create test scripts module-wise by breaking down the whole application into smaller modules as per the client's requirements and creating test scripts individually. A modular-driven framework ensures the division of scripts which leads to easier maintenance and scalability. You can write independent test scripts.

## How to Install and Run the Project
Steps required to install the project and also the required dependencies.
1. Clone this repository.

2. Go to the project folder and install dependencies:

          1. Pytest - pip3 install pytest --user

          2. Request - pip3 install requests --user

          3. Selenium - pip3 install selenium --user

          You may need to install it as a superuser
3. Download ChromeDriver for Selenium.
              Go to the link https://chromedriver.chromium.org/downloads. Select the driver according to the Chrome version, and then select the platform.

4. To test the API, you will need a GitHub token. I wrote my GitHub token into an environment variable (I use Linux Ubuntu) and called it using the class GitToken.

In the terminal, enter the command pytest which will automatically find all the tests and run them.

## Usage
In most web applications, we have a few sets of actions that are always executed in a series of actions. Rather than writing those actions again and again in our test, we can club those actions into a method and then call that method in our test script. Modularity avoids duplicity of code.

This means that we can run our tests on each unit under test separately, or we can run all tests.
The generated pytest.ini file contains markers. Marks are a special marking of tests to combine them into groups.

If you need to run all the test scripts, just type the pytest command in the terminal.

However, you do not need to test the entire product with tests to solve your working question. If you want to check its small component, then in the terminal you need to specify the pytest command - m <mark.name>

For example, to call test cases for API only:  

                                                  pytest -m api
