import subprocess


def get_script_output(script_location):
    process = subprocess.Popen(script_location, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode("utf-8")
