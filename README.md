# E-Waste Monitoring System

## Overview

This project is a simple Python-based E-Waste Monitoring System. The goal is to track electronic items, calculate their replacement periods, and suggest nearby e-waste collection points. It also provides an analysis of how many items need to be replaced, helping users manage their electronic devices more sustainably.

## Features

- **Inventory Tracking**: Records electronic items with their purchase dates and expected replacement periods.
- **Replacement Notification**: Checks which items are due for replacement and alerts the user.
- **E-Waste Collection Points**: Suggests the nearest e-waste collection point based on the user's location.
- **E-Waste Impact Analysis**: Provides an analysis of the total number of items and how many are due for replacement.

## Prerequisites

- Python 3.x
- pandas library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/e-waste-monitoring-system.git
   cd e-waste-monitoring-system

Install the required Python libraries:

pip install pandas

The script will:

Display items that need replacement.
Suggest the nearest e-waste collection point based on your location.
Provide an e-waste impact analysis, showing the total items and those that need to be replaced.

Enter your location (e.g., 'New York'): New York

Example Output

Checking for items that need replacement...
Items that need replacement:
        Item  Purchase Date Replacement Date
0     Laptop     2021-08-17       2024-08-16

Suggesting e-waste collection point...
Nearest collection point in New York: 123 Recycle St, NY

E-Waste Impact Analysis:
Total items: 6, Items to replace: 1


Customization
Inventory Data: Modify the data dictionary in the script to add or remove electronic items.
Collection Points: Update the collection_points dictionary with the e-waste collection points relevant to your location.


![image](https://github.com/user-attachments/assets/47f513d1-9f55-4aa0-b0c1-084993e61bb1)

