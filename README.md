## TODOS

- [ ] Figure out how to save private keys and other info
- [x] Implement the password creator
	- [x] new password creation
	- [ ] password changing
	- [x] unifying all passwords under one private key (involves changing all the passwords);
- [ ] Implement the CLI

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

changing password is a pain in the ass cuz it requires changing something in the private-key+website-name+master-pass. If either master-pass or private-key is changed then all the website passwords have to be changed. Which leaves us with website name. Only the website name in the combination can be changed to change the whole password without disrupting other passwords.

im thinking a prefix that gets added at the end of the website name. But then that has to be saved to keep track of the password changes.

Is there a way to add a prefix to the website name without saving the prefix. The prefix comes from the whole combination maybe?

is it possible to change a private-key in a way that only changes one particular websites password?

lets put a pin in this for now if you wanna change password all website passwords will be changed.




