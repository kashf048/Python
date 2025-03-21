import subprocess

# TIME WASTE METHOD
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

try:
    # completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
    # completed = subprocess.run(["python", "other.py"], capture_output=True, text=True)
    completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
    print("args", completed.args)
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
    # if completed.returncode != 0:
    #     print(completed.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)