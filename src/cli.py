import argparse
from pass_gen import gen_password
import json
import sys
import os


def create_new_pass(website_name, master_pass=None, private_key=None):


  json_found = True

  if not master_pass:
    master_pass = input("enter your master password: ");

  print("generating your password for {}...".format(website_name));

  if not private_key:
    private_key = get_private_key_from_json();
    
    if not private_key:
      json_found = False;
      print("private_key json not found");
      print("generating new private key...");

  new_pass, private_key =  gen_password(website_name, master_pass, private_key);


  if not json_found:
    do_save = True if input("do you want to save the private key in private_key.json?(y/n)") == 'y' else False;
    if do_save:
      save_private_key(private_key);

  show_key_pass = input("do you want to see the password and the private_key?(y/n)")

  if show_key_pass == 'y':
    print("your password for {} ".format(website_name), new_pass);
    print("your private key: ", private_key);

   

  return new_pass, private_key


def get_pass(website_name, master_pass=None, private_key=None):
  
  if not master_pass:
    master_pass = input("enter your master password: ");

  if not private_key:
    from_json = get_private_key_from_json();

    if from_json:
      private_key = from_json;

    else:
      private_key_prompt = input("enter your private_key or path to private_key.json: ");

      if private_key_prompt.isalnum():
        private_key = private_key_prompt

      else:
        print("error: invalid private key");
        return None;
  
  ret = gen_password(website_name, master_pass, private_key=private_key);

  return ret;




def save_private_key(private_key):
  private_key_json = {'private_key':private_key};

  with open('private_key.json', 'w') as outputfile:
    json.dump(private_key_json, outputfile);

def get_private_key_from_json():

  exe_path, _ = os.path.split(sys.argv[0])
  path = exe_path + '/private_key.json'

  try:
    ret = open(path, 'r');
  except FileNotFoundError:
    print(f'error: file was not found in the given path {path}');
    return None

  return json.load(ret)['private_key'];
    


