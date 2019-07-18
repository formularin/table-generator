# table-generator

### Generates code for html tables from csv files

## Installation

Install with git:

```bash
git clone https://github.com/lol-cubes/table-generator.git
chmod +x initialize.sh
./initialize.sh
```

## Usage
```bash
./table_generator.py [-achp] [attrs.json] input.csv
```
Options:

`-a`: following arg is path to a json file with html attributes for table element and corresponding values

`-c`: writes code for complete html file, such as `<!DOCTYPE html>` and `<html></html>` tags.

`-h`: turns first row of values in csv files into `<th>` or table header elements

`-p`: pretty prints output code