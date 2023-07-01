from pywizlight import wizlight

# Define the IP range of your local network
ip_range = "192.168.0."

# Iterate over possible IP addresses and attempt to connect to each one
for i in range(256):
    ip_address = ip_range + str(i)
    bulb = wizlight(ip=ip_address)

    try:
        # Attempt to get the bulb's state
        bulb.get_state()

        # If successful, the bulb is discovered
        print("Bulb IP:", bulb.ip)
        print("Bulb MAC:", bulb.mac)
        print()

    except Exception:
        # Ignore any exceptions and continue to the next IP address
        pass
