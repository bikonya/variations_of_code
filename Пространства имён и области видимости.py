n = int(input())
namespaces = {
    'global': {'parent': None, 'vars': []}
}

for each in range(n):
    cmd, namespace, arg = input().split()
    if cmd == 'create':
        namespaces[namespace] = {'parent': arg, 'vars': list()}
    elif cmd == 'add':
        namespaces[namespace]['vars'].append(arg)
    elif cmd == 'get':
        while namespaces[namespace]['parent'] is not None:
            if arg not in namespaces[namespace]['vars']:
                namespace = namespaces[namespace]['parent']
            else:
                print(namespace)
                break
        else:
            if arg in namespaces['global']['vars']:
                print('global')
            else:
                print(None)
