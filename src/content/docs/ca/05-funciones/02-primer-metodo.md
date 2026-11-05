---
title: "02 · El teu primer mètode"
description: "Desmuntem la firma `public static void` en quatre paraules i escrivim la primera recepta del receptari 🍳"
---

<p><small>Desmuntem la firma <code>public static void</code> en quatre paraules i escrivim la primera recepta del receptari 🍳</small></p>

> 🗺️ **Estàs en:** 🔧 **U05 · Funcions i mètodes** → 02 · El teu primer mètode

---

## 📬 La idea en una frase

> **Declarar un mètode és escriure la seva recepta (`public static void nom() { ... }`); cridar-lo és dir el seu nom amb parèntesis i punt i coma perquè executi el seu cos.**

---

## ✍️ La primera recepta

Aquest és un programa complet amb un mètode propi:

```java
public class Saludo {
    public static void saludar() {
        System.out.println("Hola, classe!");
    }

    public static void main(String[] args) {
        saludar();
        saludar();
    }
}
```

Sortida:

```
Hola, classe!
Hola, classe!
```

Dues parts: **`saludar()`** és la recepta (declarada amunt), i en `main` la **cridem** dos vegades. Fixa't en els dos detalls d'escriptura:

- La **declaració** no porta punt i coma al final: acaba amb el seu bloc `{ ... }`.
- La **crida** sí porta `;`, perquè és una sentència, igual que `int x = 5;`.

---

## 🔍 La firma, paraula per paraula

```java
public static void saludar() {
```

| Paraula | Què significa | Quan la veuràs explicada |
|---|---|---|
| `public` | Visible des de qualsevol lloc | U10 (visibilitat) |
| `static` | Pertany a la classe, no a un objecte | U10 (mètodes static) |
| `void` | **No torna** res | Punt 4 d'aquesta unitat |
| `saludar()` | El nom i els seus parèntesis | Avui |

De moment escrius **sempre** `public static` davant dels teus mètodes. No els oblides: sense `static`, `main` no podrà cridar-los (l'explicació completa arriba en la U10, quan ja sàpigues què és un objecte).

> 📝 **Nota:** el nom segueix la convenció camelCase: `calcularMedia`, `mostrarMenu`, `esPar`. Sense espais, sense accents, i la primera paraula en minúscula. Java és mandrós amb els accents i puntual amb les majúscules.

### Les regles del joc

1. Els mètodes es declaren **dins de la classe**, mai dins d'un altre mètode (ni tan sols dins de `main`).
2. L'**ordre no importa**: pots cridar a un mètode declarat més baix de tot. Java no llegeix d'amunt a avall; busca per nom.
3. Cada mètode és una illa amb el seu propi nom: dos mètodes no poden cridar-se igual **amb els mateixos paràmetres** (això ho veuràs en la U09, amb la sobrecàrrega).

> ⚠️ **Advertència:** l'error de compilació `cannot find symbol` en cridar un mètode gairebé sempre vol dir que li has posat un nom diferent del que té, o que el crides des de fora de la classe.

---

## 🎬 `main` també és un mètode

Aquí està la revelació del dia: `main` no és especial perquè sigui màgic, sinó perquè la JVM **el busca per aquell nom exacte** per a arrancar el teu programa:

```java
public static void main(String[] args) {
```

- `public` → la JVM ha de poder veure'l.
- `static` → la JVM el crida **sense crear un objecte** de la teva classe.
- `void` → torna res (només executa).
- `String[] args` → l'array d'arguments de la línia d'ordres (ho vas veure en la U02).

Tot el que has vingut usant des de la U02 era... un mètode més. La diferència és que tu només cridaves a un sense adonar-te'n. Ara crides a tots els que et vingui de gust.

```java
public class Reencuentro {
    public static void main(String[] args) {
        saludar();               // cridem a un mètode nostre
        System.out.println("Continuar amb el programa...");
    }

    public static void saludar() {
        System.out.println("Hola una altra volta");
    }
}
```

Funciona encara que `saludar` estigui **baix** de `main`. Regla 2: l'ordre no importa.

---

## ⭐ Be the Code, my friend...

> 🕶️ **Don Tip:** si `main` necessita cridar a un mètode, aquell mètode gairebé sempre necessita `static`. Sense `static`, hauràs d'esperar a la U10 perquè les coses encaixen.

**Exercici: la firma trencada**

Quin d'aquests mètodes **compila**?

```java
// Opció A
static public void contar() {
    System.out.println("1");
}

// Opció B
public static contar() {
    System.out.println("1");
}

// Opció C
public static void contar {
    System.out.println("1");
}

// Opció D
public static void contar() System.out.println("1");
```

<details>
<summary>🔄 Solució</summary>

La **A**. `static` i `public` poden anar en qualsevol ordre: les dues són modificadors. La B oblida el tipus de retorn (`void`). La C oblida els parèntesis `()`. La D oblida les claus `{ }`: el cos **sempre** va entre claus.

</details>

---

## 🎯 Mini-chequeig

Posat a prova en 30 segons (les respostes estan amagades):

1. Escriu la firma completa d'un mètode anomenat `acomiadar` que no torno res.
2. Quina línia (i en quin lloc) executa el cos de `acomiadar()`?
3. Pot `main` estar declarat DESPRÉS d'acomiadar en la classe? I a l'inrevés?
4. Quina és la diferència de puntuació entre declarar i cridar?

<details>
<summary>🔄 Respostes</summary>

1. `public static void acomiadar() { ... }`
2. Una **crida** com `acomiadar();` (amb punt i coma), per exemple dins de `main`.
3. Sí a les dues: l'ordre dels mètodes dins de la classe no importa.
4. Declarar acaba en `{ ... }` **sense** `;`; cridar és una sentència i porta `;`.

</details>

---

## ✅ Resum en 3 frases

1. Un mètode es declara amb la seva firma (`public static void nom() {...}`) dins de la classe i **s'executa només quan el cries**.
2. `public static void main(String[] args)` és un mètode més: la JVM el crida en arrancar perquè té aquell nom exacte.
3. L'ordre dels mètodes no importa; el que importa és el nom correcte i no declarar un mètode dins d'un altre.

> 🐛 **Vocabulari ràpid**
>
> | Terme | Idea general |
> |---|---|
> | Firma | La línia completa: modificadors + retorn + nom + paràmetres |
> | Declaració | Definir la recepta (amb el seu cos `{...}`) |
> | Crida | Executar el mètode: `nom(args);` |
> | `static` | De classe: s'usa sense crear objectes (detall en U10) |
> | `void` | "No torno res" |
> | camelCase | `calcularMedia`: minúscula a l'inici, majúscules entre paraules |

📚 [Tornar a l'índex de la unitat](/ApuntsProgramacio/ca/05-funciones) · **Anterior:** [01 · Què és una funció?](/ApuntsProgramacio/ca/05-funciones/01-que-es-funcion) · **Següent:** [03 · Paràmetres: l'entrada](/ApuntsProgramacio/ca/05-funciones/03-parametros)
