# Chapter 9 SLM Judging LLM Example

## Pre Requisites:

You should have already installed ollama at v0.5.0+ and have it capable of running tinyllama. You can do this in a virtual environment, or not depending on preference. 

install Ollama:

```curl -fsSL https://ollama.com/install.sh | sh```
or
```pip install ollama```

On linux once installed it should be avealable on localhost at port 11434, but if it's not or you operatorint system requires you to manually start it run:

```ollama start```

Once it's running pull the tinyllama model:
```ollama pull tinyllama```

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

### Step 2: Install Dependencie

Requires Ollama running and the tinyllama SLM pulled.

You can install transformers and other necessary libraries via 
```pip install -r requirements.txt```

# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.

### Step 3 Run the test
DeepEval is a CLI. You'll notice there's no main function in our script. To run the script use 
``` deepeval test run test_deepeval1.py```