
#Author: Arun Kumar
#Date: 2024-01-25
# Description: This script generates a CSV report of available volumes, their snapshots with created dates and source volumes.

import json
import pandas as pd

# Step 1: Load JSON data
with open("volumes.json") as f:
    volumes = json.load(f)

with open("snapshots.json") as f:
    snapshots = json.load(f)

# Step 2: Build snapshot ID maps
snapshot_id_to_volume = {snap["ID"]: snap["Volume"] for snap in snapshots}
snapshot_id_to_created = {snap["ID"]: snap["Created At"] for snap in snapshots}

# Step 3: Prepare the report
report_data = []
for vol in volumes:
    if vol.get("Status") != "available":
        continue

    snapshot_id = vol.get("Snapshot ID") or None
    source_volume = snapshot_id_to_volume.get(snapshot_id, None) if snapshot_id else None
    snapshot_created_at = snapshot_id_to_created.get(snapshot_id, None) if snapshot_id else None

    report_data.append({
        "Volume ID": vol["ID"],
        "Volume Name": vol["Name"],
        "Volume Created At": vol.get("Created At", "None"),
        "Snapshot ID": snapshot_id or "None",
        "Snapshot Created At": snapshot_created_at or "None",
        "Snapshot Source Volume": source_volume or "None",
        "Size (GB)": vol["Size"],
        "Status": vol["Status"]
    })

# Step 4: Export to CSV
df = pd.DataFrame(report_data)

# Reorder columns exactly as required
ordered_columns = [
    "Volume ID", "Volume Name", "Volume Created At",
    "Snapshot ID", "Snapshot Created At", "Snapshot Source Volume",
    "Size (GB)", "Status"
]

df = df[ordered_columns]
df.to_csv("available_volume_snapshot_report24.csv", index=False)

print("✅ CSV report saved as: available_volume_snapshot_report24.csv")
