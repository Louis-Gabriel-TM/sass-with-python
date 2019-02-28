# Basic **sass** compilation with python library _libsass_

> Just a little script to compile scss to css file.


## Links
- [SASS tutorial on official website](https://sass-lang.com/guide)
- [libsass module repository](https://github.com/sass/libsass-python)

## Python side

### Requirements
- Python 3.6 (because of f-strings)
- libsass python module

### lib installation
On Linux system:
1.  `python -m venv venv`*
2.  `. venv/bin/activate`
3.  `pip install libsass`

*you can skip virtualenv step if you are a dirty dev. 

## How to
> This version of the script convert a file named _main.scss_ to a file named _main.css_.
> _main.scss_ have to be next to _compile.py_, _main.css_ will be created at the same place, and overwritten each time _compile.py_ is runned.

1. create a valid scss file named _main.scss_
2. run the script with `python compile.py`
