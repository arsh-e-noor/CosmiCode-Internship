#!/bin/bash

echo "DevOps Shell Script Execution Started"

touch hello.txt
echo "This is a DevOps internship task." > hello.txt
echo "Practicing basic shell scripting." >> hello.txt

mkdir test_dir
mv hello.txt test_dir/

echo "Directory Contents:"
ls -l test_dir/

echo "File Content:"
cat test_dir/hello.txt

echo "Script Execution Complete"
