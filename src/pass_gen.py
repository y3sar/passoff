import base64
import hashlib
import os
import random





def gen_password(website_name, master_pass, private_key=''):
  if private_key == '':
    postfix1 = random.randint(2,6);
    postfix2 = random.randint(100, 999);
    # generate random private_key
    private_key = hashlib.sha256(os.urandom(128)).hexdigest() + str(postfix1) + str(postfix2);
  else:
    postfix1 = int(private_key[-4]);
    postfix2 = int(private_key[-3:]);

  print(private_key);
  joined_text = (private_key+website_name+master_pass).encode('utf-8');

  password_hash = hashlib.sha256(joined_text).hexdigest();

  # to add capital letters 
  password = password_hash[:postfix1] + base64.b64encode(password_hash.encode('utf-8')).decode()[:12 - postfix1];
  
  is_valid = is_pass_valid(password);

  if is_valid == '':
    return password, private_key;

  return fix_password(password, is_valid, postfix2), private_key;


def fix_password(password, token, postfix):
  ret = list(password);


  if 'n' in token:
    n_idx = int(str(postfix)[0]);
    new_char = str(ord(ret[n_idx]))[-1];
    ret[n_idx] = new_char;

  if 'l' in token:
    l_idx = int(str(postfix)[1]);
    new_char = ret[l_idx].lower();
    ret[l_idx] = new_char;

  if 'u' in token:
    u_idx = int(str(postfix)[2]);
    new_char = ret[u_idx].upper();
    ret[u_idx] = new_char;

  return ''.join(ret);



def is_pass_valid(password):
  """Checks if a password is valid (has atleast one number, lowercase, uppercase"""
  ret = "nlu"

  for char in password:
    if 'l' in ret and char.islower():
      ret = ret.replace("l", "");

    if 'u' in ret and char.isupper():
      ret = ret.replace("u", "");

    if 'n' in ret and char.isnumeric():
      ret = ret.replace("n", "");

  return ret;




new_password, private_key = gen_password('twitch', 'bohogarden');
new_password2, _ = gen_password('twitch', 'bohogarden', private_key=private_key);

print(new_password);
print(new_password2);








