# Packet Tracer IoT Network Debugging

## 1. Project Overview

This project contains a small IoT network simulated using **Cisco Packet Tracer**.

The network uses a **DLC100 Home Gateway** as the central device in a star topology. It connects the laptop and IoT devices through Ethernet connections.

### Network Devices

* **DLC100 Home Gateway0** — Central gateway
* **Laptop0** — Client laptop
* **Motion** — Motion detector
* **Parking** — Garage door actuator
* **RFID Reader** — RFID sensor
* **IoT2 / RFID Card** — Physical RFID token

---

## 2. Initial Problem

The main issue observed in the topology was that the connections between the Home Gateway and the connected devices initially showed **orange indicators** on the gateway side.

The end-device indicators were green, while the gateway-side indicators were orange.

This suggested that the network ports had not yet become fully operational.

---

## 3. Debugging Process

### Step 1 — Initialize the Network

The first step was to allow Packet Tracer enough time to initialize the network.

The **Fast Forward Time** button was used to advance the simulation.

After waiting for the network to initialize:

* Gateway-side links changed from **orange to green**.
* The physical connections were confirmed to be operational.

### Result

**Status: Fixed**

The orange indicators were caused by the initial network initialization delay.

---

## 4. Step 2 — Check Laptop IP Configuration

The IP configuration of `Laptop0` was checked using:

```text
ipconfig
```

The following configuration was obtained:

| Setting         | Value            |
| --------------- | ---------------- |
| IPv4 Address    | `192.168.25.101` |
| Subnet Mask     | `255.255.255.0`  |
| Default Gateway | `192.168.25.1`   |

### Result

The laptop was correctly configured and belonged to the same network as the Home Gateway.

**Status: Correct**

---

## 5. Step 3 — Test Gateway Connectivity

The Home Gateway was accessed from `Laptop0` using a web browser.

The gateway address was:

```text
http://192.168.25.1
```

The Home Gateway login page successfully appeared.

### Result

This confirmed that:

* Laptop0 had network connectivity.
* The Home Gateway was reachable.
* The gateway IP address was correct.

**Status: Working**

---

## 6. Step 4 — Check Home Gateway

The Home Gateway GUI was inspected.

The HTTP service was found to be enabled.

The gateway was accessible through:

```text
192.168.25.1
```

The web interface did not provide a directly visible IoT device list from the section initially inspected, so the IoT devices were checked individually.

---

## 7. Step 5 — Check IoT Devices

The IoT configuration of the devices was inspected.

### Motion Detector

The `Motion` device showed:

```text
Default Gateway: 192.168.25.1
IoT Server: Home Gateway
```

The device was configured to use the Home Gateway as its IoT server.

### Garage Door

The `Parking` device was also configured to use:

```text
IoT Server: Home Gateway
```

### RFID Reader

The `RFID Reader` configuration showed:

```text
Default Gateway: 192.168.25.1
IoT Server: Home Gateway
```

The RFID Reader was therefore correctly configured to communicate through the Home Gateway.

---

## 8. RFID Card

The `RFID Card IoT2` does not require an Ethernet connection.

It is a physical RFID token used with the RFID Reader.

Therefore, its lack of a network cable is **normal behavior** and is not a network fault.

To test the RFID system:

1. Select the RFID Card.
2. Hold the `Alt` key.
3. Drag the card over the RFID Reader.
4. Observe the RFID Reader response.
5. If automation rules are configured, verify that the Garage Door responds.

---

## 9. Final Network Status

After debugging, the following conditions were confirmed:

| Component               | Status                        |
| ----------------------- | ----------------------------- |
| Home Gateway            | 🟢 Working                    |
| Laptop0 Ethernet        | 🟢 Working                    |
| Laptop IP Configuration | 🟢 Correct                    |
| Gateway IP              | 🟢 `192.168.25.1`             |
| Laptop IP               | 🟢 `192.168.25.101`           |
| Physical Links          | 🟢 Green                      |
| Motion IoT Server       | 🟢 Home Gateway               |
| Garage Door IoT Server  | 🟢 Home Gateway               |
| RFID Reader IoT Server  | 🟢 Home Gateway               |
| RFID Card               | 🟢 Normal / No cable required |

---

## 10. Conclusion

The primary network problem was caused by the **initial orange gateway-side link indicators**.

After advancing Packet Tracer time, the links became green and the network connections became operational.

The laptop was confirmed to have a valid IP configuration and successfully accessed the Home Gateway at `192.168.25.1`.

The IoT devices were also checked and configured to use the **Home Gateway** as their IoT server.

The RFID Card does not require a network connection because it functions as a physical RFID token.

### Final Status

**Network connectivity: Working**

**IoT Gateway configuration: Correct**

**Physical network links: Working**

**RFID Card connection: Normal**

---

## 11. Useful Troubleshooting Checklist

If the problem occurs again:

* [ ] Wait for Packet Tracer network initialization.
* [ ] Use Fast Forward Time.
* [ ] Check that gateway-side links become green.
* [ ] Check Ethernet/LAN cable connections.
* [ ] Verify the laptop IP address.
* [ ] Verify the subnet mask.
* [ ] Verify the default gateway.
* [ ] Open the Home Gateway using its IP address.
* [ ] Check each IoT device's IoT Server setting.
* [ ] Ensure IoT devices use **Home Gateway**.
* [ ] Test the RFID Card by moving it over the RFID Reader.
* [ ] Verify the Garage Door response if automation is configured.

## 12. Network Address Summary

```text
Network:          192.168.25.0/24
Subnet Mask:      255.255.255.0
Home Gateway:     192.168.25.1
Laptop0:          192.168.25.101
```

**Debugging completed successfully.**
