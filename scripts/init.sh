#!/bin/bash
set -e # if any of below commands is failed then the script will be terminate, if i didnt use this command then if any command is failed then the script will continue

# Print Databricks CLI version
databricks -v

# Configure Databricks CLI Authentication
cat <<EOF > ~/.databrickscfg
[DEFAULT]
host = $DATABRICKS_HOST
client_id = $DATABRICKS_CLIENT_ID
client_secret = $DATABRICKS_CLIENT_SECRET
cluster_id = $DATABRICKS_CLUSTER_ID
EOF

# Print config file
cat ~/.databrickscfg

# Verify auth profiles
databricks auth profiles
