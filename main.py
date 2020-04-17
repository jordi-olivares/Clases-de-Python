import sys
import copy
clientes=[
    {
        'name':'pablo',#en los diccionarios tambien los elementos se separan con una coma
        'company':'google',
        'email':'pablo@google.com',
        'position':'Software engineer',
    },#porque son dos elementos de una lista
    {
        'name':'ricardo',
        'company':'facebook',
        'email':'ricardo@facebook.com',
        'position':'Data engineer',
    }  
]
def add_client(client):   
    global clientes       #si funcionan porque los diccionarios son elementos de una lista
    if client not in clientes:        
        clientes.append(client)
    elif name in clientes:
        print('el usuario ya existe')


def list_clients():
    global clientes
    for index,cliente in enumerate(clientes):
        print('{uid} | {name} | {company} |{email} | {position}'.format(
            uid=index,
            name=cliente['name'],
            company=cliente['company'],
            email=cliente['email'],
            position=cliente['position'],
        ))

#clase de estructuras condicionales

def _print_welcome():
    print('Bienvenidos')
    print('*'*50)   #repiteel asterisco 50 veces
    print('What do you like to day')
    print('[U] update name client')
    print('[C] create client')
    print('[D] delete client')
    print('[S] for search a client')
    print('[L] for view client\'s list')


def existClient(name):
    f=False
    for index in range(len(clientes)):
        if clientes[index]['name']==name:
            f=True
        else:
            continue
    return f


def delete_client(id):
    global clientes
    clientes.remove(clientes[id])
    """borra todos los usuarios con ese nombre"""


def update_client(oldName,newName):
    global clientes
    f=existClient(oldName)
    if f:
        for index in range(len(clientes)):
            if clientes[index]['name']==oldName:
                clientes[index]['name']=newName
            else:
                continue
    else:
        print("The client is not exist")
    """cambia el nombre de todos los usuarios que se llamen igual"""

def getClientField(action):
    field=None
    while not field:
        field=raw_input('what is the {} of client?     '.format(action))
    return field

def getNameClient(action):
    name=None
    while not name:
        print('What is the name of client to {}?'.format(action))
        name=raw_input()
        if name=='exit':
            name=None
            break
    if not name:
        sys.exit()
    return name


if __name__ == "__main__":
    _print_welcome()
    action=raw_input()
    list_clients()
    if action =="C":
        client={
            'name':getClientField('name'),
            'company':getClientField('company'),
            'email':getClientField('email'),
            'position':getClientField('position'),
        }
        add_client(client)
        list_clients()
    elif action =="D":
        id=int(getClientField('id'))
        delete_client(id)
        list_clients()
    elif action=='U':
        print('What is the name of clien that you want to update?')
        _name_client=getNameClient(action)
        print('What is the new name of client '+_name_client+'?')
        _new_client=getNameClient(action)
        update_client(_name_client,_new_client)
        list_clients()
    elif action=='S':
        print('What is the name of clien that you want to search?')
        _name_client=getNameClient(action)
        a=existClient(_name_client)
        if a==True:
            print('the user {} is in client\' list'.format(_name_client))
        else:
            print('the user {} is not in client\'list'.format(_name_client))
    elif action=='L':
        list_clients
    else:
        print('The command is not exist')
   