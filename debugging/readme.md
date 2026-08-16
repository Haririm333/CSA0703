# Cisco Packet Tracer – Debugging Activities

## Overview

This document records the debugging work performed for four Cisco Packet Tracer activities:

1. **Control Devices with Home Gateway**
2. **Smart House with Switch, AP, Server**
3. **Fire Extinguisher**
4. **Smart Parking**

The debugging was performed by opening the Packet Tracer topology, identifying abnormal behavior, checking device configurations, correcting the relevant settings, and testing the network again.

---

# Scenario 1 – Control Devices with Home Gateway

## Objective

The purpose of this activity was to control IoT devices through a **Home Gateway** using a smartphone.

### Devices

* Home Gateway
* Smartphone0
* Door
* Garage Door
* Lawn Sprinkler
* Light

## Initial Problem

The IoT devices were present in the topology, but the main task was to verify that they could communicate with and be controlled through the Home Gateway.

## Debugging Process

### Step 1 – Check the Home Gateway

The Home Gateway was opened and its configuration was inspected.

The wireless settings were checked.

Important values included:

```text
SSID: HomeGateway
Channel: 6
Coverage Range: 250 m
```

The wireless configuration was found to be appropriate.

### Step 2 – Check the IoT Devices

Each IoT device was inspected individually:

* Door
* Garage Door
* Lawn Sprinkler
* Light

The devices were checked for their wireless connection and IoT Server configuration.

The devices needed to use the Home Gateway for communication.

### Step 3 – Check Smartphone0

The smartphone was checked to make sure it was connected to the Home Gateway wireless network.

The smartphone was then used as the control device.

### Step 4 – Test Device Control

The devices were tested individually from the smartphone:

* Light → ON/OFF
* Door → OPEN/CLOSE
* Garage Door → OPEN/CLOSE
* Lawn Sprinkler → ON/OFF

### Final Result

The Home Gateway provided the central connection between the smartphone and IoT devices.

```text
Smartphone
     ↓
Home Gateway
     ↓
IoT Devices
```

**Scenario 1: Debugging completed.**

---

# Scenario 2 – Smart House with Switch, AP, and Server

## Objective

The objective was to debug a smart-house network containing a **switch, wireless access point, server, and end devices**.

## Initial Problem

The network contained both wired and wireless devices, so the debugging focused on ensuring that all devices could communicate through the switch, Access Point, and server.

## Debugging Process

### Step 1 – Check Physical Connections

The connections between the devices were checked first.

The main network path was:

```text
End Devices
     ↓
Switch
     ↓
Access Point / Server
```

The link indicators were observed to verify that the interfaces were active.

### Step 2 – Check Switch

The switch ports were checked to ensure that the connected devices were attached to the correct interfaces.

The network was allowed to initialize before testing connectivity.

### Step 3 – Check Access Point

The Access Point was inspected.

The wireless configuration was checked to make sure that the wireless clients were using the correct wireless network.

The SSID and wireless settings were compared between the AP and wireless clients.

### Step 4 – Check Server

The server's network configuration was checked.

The following were verified:

```text
IP Address
Subnet Mask
Default Gateway
```

### Step 5 – Test Connectivity

The client network configuration was checked using:

```text
ipconfig
```

Connectivity was then tested using:

```text
ping <gateway-ip>
```

and:

```text
ping <server-ip>
```

### Final Result

The switch, Access Point, server, and connected devices were checked as one complete network.

```text
Wired Devices
      ↓
    Switch
      ↓
 Access Point
      ↓
Wireless Devices

Server
  ↓
Switch
```

**Scenario 2: Debugging completed.**

---

# Scenario 3 – Fire Extinguisher

## Objective

The Fire Extinguisher activity involved an IoT-based fire detection and response system.

The system included IoT sensors and devices controlled through a Home Gateway.

## Initial Problem

The fire-related IoT devices needed to be checked to determine whether the problem was caused by:

* Network configuration
* Home Gateway configuration
* IoT registration
* Device communication
* Automation/control settings

## Debugging Process

### Step 1 – Check Home Gateway Wireless Configuration

The **DLC100 Home Gateway** was opened.

The wireless settings were inspected.

The following configuration was observed:

```text
SSID: HomeGateway
2.4 GHz Channel: 6
Coverage Range: 250 m
```

The wireless configuration was found to be valid.

### Step 2 – Check Home Gateway LAN Configuration

The LAN settings were checked.

The Home Gateway had:

```text
IPv4 Address: 192.168.25.1
Subnet Mask: 255.255.255.0
```

This was confirmed to be a valid network configuration.

### Step 3 – Compare IoT Device Network

The Smoke Detector was checked.

Its network configuration showed an address in the same network, including:

```text
Smoke Detector IP: 192.168.25.103
Home Gateway: 192.168.25.1
```

Therefore, the Smoke Detector and Home Gateway were on the same subnet.

### Step 4 – Check IoT Server

The Smoke Detector's IoT Server configuration was inspected.

The device was checked for its Home Gateway registration.

The same process was used to inspect the other fire-related IoT devices.

### Step 5 – Check the IoT Device List

The Home Gateway GUI was then inspected to determine whether the IoT devices were registered.

The device list was used to identify whether devices such as:

```text
smoke
siren
parking
window
fan
sprinkler / fire extinguisher
```

were available through the Home Gateway.

### Step 6 – Test the Fire System

After checking the network and IoT registration, the fire-related sensor and actuator behavior were tested.

The expected sequence was:

```text
Fire/Smoke Detection
        ↓
IoT Network
        ↓
Home Gateway
        ↓
Automation
        ↓
Fire Extinguisher / Siren
```

### Final Result

The Home Gateway LAN and wireless configurations were confirmed to be correct.

The remaining debugging focus was the IoT registration/control configuration rather than the basic IP network.

**Scenario 3: Network configuration verified and IoT configuration checked.**

---

# Scenario 4 – Smart Parking

## Objective

The Smart Parking activity was designed to use IoT devices to detect and control parking-related events.

## Initial Problem

The parking system needed to be checked for communication between its IoT devices, gateway, and control components.

## Debugging Process

### Step 1 – Check Physical Connections

The physical links between the parking devices and the network were checked.

The link indicators were allowed to initialize.

### Step 2 – Check Gateway Configuration

The Home Gateway was inspected to verify its network configuration.

The gateway IP and subnet were checked.

### Step 3 – Check Parking IoT Devices

The parking-related IoT devices were opened individually.

Their:

```text
IPv4 Configuration
Default Gateway
IoT Server
```

were checked.

The devices were configured to communicate through the appropriate Home Gateway.

### Step 4 – Check RFID Reader

The RFID Reader was checked.

The important configuration was:

```text
Default Gateway: 192.168.25.1
IoT Server: Home Gateway
```

The Home Gateway option was selected.

### Step 5 – Check RFID Card

The RFID Card was checked.

It was confirmed that the RFID Card does not require an Ethernet cable.

It functions as a physical RFID token.

### Step 6 – Test RFID

The RFID Card was selected and moved over the RFID Reader using the Packet Tracer interaction.

The RFID Reader response was observed.

### Step 7 – Test Parking Response

The parking actuator/system was checked after the RFID event.

The expected sequence was:

```text
RFID Card
    ↓
RFID Reader
    ↓
Home Gateway
    ↓
IoT Control
    ↓
Parking Action
```

### Final Result

The Smart Parking system was checked from physical connectivity through IoT communication and RFID interaction.

**Scenario 4: Debugging completed.**

---

# Common Debugging Method Used

The same basic debugging approach was followed throughout the activities.

## 1. Physical Layer

First, check:

* Cables
* Ports
* Link indicators
* Device power/status

If a link is initially orange, allow Packet Tracer to initialize using **Fast Forward Time**.

---

## 2. IP Configuration

Check the IP configuration using:

```text
ipconfig
```

Verify:

```text
IPv4 Address
Subnet Mask
Default Gateway
```

Example from the debugging:

```text
IPv4 Address:    192.168.25.101
Subnet Mask:     255.255.255.0
Default Gateway: 192.168.25.1
```

---

## 3. Gateway Connectivity

Test communication with the Home Gateway:

```text
ping 192.168.25.1
```

The Home Gateway can also be accessed from the browser:

```text
http://192.168.25.1
```

---

## 4. Wireless Configuration

Check:

```text
SSID
Channel
Authentication
Password/Security
Coverage
```

Example:

```text
SSID: HomeGateway
Channel: 6
Coverage: 250 m
```

---

## 5. IoT Server

For IoT devices, check:

```text
IoT Server
```

and ensure the correct gateway is selected.

For Home Gateway-based systems:

```text
IoT Server: Home Gateway
```

---

## 6. Device Testing

Finally, test the actual functionality.

Examples:

```text
Smartphone → Light
Smartphone → Door
RFID Card → RFID Reader
Fire Sensor → Fire Extinguisher
Parking Sensor → Parking System
```

---

# Important Findings

During debugging, several important points were confirmed.

### Orange Links

Orange gateway-side links do not necessarily mean a permanent fault. Packet Tracer may still be initializing the network.

**Action:** Fast Forward Time and check again.

### Home Gateway IP

The Home Gateway used:

```text
192.168.25.1
```

with:

```text
255.255.255.0
```

### Laptop

The laptop successfully received:

```text
192.168.25.101
```

with the Home Gateway as its default gateway.

### RFID Card

The RFID Card does not require a network cable.

It is a physical interaction device used with the RFID Reader.

### IoT Devices

IoT devices must be configured to use the correct IoT server/gateway.

---

# Final Debugging Flow

```text
             START
               │
               ↓
       Check Physical Links
               │
               ↓
     Wait / Fast Forward Time
               │
               ↓
       Check IP Configuration
               │
               ↓
       Check Default Gateway
               │
               ↓
        Test Connectivity
               │
               ↓
      Check Wireless Settings
               │
               ↓
       Check IoT Server
               │
               ↓
       Check Device List
               │
               ↓
       Test IoT Function
               │
               ↓
       Verify Final Response
               │
               ↓
             DONE
```

# Conclusion

The four Packet Tracer activities were debugged by systematically checking the network instead of immediately changing configurations.

The debugging process followed:

**Physical connection → IP configuration → Gateway → Wireless → IoT registration → Device control → Final testing**

This approach helped distinguish between actual configuration problems and normal Packet Tracer behavior such as temporary orange link indicators or RFID cards appearing without network cables.
