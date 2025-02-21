# Trashbot
Trash Sorting Robot

**Components:**
1. Arduino UNO R3 - https://store.arduino.cc/products/arduino-uno-rev3?srsltid=AfmBOorrB9WzC0gIFRTp5U0SmJ5peaQ4KQ1HP_Y2s53RNQZaKjdl6FIV
2. CNC Shield V3 Engraving Machine Expansion Board A4988 Driver Expansion Board for Arduino 3D Printer CNC A4988 - https://blog.protoneer.co.nz/arduino-cnc-shield/
3. Stepper Motor Drive with Heat Sink for Arduino, 3D Printer, CNC Machine or Robotics - https://reprap.org/wiki/StepStick

**1. Assembly guide:**

   Below is a step-by-step guide to connecting the CNC Shield V3 with an Arduino Uno R3 and interfacing it with A4988 stepper drivers (with heat sinks) and stepper motors. This setup is common for DIY CNC machines, 3D printers, and robotics projects.
   
  1.1. Mounting the CNC Shield on the Arduino Uno R3
Power Off: Always disconnect power from the Arduino before connecting or disconnecting shields.
Align and Plug In: The CNC Shield V3 is designed to fit directly onto an Arduino Uno R3. Line up the shield’s female headers with the Arduino’s male pins and press firmly so that the shield is fully seated.
Ensure Firm Connection: Check that all header pins are securely connected, as a loose connection may lead to erratic behavior.
   
  1.2. Inserting the A4988 Stepper Driver Modules
Orientation:
Critical: The A4988 driver module must be inserted in the correct orientation. Usually, the stepper driver board will have a small “+” or a label on one side—make sure that this orientation matches the layout indicated on the CNC shield.
Driver Alignment: On most CNC Shields, the driver sockets are arranged so that the microstepping adjustments (potentiometer) face outward or in a specified direction. Double-check the documentation for your shield.
Installation:
Slide each A4988 module into its designated slot on the shield.
If your modules come with heat sinks already attached, ensure they don’t interfere with the shield’s other components.

  1.3. Power Supply Considerations
Logic vs. Motor Supply:
The Arduino and shield logic typically run at 5V.
Stepper motors, however, require a separate motor power supply (commonly in the range of 12V–24V, depending on your motor specifications).
Connections:
Connect the motor power supply to the dedicated terminal block on the CNC Shield.
Verify that the power supply’s voltage and current ratings match the requirements of your stepper motors and A4988 modules.
Safety Note:
Double-check all polarity markings on the CNC shield before applying power.

  1.4. Wiring the Stepper Motors
Identify Motor Wires:
Use the datasheet or wiring diagram for your stepper motor to identify the coil pairs. Often, stepper motors have four wires corresponding to two coils.
Connect to Shield:
The CNC shield typically has clearly labeled output terminals (often labeled X, Y, Z, and sometimes A) for connecting stepper motor wires.
Connect each pair of wires to the corresponding terminals. If you experience issues with movement (e.g., motors not turning or turning in the wrong direction), try swapping one pair of wires on the affected motor.
Secure Connections:
Use the screw terminals to secure the wires. Make sure the connections are tight to avoid intermittent contact.

  1.5. Adjusting the A4988 Driver Modules
Set Current Limits:
Each A4988 module has a potentiometer that lets you adjust the current limit.
Before powering your motors, consult the A4988 datasheet and use a multimeter to set the current limit appropriate for your motor’s specifications.
Heat Sink Consideration:
The A4988 modules usually come with heat sinks. Ensure that they have proper airflow to prevent overheating, especially under continuous use.
Testing:
With power applied (initially at low speeds or using a simple test sketch), verify that the motors operate as expected without excessive heat buildup on the drivers.

  1.6. Programming and Firmware
Upload a Test Sketch:
Use the Arduino IDE to upload a simple stepper motor test program to the Arduino Uno.
Alternatively, if you’re building a CNC machine or 3D printer, you might load firmware like GRBL which is designed to interpret G-code commands.
Verify Pin Assignments:
The CNC Shield is designed with specific pins routed from the Arduino. Verify that your code uses the correct pins for step, direction, and enable signals for each axis.
Final Tips
Documentation:
Always refer to the datasheets for your A4988 drivers and stepper motors as well as the CNC shield’s user manual for any specific wiring diagrams or configuration details.
Double-Check Connections:
Before powering up, review all connections for proper orientation and secure seating. Incorrect wiring can damage your Arduino, drivers, or motors.
Incremental Testing:
Power up the system gradually and test one motor or axis at a time to troubleshoot any issues.
Following these steps should help you successfully connect your CNC Shield V3 with an Arduino Uno R3, install the A4988 stepper drivers, and wire your stepper motors for a CNC machine, 3D printer, or robotics project. If you need further details, many community tutorials and manufacturer datasheets provide additional diagrams and troubleshooting tips.
