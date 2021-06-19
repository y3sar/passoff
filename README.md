## TODOS

- [ ] Figure out how to save private keys and other info
- [x] Implement the password creator
	- [x] new password creation
	- [ ] password changing
	- [x] unifying all passwords under one private key (involves changing all the passwords);
- [ ] Implement the CLI
- [ ] Solve repeating uppercase letters
another postfix can be added to the privatekey that suggests how many characters will be taken from the password hash and how many from the base64 encoding.


- [ ] Solve repeating lowercase letters
- [ ] Solve repeating letters


* If private-key.json exist
	$ passoff twitch
	$ checking for private_key.json 
	$ private_key found  
	$ enter master pass: 

* If private-key.json does not exist
	$ passoff twitch
	$ checking for private_key.json 
	$ private_key.json not found  
	$ enter private_key/private-key.json path:  
	$ enter master pass: 

* Create new password
	$ passoff create twitch
	$ heres your private key : 123qadsfjp02934u03
	$ do you want to create a private-key.json (y/n)?:
	$ enter master pass (make sure its the same one for all the sites): 
  







