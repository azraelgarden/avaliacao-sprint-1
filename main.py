import docker
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["APIdocker"]
mycol = mydb["dockers"]

client = docker.from_env()

def print_all_containers():
    container_list = client.containers.list()
    for container in container_list:
        print(f'Container ID: {container.id}')
        print(f'Container sort ID: {container.sort_id}')
        print(f'Container Name: {container.name}')
        print(f'Container Status: {container.status}')
        print()


def get_containers_running():
    container_list = client.containers.list(filters={'status': 'runnig'})
    if container_list:
        return container_list


def remove_all_containers_runnig():
    containers_list = get_containers_running()
    if containers_list:
        for container in containers_list:
            try:
                print(f'Tente remover o container {container.name}')
                container.remove(force=True)
                print(f'Container selecionado {container.name} sucessfully removed')
            except Exception as err:
                print(f'Falha ao remover container selecionado {container.name} Erro: {err}')


def action_container(containerid, action, ):
    if action.lower() in ['start', 'stop ']:
        try:
            container = client.containers.get(containerid)
            try:
                getattr(container, action)()
                print(f'Container selecionado {container.name} sucessfully {action}')
            except Exception:
                print(f'Falha em {action} o container {container.name}')
        except docker.erros.NotFound:
            print('Container não existe.')
    else:
        print('Invalid action')


action_container('8fc5d5426c4a', 'started')
