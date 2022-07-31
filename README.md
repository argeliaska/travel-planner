# travel-planner
Personal travel planner

## Database and modeling
I choshed MongoDB because I considered this travel-planner can be easily a mobile application as well as web application and I think a No SQL database has a better performance as a relational database. 

I only made the travel model, because it's enough for the practice purposes. <br/> In this collection, there are the travel documents with all the required fields and the user_email of course. We can find documents very easy and quickly and even add fields (if needed) without break the structure of the documents already exist in the database.

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running on a local environment with Docker

### Environment
For running the API in a right way it needs some variables, there is a default file named `env.example` which you can use as a example. If you want the `.env` file with all the variables used in this project please contact me by sending an email to argeliaska@gmail.com.

### Running services
If you have already set up your local environment and have a **.env** file with the development variables set, this command builds the image `travel-planner-api:1.0.1` and starts the services `travel-planner-api` and `travel-planner-api-db`:

```shell
$ docker-compose up -d
```
Load the URL http://localhost:8000/ into your browser.
