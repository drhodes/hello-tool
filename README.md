# Hello Tool for OpenCode

The purpose of this project is to create a simple "Tool" for the
OpenCode coding agent, using the `@opencode-ai/plugin` framework.
	
## Directory Structure & Architecture

### 1. The OpenCode Implementation (`/.opencode/tools`)
(Note the dot directory) The actual tools used by the OpenCode agent
are implemented in TypeScript:
- **`hello-tool.ts`**: Implements `hello world` in typescript
- **`hello-python-tool.ts`**: Implements `hello world` in python

### 2. The Python Environment
- **`main.py`**: A simple Python entry point intended to be invoked by
  the OpenCode tools via the `uv` python package manager. The tools
  called from OpenCode are written in either typescipt or javascript
  and run under Node, which can shell out to bash and in this case
  does $(uv run main.py)
