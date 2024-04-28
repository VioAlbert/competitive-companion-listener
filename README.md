# Competitive Companion Listener

A simple parser that receives input from [Competitive Companion](https://github.com/jmerle/competitive-companion) and download sample testcases.

## Usage

First, clone this repository.

Run the main script to execute the parser.
```
python main.py
```

Then, run the [Competitive Companion](https://github.com/jmerle/competitive-companion). The testcases will be downloaded to the `sample` directory.

To call the parser from any directory, add an alias pointing to `start.sh` in your `bashrc` or `zshrc`.

For `bashrc`:
```
alias "cplisten"="path/to/competitive-companion-listener/start.sh"
```

For `zshrc`:
```
alias "cplisten=path/to/competitive-companion-listener/start.sh"
```
