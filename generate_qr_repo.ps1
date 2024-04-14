# Define paths
$pythonExecutable = "C:\Users\Abdallah.Ashry\Desktop\Repo\generate-qr-code\myenv\Scripts\python.exe"
$djangoManagePy = "C:\Users\Abdallah.Ashry\Desktop\Repo\generate-qr-code\manage.py"
$port = "8001"  # Adjust the port as needed
$host_name = "0.0.0.0"  # Adjust the host address as needed

# Build the command to run Django's runserver
$command = "$pythonExecutable $djangoManagePy runserver ${host_name}:$port"

# Start Django runserver in the background
Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/c", $command
