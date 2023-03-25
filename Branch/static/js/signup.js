function next(){
	if (document.getElementById("sec_1").style.display == "block" && document.getElementById('id_username').value != "" && document.getElementById('id_email').value != ""){
		document.getElementById("sec_1").style.display = "none"
		document.getElementById("sec_2").style.display = "block"
	}
}