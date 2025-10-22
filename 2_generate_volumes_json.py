import subprocess
import json
import time

# Step 1: Get all volumes
print("📦 Getting all volumes...")
volumes_raw = subprocess.check_output([
    "openstack", "volume", "list", "--long", "-f", "json"
])
volumes_list = json.loads(volumes_raw)

# Step 2: Filter only "available" volumes
available_volumes = [v for v in volumes_list if v["Status"] == "available"]
print(f"✅ Found {len(available_volumes)} available volumes")

# Step 3: Loop through each and get full details (with snapshot_id)
enriched_volumes = []

for idx, vol in enumerate(available_volumes, 1):
    vol_id = vol["ID"]
    print(f"[{idx}/{len(available_volumes)}] Inspecting volume {vol_id}...")

    try:
        vol_details_raw = subprocess.check_output([
            "openstack", "volume", "show", vol_id, "-f", "json"
        ])
        vol_details = json.loads(vol_details_raw)

        enriched_volumes.append({
            "ID": vol_details.get("id"),
            "Name": vol_details.get("name"),
            "Size": vol_details.get("size"),
            "Status": vol_details.get("status"),
            "Snapshot ID": vol_details.get("snapshot_id") or "None",
            "Created At": vol_details.get("created_at"),
            "Tenant ID": vol_details.get("os-vol-tenant-attr:tenant_id")
        })

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Failed to get details for volume {vol_id}")

    # Optional: pause to avoid API rate limits (can adjust)
    time.sleep(0.1)

# Step 4: Save to volumes.json
with open("volumes.json", "w") as f:
    json.dump(enriched_volumes, f, indent=2)

print("📁 Done. Saved to volumes.json")

