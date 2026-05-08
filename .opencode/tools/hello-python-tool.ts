import { tool } from "@opencode-ai/plugin"
import { execSync } from "child_process"

export default tool({
	description: "This tool runs the Python main.py script using uv.",
	args: {},
	async execute() {
		const output = execSync("uv run main.py", {
			encoding: "utf8",
			cwd: "/usr/backup-working/work/hello-tool"
		})
		return output.trim()
	}
})