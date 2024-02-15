import os
import re
import sys

def main():
    for line in sys.stdin:
        # Use re.match to check for lines starting with a '#'
        match = re.match(r'^#', line)
        fields = line.strip().split(':')  # Strip whitespace and split by colon

        # Check if the line starts with '#' or doesn't have five fields
        if match or len(fields) != 5:
            continue  # Skip to the next iteration of the loop

        username = fields[0]
        password = fields[1]
        gecos = "{} {},,,".format(fields[3], fields[2])  # User's full name
        groups = fields[4].split(',')  # Split group names into a list

        print("==> Creating account for {}...".format(username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '{}' {}".format(gecos, username)
        # print(cmd)  # Uncomment for debugging
        os.system(cmd)

        print("==> Setting the password for {}...".format(username))
        cmd = "echo '{}:{}' | sudo chpasswd".format(username, password)
        # print(cmd)  # Uncomment for debugging
        os.system(cmd)

        for group in groups:
            if group != '-':
                print("==> Assigning {} to the {} group...".format(username, group))
                cmd = "/usr/sbin/adduser {} {}".format(username, group)
                # print(cmd)  # Uncomment for debugging
                os.system(cmd)

if __name__ == '__main__':
    main()

