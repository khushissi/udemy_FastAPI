import docker
import docker.errors

def start_database_container():
    client = docker.from_env()
    container_name = "test-db"

    try:
        existing_container = client.containers.get(container_name)
        print(f"container '{container_name}' exists. stopping and removing...")
        existing_container.stop()
        existing_container.remove()
        print((f"contaier '{container_name}'stoped and removed"))
    except docker.errors.NotFound:
        print(f"container {container_name} do not exist.")

    container_config = {
        "name" : container_name,
        "image": "postgres:16.1-alpine3.19",
        "detach":True,
        "ports": {"5432" : "5434"},
        "enviroment": {
            "POSTGRES_USER": "postgres",
            "POSTGRES_PASSWORD": "postgres",
        },

    }