
import os
import subprocess

import minecraft_launcher_lib

# minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

minecraft_directory = os.getcwd()+"/minecraft"

print(minecraft_directory)

current_max = 0


def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}

# minecraft_launcher_lib.install.install_minecraft_version('1.18.2', minecraft_directory, callback=callback)

minecraft_launcher_lib.fabric.install_fabric('1.18.2', minecraft_directory, callback=callback)

# options = minecraft_launcher_lib.utils.generate_test_options()

# options["jvmArguments"] = ["-Xmx2G", "-Xms2G"]

# options["username"] = "WV"
# options["port"] = "103.219.30.51:24150"


# minecraft_command = minecraft_launcher_lib.command.get_minecraft_command('1.18.2', minecraft_directory, options)

# subprocess.call(minecraft_command)