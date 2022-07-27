## Execute the project
```
cd <project_directory>
python convert_locale_json.py

```

## Code Files
### 1. convert_locale_exceptions.py
#### This file contains custom exceptions for project
Custom exceptions are handled within this file

### 2. convert_locale_json.py
#### Main file to convert the json format
a. It loads the json file and check the file is loaded properly.
b. It also validates the json which is loaded from file.
c. It converts the json input into expected json output

** For example **

** Example Input Json :  **
{"msiPropertyName1": {"it_IT": "value 1", "en_US": "value2"}, "msiPropertyName2": {"it_IT": "value3", "en_US": "value4"}}

** Exaample Output Json: **

{"it_IT": {"msiPropertyName1": "value1", "msiPropertyName2": "value3"}, "en_US": {"msiPropertyName1": "value2", "msiPropertyName2": "value4"}}

### 3. test_locale.py
#### This file performs the unit test cases

** It checks two cases: **

a. One is json file path validation.
b. Checks the json input and output matches.
