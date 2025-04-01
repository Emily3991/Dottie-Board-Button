Raspberry Pi Pico 2 W Wi-Fi Button with LED and HTTP Requests
=============================================================

Overview
--------

This project runs on a **Raspberry Pi Pico 2 W** and connects to Wi-Fi to send an HTTP POST request when a button is pressed. The onboard LED and an external LED provide visual feedback for Wi-Fi connectivity and button presses. The external LED blinks continuously and changes blinking patterns when the button is pressed.

Features
--------

*   Connects to Wi-Fi using credentials stored in a separate secrets.py file.
    
*   Continuously blinks an external LED every second when idle.
    
*   When the button is pressed:
    
    *   The external LED blinks rapidly (every 500ms) for 2.5 seconds.
        
    *   An HTTP POST request is sent to a predefined endpoint.
        
*   The HTTP request has a **1-second timeout** to avoid blocking execution.
    
*   Uses **non-blocking code** to allow all functionalities to run smoothly.
    

Hardware Requirements
---------------------

*   **Raspberry Pi Pico 2 W**
    
*   **External LED** connected to **GP1** and ground
    
*   **Push button switch** connected to **GP0** and ground
    
*   **Mac, Windows, or Linux PC** for programming the Pico 2 W
    

Software Requirements
---------------------

*   **Thonny IDE** (recommended for MicroPython development)
    
*   **MicroPython firmware** installed on the Pico 2 W
    
*   Python 3 installed on your PC (if using Windows or Linux)
    

Setup Instructions
------------------

### 1\. Install MicroPython on the Pico 2 W

If MicroPython is not installed on your Pico 2 W, follow these steps:

*   Download the latest **MicroPython UF2** file for the Pico 2 W from the official Raspberry Pi website.
    
*   Connect the Pico 2 W to your computer while holding the **BOOTSEL** button.
    
*   Copy the UF2 file to the mounted drive named **RPI-RP2**.
    

### 2\. Install and Configure Thonny

#### macOS

1.  Install **Thonny** from [thonny.org](https://thonny.org/).
    
2.  Open Thonny and select **Run → Select Interpreter**.
    
3.  Choose **MicroPython (Raspberry Pi Pico)**.
    
4.  Click **OK**.
    

#### Windows

1.  Download and install Thonny from [thonny.org](https://thonny.org/).
    
2.  Plug in the Pico 2 W and open Thonny.
    
3.  Select **Run → Select Interpreter**.
    
4.  Choose **MicroPython (Raspberry Pi Pico)** and click **OK**.
    

#### Linux

1.  bashCopyEditsudo apt install thonny
    
2.  Open Thonny and configure the **MicroPython (Raspberry Pi Pico)** interpreter.
    

### 3\. Create the secrets.py File

Your Wi-Fi credentials should be stored in a **separate file** named secrets.py to keep them private. Create this file inside Thonny and add:

`SSID = "your_wifi_ssid"  PASSWORD = "your_wifi_password"   `

Replace your\_wifi\_ssid and your\_wifi\_password with your actual Wi-Fi details.

### 4\. Upload the Project Code

1.  Open **Thonny**.
    
2.  Copy the main project script to Thonny.
    
3.  Save it as main.py on the Pico 2 W.
    
4.  Run the script and observe the LED behavior.
    

Running the Project
-------------------

1.  Connect the **Pico 2 W** to a power source (USB cable or external power supply).
    
2.  The **onboard LED** will light up for 5 seconds once Wi-Fi is connected.
    
3.  The **external LED** will blink every second when idle.
    
4.  When you **press the button**:
    
    *   The LED blinks every 500ms for 2.5 seconds.
        
    *   A **POST request** is sent to the server.
        
5.  If the request does not receive a response within **1 second**, it is canceled.
    
6.  The LED resumes its normal blinking pattern.
    
3D Box
------

Contains a .stl file for a 3D box to hold the button.

Troubleshooting
---------------

### Wi-Fi Issues

*   Double-check that secrets.py contains the correct **SSID** and **password**.
    
*   Ensure the Wi-Fi network is **2.4 GHz** (Pico 2 W does not support 5 GHz).
    
*   Try restarting the Pico 2 W.
    

### Button Not Responding

*   Make sure the button is properly connected between **GP0** and **ground**.
    
*   Check if switch.value() correctly detects presses in Thonny’s **Shell**.
    

### HTTP Request Failures

*   Ensure the **API endpoint URL** is correct.
    
*   Check the **server status**.
    
*   Make sure the **Pico 2 W has an internet connection**.
    

Possible Future Improvements
-------------------

*   Add support for **MQTT** to send button press events to a message broker.
    
*   Store **server endpoint** in secrets.py for easy configuration.
    
*   Implement **debouncing** to improve button press accuracy.
    

License
-------

This project is MIT LICENSED.