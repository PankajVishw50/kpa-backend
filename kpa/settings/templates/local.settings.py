"""Template file for local settings.

Copy this file to `/local/local.settings.py`
or if you would like to use another path
you can set it to `LOCAL_SETTING_PATH` environment variable.
"""

# You Must Change This
SECRET_KEY = "lkfjelkfjeljfelkjfelkfjelkfkjeklfjelkfje9fj0930jfieko"

DEBUG = False
ALLOWED_HOSTS = ["localhost"]

# You Can Use variable directly from previous settings files
SHELL_PLUS_PRE_IMPORTS += [  # type:ignore
    ("data.sample_wheel_specs_data", "*"),
]
