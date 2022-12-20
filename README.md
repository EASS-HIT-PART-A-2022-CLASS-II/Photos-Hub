# Photos-Hub

This project is a microservice that will let you view / edit / add Champions for League Of Legends !

The project consists of 3 parts, front-end, back-end, and MySQL database.

in order to run the backend and the database (temporarily for now) :

Prerequisites :
- Docker
- Git

1. first clone the repository to your local system :

``` git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/Photos-Hub.git```

2. then simply write the command : 

``` docker-compose up ```

this will create 2 containers for backend and database.

3. open your browser and enter the URL : 
   ``` localhost:9090/docs ```
   
now the backend is up and running and you can view the FastAPI UI with all the methods that are available.

To see the front-end (UI), temporarily for now :

``` docker build -t ph-front ./front-dockerfile ```

``` docker run -d --network=host ph-front ```
