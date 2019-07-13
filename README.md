# Pelican project to build embeddedlog.com

## Installation instructions

This repository has submodules, so make sure they are initialised after clone:

```
git clone --recursive https://github.com/carlosperate/carlosperate.github.io.git 
```

General documentation also found in the
[Pelican website](http://docs.getpelican.com/en/stable/install.html).

```
pip install pelican
pip install markdown
pip install requests
pip install feedparser
pip install scrapy
```

Or if you have pipenv:

```
pipenv install .
```

## Repository structure

* **embeddedlog**: Pelican content directory.
* **plugins**: Pelican plugins used (downloaded or created this website).
* **themes**: Tested themes, and the theme created for the website.


## Building the website

From the root directory of this repository:

```
pelican -s pelicanconf.py
```

For the final publishing output the `pelicanconfpublish.py` script imports the
`pelicanconf.py` and updates or adds values:

```
pelican -s pelicanconfpublish.py
```
