import subprocess

def get_wifi_profiles():
    """Retrieve all Wi-Fi profiles saved on the system."""
    try:
        # Run command to get all Wi-Fi profiles
        command = ["netsh", "wlan", "show", "profiles"]
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        
        # Extract the profile names (SSIDs)
        profiles = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError:
        print("Failed to retrieve Wi-Fi profiles.")
        return []

def get_wifi_password(profile):
    """Retrieve the password for a specific Wi-Fi profile."""
    try:
        # Run command to get details of the Wi-Fi profile, including the password
        command = ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        output = subprocess.check_output(command, shell=True).decode('utf-8')

        # Extract the password from the output
        for line in output.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return "No password found (open network or password not stored)."
    except subprocess.CalledProcessError:
        return "Failed to retrieve password."

def main():
    """Main function to display Wi-Fi profiles and their passwords."""
    profiles = get_wifi_profiles()

    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    print("Saved Wi-Fi profiles and their passwords:\n")
    for profile in profiles:
        password = get_wifi_password(profile)
        print(f"Wi-Fi Network: {profile}\nPassword: {password}\n")

if __name__ == "__main__":
    main()
