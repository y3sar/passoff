import base64
import hashlib
import os

def gen_password(website_name, master_pass, private_key=''):
  if private_key == '':
    # generate random private_key
    private_key = hashlib.sha256(os.urandom(128)).hexdigest();

  joined_text = (private_key+website_name+master_pass).encode('utf-8');

  password_hash = hashlib.sha256(joined_text).hexdigest();
  print(password_hash);

  # to add capital letters 
  password = base64.b64encode(password_hash.encode('utf-8'));

  return password.decode()[:12], private_key;


new_password = gen_password('twitch', 'bohogarden');


print(new_password);






