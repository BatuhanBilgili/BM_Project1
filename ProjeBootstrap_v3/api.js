const data = null;

const xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener('readystatechange', function () {
	if (this.readyState === this.DONE) {
		console.log(this.responseText);
	}
});

xhr.open('GET', 'https://api-football-v1.p.rapidapi.com/v3/timezone');
xhr.setRequestHeader('X-RapidAPI-Key', 'a32765c167msh2cfd8e64f939f7ap1c10bfjsn77c2983b8b70');
xhr.setRequestHeader('X-RapidAPI-Host', 'api-football-v1.p.rapidapi.com');

xhr.send(data);
