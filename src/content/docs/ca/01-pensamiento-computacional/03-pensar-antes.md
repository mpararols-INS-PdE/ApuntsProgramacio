---
title: "03 — Primer pensem, després escrivim"
description: "El camí sagrat del programador i el test del Robot Literal 📝➡️💻"
---

<p><small>El camí sagrat del programador i el test del Robot Literal 📝➡️💻</small></p>

> 🗺️ **Estás en:** 🧠 **U01 · Introducció al pensament computacional** → 03 · Primer pensem, després escrivim

---

Hi ha un error clàssic de principiant que es repeteix des de la invenció dels ordinadors: obrir l'editor de codi, posar les mans sobre el teclat i començar a escriure línies sense tenir ni la més remota idea de com es resol el problema. 🤦‍♂️💥

El resultat d'això sol ser una mescla de frustració, errors de sintaxi en vermell per tota la pantalla i la sensació que la informàtica és una mena de màgia negra reservada per a uns pocs triats. 🧙‍♂️❌

Avui volem trencar aquest mite amb una regla d'or que t'estalviarà centenars d'hores de dolor durant el curs: **El codi és simplement la traducció d'una solució que JA has pensat prèviament en paper.** 📄✍️

---

## 🔮 La il·lusió de la literalitat (El teu ordinador no és endeví)

Els humans som unes màquines de "llegir entre línies". Si li dius a un amic *"Vaig a la cuina, vols aigua?"* i et respon *"Sí, si us plau"*, tu entens perfectament que has d'agafar un got, obrir l'aixeta o la botella, omplir el got i portar-li-lo. No et passa pel cap anar a la cuina, agafar un doll d'aigua amb les mans i tirar-li-lo per sobre a la cara, veritat? 🌊😳

**Si li demanes això mateix a un ordinador:**

* No sap què és un got 🥃.
* No sap quan ha de parar d'abocar aigua (inundació a la cuina 🌊).
* Es queda bloquejat per sempre esperant que li digues si l'aigua ha de ser del temps o freda 🧊.

> 🤖 **La crua realitat:** Un ordinador no té intuïció, no té sentit comú, no té empatia i **no interpreta el que vols dir: executa exactament les instruccions que li dones**. Si el teu programa fa coses rares, no és que la màquina et tingui mania; és que tu has assumit que l'ordinador "ja t'entenia". I no, no t'entén!

---

## 🛣️ El camí sagrat del programador

Per a no col·lapsar el teu cervell, el flux de treball per a resoldre qualsevol exercici ha de seguir SEMPRE aquesta seqüència de 4 passos:

***[1. Problema 🧩] ──► [2. Pas a pas (Algorisme) 👣] ──► [3. Solució en paper 📄✍️] ──► [4. Codi 💻]***

1. **Entendre el problema 🧩:** Llegir l'enunciat fins que siguis capaç d'explicar-li-ho a la teva àvia o al teu gat. Si no saps què et demanen, és impossible resoldre-ho!
2. **Pensar els passos (Algorisme) 👣:** Dissenyar la seqüència lògica de passos que solucionen el problema. Quina dada va primer? Què he de calcular? Quina decisió he de prendre?
3. **Escriure la solució en paper 📄:** Usar el teu propi idioma (valencià/castellà) o un dibuix per a comprovar que la lògica té sentit.
4. **Traduir a Java 💻:** Obris l'ordinador. Ara només has de preocupar-te per la sintaxi (punts i comes ;, claus {}, etc.), perquè la lògica ja la tens resolta en el paper.

Si intentes fer el Pas 2 i el Pas 4 al mateix temps directament al teclat, la teva "RAM mental" es col·lapsarà i apareixerà el bloqueig. 🤯❌

---

## 🤖🧪 Exercici pràctic: El test del Robot Literal

Per a experimentar això en la teva pròpia pell sense tocar cap ordinador, anem a fer un experiment mental.

Imagina que has de donar instruccions a un **Robot Literal** (un ésser que no té sentit comú i ho fa TOT al peu de la lletra) per a una d'aquestes tasques quotidianes:

* ☕ **Fer un cafè en cafetera de degoteig.**
* 🎒 **Preparar la motxilla per a anar a classe.**
* 🍳 **Fer una truita de creïlles.**
* 🚗 **Canviar una roda picada d'un cotxe.**
* 🛒 **Fer una compra en una botiga en línia.**

### Què passa quan intentem escriure les instruccions? ⚠️

Si escrius: *"Agafa el cafè i posa'l a la cafetera"*, el Robot Literal agafarà el paquet de cafè TANCAT i el tirarà damunt de la cafetera sense obrir-lo. 📦💥

Perquè el Robot ho faci bé, has de desglossar-ho així:

1. Agafa el paquet de cafè amb la mà dreta.
2. Amb la mà esquerra, obre la pestanya superior del paquet.
3. Agafa la cullera... *(i així 20 passos més)*.

---

## 👿 Els 5 dimonis de la lògica

Quan fem aquest exercici, apareixen immediatament els 5 problemes que després et trobaràs programant en Java:

1. **Passos que falten 🚫:** Obrir la botella d'aigua abans d'abocar-la.
2. **Ordre incorrecte 🔀:** Posar-te les sabates abans que els mitjons.
3. **Ambigüitats ❓:** En comptes de dir *"Gira a la dreta"*, dir *"Gira un poc"*. Quant és "un poc"? 45 graus? 180 graus?
4. **Informació implícita 🤫:** Donar per fet que el Robot sap que l'aigua crema.
5. **Decisions no contemplades 🔀:** Què fa el Robot si quan agafa el cafè... s'ha acabat el cafè? *(Si no li ho has dit, el Robot es queda penjat per sempre).*

---

## 💡 Idea clau per a recordar

> **El codi és només l'últim pas.**

> Si no saps resoldre un problema amb un paper i un bolígraf en el teu propi idioma, és absolutament impossible que el puguis resoldre en Java davant de la pantalla. Pensa primer, tecleja després! 🧠📄➡️⌨️

---

📚 [Tornar a l'índex de la unitat](/ApuntesProgramacion/ca/01-pensamiento-computacional) · **Anterior:** [02 · Programar no és memoritzar codi](/ApuntesProgramacion/ca/01-pensamiento-computacional/02-no-memorizar) · **Següent:** [04 · La descomposició](/ApuntesProgramacion/ca/01-pensamiento-computacional/04-descomposicion)
