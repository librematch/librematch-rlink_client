set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

generate:
    Rename-Item -Path "rlink_client_python" -NewName "rlink_client_python_old"
    openapi-generator-cli.cmd generate -g python -o rlink_client_python -i openapi.yaml --package-name rlink_client
    Copy-Item -Path "rlink_client_python_old/pyproject.toml" -Destination "rlink_client_python/pyproject.toml"
