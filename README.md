# dealcrawler
Simple django and scrapy integration for crawling deal site.

# README #
### What is this repository for? ###

* Simple django and scrapy integration for crawling deal site.
* Version 1.0

### How do I get set up? ###

  1. We need to install `virtualenv` and `virtualenvwrapper`.  You visit this link for the installation guide: [Virtualenv and Virtualenvwrapper](http://bicofino.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu-14-dot-04/)
  2. Clone the project in your local machine: `git@github.com:iamriel/dealcrawler.git`
  3. While the virtual environment is activated, you need to install the project dependencies. Go to the root directory of the project and run `pip install -r requirements.txt`.  This may take a while.  If you encounter an error, please google it first as it is just caused by missing dependencies.
  4. After the installation, run the command `./manage.py migrate`. This will create the database tables used in the project.
  5. After that, we need to load our initial data, run the command `./manage.py loaddata deals/fixtures/country.json`.  This will load the data about the countries.
  6. To access the admin page, run the command `./manage.py createsuperuser` and follow the instructions.
  7. You should be able to run the server by now: `./manage.py runserver` and visit `localhost:8000`, the admin page is in `localhost:8000/admin`

### Runing the spiders ##

  1. You can run the spider by going to `scraper` directory and just run the crawl command `scrapy crawl spider_name`.  For this setup, we only have one spider which is `metro_deal` so you can run `scrapy crawl metro_deal`.
  2. You can access the data in the admin page.
  3. You can also run the spiders by a management command `./mange.py runspider company_name`. For this setup, `./manage.py runspider metrodeal`.  You can see the companies in the django admin.


### TODO  ###

  * The spiders can be ran periodically using celery.  This can be done easily by following the docs in celery.


### Who do I talk to? ###

* Riel (me@iamriel.com)