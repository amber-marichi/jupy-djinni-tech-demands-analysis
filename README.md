# Djinni Python keywords found statistics
Parse current vancancies on Djinni.co to make a pandas dataframe. Analyzing it may help to understand the most demanded technologies on the tech market right now by count of relative words from parsed descriptions.

## Features

- asynchronous web parsing with aiohttp and asyncio
- text processing with nltk with possibility to create and maintain custom stopwords sets
- store results in files to be able analize them without additional parsing
- convenient set of filds (views, date of post, experience required etc) for parsed data to have various possibilities to analyze and compare
- step by step procedure in jupyter file with comments and variables to set changes inplace
- customizable naming and location for files and folders to make things more understandable


## Setting up project and getting started

Install using GitHUB
```sh
git clone https://github.com/amber-marichi/jupy-djinni-tech-demands-analysis.git
cd jupy-djinni-tech-demands-analysis
```

### To run locally

!! Python3.8+ with pip should be installed and ready.

1. Create and activate venv:
```sh
python -m venv venv
```

2. Activate environment:

On Mac and Linux:
```sh
source venv/bin/activate
```
On Windows
```sh
venv/Scripts/activate
```

3. Install requirements:

```sh
pip install -r requirements.txt
```

4. Check the "config.py" file to get the idea about urls to parse, folders name, stopwords files. Feel free to make changes according to general logic of project (add/modify custom stopwords files, change url to another pl, make additional folders etc).

5. Proceed to file "main.ipynb" and follow instructions there step-by-step.
