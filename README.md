# AQI Pollutant Calculator

> 💡 This simple python program was written for university assignment and serves no real-world purpose. This is part 2 of a series, [part i](https://github.com/miclgael/air-quality) and [part iii](https://github.com/miclgael/air-quality-gui) are available if interested.

This program is for use by Codetown council workers to summarise collected air quality information by calculating averages from each location.

## Table of Contents

- [AQI Pollutant Calculator](#aqi-pollutant-calculator)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example of `readings.txt`](#example-of-readingstxt)
    - [Running the program](#running-the-program)
  - [Example Usage](#example-usage)
    - [1. Running the program](#1-running-the-program)
    - [2. Example Input (from your `readings.txt`)](#2-example-input-from-your-readingstxt)
    - [2. Expected Output](#2-expected-output)
  - [Troubleshooting Guide](#troubleshooting-guide)
  - [Help](#help)

## Installation

No package dependencies (eg, pip) are required. Note, however, this program was designed to run optimally with `Python 3.8.2`

## Usage

The program requires an input file with special formatting in order to run correctly. 

1. The file _must_ be named `readings.txt`
2. Each line of the file should consist of a location name and an AQI reading, separated by a single comma (with no spaces between location and reading).

### Example of `readings.txt`

```
Mallowbeach,67.4
Glassdell,14
Fayhedge,68.86
Glassdell,15
Mallowbeach,70.3
```

### Running the program

To run the program, enter the following commands into your terminal prompt

1. Change to the directory where the application is installed with `cd /<PATH>/<TO>/<PROGRAM>/air-quality-list`
2. **Important** Create or copy your `readings.txt` **into the same directory** as the `air_quality_list.py` file
3. Start the program with `python air_quality_list.py`, or `python3 air_quality_list.py` (depending on your system configuration).

## Example Usage

### 1. Running the program

```bash
$ python3 air_quality_list.py
```

### 2. Example Input (from your `readings.txt`)

```
Mallowbeach,67.4
Glassdell,14
Fayhedge,68.86
Glassdell,15
Mallowbeach,70.3
```

### 2. Expected Output

```bash
Fayhedge 68.86
Mallowbeach 68.85
Glassdell 14.5
```
## Troubleshooting Guide

The program will produce warnings or errors when it encounters a file in an incorrect format. 
Some errors will corrupt the results in the output, so care should be taken to ensure any issues are resolved.

Below is a guide to errors you may encounter, and steps to resolve.
 
Error / Warning    | Solution                                              
------------------ | ------------------------------------------------------
`comma-space`      | Remove spaces between comma, location and AQI reading.
`value-is-missing` | Provide an AQI reading for every location. There should be no empty lines in the file
`value-is-float`   | The AQI must be a valid integer (eg. `1`) or floating point integer (eg. `1.1`).
`no-location-name` | A location name should be provided for every line of the program.

Please note that `comma-space` and `no-location-name` are warnings only. These are messages (displayed in yellow) that indicate problems with formatting, but are handled automatically, and don't necessarily corrupt the output of the program.

Other errors such as `value-is-missing` and `value-is-float` (displayed in red) indicate that the results have been corrupted by the malformed input, and should be resolved (manually) before the output of the program can be trusted.

## Help

Please email [Michael Gale](mailto:mgale8@myune.edu.au) to report bugs or for any technical assistance.
