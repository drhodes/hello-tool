# Hello Tool for OpenCode

Welcome to the `hello-tool` project! This repository contains OpenCode
tools. The purpose of this project is to create a simple "Tool" for
OpenCode using the `@opencode-ai/plugin` framework.

## Directory Structure & Architecture

### 1. The OpenCode Implementation (`/.opencode/tools`)
The actual tools used by the OpenCode agent are implemented in TypeScript:
- **`hello-tool.ts`**: Implements the `Hello` specification.
- **`hello-python-tool.ts`**: Implements the `HelloPython` specification.

### 2. The Python Environment
- **`main.py`**: A simple Python entry point intended to be invoked by
  the OpenCode tools via the `uv` python package manager. The tools
  called from OpenCode are written in either typescipt or javascript
  and run under Node, which can shell out to bash.
