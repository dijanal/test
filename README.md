Teorijski deo
---

Dati sto konciznije odgvore u formi prosto prosirenih recenica na svako od sledecih pitanja.

01. Sta je to JSON? 
JavaScript Object Notation format za razmenu podataka.

02. Sta je to XML?
Extensible Markup Language je meta jezik koji se koristi za definisanje drugih jezika ili za razmenu podataka.

03. Sta je to URL? 
Uniform resource locator-putanja do odredjenog sadrzaja na internetu,tj. web adresa.

04. Sta je to HTTP? 
Hypertext transfer protocol-protokol za razmenu fajlova koji sadrze tekst napisan u HTML-u.

05. Sta je to RESTful API?

06. Koje HTTP metode imamo? Get,post,head,option,put,delete,connect.

07. Sta je to DNS? 
Domain name service-servis 

08. Sta je to private IP?

09. Sta je to AJAX?
 -nova tehnika za kreiranje bolje,brze i interaktivne veb aplikacije uz pomoc XML,HTML,CSS i JS.

10. Sta je to TCP/IP? 
TCP/IP protokol  je skup protokola razvijen da omogući umreženim računarima da dele resurse putem mreže. 

11. Sta je to kes memorija?
Keš memorija je memorija malog kapaciteta koja služi za zapis podataka koji se često koriste.

12. Koja je razlika izmedju klase i objekta? 
Klasa je template na osnovu kog se kreira objekat.

Backend
---

1. U `models.py` fajlu implementirati `Comment` model (klasu) u Python-u koja sadrzi atribute:
- `text`: sam komentar, i
- `date`: datum komentara u formatu `YYYY-MM-DD`
"Override"-ovati `__repr__` metod.

2. U `models.py` fajlu definisati `COMMENTS` varijablu koja sadrzi niz od 3 elementa koji su tipa `Comment`. 

3. U `app.py` fajlu napraviti Flask applikaciju koja ima `index` "view" funkciju koja handle-uje `/` route. Funkcija bi trebalo da vraca HTML string koji u `body`-ju sadrzi heading "Welcome!".

4. U `app.py` dodati `comments` "view" funkciju koja handle-uje `/comments` route. Funkcija bi trebalo da vraca HTML koji u `body`-ju sadrzi tabelu komentara. Koristiti Flask template.

5.  U `app.py` dodati `api_comments` "view" funkciju koja handle-uje `/api/v1.0/comments` route. Funkcija bi trebalo da vraca JSON reprezentaciju `COMMENTS` niza.

Frontend
---

U `home.html` fajlu imlementirati jednostavnu klijent aplikaciju kojom moze da testira prethodno implementirani API end point. Koristiti `form` i `iframe`.

Algoritmi
---

Napisati i JavaScript i Python funkciju koja predstavlja resenje sledeceg zadataka:

Write a program that prints the numbers from 1 to 100. But for multiples of three print `Fizz` instead of the number and for the multiples of five print `Buzz`. For numbers which are multiples of both three and five print `FizzBuzz`.

Uputstvo
---

Resenja i odgovore predati u okviru GitHub repozitorijuma.
