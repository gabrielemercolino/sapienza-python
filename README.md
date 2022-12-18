# Repo of python homeworks

## Table of contents
- [intro](#intro)
- [installation](#installation)
- [run tests](#run-tests)


## Intro
Here I upload my homeworks.

In particular inside `homework` there are, obliviusly, the homeworks wich are necessary to get access to the final exams. Everithing else is just for exercise

## Installation
Everithing inside this repo is based on **Python 3.9**.

I used anaconda to get everything set up.

**Attention**: if you use anaconda every time you need to use the console you have to activate the enviroment using:
```bash
conda activate <env name>
```

You will also need to install this packages:
```bash
conda install -c conda-forge typeguard
conda install -c conda-forge ddt
conda install -c conda-forge pytest-timeout
conda install -c conda-forge stopit	
conda install -c conda-forge pytest-profiling
conda install -c conda-forge radon
conda install -c conda-forge typeguard
```
If you use *Spyder IDE* you can also install
```bash
conda install -c conda-forge spyder
conda install -c conda-forge spyder-unittest
conda install -c conda-forge pylsp-mypy
```
If you prefer *Pycharm* (like me) you can also install the `line-profiler` extension  

When you want to update all the packages you can use
```bash
conda update --all
```
## Run-tests
To run the tests (only the programs inside `homework`) you can use the unittest in Spyder or `cd` inside the correct root, like:
```bash
cd <path>/homework/8\ -\ obbligatorio
```
and the run:
```bash
pytest test_01.py -v -rA
```
You can also add the following switches to get more info:
- `--profile` to get the top 10 longest calls (not very useful if you use the line-profiler)
- `--durations 0` to get a more detailed list of times for every test (idk, even without it is printed, I'm literally copying what my teacher wrote)
- `-x` to stop to the first failure (useful in production but usally here there is only working code)