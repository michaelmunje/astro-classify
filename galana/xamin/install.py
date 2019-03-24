import os
from .helpers import get_script_output


root_dir = os.getcwd()
xamin_script_loc = root_dir + "/utils/get_xamin.sh"


def install():
    get_script_output(xamin_script_loc)
