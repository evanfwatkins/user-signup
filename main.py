from flask import Flask, request, redirect, render_template 
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/") 
def index():
   return render_template("form_1.html")


@app.route("/validate_user", methods=["POST"])
def validate_user():
    username_from_form = request.form["username"]
    password_from_form = request.form["password"]
    verify_from_form = request.form["verify"]
    email_from_form = request.form["email"]

    username_logic_error = ""
    password_logic_error = ""
    verify_logic_error = ""
    email_logic_error = ""
    
    #username logic
    if username_from_form == "":
        username_logic_error="Username was left blank"

    if len(username_from_form) < 3:
        username_logic_error = "User name must be longer than 3 and less than 20 characters" 
    
    if len(username_from_form) >20:
        username_logic_error = "User name must be longer than 3 and less than 20 characters"
    
    if " " in username_from_form:
        username_logic_error = "Spaces are not allowed" 
    
    #password logic
    if password_from_form == "":
        password_logic_error = "Password was blank"
    
    if " " in password_from_form:
        password_logic_error = "Spaces are not allowed"
    
    if len(password_from_form) < 3:
        password_logic_error = "User name must be longer than 3 and less than 20 characters" 
    
    if len(password_from_form) >20:
        password_logic_error = "User name must be longer than 3 and less than 20 characters"
    
    #verify field logic
    if verify_from_form =="":
        verify_logic_error = "Verification was blank"
     
    if " " in verify_from_form:
        verify_logic_error = "Spaces are not allowed"    
    
    if not password_from_form == verify_from_form:
        verify_logic_error = "Passwords do not match"

    # email logic
    # space or not text handeling
 
    if " " in email_from_form:
        email_logic_error = "Spaces are not allowed in the email"       
   
    # length of email and format (requires 1 "@" and 1 ".") 
    if len(email_from_form) <3:
        email_logic_error = "Email must be longer than 3 and less than 20 characters" 
    
    if len(email_from_form) >20:
        email_logic_error = "Email must be longer than 3 and less than 20 characters"    
    
    for char in email_from_form:
        if email_from_form.count ("@") < 1:
            email_logic_error = "The email must have only one '@' and one '.'"

        elif email_from_form.count ("@") > 1:
            email_logic_error = "The email must have only one '@' and one '.'"
        
        else:
            email_logic_error=""

    all_error_messages_combined = (username_logic_error + password_logic_error + verify_logic_error + email_logic_error)
    if all_error_messages_combined == "":
        return render_template("hello_greeting.html",
            username=username_from_form)
    else:
        return render_template("form_1.html", 
            username=username_from_form, 
            email=email_from_form, 
            email_error=email_logic_error,
            username_error=username_logic_error, 
            password_error=password_logic_error,
            verify_error=verify_logic_error)

app.run()   