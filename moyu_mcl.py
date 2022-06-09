
import os
import subprocess

import minecraft_launcher_lib

f = open(os.getcwd()+'/setting', 'r')
setting_data = f.read()
setting_data = eval(setting_data)

minecraft_directory = os.getcwd()+'/.minecraft/'+setting_data[0]['version']

options = minecraft_launcher_lib.utils.generate_test_options()

options['jvmArguments'] = ['-Xmx'+setting_data[0]['java_ram'], '-Xms'+setting_data[0]['java_ram']]

if setting_data[0]['player_name'] != '':
    options['username'] = setting_data[0]['player_name']

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(setting_data[0]['core_version'], minecraft_directory, options)

subprocess.call(minecraft_command)