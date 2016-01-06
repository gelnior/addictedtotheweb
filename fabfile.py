from fabric.api import hosts, run, env

sheeva1 = '192.168.1.15'
env.user = "addictedtotheweb"


@hosts(sheeva1)
def update():
    #run("su addictedtotheweb")
    run("cd /home/addictedtotheweb/addictedtotheweb/; git pull")

