import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horseproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == '__main__':
    main()
