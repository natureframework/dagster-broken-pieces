# Dagster Boilerplate

Welcome to the Dagster Boilerplate! This project is designed to help you get started with Dagster, a data orchestrator for machine learning, analytics, and ETL. Whether you're new to Dagster or looking to create a simple project, this boilerplate has everything you need to hit the ground running.

## Rapid Prototyping with Dagster

Dagster is well-suited for rapid prototyping of complex data workflows. Its asset-based structure not only encourages a clean code structure from day one but also ensures that your prototype is ready for production with minimal adjustments. This approach significantly reduces the development time and effort required to transition a prototype into a fully operational production system.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.7 or newer
- [Poetry](https://python-poetry.org/docs/#installation), a tool for dependency management and packaging in Python.

## Getting Started

Follow these steps to get your Dagster project up and running:

### 1. Download the Repository

First, download this repository to your local machine. You can do this by clicking on the `Code` button and then selecting `Download ZIP`.

### 2. Extract the ZIP File

Locate the downloaded ZIP file in your downloads folder and extract it.

### 3. Change Directory

Open a terminal and change into the project directory:

```bash
cd dagster-hello-world
```

### 4. Install Dependencies

Run the following command to install the project dependencies using Poetry:

```bash
poetry install
```

### 5. Activate the Virtual Environment

Activate the Poetry-created virtual environment:

```bash
poetry shell
```

### 6. Code Linting

Use the provided script to execute code linting tools (black, flake8, and pylint):

```bash
bin/lint
```

### 7. Run Unit Tests

Execute the unit tests to ensure everything is set up correctly:

```bash
pytest
```

### 8. Start the Dagster Development Environment

Finally, start the Dagster development environment with the following command:

```bash
dagster dev
```

### 9. Access the Dagster Interface

After starting the development environment, open your web browser and navigate to:

[http://localhost:3000/](http://localhost:3000/)

You should now see the Dagster interface!

## Next Steps

Congratulations! You've successfully set up your Dagster Hello World project. From here, you can start exploring Dagster's features and begin building your own data pipelines.

For more information and further reading, check out the [Dagster Documentation](https://docs.dagster.io/).
