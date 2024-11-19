set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

generate:
    podman run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate -i /local/openapi.yaml -g python -o /local/rlink_client_python_new --package-name rlink_client

renew: generate
    cp "rlink_client_python/pyproject.toml" "rlink_client_python_new/pyproject.toml"
    rmdir -R "rlink_client_python"
    mv "rlink_client_python_new" "rlink_client_python"
    mkdir "rlink_client_python/src"
    mv "rlink_client_python/rlink_client" "rlink_client_python/src/rlink_client"

build: renew
    uv build --directory rlink_client_python

copy-oa:
    git checkout gh-pages
    git checkout main openapi.yaml
    git commit -am "Update openapi.yaml"
    git push origin gh-pages
    git checkout main

release: build copy-oa
    git add rlink_client_python
    git commit -am "Update rlink_client_python"
    git push origin main
