my_text = "Remarcată încă de la primul campionat mondial de gimnastică pentru expresivitatea artistică, Andreea Răducan (40 de ani) și-a văzut toate eforturile și sacrificiile răsplătite la Jocurile Olimpice de la Sydney din 2000, atunci când câștiga aurul pe echipe și argintul la sărituri. Deși experiența a fost umbrită de un moment dureros – retragerea medaliei de aur la individual compus –, multipla campioană mondială nu s-a lăsat înfrântă, ci și-a continuat parcursul în sportul de înaltă performanță, urcând de mai multe ori pe prima treaptă a podiumului marilor competiții. După retragerea din activitatea sportivă de înaltă performanță, începând din anul 2006, lucrează la Fundaţia Olimpică Română, unde promovează importanţa mişcării şi a sportului, iar din 2011 organizează Cupa de Gimnastică „Andreea Răducan“, acestea fiind doar câteva dintre proiectele în care este implicată."
print(len(my_text))
prima_parte = (my_text[0:440:1])
print(prima_parte)
a_doua_parte = (my_text[440::1])
print(a_doua_parte)

Parte1Majuscule = (prima_parte.upper())
print(Parte1Majuscule)
p1 = Parte1Majuscule.strip()
print(p1)
a_2_invers = (my_text[881:440:-1])
print(a_2_invers)
Majuscula = a_2_invers.replace('ă','Ă')
print(Majuscula)
MfaraPunct = Majuscula.replace('.','')
MfaraVirgula = MfaraPunct.replace(',','')
MfaraGhilimele = MfaraVirgula.replace('“','')
p2 = MfaraGhilimele.replace('„','')
print(p2)

print(p1 + p2)



