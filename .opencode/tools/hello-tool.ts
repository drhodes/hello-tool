import { tool } from "@opencode-ai/plugin"
import { execSync } from "child_process"

export default tool({
	description: "This is a tool for use with opencode. The only thing it does is tell the coding agent 'Hello world!'.",
	args: {},
	async execute() {
		const output = execSync("echo Hello, World!", { encoding: "utf8" })
		return output.trim()
	}
})
