import { tool } from "@opencode-ai/plugin"
import { execSync } from "child_process"
import path from "path"

export default tool({
	description: "This tool runs the Python main.py script using uv.",
	args: {},
	async execute() {
		const output = execSync("uv run main.py", {
			encoding: "utf8",
			cwd: path.resolve(__dirname, "../../")
		})
		return output.trim()
	}
})