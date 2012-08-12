I have a collection of flickr tools/app that i'm gonna move over a django project. For now i've migrated just one.

# Dynamic flickr sets based on tags

## Why 

I love using [ifttt](http://ifttt.com) to automate replication of content over different services. I have one task setup to upload instagram photos to flickr so my family and some old school friends can see them (basically people that don't know/give a crap about [instagram](http://instagram.com)). 

Currently [ifttt](http://ifttt.com) can upload this pictures to your photostream providing a tag attached to them. That's about it, you can't put them on a set dynamically based on given criteria. Also this pictures are uploaded with 'only family' permissions.

This app just do that. Scans your photostream for pictures with given tags, make them public and put them in predefined sets.

## Non pip requirements

+ Python 2.7
+ pip
+ virtualenv
+ Some messaging service compatible with celery, i use [redis](http://redis.io)
+ a db compatible with django, i use sqlite 3 in dev, postgres or mongodb in prod. If you are not familiar how django manages dbs go [here](https://docs.djangoproject.com/en/1.3/ref/databases/)
+ your user id, the real one, not the login id. Get it [here](http://idgettr.com/)
+ your own key and secret for the flickr api. Get it [here](http://www.flickr.com/services/apps/create/apply/)

## Installation

Any settings override (Database config, broker message config, etc) are conveniently made inside **settings_local.py**. Just copy the demo file:

```bash
cp flickrtools/settings_local_demo.py flickrtools/settings_local.py
```

and start customizing whatever you want/need.


```bash
fab DEV setup
```


## Setup

We need to set up a flickr api access and some dynamic photosets to make this work. Open a django shell:

```bash
source bin/activate
python flickrtools/manage.py shell
```

initialize an Access and Photoset instances to meet your needs

```python
from flickrauth.models import Access
from photosets.models import Photoset
access=Access()
# this is an example userid get your own with http://idgettr.com/
access.user='19332439@F09'
# this is an example (key,secret), get your own at http://www.flickr.com/services/apps/create/apply/
access.key='daskdaksdl1231231'
access.secret='daskdaksdl1231231'
access.save()
# set up your photoset
photoset=Photoset()
photoset.access=access
photoset.title='My title'
photoset.tags='tag1,tag2,tag3'
photoset.save()
```

With this two instances the script will search for photos that belongs to the user and have all those tags. It will then create the photoset, if it does not exits in flickr, and assing the photos to the photoset via a async celery task.

Just so you know, you could go nuts with it. Create several access instances and photosets. The bottleneck is at adding the photos one by one to  the flickr set and that's where celery pays. The script itself should run in a couple of seconds.

## Run the script

Start your message broker, mine is redis so:

```bash
redis-server
```

Start your celery instance with django:

```bash
python manage.py celeryd --loglevel=info
```

Run the management command (aka script)

```bash
python manage.py scanfortags
```

The first time, it will open a browser and ask you to accept/reject access to the flickr api on your behalf. Just accept, come back to the terminal and press enter to continue.

## That's about it, enjoy.