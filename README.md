# Lean TECHniques Technical Showcase - Matt Hutchison
An application displaying photo album information for the purpose of demonstrating technical qualifications to the review team.

## Dependencies
The application requires either that Docker is installed or a local installation of Python (3.9 or greater).

## Running with Docker
If GNU `make` and Docker are installed, the simplest way to run the application is `make run` from this directory. If `make` is not present, the container can be built and run using `docker build -t leantechniques-demo . && docker run -it --rm leantechniques-demo`.

## Running with local Python
It is possible to run the application without Docker if you have a current installation of Python (3.9 or greater). A virtual environment (venv or conda) is highly recommended if you take this approach. To use:
- Activate the desired virtual environment
- Install the requirements found in requirements.txt (generally `pip install -r requirements.txt`)
- Run the application with `python3 main.py`

## Development
Automated tests can be run using `make test`, which will build the latest docker image and execute the test suite. Tests can also be run on a local python installation using `python3 -m unittest`.