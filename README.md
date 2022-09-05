# Metta Forum

#### Video Demo: <URL [HERE](https://youtube.com)>

#### Visit website deployed on heroku: <URL [HERE](https://metta-forum.herokuapp.com/)>

#### Github Repo: <URL [HERE](https://github.com/LD8/metta)>
#### Description

This is a Django engined forum, a platform for users to share their meditation experiences.

##### The goal

Metta in Pali means _mercy_ or _loving-kindness_, _friendliness_, _goodwill_.

The goal of any Meditation is for the practitioner to gain awareness and, like any other practices, it is crucial for them to communicate with one another in order to become a better practitioner. This forum will hopefully offer a cosy atmosphere in a minimal setting where people can share freely of their experiences and discuss their meditation techniques lovingly, friendly and in goodwill.

##### What can users do here?

Users can:

- sign in
- post related content
- comment on others' posts
- search for interesting subjects and so on

#### Technical Sheet

- Bootstrap
- SASS, CSS3
- Django with SQlite

##### Folder structure

```bash
./
├── forum/            # module to handle forum part of the logic as an app by itself
│ ├── migrations/     # db migrations
│ ├── static/         # static files (CSS, images, fonts)
│ ├── templates/      # html files for forum module
│ ├── admin.py        # register models
│ ├── apps.py         # entry of the module
│ ├── forms.py        # define form models for Topic, Post, Comment
│ ├── models.py       # define db models for Topic, Post, Comment
│ ├── tests.py
│ ├── urls.py         # register url paths (to link paths and view logics)
│ └── views.py        # view logics
├── metta/            # the main setups
│ ├── __init__.py
│ ├── asgi.py         # https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
│ ├── settings.py     # main configs for Django framework
│ ├── urls.py         # register url paths for different apps (forum and users in this case)
│ └── wsgi.py         # https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
├── templates/        # global template to handle status code 404 and 500
│ ├── 404.html
│ └── 500.html
├── users/            # module to handle user authentication part of the logic
│ ├── migrations/     # db migrations
│ ├── templates/      # html files for users module
│ ├── __init__.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py         # register url paths (to link paths and view logics)
│ └── views.py        # view logics
├── Procfile
├── README.md         # README doc file
├── datadump.json     # a copy of db
├── db.dump
├── manage.py         # Django's command-line utility for administrative tasks
├── requirements.txt  # packages required
└── runtime.txt
```

#### At the end

I built this website 2 years ago as a practice project. Although I did not have a systematic understanding of computer science, I learned a great deal on building a project with a python framework.

However, after 3 years working as a frontend engineer and UX designer, CS50 at Harvard University offered me the chance to explore the fundamentals of computer science (`C` specifically and the memory section of the course), which certainly helps me to grasp the bigger picture when I design and build web apps or any software in the future.

Therefore, THANK YOU CS50!
