"""
Script: my_forloop.py
By: L00171202
Purpose: Working on For loops
"""
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
print(scan.items())
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")

#if we directly iterate over dictionary we only get keys in return
for item in scan:
    print(item)

		 
