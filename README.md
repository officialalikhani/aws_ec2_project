# Create a Instances  in aws with API

Create a Instances  in aws with API , This project has made with python fastapi for beckend and postgresql for database.
Also, You can use the Docker images that has been built for more convenient and stable solution , There are  Dockerfiles and Docker-compose.

## Installation

-Use the Dockerfile(postgres) for database
-Use the Dockerfile(python) for beckend API
And use postgres.sh for create database with tables and columns , you should copy this file onto docker image but don't worry about this on dockerfile this problem was solved.
At first install docker and docker-compose in your os environment.
After that run this command 

```bash
docker-compose up
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
