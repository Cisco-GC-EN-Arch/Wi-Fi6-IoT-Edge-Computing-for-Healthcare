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

1. git clone https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare.git
2. cd Wi-Fi6-IoT-Edge-Computing-for-Healthcare
3. pip install requirements.txt
4. py data_collection.py</br>
  This Python script is running in WIFI6 AP to collect data.
5. py data_analysis.py</br>
  This Python script is running in analysis server to filter data and store the useful data to MySQL.

## MySQL Configuration

1. Create database: mysql>create database wifi6_edge_computing;
2. Select database: mysql>use wifi6_edge_computing;
3. Create table: mysql>CREATE TABLE t_h_test(update_time timestamp DEFAULT CURRENT_TIMESTAMP,
    -> temperature float(10,2) NOT NULL,
    -> humidity float(10,2) NOT NULL,
    -> PRIMARY KEY (update_time))ENGINE=InnoDB DEFAULT CHARSET=utf8;
4. Select table: mysql>desc t_h_test;
</br>We are going to use the database named wifi6_edge_computing and the tables named t_h_test with columns update_time(PRIMARY KEY), temperature and humidity.

## Known issues

Issues please refer to [here](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/about-issues) to track issues.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

