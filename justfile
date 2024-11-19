set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

generate:
    podman run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python -o /local/rlink_client_python_new --package-name rlink_client

renew: generate
    cp "rlink_client_python/pyproject.toml" "rlink_client_python_new/pyproject.toml"
    rmdir -R "rlink_client_python"
    mv "rlink_client_python_new" "rlink_client_python"
    mkdir "rlink_client_python/src"
    mv "rlink_client_python/rlink_client" "rlink_client_python/src/rlink_client"
