#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tanks.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
>>>>>>> 1a7ce2e7043b9ae5bf06962fad6c4dcf27f3b183

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
