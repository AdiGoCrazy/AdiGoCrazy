#!/usr/bin/env python3
"""
Script to update GitHub repository descriptions and topics for AdiGoCrazy.
Usage: python3 update_descriptions.py <YOUR_GITHUB_TOKEN>
"""

import sys
import json
import urllib.request

REPOS_DATA = {
    "dotfiles": {
        "description": "🌌 Modern Hyprland + Waybar Linux rice for Arch Linux featuring custom GTK3 Python telemetry widgets for Ollama LLMs, GPU & Docker.",
        "topics": ["hyprland", "waybar", "dotfiles", "arch-linux", "rice", "gtk3", "wayland"]
    },
    "radarr-agent": {
        "description": "🤖 Autonomous, self-hosted AI agent architecture designed to manage local Arr media stacks via natural language, LangGraph, FastMCP & Ollama.",
        "topics": ["ai-agent", "langgraph", "ollama", "fastmcp", "python", "self-hosted", "radarr"]
    },
    "ProjectTUI": {
        "description": "💻 High-performance, keyboard-driven Terminal User Interface (TUI) for local project discovery, dependency management & container execution.",
        "topics": ["tui", "terminal", "python", "textual", "docker", "developer-tools"]
    },
    "Video-Generator": {
        "description": "🎥 Automated video creation, editing & rendering desktop application built with CustomTkinter & MoviePy.",
        "topics": ["python", "video-generator", "moviepy", "customtkinter", "gui"]
    },
    "Backend-Programming": {
        "description": "⚡ Enterprise transit operations & fleet management platform developed as a hackathon project (Odoo TransitOps).",
        "topics": ["python", "odoo", "postgresql", "backend", "transit-management"]
    },
    "AdiGoCrazy": {
        "description": "✨ Personal GitHub Profile README matching my Hyprland Frosted Midnight Linux desktop theme.",
        "topics": ["github-config", "profile-readme", "hyprland-theme"]
    }
}

def update_repo(repo_name, info, token):
    url = f"https://api.github.com/repos/AdiGoCrazy/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Python-Script"
    }

    # 1. Update Description
    desc_data = json.dumps({"description": info["description"]}).encode("utf-8")
    req = urllib.request.Request(url, data=desc_data, headers=headers, method="PATCH")
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"✅ Updated description for {repo_name}")
    except Exception as e:
        print(f"❌ Failed to update description for {repo_name}: {e}")

    # 2. Update Topics
    topics_url = f"{url}/topics"
    topics_data = json.dumps({"names": info["topics"]}).encode("utf-8")
    req_topics = urllib.request.Request(topics_url, data=topics_data, headers=headers, method="PUT")
    try:
        with urllib.request.urlopen(req_topics) as resp:
            print(f"✅ Updated topics for {repo_name}")
    except Exception as e:
        print(f"❌ Failed to update topics for {repo_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 update_descriptions.py <YOUR_GITHUB_TOKEN>")
        sys.exit(1)

    token = sys.argv[1]
    for repo, data in REPOS_DATA.items():
        update_repo(repo, data, token)
