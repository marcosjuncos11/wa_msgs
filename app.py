import os
from src.application import application

debug = os.getenv('DEBUG', False)



if os.getenv('DEBUG', False):
    import ptvsd
    try:
        my_pid = os.getpid()
        print('Stating debugger config...')
        if os.environ.get('PPID') == str(os.getppid()):
            print('Reloading...')
            print(f"Current process ID: {my_pid}")
            try:
                port = 4444
                ptvsd.enable_attach(address=('0.0.0.0', port))
                print(f'========================== PTVSD waiting on port {port} ==========================')
                # ptvsd.wait_for_attach()   # Not necessary for my app; YMMV
            except Exception as ex:
                print(f'PTVSD raised {ex}')
        else:
            print('Starting...')
            os.environ['PPID'] = str(my_pid)
            print(f"First process ID: {my_pid}")      
    except Exception as ex:
        print(f'DEBUG: PTVSD Failed To Initialize: {ex}')



if __name__ == '__main__':
    application.run(debug = debug, host='0.0.0.0')