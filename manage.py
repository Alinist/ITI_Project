#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Use 'iti_project.settings' as default, but allow overrides 
    # This is helpful when switching between local GPU dev and production.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'iti_project.settings'))
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # Optional: Logic to warn you if you're running without your AI venv
    if 'fastapi_ai_service' not in sys.prefix and 'runserver' in sys.argv:
         print("⚠️  Warning: Virtual environment 'fastapi_ai_service' not detected.")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
