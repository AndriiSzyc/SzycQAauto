# Modular-Based Testing Framework for Automated Testing

# Description
This framework was developed to automate API, UI testing on GitHub.com. Also contains a database testing module and test cases for HTTP responses.
In this Framework, the tester can create test scripts module wise by breaking down the whole application into smaller modules as per the client requirements and create test scripts individually. Modular driven framework ensures the division of scripts that leads to easier maintenance and scalability. You can write independent test scripts.

# How to Install and Run the Project
Steps required to install project and also the required dependencies.
1. Clone this repository.

2. Go to the project folder and install dependencies:

          1. Pytest - pip3 install pytest -U

          2. Request - pip3 install requests -user

          3. Selenium - pip3 install selenium --user

          You may need to install as superuser
3. Download ChromeDriver for Selenium.
              Go to the link https://chromedriver.chromium.org/downloads. Select the driver according to the Chrome version, and then select the platform.
              
4. To test the API, you will need a GitHub-token. I wrote my GitHub-token into an environment variable (I use Linux Ubuntu) and called it using the class GitToken.

In the terminal, enter the command pytest which will automatically find all the tests and run them.
