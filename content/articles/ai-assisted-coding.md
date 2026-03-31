description: A comprehensive guide to AI coding tools — from autocomplete to agentic systems like Claude Code. How they work, how to use them well, and how to build a safety net around AI-generated code.
title: AI Assisted Coding: A Practical Guide | Westsmith
author: Daniel Ball, founder of Westsmith

# AI Assisted Coding

<div style="font-family:monospace;background:#111;color:#ccc;border-radius:8px;padding:1.25rem 1.5rem;margin:1.5rem 0;max-width:480px;font-size:0.82rem;line-height:1.7;">
  <div style="margin-bottom:0.6rem;"><span style="color:#ff5f57;">●</span> <span style="color:#febc2e;">●</span> <span style="color:#28c840;">●</span></div>
  <span style="color:#7c8;">$</span> claude "refactor the auth module"<br>
  <span style="color:#666;">Reading 9 files…</span><br>
  <span style="color:#7c8;">✓</span> auth.py — simplified token logic<br>
  <span style="color:#7c8;">✓</span> tests/test_auth.py — 6 new cases added<br>
  <span style="color:#7c8;">✓</span> README.md — updated<br>
  <span style="color:#555;">3 files changed, 94 insertions(+), 71 deletions(-)</span>
</div>

This is my attempt to make sense of the AI-assisted coding landscape — written to educate and as a reference for anyone trying to navigate this space without the hype.

## AI Coding Glossary

- **Agentic AI** — An AI system that doesn't just respond to a single prompt but takes sequences of actions autonomously

- **Cargo-Cult Programming** — Writing code by copying patterns or snippets without understanding why they work, hoping the result will behave correctly by association. Stack Overflow made this easy. AI tools risk amplifying it further.

- **Context Window** — The maximum amount of text (code, instructions, conversation history) an AI model can "see" at once when generating a response. Measured in tokens.

- **Code Completion** — A feature in IDEs that suggests the next token, method or block of code as you type, ranging from simple symbol lookup to ML-ranked suggestions to full-line and multi-line generation.

- **Frontier models** are the most advanced, large-scale, general-purpose AI systems that push the boundaries of current capabilities in reasoning, multimodality and scale. These high-cost models from companies like OpenAI, Anthropic and Google set the benchmark for intelligence and are considered the foundation of the AI industry.

- **[MCP (Model Context Protocol)](https://modelcontextprotocol.io/docs/getting-started/intro)** — An open standard for connecting AI agents to external data sources and tools. With MCP, a coding assistant can be connected to Jira, Slack, Google Drive, Figma, or any custom internal tooling that exposes an MCP server. Increasingly supported across Claude Code, Cursor, Windsurf and other agentic tools.

- **Vibe Coding** — A term coined by [Andrej Karpathy in early 2025](https://x.com/karpathy/status/1886192184808149383?lang=en) describing a style of development where the programmer describes intent in natural language and largely accepts whatever the AI generates, iterating through prompts rather than writing code directly.

- **Zero-shot / Few-shot Prompting** — Zero-shot means asking an AI to perform a task with no examples, relying purely on its training. Few-shot means providing one or more examples in the prompt to demonstrate the desired pattern before asking it to continue.

## The Evolution of Code Assistance

**Paper Manuals & Reference Books** — The original developer companion. You'd thumb through language references, API docs or O'Reilly books to find the right method signature.

**Online IDE Documentation & Language References** — As the web matured, documentation moved online. IDEs integrated this so you could hover over a symbol and get inline docs.

**Copying from Stack Overflow, GitHub & Open Source** — Arguably the most impactful "tool" of the mid-2000s to 2010s developer toolkit. For coding capability, today's AI models are heavily dependent on the content of Stack Overflow and GitHub.

**Early Code Completion (2000s IDEs)** — Tools like early Eclipse, Visual Studio and IntelliJ began offering basic autocomplete, typically triggered by typing a dot after an object. Useful for reducing typos in method names but rarely capable of suggesting whole patterns or intent.

**Autocompletion Before AI — Jedi & Rope** — Python's dynamic typing made static autocompletion genuinely hard. Early tools like [Rope](https://github.com/python-rope/rope) and later [Jedi](https://jedi.readthedocs.io/en/latest/) tackled this with deep static analysis.

**Autocompletion — Using AI** — The landscape shifted significantly when GitHub launched [GitHub Copilot](https://github.com/features/copilot) in 2021, generating entire functions and suggesting multi-line logic from natural language comments rather than simply ranking symbol candidates.

**Copying and Pasting into ChatGPT (Pre-Agentic)** — When [ChatGPT](https://chatgpt.com) launched publicly in late 2022 it changed developer workflows overnight. For the first time you could have a conversation about your code, ask follow-up questions, request a refactor or say "that didn't work, here's the error."

**Agentic tools** like [Claude Code](https://claude.ai/code) operate at a fundamentally different level. Rather than completing tokens or ranking symbols, they understand intent across an entire codebase. You describe what you want in plain language, and they can generate, refactor, debug and explain across multiple files simultaneously. Used via the CLI, Claude Code can run commands, read outputs and iterate — behaving less like a tool and more like a junior engineer pair-programming alongside you.

**The Near Future — Agents with Persistent Context** — The next step is likely persistent, project-aware agents that maintain a living model of your codebase between sessions. Think less "answer my question" and more "autonomous collaborator" that files its own PRs, writes tests as code changes and flags when a new feature conflicts with an architectural decision made six months ago.

## How AI Coding Assistants Work

### The Spectrum of Assistance

It helps to think of AI coding assistants as sitting on a spectrum from **ambient/reactive** at one end to **agentic** at the other.

At the reactive end, tools like **GitHub Copilot** sit close to your cursor. They observe what you're typing, infer your intent from the surrounding code and comments, and suggest completions inline. The interaction model is passive: you write, it suggests, you accept or ignore.

At the agentic end, tools like **Claude Code** take a fundamentally different approach. Rather than predicting the next token of your code, they reason about goals, decompose tasks into steps, invoke tools, observe the results and decide what to do next.

### How Agentic Tools Work

<img src="/static/images/articles/agentic_coding_loop.png" alt="Agentic coding loop diagram">

The engine underneath an agentic coding assistant is an LLM equipped with a set of tools it can call. When you give Claude Code a task, it doesn't just generate text — it generates _decisions about what actions to take_. These might include reading a file, running a shell command, searching the codebase for a pattern or editing a file. Each action produces a result that is fed back into the model's context, informing the next decision.

Project-specific context can be injected into this loop at initialisation. Claude Code, for instance, reads a `CLAUDE.md` file from your project root at the start of every session, shaping every decision it makes.

### AI-Native IDEs

Tools like **Cursor** ([cursor.com](https://www.cursor.com)) replace the editor itself rather than operating in the terminal or as an extension. Built as a fork of VS Code, Cursor embeds AI as a first-class participant in how you navigate, write and refactor code.

### The Role of the Context Window

Every LLM-based tool is fundamentally constrained by its context window. A large repository can contain millions of tokens worth of code. The model can't read all of it at once. Agentic tools therefore need strategies for deciding _what to include_ in the context at any moment — semantic search, LSP integration to understand code structure, and explicit user-directed context attachment (the `@filename` pattern).

### Model Context Protocol

**MCP** is an open standard for connecting AI agents to external data sources. With MCP, a coding assistant isn't limited to your local files — it can be connected to your Jira board, your Slack workspace, your Google Drive or any custom internal tooling that exposes an MCP server.

This shifts the agent's effective context from "what's in this repository" to "what's in your entire development environment."

## How to Use an AI Coding Assistant

### Starting with the Right Mental Model

**Context is everything. Context costs tokens. Tokens cost money.**

AI coding assistants operate within a finite amount of text they can "see" at one time. The assistant doesn't remember last session's decisions. It doesn't know your project's conventions, your team's opinions or the architectural choices made six months ago — unless you tell it.

### Customising Your Assistant

In Claude Code, you can create a `CLAUDE.md` file in the root of your project. This file is read at the start of every session and can contain anything you'd want a new developer to know before touching your codebase:

- The tech stack
- Coding conventions
- Which directories to leave alone
- How tests are structured
- Which commands to run to start the dev server

Think of it as your project's onboarding document for the AI. The difference between a session that starts with this context and one without is significant.

**Custom commands and slash commands** are another underused feature. Claude Code lets you define custom `/commands` that encapsulate common workflows like running your test suite or triggering a code review prompt against your own standards.

### The Token Economy: Where People Go Wrong

- **Pasting entire files when only a function is relevant.** If you're asking about a bug in a 40-line function, you don't need to include the entire 800-line module.
- **Repeating context that's already been established.** Once you've explained your stack and architecture, you shouldn't keep re-stating it.
- **Ignoring conversation history bloat.** Long, meandering sessions accumulate tokens fast. Consider starting a fresh session once a side issue is resolved rather than carrying all that history forward.
- **Asking for broad rewrites when targeted edits would do.** "Refactor this entire service" consumes far more tokens than "Extract the database logic from this controller into a separate repository class."
- **Not using Plan Mode or equivalent.** Many tools offer a mode where the assistant describes what it intends to do before doing it. This lets you catch misunderstandings before the assistant has burned tokens on the wrong approach.

### Planning as a First-Class Activity

Before starting a significant task, it's worth spending a few minutes writing down in plain language what you're trying to achieve, what constraints apply and what a successful outcome looks like.

Some developers maintain a suite of markdown files that together form a kind of living project memory: an `ARCHITECTURE.md` covering high-level design decisions, a `CONVENTIONS.md` for style and naming rules, a `DECISIONS.md` logging why certain approaches were chosen and a `PROGRESS.md` tracking what's done and what's next.

### Asking Well

- Be explicit about what you already know
- Specify the format you want for the response
- Break complex tasks into discrete steps
- Use the `@filename` pattern to attach precise context
- If a response isn't right, refine the prompt rather than argue with the output

## The Landscape

### AI Coding Tools

| Tool | Description |
| --- | --- |
| [Claude Code](https://www.anthropic.com/claude-code) | Uses Anthropic models. Agentic coding tool that lives in your terminal. Reads, edits and reasons across entire codebases. |
| [Cursor](https://www.cursor.com) | AI-native code editor (VS Code fork). Composer mode handles multi-file edits autonomously. |
| [Lovable](https://lovable.dev) | Browser-based platform that turns natural language prompts into full-stack React/Supabase apps. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Open source. Uses Google's Gemini models. Terminal coding agent with MCP and Google Search integration. |
| [GitHub Copilot](https://github.com/features/copilot) | Integrated into VS Code, JetBrains and the GitHub ecosystem. Covers inline completions, chat, agent mode and PR summaries. |
| [Devin](https://devin.ai) | Autonomous software engineer that operates independently via Slack or a VSCode-style interface, spawning its own environment to plan, code, test and open PRs. |
| [Aider](https://aider.chat) | Open source. Model-agnostic. Terminal coding agent. Stages git changes and writes commit messages automatically. |
| [Cline](https://cline.bot) | Open source. Model-agnostic. VS Code extension. Shows diffs inline and requires explicit approval before running terminal commands. |

### Models that perform well at coding

Several benchmarks track coding capability. The most useful:

- [SWE-bench](https://www.swebench.com/) — measures how often a model can resolve real GitHub issues autonomously
- [LiveCodeBench](https://livecodebench.github.io/index.html) — live competitive programming problems, updated continuously
- [Vellum LLM Leaderboard](https://www.vellum.ai/llm-leaderboard) — practical comparison of frontier models across quality, speed and cost

## Building in a Safety Net

Vibe coding and automated code generation introduce the risk of unmaintainable, non-working or insecure code. This is where automated tooling becomes not just useful but essential.

### Quick to run and free: static analysis

Linting tools have been around for years, are generally free and can run in seconds. Including them in a pre-commit hook means you can't forget to run them.

- **Ruff** — fast Python linter and formatter. Catches style issues, unused imports and obvious bugs.
- [**Bandit**](https://bandit.readthedocs.io/) — analyses Python code for common security issues.
- [**Semgrep**](https://semgrep.dev/docs/) — language-agnostic, uses rules to detect patterns and has a large library of security-focused rules.

### Quick to run: unit testing

Unit testing is non-negotiable in modern software development, and AI tools have made high coverage levels more achievable than ever. Feed the AI your function signatures, docstrings and intent, then ask it to surface edge cases, boundary conditions and failure modes you might not have considered.

**A few rules worth following:**

- Every file should have a corresponding test file
- Target 90% coverage as a minimum
- Generate tests from descriptions first, then iterate by asking the AI to find edge cases
- Write some tests by hand to stay close to what the code is actually supposed to do
- Treat the need for patching as a design smell to fix in the production code

### Slower to run: AI PR reviewers

**CodeRabbit** is the current market leader in purpose-built AI code review. It installs as a GitHub or GitLab app, runs automatically on every pull request and leaves line-by-line comments with severity rankings. Free for open source.

**GitHub Copilot Code Review** was added in April 2025 and is bundled into existing Copilot subscriptions. Shallower than CodeRabbit but costs nothing extra if you're already paying for Copilot.

### SAST Platforms

**SonarQube / SonarCloud** combines code quality and security into a single dashboard. The Community Edition is free and self-hosted.

**Snyk Code** uses data-flow analysis to catch things like second-order SQL injection where tainted data passes through multiple functions before hitting a sink. It also bundles dependency scanning, container scanning and IaC analysis.

### Dependency security

**Dependabot** is free, built into GitHub and opens automatic pull requests for vulnerable dependencies. Enable it if you haven't. For more serious supply chain concerns, **Socket.dev** analyses the behaviour of npm and PyPI packages and can detect packages that exfiltrate data at install time.

### Integration and end-to-end tests

Integration tests verify that your code works correctly with the real systems it depends on. **Docker Compose** and **testcontainers-python** make it straightforward to run a real Postgres instance, Redis cache or message queue locally or in CI.

For end-to-end tests, **Playwright** is the current tool of choice. It supports Python, JavaScript and TypeScript, runs headlessly in CI and has a codegen feature that records browser interactions and outputs test code automatically.
