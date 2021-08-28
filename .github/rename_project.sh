#!/usr/bin/env bash
while getopts a:n:u:d: flag
do
    case "${flag}" in
        a) author=${OPTARG};;
        n) name=${OPTARG};;
        u) urlname=${OPTARG};;
        d) description=${OPTARG};;
    esac
done

echo "Author: $author";
echo "Project Name: $name";
echo "Project URL name: $urlname";
echo "Description: $description";

echo "Renaming project..."

original_author="jovyan123-playground"
original_name="python_from_template"
original_urlname="python-from-template"
original_description="Awesome python_from_template created by jovyan123-playground"
# for filename in $(find . -name "*.*") 
for filename in $(git ls-files) 
do
    sed -i "s/$original_author/$author/g" $filename
    sed -i "s/$original_name/$name/g" $filename
    sed -i "s/$original_urlname/$urlname/g" $filename
    sed -i "s/$original_description/$description/g" $filename
    echo "Renamed $filename"
done

mv python_from_template $name

# This command runs only once on GHA!
if [ -f .github/workflows/python_from_template.yml ]; then
    mv .github/workflows/rename_project.yml .github/workflows/rename_project.yml.disabled
fi
