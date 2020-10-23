# Wi-Fi6 IoT Edge Computing for Healthcare

There is a lot of patient data information to collect in the hospital, yet a shortage of nurses is common. Cisco Smart AP provides edge computing capabilities to automate data collection for scenarios like hospitals, saving human resources, improving data accuracy, automating emergency response, and more.

![Topology](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/Topology.png)


## Use Case Description

Business Challenges
1. It takes extra time on patient info collecting, like blood pressure etc.
2. There might be mistakes when info is collected manually.
3. Extra deployment and management with a dedicated IoT network.

## Installation

Components:
1. AP 9120 (physical) - Collecting patients info (like blood pressure etc.) and environment info (like temperature humidity etc.)
2. MySQL (VM) - Store the data that collected by APs.
3. Grafana (VM) - Data visibility.
4. Python - Making the Impossible Possible.

## Files instruction

1. [file] data_collection.py - Python script running in WIFI6 AP to collect data.
2. [file] data_analysis.py - Python script running in analysis server to filter data and store the useful data to MySQL.

## Configuration

  Google is awesome!     
  If the code is configurable, describe it in detail, either here or in other documentation that you reference.

## Usage

Please refer to PPT file.

## Known issues

Issues please refer to [here](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/about-issues) to track issues.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

