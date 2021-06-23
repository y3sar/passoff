#!/home/samx/anaconda3/bin/python
from cli import create_new_pass, get_pass
import argparse


parser = argparse.ArgumentParser();
parser.add_argument('website_name');
parser.add_argument('-n', '--new', action='store_true');
parser.add_argument('-m', '--master');
parser.add_argument('-p', '--private');

args = parser.parse_args();

website_name = args.website_name


# Creates new password and private key
if (args.new):
  password, private_key = create_new_pass(website_name, master_pass=args.master);

else:
  password, _ = get_pass(website_name, master_pass=args.master, private_key=args.private);

print(password);


