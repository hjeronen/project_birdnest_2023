#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # set settings file to use
    use_prod_settings = os.environ.get('DJANGO_PRODUCTION', 'false')
    if use_prod_settings == 'false':
        print('Using development settings.')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings_dev')
    else:
        print('Using production settings.')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
