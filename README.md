# course stream in django :notebook: &nbsp;[![](https://camo.githubusercontent.com/17fa56d1fbad7bb4082c9711a77b984b85e79446/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e362d627269676874677265656e2e737667)](https://python.org)

 - In this repo I have developed online learning platform like udemy. In this project free courses as well as paid courses both are developed.
 - This project are on the way so some features may be not work.

[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

# How to run the project? :thinking:
**1).** Run all command manually
  - Clone github repository in your local system  `git clone https://github.com/yogeshnile/course-stream-in-django.git`
  - Move in course-stream-in-django repository  `cd course-stream-in-django`
  - Create new virtual python environment  `python3 -m venv venv`
  - Activate virtual python environment  `source venv/bin/activate`
  - Install all the libraries mentioned in [requirements.txt](https://github.com/yogeshnile/course-stream-in-django/blob/master/requirements.txt)  using  `pip install -r requirements.txt`
  - Run Django project  `python manage.py runserver`
  - Go to your browser and type http://127.0.0.1:8000/ in the address bar.
  - Hurray! That's it. <br>


**2).** Run Shell Script
  - Clone github repository in your local system  `git clone https://github.com/yogeshnile/unix.git`
  - Give execute permission to [course-stream-in-django.sh](https://github.com/yogeshnile/unix/blob/master/course-stream-in-django.sh) file via  `chmod +x course-stream-in-django.sh`
  - Run course-stream-in-django.sh file using `./course-stream-in-django.sh`
  - Go to your browser and type http://127.0.0.1:8000/ in the address bar.
  - Finished...
  
# Technology used in Project :hotsprings:
<img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/django.png" width="300">     <img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/AJAX.png" width="300">

# Directory Tree :cactus:
<details><summary>Show Tree</summary>
 
 ```bash
.
├── blog
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20201004_1907.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templatetags
│   │   ├── extras.py
│   │   └── __init__.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db2.sqlite3
├── db.sqlite3
├── Images
│   ├── 1.png
│   ├── 2.png
│   ├── 3.png
│   ├── 4.png
│   ├── 5.png
│   ├── 6.png
│   ├── 7.png
│   └── 8.png
├── LICENSE
├── manage.py
├── mysite
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_lecture_course.py
│   │   ├── 0003_auto_20201001_1806.py
│   │   ├── 0004_auto_20201002_1139.py
│   │   ├── 0005_lecture_lecture_type.py
│   │   ├── 0006_lecturecomment.py
│   │   ├── 0007_course_course_price.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── secret key.json
├── startup
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── css
│   │   └── dashboard.css
│   ├── images
│   │   ├── Courses.png
│   │   └── courses.webp
│   └── js
│       ├── pass_validation.js
│       └── validation.js
├── student
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_coursesubscription.py
│   │   ├── 0003_coursesubscription_datestamp.py
│   │   ├── 0004_auto_20201102_1949.py
│   │   ├── 0005_coursesubscription_payment_id.py
│   │   ├── 0006_auto_20201104_1008.py
│   │   ├── 0007_auto_20201104_1238.py
│   │   ├── 0008_studentinfo_email_id.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates
│   ├── 404.html
│   ├── base.html
│   ├── blog
│   │   ├── blog.html
│   │   └── blogpost.html
│   ├── course
│   │   ├── checkout.html
│   │   ├── course_detail.html
│   │   ├── courses.html
│   │   ├── index.html
│   │   ├── lecture.html
│   │   └── pricing.html
│   └── student
│       ├── change_password.html
│       ├── info.html
│       └── user_course.html
└── validation
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py

19 directories, 89 files
 ```
</details>


## ScreenShot :camera_flash:
 - Backend <br> 
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/1.png)
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/2.png)

 - Courses <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/3.png)

 - Course Detials <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/4.png)

 - Checkout Page <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/5.png)

 - Payment Process <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/6.png)

 - Subscribed Courses <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/7.png)

 - Password Change Page <br>
 
![](https://github.com/yogeshnile/course-stream-in-django/blob/main/Images/8.png)


## Bug / Feature Request :man_technologist:
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/yogeshnile/course-stream-in-django/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/yogeshnile/course-stream-in-django/issues/new). Please include sample queries and their corresponding results.


## Connect with me! 🌐
Known on internet as **Yogesh Nile**

[![][I_LinkedIn]][LinkedIn]  [![][I_Github]][Github] [![][I_Twitter]][Twitter] [![][I_Telegram]][Telegram] [![][I_Instagram]][Instagram]  [![][I_Instagram Personal]][Instagram Personal]   [![][I_discord]][discord]

## Email Me :e-mail:

[![][I_Email]][E-mail]


[LinkedIn]: https://bit.ly/2Ky3ho6
[Github]: https://bit.ly/2yoggit
[Twitter]: https://bit.ly/3dbLJLC
[Telegram]: https://t.me/yogeshnile
[Instagram]: https://bit.ly/3b9Qeo4
[Instagram Personal]: https://bit.ly/32SXHV0
[E-mail]: mailto:yogeshnile.work4u@gmail.com
[discord]: https://discord.gg/R2ug3gR

[I_discord]: https://img.icons8.com/bubbles/100/000000/discord-logo.png
[I_LinkedIn]: https://img.icons8.com/bubbles/100/000000/linkedin.png
[I_Github]: https://img.icons8.com/bubbles/100/000000/github.png
[I_Twitter]: https://img.icons8.com/bubbles/100/000000/twitter.png
[I_Telegram]: https://img.icons8.com/bubbles/100/000000/telegram-app.png
[I_Instagram]: https://img.icons8.com/bubbles/100/000000/instagram-new.png
[I_Instagram Personal]: https://img.icons8.com/bubbles/100/000000/instagram.png
[I_Email]: https://img.icons8.com/bubbles/100/000000/secured-letter.png
