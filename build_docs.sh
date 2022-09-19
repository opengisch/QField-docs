#!/usr/bin/env bash

### Build the documentation for all languages in Docker ###
# Run with for example:
# docker build . -f Dockerfile-parbuild --build-arg tx_token=... -t qfield-docs
# docker run -it -v ${PWD}/build:/opt/app/build --rm qfield-docs

# Import languages from an .env file
export $(grep -v '^#' .env | xargs)

# Languages
##  this presupposes we have:
##  - LANGUAGE_CODES=de,en,es,fr...
##  - LANGUAGES=Deutsch,English,Espagñol,Français,
language_codes=(${LANGUAGE_CODES//,/ })
languages=(${LANGUAGES//,/ })
language_codes_hashmap=hash[${language_codes[i]}]=${languages[i]}

# Cores
cores=4

# Task
run_task(){
    # Build output
    output_dir="build"

    lang_code="$1"
    lang="${language_codes_hashmap[lang_code]}"
    path="$output_dir/$lang_code"

    echo "Building $lang (code: $lang_code) to $path"
    mkdir -p $path
    LANGUAGE_CODE="$lang_code" LANGUAGE="$lang" bash -c "mkdocs build -d $path"
    return 0
}

export -f run_task output_dir

# Initial check
if [ "${#language_codes_hashmap[@]}" -eq 0 ]; then
    echo 'No language found. Aborting.'
    exit -1
fi

# Set up
echo "Found these languages: ${languages[@]}"
echo "Building now in parallel using $cores cores..."

# Building in parallel
source .venv/bin/activate
printf "%s\n" "${language_codes[@]}" | xargs -n 1 -P $cores -I lang_code bash -c 'run_task lang_code'
