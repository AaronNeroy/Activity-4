#!/bin/bash
# Usage: bash update_index.sh <todo_output_file> <test_output_file>

TASK_FILE=$1
TEST_FILE=$2
HTML_FILE="index.html"

# Extract ToDo and Done sections
TODO_CONTENT=$(awk '/^ToDo Tasks:/{found=1; next} /^Done Tasks:/{found=0} found{print}' "$TASK_FILE")
DONE_CONTENT=$(awk '/^Done Tasks:/{found=1; next} found{print}' "$TASK_FILE")
TEST_CONTENT=$(cat "$TEST_FILE")

# Update a <pre> tag by id using perl
update_pre() {
    local id=$1
    local content=$2
    local file=$3
    local escaped_content
    escaped_content=$(printf '%s' "$content" | perl -pe 's/([\\\/\@\$])/\\$1/g')
    perl -i -0777 -pe "s|(<pre id=\"$id\">)(.*?)(</pre>)|\${1}${escaped_content}\${3}|s" "$file"
}

update_pre "todo-tasks" "$TODO_CONTENT" "$HTML_FILE"
update_pre "done-tasks" "$DONE_CONTENT" "$HTML_FILE"
update_pre "test-results" "$TEST_CONTENT" "$HTML_FILE"

# Git integration
git config user.email "ci-bot@github.com"
git config user.name "CI Bot"
git add "$HTML_FILE"
git commit -m "Update index.html with latest task and test results [ci skip]"
git push
