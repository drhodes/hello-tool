# Hello Tool for OpenCode

Welcome to the `hello-tool` project! This repository contains OpenCode tools and a specification-driven architecture designed to be robust and highly extensible.

## Overview

This project is built around creating robust tools for OpenCode (an AI coding agent ecosystem) using the `@opencode-ai/plugin` framework. It utilizes a custom Python-based requirement specification framework (`libspec`) to rigorously define features and expected behaviors before they are implemented.

## Directory Structure & Architecture

### 1. The Specification Framework (`/spec`)
Instead of just writing code, this project uses a structured specification framework to define what the tools should do:
- **`spec/err.py`**: Defines the foundational `Err` specification. This mandates that all tools must implement *extreme, elegant error handling*. It ensures that if a function or tool fails, the generated error messages are highly descriptive, capturing standard out/error and making the failure completely understandable.
- **`spec/app.py`**: Defines the specific OpenCode tool requirements:
  - `Hello` (`hello-tool.ts`): A simple tool that shells out and runs `echo Hello World!`.
  - `HelloPython` (`hello-python-tool.ts`): A tool that shells out and runs a Python script (`uv run main.py`) from the project root.
- **`spec/main_spec.py`**: The entry point that bundles these specs to generate XML definitions for validation and review.

### 2. The OpenCode Implementation (`/.opencode/tools`)
The actual tools used by the OpenCode agent are implemented in TypeScript:
- **`hello-tool.ts`**: Implements the `Hello` specification.
- **`hello-python-tool.ts`**: Implements the `HelloPython` specification.


### 3. The Python Environment
- **`main.py`**: A simple Python entry point intended to be invoked by the OpenCode tools via the high-performance `uv` package manager.
- **`Makefile`**: Contains utility commands for building the specifications.


### Extending the Project
When adding a new OpenCode tool:
1. Define the tool requirement in `/spec/app.py` (ensure it inherits from `Req` or `Tool`).
2. Add your TypeScript implementation in `/.opencode/tools/`.
3. Ensure you follow the strict error-handling paradigm as defined in `spec/err.py`.
