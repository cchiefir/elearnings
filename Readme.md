# Project Title

Elearning platform where you can find existing courses, subscribe to them or create your own new courses.

## Getting Started

This project use Redis for caching. You have to have it installed.

### Prerequisites

What things you need to install the software and how to install them

```
Django 2.0+
Django Rest Framework
Redis

more in requirements.txt
```

### Installing

Download a fixture with some Subjects:

```
loaddata initial_data.json
```

Run Redis server

```
$ sudo service redis_6379 start
```

## API
API prefix:
```
/api/
```
#### Title:
Show all available subjects.
##### URL:
```
/subjects/
```
##### Method:
```
GET
```
##### URL Params:
--
##### Data Params:
--
##### Success Response:
Code: 200 <br>
Content example:
```
[
    {
        "id": 2,
        "title": "Mathematics",
        "slug": "mathematics"
    },
    {
        "id": 4,
        "title": "Music",
        "slug": "music"
    },
 ]
```
##### Error Response:
--

________________________________________________________________________
#### Title:
Show details for 1 selected subject
##### URL:
```
/subjects/:id
```
##### Method:
```
GET
```
##### URL Params:
--
##### Data Params:
--
##### Success Response:
Code: 200 <br>
Content example:
```
[
    {
        "id": 2,
        "title": "Mathematics",
        "slug": "mathematics"
    }
 ]
```
##### Error Response:
--

________________________________________________________________________
#### Title:
Show all available courses
##### URL:
```
/subjects/elearning
```
##### Method:
```
GET
```
##### URL Params:
--
##### Data Params:
--
##### Success Response:
Code: 200 <br>
Content example:
```
[
    {
        "id": 2,
        "subject": 4,
        "title": "This is some course",
        "slug": "this_is_some_course",
        "overview": "Good description for good course",
        "created": "2018-05-29T17:32:39.751099Z",
        "owner": 1,
        "modules": [
            {
                "order": 0,
                "title": "This is first big Module",
                "description": "This is starting module"
            },
     },
     {...another course...}
 ]
```
##### Error Response:
--

________________________________________________________________________
#### Title:
Subscribe to the course
##### URL:
```
/subjects/elearning/:id/enroll
```
##### Method:
```
POST
```
##### URL Params:
--
##### Data Params:
```
{
  u : {
    user : [string],
    password : [alphanumeric],
  }
}
```
##### Success Response:
Code: 200 <br>
Content example:
```
{'enrolled': True}
```
##### Error Response:
 ```
 HTTP 401: Unauthorized
 HTTP 403: Forbidden
 {
    "detail": "You do not have permission to perform this action."
 },
 {
    "detail": "Authentication credentials were not provided."
}
 HTTP 405: Method Not Allowed
 {
    "detail": "Method \"GET\" not allowed."
}
 ```

________________________________________________________________________
#### Title:
Show the content of the selected course
##### URL:
```
/subjects/elearning/:id/conents
```
##### Method:
```
GET
```
##### URL Params:
--
##### Data Params:
--
##### Success Response:
Code: 200 <br>
Content example:
```
{
    "id": 2,
    "subject": 4,
    "title": "This is good course",
    "slug": "this_is_good_course",
    "overview": "Good description for good course",
    "created": "2018-05-29T17:32:39.751099Z",
    "owner": 1,
    "modules": [
        {
            "order": 0,
            "title": "This is first big Module",
            "description": "This is starting module",
            "contents": [
                {
                    "order": 0,
                    "item": "<p>Text for students go study.</p>"
                },
                {
                    "order": 1,
                    "item": "<p><img src=\"/media/images/6_model.jpg\" height=\"200\"></p>"
                }
            ]
        }
    ]
 }
```
##### Error Response:
 ```
 HTTP 401: Unauthorized
 HTTP 403: Forbidden
 {
    "detail": "You do not have permission to perform this action."
 },
 {
    "detail": "Authentication credentials were not provided."
}
 ```


## How to create new course

You need to have a permission to add new courses. You need have Instructors permissions. You can change the permission group on the admin page.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [DRF](http://www.django-rest-framework.org/) - For building API
* [Redis](https://redis.io/) - Used to cache some content




