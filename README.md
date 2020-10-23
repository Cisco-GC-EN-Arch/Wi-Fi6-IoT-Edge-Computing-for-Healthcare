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
4. py data_collection.py 
  This Python script is running in WIFI6 AP to collect data.
5. py data_analysis.py
  This Python script is running in analysis server to filter data and store the useful data to MySQL.

## MySQL Configuration

Some useful commands for MySQL:
  List all database: mysql>show databases;
  Create database: mysql>create database <your database name>;
  Select database: mysql>use <your database name>;
  List all tables in selected database: mysql>show tables;
  Create table: mysql>create table <your table name> (column1_name column1_type, column2_name column2_type, ... )
  Check details of a table: mysql>show create table <your table name>;
  Select table: mysql>desc <your table name>;
  Delete a table: mysql>drop table <your table name>;
  Google is awesome!     

## Known issues

Issues please refer to [here](https://github.com/Cisco-GC-EN-Arch/Wi-Fi6-IoT-Edge-Computing-for-Healthcare/blob/main/about-issues) to track issues.

## Getting help

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

