# UV Template

This repository is a minimal template for a project on the UV build system.  
It provides an opiniated Python development experience on VS Code.

## Features
- VS Code 
[Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 
for reproducable set up
- [UV](https://docs.astral.sh/uv/) package management
- [Ruff](https://docs.astral.sh/ruff/) linter and formatter
- [Ty](https://docs.astral.sh/ty/) type checker and language server
- [Pre-Commit](https://pre-commit.com/) hooks to enfore code quality
- GitHub 
[Dependabot](https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide) 
configuration

## Setup
### Dev Container (_Recommended_)

Just open this project in VS Code with the official 
[Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 
to get an automatically set up development experience.

### Manual Setup
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Run `uv sync` to have uv create the virtual environment and install the packages
- Install the 
[Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) 
and [Ty](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) 
VS Code Extensions.
- Setup pre-commit hooks `uvx pre-commit install`

## Next steps
- Edit project metadatas in `pyproject.toml`.
- Sync the environment with `uv sync`.
- Use uv to manage packages `uv add `.

## License
This project is licensed under the MIT License — see the [LICENSE file](LICENSE) for details.
