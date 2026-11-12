# Environment Setup Notes

## Purpose

Prepare a reproducible editor environment for comparing manual coding with AI-assisted coding. This sprint uses OpenAI Codex as the alternative coding assistant permitted by the assignment.

## Environment

Versions below were collected from the participant's Windows PowerShell terminal on November 12, 2026.

| Tool | Version / details |
| --- | --- |
| Operating system | Windows; exact OS version not recorded |
| Terminal | PowerShell; version not recorded |
| IDE | Visual Studio Code 1.146.0, x64 |
| VS Code commit | 69047191fc427f2f92828279aae1d90d8eeda7ab |
| Version control | Git 2.55.0.windows.3 |
| AI coding assistant | OpenAI Codex extension (`openai.chatgpt`) 26.1106.51428 |

## Installed Extensions

| Extension ID | Version | Purpose |
| --- | --- | --- |
| openai.chatgpt | 26.1106.51428 | OpenAI coding assistant / Codex integration |
| openai.codex-audio | 26.1106.51428 | Codex audio integration |
| esbenp.prettier-vscode | 12.4.0 | Code formatting |
| ms-azuretools.vscode-containers | 2.5.3 | Container tooling |
| ms-vscode-remote.remote-containers | 0.469.0 | Development container support |

GitHub Copilot was not present in the supplied extension inventory. OpenAI Codex is the selected alternative; no Copilot installation is claimed.

## Setup and Verification Process

The editor and extensions were already installed. The following steps document the verified environment rather than claiming a new installation:

1. Open PowerShell on the development computer.
2. Run `code --version` to identify the VS Code version, commit, and architecture.
3. Run `code --list-extensions --show-versions` to identify installed extensions and confirm the OpenAI extension is present.
4. Run `git --version` to confirm Git is available.
5. Use the OpenAI Codex panel in VS Code for the AI-assisted trial. Authentication and a successful local chat response still need to be verified on the development computer.

## Recorded Verification Results

- VS Code CLI: confirmed working from the supplied output.
- Git CLI: confirmed working from the supplied output.
- OpenAI extension installation: confirmed by the supplied extension list.
- Local Codex authentication and response: not independently verified. Installation alone does not prove that the assistant is authenticated or responding.
- Model, account plan, runtime, and test framework versions: not yet recorded; record them when selecting benchmark tasks.

## Controlled Sprint Procedure

- Use the same task requirements, starting files, runtime, formatter, and tests for both trials.
- For the manual trial, disable AI extensions for the workspace and do not use AI chat, agents, or completions.
- For the assisted trial, enable Codex and record the model shown in the interface, prompts, and any manual corrections.
- Record trial order: doing the same task twice creates a practice effect, so time differences cannot be attributed entirely to AI.
- Measure time from reading the task until the solution passes the agreed checks, including review, debugging, and testing.
- Evaluate correctness and readability alongside elapsed time; line count alone is not a quality measure.
- Keep credentials and account tokens out of repository files.
