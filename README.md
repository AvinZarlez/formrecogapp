# About this project

This project was created by following [Quickstart: Use the Form Recognizer client library](https://docs.microsoft.com/en-us/azure/cognitive-services/form-recognizer/quickstarts/client-library?tabs=windows&pivots=programming-language-python)

# Setup

1. Install Python3
   * Make sure you have the correct version of python installed!
   * To confirm you local python installation, run this command:
      ```PowerShell
      python --version
      ```
   * You can download Python 3 [here](https://www.python.org/downloads/).

1. Clone this Repository
   * Open a terminal, and navigate to the directory where you want to clone the repo to, then clone the repo.
   * Make sure that you have access and know how to authenticate before attempting to clone it.

1. Create Python Virtual Environment.
   * Open the repository folder in your terminal of choice.
   * Create a Python virtual environment named `venv` for the project
      ```PowerShell
      python -m venv venv
      ```

1. Active the newly created virtual environment
   * **Note**: If you are using PowerShell, make sure that the Execution Policy has been set, for example, from a PowerShell prompt running as Administrator, run:<br></br> `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`
   * Run the following script to automatically set up the virtual enviroment:
      From PowerShell:
    
      ```PowerShell
      .\venv\scripts\activate.ps1
      ```

      From a Command Prompt:

      ```PowerShell
      .\venv\scripts\activate.bat
      ```

      on MacOS:

      ```PowerShell
      source venv/scripts/activate
      ```
   * You should now see `(venv)` in front of the prompt in your terminal.  For example, with a PowerShell prompt: 

      ```PowerShell
      (venv) PS C:\path\to\project>
      ```
   * **Note**: If need to get out of the virtual enviroment at any point, you can use the following command:
      ```PowerShell
      deactivate
      ```

1. Install dependencies
   * Once the virtual environment has been activated, install the required PIP packages with:
      ```
      pip install -r requirements.txt
      pip install -r requirements-dev.txt
      ```

# Development
##  IDE
* Use visual studio code 
  * enable python lint
  * select pylint as linter

### Adding the Python Extension to VSCode

To faciliate a richer Python development experience in Visual Studio Code, you should install the Python Extension

1. Open the repository folder in Visual Studio Code.

1. From the extensions panel, search for Python, and install the Python Extension from Microsoft.


## Lint and formatting


### Pylint

Install `Pylint`

```bash
pip install pylint
```

Run `Pylint`

```bash
pylint src --output-format=colorized --rcfile=".pylintrc" # lint the source directory
```

### Black

[`Black`](https://github.com/psf/black) is an unapologetic code formatting tool.

```bash
pip install black
```

Format python code

```bash
black -l 100 .
```

## Unit tests

### Executing
```
pytest tests
```

### Reporting
```
pytest tests --doctest-modules --junitxml=junit/test-results.xml --cov=driver_training --cov=pipeline --cov-report=xml --cov-report=html -o junit_family=xunit2
```

## Configuring Environment Variables

You can change some application settings through environment variables.

None of these are required to be set, and all have default values.

However, you can customize the  environment variable

1. Add a .env file named `.env`. Ex: `ENV_VAR=some-value`
1. Use a tool like `Set-PsEnv` to set the environment variables in a PowerShell instance. [Link to Set-PsEnv](https://www.powershellgallery.com/packages/Set-PsEnv/0.0.2)
1. Configure them manually using the Environment Variables on your machine. `Control Panel > System Properties > Environment Variables.. > System Variables > New...`
