import network
import time
import secrets  # Import credentials from secrets.py
import urequests  # For sending HTTP requests
from machine import Pin, Timer


# Setup onboard LED (Pico W LED)
pico_led = Pin("LED", Pin.OUT)
pico_led.off()

# Setup external LED on GP1
external_led = Pin(1, Pin.OUT)
external_led.off()

# Setup switch on GP0 (pull-up enabled)
switch = Pin(0, Pin.IN, Pin.PULL_UP)

# Setup Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.SSID, secrets.PASSWORD)

# Variables
button_pressed = False
blink_timer = Timer()
blink_interval = 1.0  # Default blink interval (1 second)

def connect_wifi():
    """Connect to Wi-Fi and indicate success with onboard LED."""
    print("Connecting to Wi-Fi...", end="")
    for _ in range(20):
        if wlan.isconnected():
            break
        print(".", end="")
        time.sleep(1)
    
    if wlan.isconnected():
        print("\nConnected! IP Address:", wlan.ifconfig()[0])
        pico_led.on()
        time.sleep(5)
        pico_led.off()
    else:
        print("\nUnable to connect!")

def send_http_request():
    """Send a POST request with a 1-second timeout."""
    try:
        print("Sending request...")

        url = "http://example.com"
        data = {}
        headers = {"Content-Type": "application/json"}

        # Send POST request with a 1-second timeout
        response = urequests.post(url, json=data, headers=headers, timeout=1)

        # Print response details
        print("POST request sent, response code:", response.status_code)
        print("Response:", response.text)

        response.close()  # Close response to free resources

    except OSError as e:
        print("Request timed out or failed:", e)

    except Exception as e:
        print("Unexpected error sending request:", e)

def toggle_led(timer):
    """Toggle the external LED at the current blink interval."""
    external_led.toggle()

def set_blink_interval(interval):
    """Update the blink interval."""
    global blink_interval
    blink_interval = interval
    blink_timer.init(period=int(interval * 1000), mode=Timer.PERIODIC, callback=toggle_led)

def check_button():
    """Detect button press, blink LED faster, and send HTTP request."""
    global button_pressed

    if switch.value() == 0 and not button_pressed:  # Button pressed
        print("Switch pressed!")
        button_pressed = True

        # Increase blinking speed to 500ms
        set_blink_interval(0.2)

        # Send HTTP request
        send_http_request()

        # After 2.5 seconds, restore normal blinking
        time.sleep(2.5)
        set_blink_interval(1.0)

    elif switch.value() == 1:
        button_pressed = False  # Reset when button is released

# Connect to Wi-Fi
connect_wifi()

print("Waiting for switch press...")

# Start default 1-second blinking
set_blink_interval(1.0)

# Non-blocking main loop
while True:
    check_button()  
    time.sleep(0.01)  # Small delay to prevent high CPU usage

