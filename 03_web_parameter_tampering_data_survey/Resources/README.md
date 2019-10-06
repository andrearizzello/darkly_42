# Vulnerability

In http://<IP>/?page=survey
This page is accessed by clicking the `Survey` button at the top of the main page

Change the value of one of the field option in the form with a big number

Example: 

<input type="hidden" name="sujet" value="2">
	<select name="valeur" onchange="javascript:this.form.submit();">
		<option value="1">1</option> <-- Change the value of one of these with a big number
		<option value="2">2</option> <--
		<option value="3">3</option> <--
		<option value="4">4</option> <--
		<option value="5">5</option> <--
		<option value="6">6</option> <--
		<option value="7">7</option> <--
		<option value="8">8</option> <--
		<option value="9">9</option> <--
		<option value="10">10</option>
	</select>
</input>

Then submit the form by selecting the big value.

# Protection

Always check values sent by the client before processing them and if the values are abnormal or invalid, 
reject the form
