# Hidden Input Exploitation

at the password recovry page you can inspect the submit button we fund the section hidden input 

```
<form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value= "Submit">
</form>

```
we can simply set the mail and send the recovery password

# Ho wto avoid:

Backend Validation: Always handle and validate input data on the backend. Do not trust or rely solely on client-side data (including hidden inputs).
Additional Measures:
Use server-side checks to verify the authenticity of the recovery request.
Avoid relying on hidden inputs for sensitive data or use signed tokens to prevent tampering.
