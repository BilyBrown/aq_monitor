#!/bin/bash
# Step 0.8: get the ip address of the raspberry pi
get_raspberry_pi_ip() {
	raspberry_pi_ip=$(sudo nmap -sn 192.168.0.1/24 | awk '/Raspberry Pi/{print prev2} {prev2=prev; prev=$0}' | awk '{print $5}')
}

attempts=0
max_attempts=3

# look to check length of raspberry_pi_ip
while [ ${#raspberry_pi_ip} -lt 9 ] && [ $attempts -lt $max_attempts ]; do
    echo "Attempting to get Raspberry Pi IP address (Attempt $((attempts + 1)))..."
    get_raspberry_pi_ip
    attempts=$((attempts + 1))
done

# Check if the IP address was retreived
if [ ${#raspberry_pi_ip} -ge 9 ]; then
    echo "Raspberry Pi IP address is: $raspberry_pi_ip"
else
    echo "Failed to retrieve a valid Raspberry Pi IP address after $max_attempts attempts."
    exit 1
fi

# Step1: copy csv from raspberry pi
scp pi@$raspberry_pi_ip:./Desktop/datalogs/datalog_trial_0.csv . &&

# Step2: move the file to the aq_explore folder - can probably skip this step but it is fun
mv datalog_trial_0.csv ./python/aq_explore

# Step3: open up code. to run the jupyter notebook to analyze - later make a script that runs and produces an output
cd python/aq_explore &&

# Step4 initiate venv environment and run python code to see averages
conda run -n aq_data python aq_explore.py
