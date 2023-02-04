from .config import load_config
from .vortex import Client


def main():
    config = load_config()
    client = Client()
    client.login(config['username'], config['password'])
    interceptions = client.poll(config['webapp'])
    print(interceptions)


if __name__ == '__main__':
    main()
