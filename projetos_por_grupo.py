import gitlab
import urllib3


def conectar(url, token):

    # Evitar warnings por não verificar ssl.
    urllib3.disable_warnings()

    print('Conectar no servidor: {}'.format(url))
    gl = gitlab.Gitlab(url=url, private_token=token, ssl_verify=False, per_page=100, order_by='name')
    gl.auth()
    print('Conexão realizada...\n')

    id_grupo = int(input('id do grupo: '))
    grupo = gl.groups.get(id_grupo)
    nome_grupo = grupo.attributes.get('name')

    print('Consultar projetos do grupo {}...\n'.format(nome_grupo))

    for project in grupo.projects.list(all=True):
        user = gl.users.get(project.creator_id)
        print('{},{},{}'.format(project.created_at, project.name, user.name))

    print('Consulta realizada...')
    

def main():
    url = input('url: ')
    token = input('token: ')
    conectar(url, token)


if __name__ == '__main__':
    main()
