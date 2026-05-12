#!/bin/bash
set -e

SCRIPTS_DIR="/app/.github/scripts"

echo "Running todo.py..."
python3 "$SCRIPTS_DIR/todo.py" | tee /tmp/todo_output.txt

echo "Running todo-test.py..."
python3 "$SCRIPTS_DIR/todo-test.py" | tee /tmp/test_output.txt

echo "Updating index.html..."
bash "$SCRIPTS_DIR/update_index.sh" /tmp/todo_output.txt /tmp/test_output.txt

echo "Entrypoint complete."
