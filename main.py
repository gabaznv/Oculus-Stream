import subprocess
#made by gabaihype
def main():
    print("Welcome to Quest Stream!")
    print("Select your Oculus device:")
    print("1) Oculus Quest 2")
    print("2) Oculus Quest 1")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        command = "scrcpy --audio-codec=opus --crop 1600:900:2017:510"
        print("Starting stream for Oculus Quest 2...")
    elif choice == '2':
        command = "scrcpy --audio-codec=opus --crop 1280:720:1500:350"
        print("Starting stream for Oculus Quest 1...")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"Error running command: {e}")

if __name__ == "__main__":
    main()
