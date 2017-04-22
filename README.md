# Pelican project to build embeddedlog.com

## Installation instructions

General documentation from the [Pelican website][1].

```
pip install pelican
pip install markdown
```

```
git clone --recursive https://github.com/carlosperate/carlosperate.github.io.git 
```


## Repository structure

* **embeddedlog**: Pelican project directory.
* **plugins**: Pelican plugins used (downloaded or created for purpose).
* **themes**: Tested themes, and the theme created for the website.


## Building the website

From the root directory of this repository:

```
pelican embeddedlog/content -s embeddedlog/pelicanconf.py
```

For test general deployment options without using the full deployment script,
change the following line from `embeddedlog/pelicanconf.py`:

```
DEPLOY_RUN = False -> DEPLOY_RUN = True
```

For the final publishing the `publishconf.py` script imports the
`pelicanconf.py` and updates or adds values:

```
pelican embeddedlog/content -s embeddedlog/publishconf.py
```


## Test output in C9

If you are reading this document it might not be clear what the content on
this section is refering to, this is just a reminder for myself on how to set a
server to preview the ouput within my development environment.

```
cd ~/workspace/pelican-project/embeddedlog/output
sudo python -m SimpleHTTPServer 8080
```

http://pelican-website-carlosperate.c9users.io:8080



[1]: http://docs.getpelican.com/en/stable/install.html
