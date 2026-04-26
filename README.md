# 🛡️ Design and Implementation of a Basic Intrusion Detection System Using Cisco ACL

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Dashboard-black?logo=flask)
![Cisco](https://img.shields.io/badge/Cisco-Packet%20Tracer-1BA0D7?logo=cisco)
![License](https://img.shields.io/badge/License-Academic-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> A rule-based Intrusion Detection System (IDS) implemented using Cisco Access Control Lists (ACL) in Cisco Packet Tracer, combined with a real-time Python Flask web dashboard for monitoring network traffic, alerts, and blocked attacks.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Network Topology](#network-topology)
- [ACL Configuration](#acl-configuration)
- [Flask IDS Dashboard](#flask-ids-dashboard)
- [Installation & Setup](#installation--setup)
- [How It Works](#how-it-works)
- [Test Results](#test-results)
- [Project Structure](#project-structure)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

---

## 📖 About the Project

This project presents the **design and implementation of a basic Intrusion Detection System (IDS)** using **Cisco Extended Access Control Lists (ACLs)** simulated in **Cisco Packet Tracer 8.x**. The system is complemented by a **Python Flask web dashboard** that displays real-time traffic statistics, security alerts, and blocked attack counts.

The IDS detects and blocks:
- **Telnet attacks** (TCP Port 23)
- **FTP attacks** (TCP Port 21)

While allowing legitimate traffic such as **HTTP (Port 80)** and **ICMP (Ping)**.

This project was submitted as part of the **Creative and Innovative Project (CIP)** — Batch 2023 (Semester VI), Department of Computer Science & Engineering, **SCSVMV University**.

---

## ✨ Features

- ✅ Extended ACL-based traffic filtering on Cisco Router (IOS)
- ✅ Real-time detection and blocking of Telnet & FTP attacks
- ✅ ACL hit counters via `show access-lists` command
- ✅ Syslog-style alert generation using the `log` keyword
- ✅ Python Flask web dashboard with live auto-refresh (every 3 seconds)
- ✅ Traffic classification: **TRAFFIC**, **ALERT**, **BLOCK**
- ✅ Visual status indicator: `✅ SAFE` / `⚠ ATTACK DETECTED`
- ✅ Simulated network using Cisco Packet Tracer (no real hardware needed)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  NETWORK TOPOLOGY                   │
│                                                     │
│  [Attacker PC]──────[Cisco Router / IDS Engine]     │
│   10.0.0.2          GE0/1 ◄── ACL 101 applied       │
│                     GE0/0                           │
│                       │                             │
│                  [Cisco Switch]                     │
│                       │                             │
│               [Internal Host PC]                    │
│                  192.168.1.2                        │
└─────────────────────────────────────────────────────┘

         ┌──────────────────────────┐
         │   Flask IDS Dashboard   │
         │   (Python Web App)      │
         │   localhost:5000        │
         │                         │
         │  [Traffic] [Alert] [Block]│
         │  Real-time event log    │
         └──────────────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Cisco Packet Tracer 8.x | Network simulation environment |
| Cisco IOS (C1900) | Router operating system for ACL configuration |
| Extended ACL (ACL 101) | Packet filtering / IDS/IPS engine |
| Python 3.x | Backend scripting |
| Flask | Web framework for IDS dashboard |
| HTML / CSS | Frontend dashboard UI |
| Jinja2 | Template rendering for Flask |

---

## 🌐 Network Topology

| Device | Model | IP Address | Role |
|---|---|---|---|
| Router | Cisco 1941 | GE0/0: 192.168.1.1 / GE0/1: 10.0.0.1 | IDS/IPS Engine |
| Switch | Cisco 2960-24TT | — | Layer-2 Switch |
| Attacker PC | Generic PC | 10.0.0.2 | Simulates attack traffic |
| Internal PC | Generic PC | 192.168.1.2 | Protected host |

---

## ⚙️ ACL Configuration

### Step 1 — Configure Router Interfaces
```bash
Router> enable
Router# configure terminal
Router(config)# interface GigabitEthernet 0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
Router(config)# interface GigabitEthernet 0/1
Router(config-if)# ip address 10.0.0.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

### Step 2 — Define ACL 101 Rules
```bash
Router(config)# access-list 101 deny tcp any any eq 23
Router(config)# access-list 101 deny tcp any any eq 21
Router(config)# access-list 101 permit ip any any
```

### Step 3 — Apply ACL to Interface
```bash
Router(config)# interface GigabitEthernet 0/1
Router(config-if)# ip access-group 101 in
Router(config-if)# exit
```

### Step 4 — Save Configuration
```bash
Router(config)# end
Router# write memory
```

### Step 5 — Verify ACL Hit Counters
```bash
Router# show access-list
```

---

## 🖥️ Flask IDS Dashboard

The dashboard (`app.py`) provides a real-time web interface for monitoring network events.

### Run the Dashboard

```bash
# Install dependencies
pip install flask

# Run the app
python app.py
```

Then open your browser and go to:
```
http://localhost:5000
```

### Dashboard Preview

| Counter | Description |
|---|---|
| Total Traffic | All packets monitored |
| Total Alerts | Suspicious activity detected |
| Total Blocks | Packets blocked by ACL |
| Status | `✅ SAFE` or `⚠ ATTACK DETECTED` |

Each event is color-coded in the live event table:
- 🟦 **Blue** — Normal traffic
- 🟧 **Orange** — Alert (suspicious)
- 🟥 **Red** — Blocked attack

---

## 🚀 Installation & Setup

### Prerequisites

- [Cisco Packet Tracer 8.x](https://www.netacad.com/courses/packet-tracer) (free with Cisco NetAcad account)
- Python 3.x
- pip

### Clone the Repository

```bash
git clone https://github.com/your-username/intrusion-detection-system-cisco-acl.git
cd intrusion-detection-system-cisco-acl
```

### Install Python Dependencies

```bash
pip install flask
```

### Run the Flask Dashboard

```bash
python app.py
```

### Open the Packet Tracer Simulation

1. Open `network_topology.pkt` in Cisco Packet Tracer
2. The ACL is pre-configured on Router0
3. Use the Simulation mode to observe packet flows

---

## 🔄 How It Works

1. A packet arrives on **GigabitEthernet 0/1** (external interface)
2. The router checks **ACL 101** rules sequentially (top-down)
3. If the packet matches **Rule 1** (TCP Port 23 — Telnet) → **Deny** + log alert
4. If the packet matches **Rule 2** (TCP Port 21 — FTP) → **Deny** + log alert
5. If neither rule matches → **Permit** (Rule 3: `permit ip any any`)
6. The `show access-lists` command shows cumulative hit counters for each ACL rule
7. The Flask dashboard logs and displays all events in real time

---

## 🧪 Test Results

| Test Case | Protocol | Port | Expected Result | Actual Result |
|---|---|---|---|---|
| Telnet attack from Attacker PC | TCP | 23 | Blocked | ✅ Blocked |
| FTP attack from Attacker PC | TCP | 21 | Blocked | ✅ Blocked |
| Ping (ICMP) from Attacker PC | ICMP | — | Allowed | ✅ Allowed |
| HTTP traffic | TCP | 80 | Allowed | ✅ Allowed |

---

## 📁 Project Structure

```
intrusion-detection-system-cisco-acl/
│
├── app.py                    # Flask IDS Dashboard (Python)
├── network_topology.pkt      # Cisco Packet Tracer simulation file
├── README.md                 # Project documentation
│
└── report/
    └── cip_report.pdf        # Full CIP project report
```

---

## 👨‍💻 Authors

| Name | Reg. No. |
|---|---|
| Rajshekar. B | 11239M008 |
| Jayvardhan. S | 11239A082 |

**Guided by:** Dr. N.C.A. Boovarahan, Assistant Professor
**Department:** Computer Science & Engineering
**Institution:** Sri Chandrasekharendra Saraswathi Viswa Mahavidyalaya (SCSVMV), Kanchipuram

---

## 🙏 Acknowledgements

- **Cisco Networking Academy** for Packet Tracer
- **Flask** open-source community
- Department of CSE, SCSVMV University

---

## 📄 License

This project is submitted for academic purposes under the **Creative and Innovative Project (CIP)** program, Batch 2023, Semester VI.

---

> *"Security is not a product, but a process."* — Bruce Schneier
