## Docker Compose

Your goal: write a docker-compose.yml so that the integration tests pass.

The tests live in a container built from the Dockerfile in this folder. They connect to the other services by hostname, so those services need to exist, be named correctly, and be configured the way the tests expect. You need to write the compose file that creates all of them.

#### Directory Structure:
```
    app/
    ├── Dockerfile              # builds the test runner
    ├── requirements.txt        # Python dependencies for the tests
    ├── init.sql                # seed data for the database
    ├── docker-compose.yml      # the file you need to change
    ├── tests/
    │   └── test_integration.py # the tests you need to make pass
    └── README.md               # this file

```

### Create a docker-compose.yml that defines four services:
Service name	What it is	        Notes
db	            PostgreSQL 16	    See database requirements below
cache	        Redis 7	            Default configuration is fine
tests	        The test runner	    Built from the Dockerfile in this folder

## Before you start
Run this command - Only relevent to CodeSpaces
`sudo sysctl -w net.bridge.bridge-nf-call-iptables=0`
Without it, containers in Codespaces cannot talk to each other, and your tests will hang instead of failing. 

### Running docker-compose
`docker compose up --build --exit-code-from tests`

### Test Passing
```
    tests-1  | tests/test_integration.py::test_postgres_seeded PASSED
    tests-1  | tests/test_integration.py::test_redis_roundtrip PASSED
    tests-1  | ============================== 2 passed ==============================
    tests-1 exited with code 0
```

### Useful commands
docker compose down -v                             # stop everything and delete volumes
docker compose ps -a                               # see which containers exist and their state
docker compose logs db                             # logs for one service