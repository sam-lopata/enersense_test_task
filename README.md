# Enersense Backend Developer Technical Assignment

### Repository

Clone `sam-lopata/enersense_test_task`
```
gh repo clone sam-lopata/enersense_test_task
cd enersense_test_task
```

### Run
You need installed and running `docker` server and `docker-compose`.

The `docker-compose` structured with profiles to run different services.

To run mongodb, mongo-express, mqtt and fastapi applications
```
docker-compose --profile backend up
```
Mongodb web interface is asessible on `http://0.0.0.0:8081/`

API documentation is accessible on `http://localhost:8000/docs`

API is accessible on `http://localhost:8000/` and it has 2 endpoints: 
- `/` - which returns paginated results and assepts `page` and `size` query parameters.
- `/all` - which returns all results upi to 10000 records

To run publisher
```
SLEEP=30 docker-compose --profile publisher up
```
Where SLEEP is amount of seconds to sleep between generating messages, defaul is 5 sec.

To run subscriber
```
docker-compose --profile subscriber up
```
Subscriber writes logs to `./mqtt/log/sub.log` and saves messages to MongoDb.

To rebuild any service add `--build` to the end of the command. That is needed of you make changes to code.

### Helpers
The `./mqtt/helpers` folder contains basic publisher/'subscriber which could be used for testing locally.
