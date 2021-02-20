# Microservice title

Summary

# Requirements

Description, functionalities, requirements and dependencies


**Endpoints**:

|Method|URI|Description| Status |
|------|---|-----------|--------|
| POST | /name | it will receive the  payload, and it will proceed to PROCESS it | **Completed** |
| PATCH | /name/{id} | this PATCH method to update the item | **Development** |
| DELETE | /name/{id} | this method will remove the item from the storage | Not started |
| GET | /name/{id} | this method will return the room data for a given room id | Not started |
| GET | /health-check | This endpoint returns the state of the service | Not started |

# Running the environment

You need to have Docker installed in your machine, after that, just run this command `docker-compose build && docker-compose up -d`.