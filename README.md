# openstack-volume-snapshot-json
This repository contains automation scripts to generate detailed reports of **available OpenStack volumes** and their associated **snapshots**.   It helps OpenStack administrators track available Cinder volumes, their creation times, snapshot relationships, and other key metadata.

---

## 📁 Files Overview

| File Name | Description |
|------------|--------------|
| `2_generate_volumes_json.py` | Collects details of all **available volumes** from OpenStack and saves them to `volumes.json`. |
| `3_volume_snapshot_report_25.py` | Reads `volumes.json` and `snapshots.json`, then generates a CSV report mapping volumes to snapshots. |
| `available_volume_snapshot_report_05Aug.csv` | Example output showing final report format. |

---

## ⚙️ Prerequisites

Before running the scripts, ensure the following are set up:

1. **OpenStack CLI** is installed and configured:
   ```bash
   source ~/openrc.sh


