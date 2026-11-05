---
title: "U12 — Col·leccions, genèrics i mapes"
description: "L'aparcament que creix, el porter sense duplicats, el `<T>` que ho canvia tot i la guia telefònica: ArrayList, Set, genèrics i HashMap en una sola unitat 📚"
emoji: 📚
---

<p><small>L'aparcament que creix, el porter sense duplicats, el `<T>` que ho canvia tot i la guia telefònica: ArrayList, Set, genèrics i HashMap en una sola unitat 📚</small></p>

---

En la U06 vas veure els arrays: grandària fixa, accés per índex i prou treball manual per a créixer o encongir-se. Avui això s'acaba. Les **col·leccions** de Java són les estructures de dades amb superpoders: creixen soles, s'encongeixen soles, rebutgen duplicats si vols, s'ordenen automàticament i es recorren sense que t'importi com estan construïdes per dins.

I aquesta unitat va més enllà: després de dominar les col·leccions, llevarem el capó del `<String>` que portes setmanes escrivint. Els **genèrics** expliquen per què el compilador es fia de les teves llistes, i els **mapes** (`HashMap`, `TreeMap`) et donen l'estructura que més s'usa en Java real: associar una clau amb un valor.

Aquesta unitat té quatre grans actes:

- **Llistes (`List`):** `ArrayList`, l'aparcament que creix sol, i `LinkedList`, la conga que encadena els seus elements i brilla en cues i piles.
- **Conjunts (`Set`):** `HashSet`, el porter que no deixa entrar duplicats; `TreeSet`, el que els ordena sols; i `LinkedHashSet`, el que recorda l'ordre d'arribada.
- **Genèrics:** d'on surt el `<T>`, la teva pròpia classe genèrica, el diamant `<>`, el type erasure i el principi PECS.
- **Mapes (`Map`):** `HashMap`, la guia telefònica de Java; `TreeMap`, el que ordena les seves claus; i la guia definitiva per a triar estructura.

Aquesta unitat es llegeix com un **llibre de 9 capítols**: els 8 primers punts són teoria en progressió i el 9 és un aterratge pràctic per a deixar-ho tot ben lligat.

---

## 🎯 Objectiu de la unitat

En acabar, seràs capaç de:

- Usar **`ArrayList`** per a guardar llistes dinàmiques i distingir **`remove(índex)`** de **`remove(objecte)`**.
- Aplicar **`LinkedList`** per a cues (FIFO) i piles (LIFO).
- Eliminar duplicats amb **`HashSet`** i entendre per què `hashCode()` i `equals()` van sempre junts.
- Ordenar i mantenir l'ordre amb **`TreeSet`** i **`LinkedHashSet`**.
- Recórrer qualsevol col·lecció amb **`Iterator`** i esborrar durant el recorregut sense excepció.
- Manipular llistes amb la classe **`Collections`** (`sort`, `reverse`, `shuffle`, `max`, `min`, `frequency`).
- Crear les teves **classes i mètodes genèrics** amb `<T>`, límits i wildcards.
- Guardar i buscar parelles clau → valor amb **`HashMap`** i **`TreeMap`**.
- **Triar l'estructura adequada** (List, Set o Map) per a cada problema.

---

## 🗺️ Mapa de la unitat

| Punt | Què aprendràs | Dificultat |
|---|---|---|
| [01 · ArrayList i el Java Collections Framework](/ApuntsProgramacio/ca/12-colecciones/01-arraylist-jcf) | L'aparcament que creix sol, la família `java.util` i per què no guarda `int` a palpes | Tots |
| [02 · LinkedList: la conga line](/ApuntsProgramacio/ca/12-colecciones/02-linkedlist) | La llista enllaçada, cues FIFO, piles LIFO i els seus mètodes d'extrems | Tots |
| [03 · HashSet, TreeSet i LinkedHashSet: els conjunts](/ApuntsProgramacio/ca/12-colecciones/03-conjuntos-sets) | El porter sense duplicats, el que ordena sol i el que recorda l'ordre d'arribada | Tots |
| [04 · Iterator i Collections](/ApuntsProgramacio/ca/12-colecciones/04-iterator-collections) | Esborrar mentre recorres i la navalla suïssa de les col·leccions | Tots |
| [05 · Classes genèriques: la teva `Caja<T>`](/ApuntsProgramacio/ca/12-colecciones/05-clases-genericas) | D'on surt el `<String>`, convencions T/E/K/V i la teva primera classe genèrica | Tots |
| [06 · El diamant, mètodes genèrics i wildcards](/ApuntsProgramacio/ca/12-colecciones/06-genericos-avanzado) | Type erasure, inferència, límits i el principi PECS | Tots |
| [07 · HashMap: la guia telefònica](/ApuntsProgramacio/ca/12-colecciones/07-hashmap) | Clau → valor, `get`, `put`, `containsKey` i recórrer mapes | Tots |
| [08 · TreeMap i com triar estructura](/ApuntsProgramacio/ca/12-colecciones/08-treemap-elegir-estructura) | Mapes ordenats, `LinkedHashMap` i Map vs List vs Set | Tots |
| [09 · Repàs interactiu](/ApuntsProgramacio/ca/12-colecciones/09-repaso-interactivo) | Be the Code, Fireside, Laboratori, Crucigrama i més | Tots |

> 📖 **Flux de lectura:** els 8 primers punts són teoria en progressió. El 9 és l'aterratge pràctic: llegeix-lo just després del 8 i abans d'obrir els butlletins.

---

## 📝 Butlletins de la unitat

> Practica amb els parells del curs: intenta primer el per-resoldre i comprova amb el resolt quan hagis acabat.

<div class="ejercicio-links">
  <a href="/ApuntsProgramacio/ca/boletines/boletin-u12-inicial" class="elink">🟢 Inicial per resoldre</a>
  <a href="/ApuntsProgramacio/ca/boletines/boletin-u12-inicial-resuelto" class="elink">✅ Inicial resolt</a>
  <a href="/ApuntsProgramacio/ca/boletines/boletin-u12-avanzado" class="elink">⭐ Avançat per resoldre</a>
  <a href="/ApuntsProgramacio/ca/boletines/boletin-u12-avanzado-resuelto" class="elink">💪 Avançat resolt</a>
  <a href="/ApuntsProgramacio/ca/boletines/boletin-u12-extras" class="elink">🔥 Extres</a>
</div>

---

## ✅ Criteris d'avaluació coberts (RA6)

**RA6: Escriu programes que manipulen informació, seleccionant i utilitzant tipus avançats de dades.**

| CE | Criteri | On es cobreix |
|---|---|---|
| RA6 b) | S'han reconegut les llibreries de classes relacionades amb tipus avançats de dades. | ✅ Punts 1, 7 i 8 |
| RA6 c) | S'han utilitzat llistes per a emmagatzemar i processar informació. | ✅ Punts 1, 2 i 9 |
| RA6 d) | S'han utilitzat iteradors per a recórrer els elements de les llistes. | ✅ Punts 4 i 9 |
| RA6 e) | S'han reconegut les característiques i avantatges de cadascuna de les col·leccions de dades disponibles. | ✅ Punts 3, 7 i 8 |
| RA6 f) | S'han utilitzat tipus enumeradors, estructures dinàmiques de dades i classes genèriques. | ✅ Punts 5, 6, 7 i 8 |

> 📌 La **RA6** es completa amb la **U06** (arrays, CE a) i la **U14** (regex i XML, CEs g, h i i). Aquesta unitat cobreix col·leccions, genèrics i mapes: la llibreria `java.util` sencera.

---

## 🚪 Per on començo?

- Vens de la U11 i vols l'essencial? → Comença en el [punt 1](/ApuntsProgramacio/ca/12-colecciones/01-arraylist-jcf) i el [punt 2](/ApuntsProgramacio/ca/12-colecciones/02-linkedlist): les llistes de tots els dies.
- Ja uses llistes i vols conjunts? → Ves directe al [punt 3](/ApuntsProgramacio/ca/12-colecciones/03-conjuntos-sets): duplicats fora.
- Et pica la curiositat del `<T>`? → Salta al [punt 5](/ApuntsProgramacio/ca/12-colecciones/05-clases-genericas) i al [punt 6](/ApuntsProgramacio/ca/12-colecciones/06-genericos-avanzado): genèrics de cap a cap.
- Vols mapes? → [Punt 7](/ApuntsProgramacio/ca/12-colecciones/07-hashmap) i [punt 8](/ApuntsProgramacio/ca/12-colecciones/08-treemap-elegir-estructura): la guia telefònica i el mapa de decisió.
- Vens a repassar? → Fes el [Repàs interactiu](/ApuntsProgramacio/ca/12-colecciones/09-repaso-interactivo) i després els [butlletins](/ApuntsProgramacio/ca/boletines/boletin-u12-inicial).

**📍 Primer punt:** [01 · ArrayList i el Java Collections Framework](/ApuntsProgramacio/ca/12-colecciones/01-arraylist-jcf)  
**⏭️ En acabar la unitat, continua en [U13 · Programació funcional (Streams i Lambdas)](/ApuntsProgramacio/ca/13-programacion-funcional).**
