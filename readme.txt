************************************
* Studi-Projekte-Server Git ********
************************************

Diese Datei wurde beim ersten automatischen Commit zur Initialisierung und
Bereitstellung weiterer Hilfe für dich erstellt. Du kannst sie gefahrlos löschen.

Git ist ein sehr mächtiges, in seinen Grundfunktionen leicht zu bedienendes,
aber nicht ganz so einfach zu meisterndes Versionierungssystem.
Im Vergleich zu SVN ist das Konzept von Branches (Entwicklungszweig) im System
integriert und nicht durch Kopien in verschiedenen Ordnern gelöst. Das und andere
Funktionen machen es bei Git sehr leicht, für jede kleine Änderung, jedes kleine
neue Feature, eine neue Branch zu eröffnen und sehr sauber zu entwickeln.

Die Hauptfunktionen:

clone:
Bei Git besitzt jeder Entwickler eine private Kopie des Repositories, das .git-
Verzeichnis. Dies macht es einerseits kombiniert mit Hashing quasi nicht möglich,
ein Repository zu manipulieren, andererseits kann auch offline und so viel wie
nötig privat entwickelt werden, ohne ein einziges Bit ans Haupt-Repository zu
übertragen. Clone ist also nichts anderes, als sich eine private Kopie eines
anderen Repositories zu besorgen.
Ähnliches SVN-Kommando: checkout

add:
Dateien müssen zur Versionierung hinzugefügt werden. "git add ." macht einen
guten Job, alle Dateien hinzuzufügen.
Ähnliches SVN-Kommando: add

rm:
Das Gegenteil von add.
Ähnliches SVN-Kommando: rm

commit:
Überträgt Änderungen ins lokale Repository.
Ähnliches SVN-Kommando: commit, allerdings nur lokal

push:
Lokale Änderungen ans Quellrepository übertragen.
Ähnliches SVN-Kommando: commit lokaler Änderungen

pull:
Änderungen vom Quellrepository holen.
Ähnliches SVN-Kommando: update

stash:
Verschiebt aktuelle, nicht comittete Änderungen in eine Art benannten
Zwischenspeicher. Seht nützlich, wenn ein anderer Branch sauber ausgecheckt
werden soll, um z.B. zwischenzeitlich an einem anderen Feature/Bug zu arbeiten.

checkout:
Managet Branches.

switch:
Wechselt in Branches.

merge:
Überführt Änderungen eines anderen Branches in den aktuellen.

rebase:
Eine fortschrittliche Technik, mit der ein Branch quasi rückstandslos in den 
master-Branch eingepflegt werden kann. Sehr interessant für kleine Änderungen,
welche keinen extra Branch in der History zeigen sollen.


Das soll es an dieser Stelle mit der Vorstellung einiger wichtiger Kommandos
gewesen sein. Im Internet finden sich viele sehr gute Referenzen zu Git, z.B.
http://de.gitready.com/, welche bei Problemen neben der eingebauten Hilfe
immer nützlich sind.
