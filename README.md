# CoinMena

Get the latest crypto currency information from AlphaVantage API.

## Getting Started

Kindly create virtual environment if you don't want to mess up libraries =)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9
- Django 3.2.1
- Django Rest Framework 3.12.4
- AlphaVantage 2.3.1
- Docker 


### Installing

Install [docker.com] (https://docs.docker.com/docker-for-mac/install/) and run docker process in background.

First clone the repo into your local directory.

```
git clone https://github.com/MirzaBaig715/CoinMena.git
```
### Setup
Please create API key in AlphVantage which is needed to run this project. Claim you key [here](https://www.alphavantage.co/support/#api-key).

Create `.env` text file in project directory and add these following data
```
DEBUG=1
SECRET_KEY=(*^@#JBUI&AT^CBMN!@KLHLA&^#(!)(@#
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
ALPHA_API_KEY=Your claimed key from AlphaVantage
```
### Build and Run docker
```
docker-compose build
docker-compose up -d
```
### Check the Logs
```
docker-compose logs -f
```
There are two method `GET` and `POST`. `GET` will retreive the latest price from database. `POST` will forcefully call the AlphaVantage API to get the latest price.

Thats it! Now you can go to [localhost:8000/api/v1/qoutes/](localhost:8000/api/v1/qoutes/).
