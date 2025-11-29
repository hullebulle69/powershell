# Get the path to your Desktop
$desktop = [Environment]::GetFolderPath("Desktop")

# Create a file called hello.txt with "Hello" inside
Set-Content -Path "$desktop\hello.txt" -Value "Hello"
