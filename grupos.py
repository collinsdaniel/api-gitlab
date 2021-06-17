import gitlab
import urllib3


def conectar(url, token):

    urllib3.disable_warnings()

    gl = gitlab.Gitlab(url=url, private_token=token, ssl_verify=False, per_page=100, order_by='name')
    gl.auth()

    grupo_miv = gl.groups.get(1864)
    nome_grupo = grupo_miv.attributes.get('name')
    print('Grupo {}'.format(nome_grupo))

    for project in grupo_miv.projects.list(all=True):
        user = gl.users.get(project.creator_id)
        print('{},{},{}'.format(project.created_at, project.name, user.name))


def main():
    url = input('url: ')
    token = input('token: ')
    conectar(url, token)


if __name__ == '__main__':
    main()
