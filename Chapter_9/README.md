# Chapter 9 SLM Judging LLM Example

### Step 1: Activate the Virtual Environment
Create a directory we used virtual_env for our example.

On Windows/macoS/Linux:
```sh
python3 -m venv virtual_env/
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

Requires Ollama running and the tinyllama SLM pulled.

You can install transformers and other necessary libraries via 
```pip install -r requirements.txt```

# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.
