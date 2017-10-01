# Simple API

Simple API can be used as boilerplate for starting backend API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

First of all you have to install vagrant and virtual box. Download you copies here:

[Vagrant](https://www.vagrantup.com/downloads.html)
[VirtualBox](https://www.virtualbox.org/wiki/Downloads)

After that, clone this repo:

```
git clone git@github.com:archix/SimpleAPIBoilerplate.git
```

### Installing

Once you've installed vagrant and cloned repo cd to project and run next command:

```
vagrant up
```

This should automatically setup whole project (download and run Ubuntu 16.04 on vm, and install all needed packages for running project)

To connect to vm just type

```
vagrant ssh
```

Once you're in, to run API type next commands:

enter dir

```
cd /home/ubuntu/app
```

activate virtual environment

```
source .env/bin/activate
```

actually run API

```
python app.py
```

You can check if app's running by visiting next link:

[http://192.168.55.56:5000/api/](http://192.168.55.56:5000/api/)

Default admin user should already be created try /login/ using next credentials via cURL:

```
curl -X POST \
  http://192.168.55.56:5000/api/login/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
        "email": "admin@maildrop.cc",
        "password": "admin"
}'
```

## Docs

To see docs visit next link:

[http://192.168.55.56:5000/apidocs/](http://192.168.55.56:5000/apidocs/)

## Running the tests

TBD

### Break down into end to end tests

TBD

### And coding style tests

TBD

## Deployment

TBD

## Built With

* [Vagrant](http://www.dropwizard.io/1.0.2/docs/)
* [PostgreSQL](https://rometools.github.io/rome/)
* [Flask](https://maven.apache.org/)
* [SqlAlchemy](https://rometools.github.io/rome/)

## Contributing

TBD

## Versioning

TBD

## Authors

* **Igor Dakić**  - [Archix](https://github.com/archix)


## License

This project is licensed under the GPL v3.0 License - see the [LICENSE.md](LICENSE.md) file for details
