#!/bin/bash

# Ensure uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ 'uv' is not installed. Please install it first."
    exit 1
fi

# Title from argument
TITLE="$*"

if [ -z "$TITLE" ]; then
    echo "❌ No post title provided."
    echo "Usage: ./create_post.sh \"Post Title Here\""
    exit 1
fi

# Run the CLI using uv
uv run cli.py create "$TITLE"
