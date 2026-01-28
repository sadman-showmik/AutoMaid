# AutoMaid
AutoMaid – Effortless and Self-Learning Cleaning Management System

## AutoMaid Project

Visit our website: [https://dazzled-value-099342.framer.app/](https://dazzled-value-099342.framer.app/)

User Interface Demo: [https://dazzled-value-099342.framer.app/](https://dazzled-value-099342.framer.app/)

Demo Pitch Video: [Automaid: Open_Video](https://youtu.be/hOYoYzM-Z0E)

## Overview
AutoMaid is an autonomous home cleaning management system that keeps your space clean without direct effort from the user. It learns household habits, predicts cleaning needs, and cleans floors, surfaces, and air when necessary. The system optimizes cleaning schedules based on residents’ routines, providing a hygienic and comfortable environment while saving natural resources.

AutoMaid can integrate with smart home systems for lighting, heating, and notifications, depending on subscription packages.

---

## Key Features
- **Autonomous Cleaning Management:** Floors, surfaces, and air are cleaned automatically.  
- **Predictive Habit Learning:** Learns daily, weekly, and special-day routines to schedule cleaning efficiently.  
- **Environment-Friendly:** Optimizes natural resource usage; non-toxic cleaning methods.  
- **Safety & Health Alerts:** Sends notifications for unusual events or emergencies.  

---

## How It Works
1. **Sensors** detect physical, chemical, or biological parameters of the room.  
2. **Machine Learning** analyzes habits and patterns to predict cleaning needs.  
3. **Cleaning Execution:** System selects the best time, method, and location for cleaning.  
4. **Self-Learning:** AutoMaid improves its predictions based on past cleaning efficiency and habits.  
5. **Dashboard:** Displays cleaning history, upcoming schedules, and environmental data.  

---

## Team Roles
- **Regina Shakirova – Project Coordination & Innovation Lead**  
  Oversees sustainability, innovation, and marketing; coordinates meetings.  
- **Sagar Parajuli – User, Market & Validation Lead**  
  Conducts user research, surveys, and project validation.  
- **B M Sadman Showmik – Hardware & Systems Lead**  
  Designs and integrates hardware, develops sensor networks, assembles prototypes, and manages system dashboards.  
- **Ashraf Hossain Khan – AI Developer**  
  Develops machine learning and AI models; implements predictive algorithms.  

---

## User Benefits
- Enjoy a consistently clean home.  
- Save time from manual cleaning routines.  
- Optimize energy, water, and material usage.  
- Enhance health and well-being.  
- Customizable automation to fit your lifestyle.  

---

## Visuals & Demonstrations (Placeholders)
- Behaviour heatmap & predictive floor plan  
- AI/ML learning storyboard  
- Digital twin cleaning simulation  
- X-ray view of underfloor cleaning mechanisms and air purification  

---

## Note
This public repository is for demonstration purposes only. Proprietary code, ML models, hardware schematics, and business plans are stored in private submodules and are **not included** in this repo.

---

## Repository Structure

AutoMaid/
├── AutoMaid_UI/                    # Frontend for monitoring & control
├── Hardware_Code/                  
│   └── pico_sensor_mqtt.py         # Pico W sensor data collection & MQTT publishing
├── Networking_Code/
│   ├── pico_mqtt_test.py           # Pico W Wi-Fi + MQTT connectivity test
│   └── MQTT_JSON_Upload/
│       ├── pico_init_sensors.py   # Pico W initialization & MQTT setup
│       └── mqtt_json_logger.py    # PC/RPi JSON logger subscribing to MQTT topic
├── demo/                            # Demo video & media via Git LFS
├── docs-public/                     # Public documentation & media folder
├── media/                           # Images & demo assets
├── LICENSE                          # Public repository license
├── README.md                         # This file
└── .gitmodules/.gitattributes       # Submodules & Git LFS settings

## Project Contact

For questions, support, or collaboration inquiries, contact us at:  
📧 automaid@europe.com


## License
Copyright (c) 2025 B M Sadman Showmik, Regina Shakirova, Sagar Parajuli, Ashraf Hossain Khan  

All rights reserved. This repository is publicly viewable for demonstration purposes only. No part of this project (including text, images, media, or documentation) may be copied, reproduced, distributed, or used for commercial purposes without explicit written permission from the AutoMaid team listed above.

Private submodules contain proprietary code, ML models, hardware schematics, and business materials, which are **not accessible** in this public repository.
