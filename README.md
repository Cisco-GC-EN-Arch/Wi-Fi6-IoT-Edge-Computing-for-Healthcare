# Wi-Fi6 IoT Edge Computing for Healthcare

There is a lot of patient data information to collect in the hospital, yet a shortage of nurses is common. Cisco Smart AP provides edge computing capabilities to automate data collection for scenarios like hospitals, saving human resources, improving data accuracy, automating emergency response, and more.

Pro tips: 

* Code Exchange displays the first few content lines of your README in the tile it creates for your repo. If you enter a GitHub Description, Code Exchange uses that instead. 
* Code Exchange works best with READMEs formatted in [GitHub's flavor of Markdown](https://guides.github.com/features/mastering-markdown/). Support for reStructuredText is a work in progress.

Other things you might include:

* Technology stack: Indicate the technological nature of the code, including primary programming language(s) and whether the code is intended as standalone or as a module in a framework or other ecosystem.
* Status:  Alpha, Beta, 1.1, etc. It's OK to write a sentence, too. The goal is to let interested people know where what they can expect from this code.
* Screenshot: If the code has visual components, place a screenshot after the description; e.g.,

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

## How smart AP collects data

![Edge Computing](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/AP%20PY%20code.PNG)

## Configuration

Google is awesome!
If the code is configurable, describe it in detail, either here or in other documentation that you reference.

## Usage

Please refer to PPT file.

## Known issues

Issues please refer to [here](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/about-issues) to track issues.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

