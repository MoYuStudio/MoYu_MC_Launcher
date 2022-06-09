
import os
import subprocess

import minecraft_launcher_lib

minecraft_directory = os.getcwd()+"/.minecraft/moyuland_mod"

options = minecraft_launcher_lib.utils.generate_test_options()

options["jvmArguments"] = ["-Xmx2G", "-Xms2G"]

options["username"] = "WilsonVinson"

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command('fabric-loader-0.14.7-1.18.2', minecraft_directory, options)

subprocess.call(minecraft_command)