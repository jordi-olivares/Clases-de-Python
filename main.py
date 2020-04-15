clientes='david,pablo,orlando'
import sys

def add_client(name):
    if name not in clientes:
        global clientes
        _add_coma()
        clientes+=name
    elif name in clientes:
        print('el usuario ya existe')
    


def _add_coma():
    global clientes
    clientes+=','


def list_clients():
    global clientes
    print(clientes)

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


def delete_client(name):
    global clientes

    if name not in clientes:
        print('This client is not exist')
    elif name in clientes:
        """_size_name=len(name)
        _index_name=clientes.find(','+name)
        aux1=clientes[0:_index_name:1]
        aux2=clientes[_index_name+_size_name+2:-1:1]
        clientes=aux1+aux2"""
        namesl=clientes.split(',')
        aux=''
        i=0
        for cliente in namesl:
            if i==0:
                if cliente!=name:
                    aux+=cliente
                else:
                    continue
            else:
                if cliente!=name:
                    aux+=','+cliente
                else:
                    continue
            i+=1                  
        clientes=aux
        #clientes=clientes.replace(name+',','')


def update_client(oldName,newName):
    global clientes
    if oldName in clientes:
        clientes=clientes.replace(oldName,newName)
    elif oldName not in clientes:
        print("The client is not exist")

def search_client(client_name):
    global clientes
    """client_list=clientes.split(',')

    for client in client_list:
        if client!=client_name:
            continue
        else:
            return True"""
    return client_name in clientes


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
        _name_client=getNameClient(action)
        add_client(_name_client)
        list_clients()
    elif action =="D":
        _name_client=getNameClient(action)
        delete_client(_name_client)
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
        a=search_client(_name_client)
        if a==True:
            print('the user {} is in client\' list'.format(_name_client))
        else:
            print('the user {} is not in client\'list'.format(_name_client))
    elif action=='L':
        list_clients
    else:
        print('The command is not exist')
   