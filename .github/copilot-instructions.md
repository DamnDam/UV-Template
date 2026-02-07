<!-- Copilot / AI agent instructions -->

# Quick context for AI coding agents

At the time of writing, this project is only a template and has no feature.
After getting familiar with the project structure, patterns, and workflows exposed below, you should edit this file right away to add project-specific details and instructions for future contributors. This will help onboard new developers and guide AI agents in making consistent contributions.

**Big-picture architecture**
This is a Python project using the UV build system, structured as a package with source code in `src/`. Linting and formatting are handled by Ruff and typing is enforced by Ty. The project is designed to be developed inside a VS Code dev container for reproducibility, but can also be set up manually with UV.

**Key files / entry points**
- `README.md`: usage and dev workflow instructions.
- `pyproject.toml`: project metadata.
- `ruff.toml`: linter/formatter configuration.
- `ty.toml`: type checker configuration.
- `.devcontainer/devcontainer.json`: VS Code dev container configuration.
- `src/`: main source code directory, structured as a package.

**Suggested development patterns**
- Objects/models: use Pydantic v2 for data validation and parsing. Ensure you always use v2 features and syntax (e.g. `model_config` instead of `Config`).
- CLI applications (if applicable)
  - Use Typer with commands organized by domain. 
  - Use `ctx.obj` for shared context => declare a dataclass for this.
  - Use Rich for all outputs including progress bars, tables, and logs; avoid `print` or `typer.echo`.
- HTTP client: use `httpx` (if applicable)
- API Server: use `FastAPI` (if applicable)
- Config management: use Pydantic `BaseSettings` for environment variable management, .env file and config validation.

**Development workflow**
- `uv run` is the main entry point for running any application code, ensuring the correct environment is used.
- `uv run` must also be used to run linters, formatters, type checkers and pre-commit hooks to ensure they run in the correct environment with the correct configuration.
- `uv sync` should be run after any changes to `pyproject.toml` to ensure the environment is up to date.

**Linting, formatting and type checking**
- Linting: `uv run ruff check`
- Formatting: `uv run ruff format`
- Type checking: `uv run ty check`

VS Code is configured to use the Ruff and Ty extensions, but these commands can also be run manually or in CI. If you see type checking or linting errors in VS Code, they should come from these tools.
Ensure that issues are fixed before pushing code, as pre-commit hooks will run these checks and prevent pushing if they fail.

**Pre-commit hooks**
Pre-commit is configured to run on pre-push, not on pre-commit.
The user will be prevented from pushing if the check fails.
`uv run pre-commit run --all-files --hook-stage pre-push` can be used to check for errors before pushing.

**Pitfalls**
- Not using `uv run` to run commands.
- Pushing failing code. VS Code won't show pre-push hook errors.
   => Run `uv run pre-commit run --all-files --hook-stage pre-push` to check for errors before pushing.
   => Have the user run `git push`
