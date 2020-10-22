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

## Configuration

Google is awesome!
If the code is configurable, describe it in detail, either here or in other documentation that you reference.

## Usage

Please refer to PPT file.

## Known issues

Document any significant shortcomings with the code. If using [GitHub Issues](https://help.github.com/en/articles/about-issues) to track issues, make that known and provide any templates or conventions to be followed when opening a new issue. 

## Getting help

Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

## Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](./CONTRIBUTING.md) file.

## Credits and references

1. Projects that inspired you
2. Related projects
3. Books, papers, talks, or other sources that have meaningful impact or influence on this code

----

## Licensing info

A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to [Code Exchange](https://developer.cisco.com/codeexchange/) or [Automation Exchange](https://developer.cisco.com/automation-exchange/) requires a commitment to maintain the code and help the community use and contribute to the code. 

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc.   This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

> Cisco employees can find licensing options and guidance [here](https://wwwin-github.cisco.com/eckelcu/DevNet-Code-Exchange/blob/master/GitHubUsage.md#licensing-guidance).

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on *Add a license* and select from a set of [OSI approved open source licenses](https://opensource.org/licenses). See [detailed instructions](https://help.github.com/articles/licensing-a-repository/#applying-a-license-to-a-repository-with-an-existing-license).

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select *Create New File*, type *LICENSE* into the filename box, and you will be given the option to select from a set of common open source licenses. See [detailed instructions](https://help.github.com/articles/adding-a-license-to-a-repository/).

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the [3-Clause BSD license template](https://opensource.org/licenses/BSD-3-Clause) has the following copyright notice:

`Copyright (c) <YEAR>, <COPYRIGHT HOLDER>`

See the [LICENSE](./LICENSE) for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See [LICENSE](./LICENSE) for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the [LICENSE](./LICENSE) itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see [NOTICE](./NOTICE). 

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see [https://github.com/cisco/ChezScheme/blob/master/NOTICE](https://github.com/cisco/ChezScheme/blob/master/NOTICE).   

----

## Best practices

**Information below can help you make your repo meet our requirements and be more useful to others.**

### Good practices

1. Manage sensitive data for scripts. For example, store passwords/API keys and other sensitive data in env.py or parse it as arguments. In Python, you can use [ConfigParser](https://docs.python.org/3/library/configparser.html) for applications and programs: encrypt sensitive data in your database.
2. Include in Installation section how to run your script for different OS like Windows/macOS/Linux
3. Print usage if you run script or program without any input data (support -h -help flags)
4. Catch an error and print useful information in console and interface
5. Add error management to handle if users miss some parameters or add them in the wrong format
6. Add links for resources where users can test code/app. For example, add links DevNet sandboxs (Always-on or reservable). You can find a list of all available sandboxes here [https://devnetsandbox.cisco.com/RM/Topology](https://devnetsandbox.cisco.com/RM/Topology)
7. Add links where users can download and how to install additional soft/app/libraries that are needed to run your code. For example, installer for Python, node, etc. 
8. Add NOTICE file with copyright if you use GPLv3 or Apache 2.0 license ([sample](https://github.com/CiscoDevNet/opendaylight-sample-apps/blob/master/NOTICE)) 
9. Dockerize app or part of an app, like a server/client

 ### Bad practices
1. Use bad quality screenshots
3. Users need to rename some files like variables_template.py
4. Users need to include credentials in source file
5. Don’t describe in which format users need to type or paste in file API endpoint or server IP. For example, sometimes devs write in code api_endpoint = “https://" + IP +"/", such that users need to paste the IP only without a slash at the end or a protocol specification. Please clarify this information in README.
