# ⚔️ Libre:Match RLink_Client

Relic Link API-Client generated from OpenAPI

## Generating Client

1. Rename the folder `rlink_client_python` to `rlink_client_python_old`.

2. Run
`openapi-generator-cli.cmd generate -g python -o rlink_client_python -i openapi.yaml --package-name rlink_client --packageVersion <python package version>`.

3. Copy over `rlink_client_python_old/pyproject.toml` to `rlink_client_python/pyproject.toml`.

4. Check if all the version values are right in `rlink_client_python/pyproject.toml` and `rlink_client_python/setup.py`.

## License

AGPL-3.0-or-later; see [LICENSE](./LICENSE).
