import subprocess

def execute_command(cmd: str):
    result = subprocess.run(
        cmd,
        cwd="/Users/vijeshshetty/Documents/projects/neoGen/generated_project",
        shell=True,              # allow full shell commands like "npm init -y && npm install"
        text=True,               # decode bytes -> str
        capture_output=True      # capture stdout & stderr
    )

    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Error:\n{result.stderr.strip()}"