#!/bin/bash

# Define variables
repository="https://github.com/seniorglez/metaPucela.git"
temp_folder="/tmp/metaPucela"
start_date="2023-09-01"
end_date="2023-09-10"
output_folder="./raw"

# Clone the repository into the temporary folder
git clone -b main "$repository" "$temp_folder"

# Create the output folder if it doesn't exist
mkdir -p "$output_folder"

# Copy the files that meet the condition to the output folder, force overwrite if necessary
for file in "$temp_folder/responses"/*.json; do
    filename=$(basename "$file")
    filedate=$(echo "$filename" | cut -d'_' -f1)
    if [[ "$filedate" > "$start_date" && "$filedate" < "$end_date" ]]; then
        cp -f "$file" "$output_folder"
    fi
done

# Delete the cloned repository from the temporary folder
rm -rf "$temp_folder"

