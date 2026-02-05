Here is the README.md file for the Practica12 repository:
```markdown
# Practica12
================

**Project Description**
------------------------

A Raspberry Pi project that demonstrates how to configure a systemd service using Python.

**Hardware Requirements**
-------------------------

* Raspberry Pi board (tested on RPi 4)
* MicroSD card with at least 8GB of storage
* Power supply for the Raspberry Pi board

**Supported Boards**
--------------------

* Raspberry Pi 4

**Libraries Used**
------------------

* None (built-in Arduino libraries)

**Pin Configuration**
---------------------

None (no pin configuration required)

**Installation**
---------------

1. Clone this repository to your Raspberry Pi's home directory using Git: `git clone https://github.com/your-username/Practica12.git`
2. Navigate to the project directory: `cd Practica12`
3. Create a new Python script in the `/home/pi/scripts` directory: `echo '#!/usr/bin/env python3' > /home/pi/scripts/mi_script.py`

**Compilation & Upload**
------------------------

No compilation required. The code is written in C++ and executed directly on the Arduino/ESP32 board.

**Project Structure**
---------------------

* `pasos.txt`: A text file containing step-by-step instructions for setting up a systemd service.
* `main.cpp`: The main program file that demonstrates how to configure a systemd service using Python.

**Usage Example**
-----------------

1. Create a new Python script in the `/home/pi/scripts` directory.
2. Configure the systemd service by creating a new file in the `/etc/systemd/system/` directory.
3. Enable and start the systemd service using the following commands: `sudo systemctl enable mi_app.service` and `sudo systemctl start mi_app.service`

**Notes**
--------

* Make sure to replace `mi_script.py` with your actual Python script name.
* This project assumes that you have Python 3 installed on your Raspberry Pi.

**License**
---------

MIT License

Copyright (c) [Year] [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```