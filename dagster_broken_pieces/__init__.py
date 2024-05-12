from dagster import Definitions
from .assets.references import references

defs = Definitions(assets=[references])
