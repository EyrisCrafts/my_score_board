# Live score board 

## Overview

This is a library implementation in python of a live score board. The library can start matches, update scores and finish matches for multiple teams at a time.

## Setup

### Create the environmnet

Create a python environment

```
python3 -m venv venv
```


Activate the environment

```
source venv/bin/activate
```

### Install dependencies

```
pip3 install -r requirements.txt
```

### Run setup

```
pip3 install -e .
```

# Run the tests

Execute in the root directory

```
pytest
```

# Important NOTE

### There is a problem with the get summary example in the exercise.
### The requirement is that the get summary function should sort by total score first and then most recent match. But the example given example has Uruguay vs Italy match before Spain vs Brazil in the summary
