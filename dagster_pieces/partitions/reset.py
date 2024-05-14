from dagster import DagsterInstance


def reset(instance: DagsterInstance, name: str, keys: list) -> None:
    for key in instance.get_dynamic_partitions(name):
        instance.delete_dynamic_partition(name, key)
    instance.add_dynamic_partitions(name, keys)
