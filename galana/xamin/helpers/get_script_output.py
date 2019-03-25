import subprocess


def get_script_output(script_location):
    process = subprocess.Popen(script_location, stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode("utf-8")


def get_inline_script_output(script_sting):
    process = subprocess.Popen(script_sting.split(), stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode("utf-8")
