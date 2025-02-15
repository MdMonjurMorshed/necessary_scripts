from io import BytesIO

import clamd

# Replace 'your_clamd_host' and 'your_clamd_port' with your clamd host and port
clamd_host = 'dev-server.evidentbd.com'
clamd_port = 31463  # Replace with the port number as an integer

# Initialize the ClamdNetworkSocket with the specified host and port
cd = clamd.ClamdNetworkSocket(host=clamd_host, port=clamd_port)


print(cd)
# Check if the clamd server is reachable
try:
    if cd.ping() == 'PONG':
        print("Successfully connected to clamd.")
    else:
        print("Failed to connect to clamd.")
except clamd.ConnectionError as e:
    print(str(e))
    print("Connection to clamd failed. Please check the host and port.")
    
    exit()

image_path = '/home/brinto/Downloads/1732901085788.jpeg'

# Open the image file in binary read mode
with open(image_path, 'rb') as image_file:
    # Read the content of the file
    file_content = image_file.read()

    # Scan the file content
    result = cd.instream(BytesIO(file_content))

# Check the scan result
print(result.get('stream')[0])
if result.get('stream', [None, None])[0] == 'FOUND':
    print(f"Malware detected: {result['stream'][1]}")
else:
    print("No malware detected.")