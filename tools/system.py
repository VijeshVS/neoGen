import subprocess

def execute_command(cmd: str):
    res = subprocess.check_output(cmd,shell=True,text=True)
    return res