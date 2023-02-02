#!/usr/bin/env python3
import secrets  # TODO: Use a more sophisticated config system
from vortex import Client


def main():
    client = Client()
    client.login(secrets.username, secrets.password)
    interceptions = client.poll(secrets.webapp)
    print(interceptions)


if __name__ == '__main__':
    main()
