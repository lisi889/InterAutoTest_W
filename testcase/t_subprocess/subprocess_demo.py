import subprocess

res = subprocess.call(["whoami"])
print(res)

subprocess.call("ls-l",shell=True) #字符串方式传命令
