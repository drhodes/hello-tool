import { tool } from "@opencode-ai/plugin"
import { z } from "zod"
import { execFileSync } from "child_process"
import path from "path"

export default tool({
	description: "This tool should shell out to the command line and run:\n$ uv run xpath.py <query>\nThe tool should open program.xml file from the directory\n. Then it should run the query on it.\nThe tool should have filename: \"hello-xpath.ts\"",
	args: {
		query: z.string().describe("The XPath query to run")
	},
	async execute({ query }) {
		try {
			const output = execFileSync("uv", ["run", "xpath.py", query], {
				encoding: "utf8",
				cwd: path.resolve(__dirname, "../../")
			})
			return output.trim()
		} catch (error: any) {
			const errorMessage = error.stderr || error.message || String(error);
			return `Error executing xpath.py:\n${errorMessage.trim()}`;
		}
	}
})
