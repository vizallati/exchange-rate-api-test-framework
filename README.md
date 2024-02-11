# Table of Contents

1. [Exchange Rate API Test Framework](#playwright-test-automation-framework)
   1. [Features](#features)
   2. [Getting Started](#getting-started)
      1. [Prerequisites](#prerequisites)
      2. [Clone Repository](#clone-repository)
      3. [Installation](#installation)
      4. [Running Tests](#running-tests)
      5. [Generating Allure Report](#generating-allure-report)
      6. [Issues found](#issues-found)
      
# Exchange Rate API Test Framework

This repository contains an automated test framework for the ExchangeRate API provided by ExchangeRate-API. The framework is implemented in Python, incorporating Behavior-Driven Development (BDD) principles using Gherkin syntax and Allure reporting for comprehensive test result analysis.

## Features
BDD Testing: Adopt Behavior-Driven Development by expressing test scenarios in Gherkin syntax. Write clear and concise feature files in the features directory.

Allure Reporting: Generate detailed and visually appealing test reports with Allure, providing insights into test execution, failures, and trends.

## Getting Started
### Prerequisites
Before you begin, ensure you have met the following requirements:

[Python 3.11](https://www.python.org/downloads/release/python-3110/) or higher

Allure (installation instructions [here](https://allurereport.org/docs/gettingstarted-installation/))
### Clone Repository
To clone the repository, run the following command in your terminal:


```bash
git clone https://github.com/vizallati/exchange-rate-api-test-framework.git
```
### Installation
1. Navigate to the project directory 
```bash
cd exchange-rate-api-test-framework
```
2. Create virtual environment
```bash
python -m venv virtual_environment
```
3. Activate virtual environment
```bash
# On Windows
virtual_environment\Scripts\activate
# On macOS/Linux
source virtual_environment/bin/activate
```
4. Install the required dependencies

```bash
pip install -r requirements.txt
```
### Running Tests
Before running the tests edit the settings.yml with respective values

Run the tests using the following command:

```bash
pytest
```
This command will execute the tests and generate Allure report data in the allure-results directory (These run configurations are all set in the pytest.ini file)

### Generating Allure Report
To generate and view the Allure report, run the following commands:

```bash
allure serve allure_results
```
This will generate the Allure report and open it in your default web browser.

### Issues found
I was not able to find any issues to do with behaviour of api endpoints but with the vague error messages returned after making requests with unsupported currency codes. To enhance the debugging process, it is recommended that the error messages include specific details about the encountered error like the actual unsupported code.