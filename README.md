# enersense_test_task


### Install
```
python3 -m venv ./venv/
source venv/bin/activate
pip install -r requirements.txt
```

### Run
To run mongodb, mongo-express, mqtt and fastapi application
```
docker-compose --profile backend up
```

To run publisher
```
docker-compose --profile publisher up
```

To run subscriber
```
docker-compose --profile subscriber up
```

To rebuild any service add `--build` to the end of the command


### Logs
See `./mqtt/log/sub.log` for mqtt subscriber logs

### Helpers
The `./mqtt/helpers` folder contains basic publisher/'subscriber which could be used for testing