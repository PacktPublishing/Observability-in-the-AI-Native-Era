# Natural Langurage Process Scoring Examples

These folder includes the natural language process scoring examples included in Chapter 5 plus one extra that didn't make it into the book. 

This project uses a virtual environment (venv) to manage dependencies.

## Instructions

### Step 1: Activate the Virtual Environment
Create a directory we used virtual_env for our example.

On Windows/macoS/Linux:
```sh
python -m venv virtual_env/
```

To activate the virtual environment, open your terminal and run:
- On Windows:
  ```sh
  .\virtual_env\Scripts\activate
  ```
- On macOS and Linux:
  ```sh
  source virtual_env/bin/activate
  ```
Where Folder is the location of the python environment. 

### Step 2: Install Dependencies
Once the virtual environment is activated, you can install the required dependencies by running:
```sh
pip install -r requirements.txt
```
Please note that some of these dependencies can be somewhat large. Check your system capabilities before installing.

### Step 3: Use the Project
These scripts are examples of how to use Python libraries for Natural Language Processing (NLP) scoring.

To run any example script, simply navigate to the project directory and execute the corresponding Python file using:
```sh
python example_bert.py
```
Use the same commandstructure for any of the scripts here.
