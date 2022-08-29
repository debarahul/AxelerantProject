Selenium Hybride Framework
(Selenium with python, PyTest, Page Object Model, HTML Report)

About Framework:
Framework is an organized way of maintaining automation files. In the Framework all the files will communicate with each other to perform certain tasks.
Framework is a code structure that makes code maintenance easy and efficient. Without frameworks, users may place the “code” and “data” at the same location which is neither reusable nor readable. Frameworks produce beneficial outcomes like increased code reusability, higher portability, reduced cost of script maintenance, better code readability
Objective:
1) Re-usability
2) maintainability

Hybrid Driven Framework:
Hybrid Framework in Selenium is a concept where we are using the advantage of both Keyword driven framework as well as Data driven framework. It is an easy to use framework which allows manual testers to create test cases by just looking at the keywords, test data and object repository without coding in the framework.

Execution Command:
For run the Regression Test Case: (Regression is marker name)

	pytest -v -m "regression" --html=Reports\report.html testCases/ --browser chrome

Run the test cases using the window batch file:

	Go to the project location run the batch file run as Administrator.


In the framework there are the, which are used to perform automation. (Selenium with python, PyTest, Page Object model, HTML Report)
Automation Site :- "http://automationpractice.com/index.php"

Setup the framework explained step by step:

Step 1: Created a New Project File

step 2: Installed Required Packages/plugins

	Selenium: Selenium libraries
	Pytest: Python unit test framework
	pytest-html: Python HTML Report
	pytest-xdist: Run test cases parallel

Step 3: Created Folder Structure

       Project Name
		 |
		PageObjects (package)
		 |	
		testCases (package)
		 |
		utilities (package)
		 |
		Configurations (folder)
		 |
		Logs (folder)
		 |
		Screenshots (folder)
		 |
		Reports (folder)
		 |
		DriverDetails (folder)
		 |
		TestData (folder)
		 |
		run.bat (Window batch File)

Step 4: Automating Test cases

        Created a PageObjects class under the PageObjects package
	 Created testcases under Testcases package
		Created a conftest.py under test case for removing duplicate of driver use.

step 5: Added a configuration file (.ini file) for reading common values and use in the test cases

	Add config.ini file in the Configuration folder.
	Created a readProperties.py utility file under utilities package to read common data from config.ini file.

step 6: Added logs for test cases(logging will help to debug the test cases)

	Created a customLogger.py under utility package folder.
	Add logs to all test cases with proper information

step 7: Created file for run test cases on desired browser

	Update conftest.py with required fixtures which will accept command line argument (--browser)
	We can use PASS browser name as argument in command line (e.g. --browser chrome)

step 8: Added code for generating pytest HTML Reports

	Added code for generating HTML report on conftest.py file.
	Now we can pass html report name as an argument in the command line. (e.g. --html=Reports\report.html)

step 9: Grouping test cases help of pytest markers

	Created pytest.ini file under testCases for custom marker name.
	Add markers to every testmethod (e.g.: @pytest.mark.sanity)
	Now we can pass marker name as argument in the command line (e.g. -m "marker name"), Mentioned marker group test cases will run only.

step 10:Create a window batch file for run the test cases in command prompt.

	Added a file run.bat, added the command line argument in that file.
	Run the "run.bat" file in command prompt

Step 11:Push the test cases to the git repository.

