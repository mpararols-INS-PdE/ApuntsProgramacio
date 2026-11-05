---
title: "07 — Constants de classe: static final"
description: "Valors immutables en MAJÚSCULES i les classes utilitàries que ningú no pot instanciar 🏛️"
---

<p><small>Valors immutables en MAJÚSCULES i les classes utilitàries que ningú no pot instanciar 🏛️</small></p>

> 🗺️ **Estàs en:** 🔒 **U10 · Visibilitat, encapsulació i static** → 07 · Constants de classe: static final

---

## 📬 La idea en una frase

> **`static final` és una constant de classe: un valor que pertany a la classe, no a l'objecte, i que ningú no pot canviar. I si a més li poses el constructor privat, tens una classe utilitària com `Math`.**

Recordes el `final` de la U03: una variable que no es pot canviar. Ara suma-li `static` (de la classe, una sola còpia) i tens la fórmula perfecta per a valors fixos de tota l'aplicació: l'IVA, el nom de l'app, el nombre màxim d'usuaris...

---

## 🏷️ La constant de classe

Declaració canònica, amb el nom en **MAJÚSCULES** i paraules separades per `_`:

```java
public class Config {
    public static final String NOMBRE_APP = "Gestión DAM";
    public static final String VERSION = "2.1.0";
    public static final int MAX_USUARIOS = 100;
    public static final double IVA = 0.21;
}
```

S'usa així, sense crear cap objecte:

```java
double precioConIva = precio * Config.IVA;
System.out.println("Benvingut a " + Config.NOMBRE_APP);
```

I si algú intenta fer `Config.IVA = 0.5`? **El compilador t'ho prohibeix.** És més ferm que els teus propòsits d'Any Nou.

> 💡 **Detall pràctic:** junta les constants en una classe dedicada (`Config`, `Constantes`, `Valores`) i tindràs un únic lloc on canviar, per exemple, l'IVA quan toqui. Ni un "número màgic" solt pel codi.

---

## 🔒 La regla de les MAJÚSCULES

És una **convenció**, no una regla del llenguatge: les constants s'escriuen en MAJÚSCULES amb `_`:

- `MAX_INTENTOS_LOGIN`
- `TIMEOUT_SEGUNDOS`
- `RUTA_LOG`

Quan un altre programador (o tu) vegis `Config.MAX_USUARIOS` en un codi, sabrà a l'instant que això és una constant: no es toca, no es pregunta, no es negocia. L'estil diu molt.

> ⚠️ **Advertència:** compte amb la temptació de declarar-ho tot `static final` "perquè mola". Només és constant el que de veritat no canviarà. El dia que l'IVA pugi, voldràs canviar-lo en un lloc... i si és constant, el canvies i llest.

---

## 🏛️ Les classes utilitàries: el "no necessiti parella" de Java

Una classe utilitària és una classe que **només té membres estàtics**. Són com l'amic que està solter i feliç: no necessita instanciar-se per a ser útil. La prova: `Math`, que ja coneixes.

Com evitem que algú faci `new StringUtils()`? Amb un **constructor privat**:

```java
public class StringUtils {
    private StringUtils() {}  // Ningú no pot fer new StringUtils()

    public static boolean esVacio(String str) {
        return str == null || str.trim().isEmpty();
    }

    public static String invertir(String str) {
        return str == null ? null : new StringBuilder(str).reverse().toString();
    }

    public static String capitalizar(String str) {
        if (esVacio(str)) return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1).toLowerCase();
    }
}
```

Des de fora, tot és `StringUtils.invertir("hola")`. Intentar `new StringUtils()` dona error de compilació: el constructor és privat, la classe "no necessita parella".

> 📝 **Nota:** el constructor privat no és obligatori perquè funcioni, però és l'**etiqueta** d'una classe utilitària ben feta: li diu al món "no m'instancies, soc pura utilitat".

---

## ⭐ Be the Code, my friend...

> 🕶️ **Don Tip:** abans d'escriure un número solt (un 100, un 0.21), pregunta't si és un *número màgic* que mereix una constant amb nom. Els números màgics són la malson de qui manté el teu codi.

**Exercici: el validador del barri**

Escriu (mentalment) una classe `Validador` que sigui utilitària: constructor privat i un mètode `public static boolean esPar(int numero)` que retorni `true` si el nombre és parell.

Com comprovaries, sense crear objectes, que 42 és parell?

<details>
<summary>🔄 Solució</summary>

```java
public class Validador {
    private Validador() {}

    public static boolean esPar(int numero) {
        return numero % 2 == 0;
    }
}
```

I per a usar-la, sense `new`: `boolean resultado = Validador.esPar(42);` → `true`. El `%` del punt 3 de la U03 i el `static` d'aquesta unitat, treballant en equip.

</details>

---

## 🎯 Mini-chequeig

Posat a prova en 30 segons (les respostes estan amagades):

1. Què significa `static final` i com es nomena?
2. Per què `Math` no es pot instanciar?
3. Què és un número màgic i com l'evites?
4. Pot canviar una constant després de declarar-la?

<details>
<summary>🔄 Respostes</summary>

1. Una constant de classe: pertany a la classe (una sola còpia) i no es pot canviar. Es nomena en MAJÚSCULES amb `_`.
2. Perquè el seu constructor és `private`: és una classe utilitària, no hi ha motius per a crear objectes.
3. Un valor literal sense explicació (com `0.21` o `100`) tirat pel codi. L'evites donant-li nom en una constant: `Config.IVA`.
4. No: el compilador prohibeix modificar una variable `final` després de la seva assignació inicial.

</details>

---

## ✅ Resum en 3 frases

1. `static final` crea una **constant de classe**: una sola còpia, immutable, en MAJÚSCULES.
2. Les **classes utilitàries** (com `Math`) només tenen membres estàtics i usen **constructor privat** perquè ningú no les instancii.
3. Evita els **números màgics** donant-los nom i ajuntant-los en una classe `Config`.

> 🐛 **Vocabulari ràpid**
>
> | Terme | Idea general |
> |---|---|
> | Constant | `static final`: valor fix de la classe |
> | Número màgic | Valor literal sense nom que hauria de ser constant |
> | Classe utilitària | Només estàtics, constructor privat |
> | Convenció | Regla d'estil (MAJÚSCULES) que tots segueixen |
> | Constructor privat | Impedeix crear objectes de la classe |

📚 [Tornar a l'índex de la unitat](/ApuntsProgramacio/ca/10-visibilidad-encapsulacion-static) · **Anterior:** [06 · Mètodes static i el main](/ApuntsProgramacio/ca/10-visibilidad-encapsulacion-static/06-metodos-static) · **Següent:** [08 · Be the Code: encapsula la teva classe](/ApuntsProgramacio/ca/10-visibilidad-encapsulacion-static/08-be-the-code)