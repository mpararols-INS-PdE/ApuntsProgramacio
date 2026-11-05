---
title: "08 — Be the Code: dissenya la teva classe"
description: "Tanca la pàgina, obre l'editor i dissenya una classe completa de principi a fi (o pateix amb honor) 🕶️"
---

<p><small>Tanca la pàgina, obre l'editor i dissenya una classe completa de principi a fi (o pateix amb honor) 🕶️</small></p>

> 🗺️ **Estàs en:** 🏗️ **U09 · POO: classes i objectes** → 08 · Be the Code: dissenya la teva classe

---

## 📬 La idea en una frase

> **Ja has vist la teoria: ara toca esborrar-la de la memòria i construir una classe completa tu sol, pas a pas, perquè una classe només s'entén de veritat quan et dol dissenyar-la.**

> 🕶️ **Don Tip:** tota classe es dissenya amb la mateixa escala: (1) tria el nom i els seus atributs, (2) el constructor que els inicialitza, (3) els mètodes que saben fer coses amb ells, (4) un `main` que la provi. Si domines aquella escala, qualsevol classe és teva.

---

## 🚦 Exercici guiat: el compte bancari

Tanca aquesta pàgina. Obre un editor en blanc. No miris ni una línia del que has llegit fins ara.

L'encàrrec: dissenyar una classe `CuentaBancaria` que guardi el titular i el saldo, i que sàpiga **ingressar** diners, **retirar** diners (sense deixar el saldo en negatiu) i **mostrar-se** per pantalla.

### Pas 1: el nom i els atributs

Quines dades necessita un compte bancari? Mínim dues: qui el té (el **titular**, un `String`) i quants diners hi ha (el **saldo**, un `double`). Els atributs van dins de la classe, fora de qualsevol mètode:

```java
public class CuentaBancaria {
    String titular;
    double saldo;
}
```

> 🧠 **Abans de seguir, respon-te a tu mateix:** el saldo hauria de ser `int` o `double`? Per què? (Pista: els diners tenen cèntims, i els cèntims no són enters.)

### Pas 2: el constructor

Els atributs no han de néixer sense rumb. Un constructor que rebi el titular i el saldo inicial i els col·loque amb `this`:

```java
public CuentaBancaria(String titular, double saldoInicial) {
    this.titular = titular;
    this.saldo = saldoInicial;
}
```

### Pas 3: els mètodes

El compte necessita tres comportaments:

- `ingresar(double cantidad)`: suma al saldo. Hauria de rebutjar quantitats negatives (qui ingressa -50 €?).
- `retirar(double cantidad)`: resta al saldo, però **sense deixar-lo negatiu**. Si no hi ha saldo suficient, no retira i avisa.
- `mostrar()`: imprimeix "Titular: X | Saldo: Y €".

Escriu cada mètode amb la seva firma i la seva lògica. Recorda: els mètodes que només fan coses són `void`; si algun necessités retornar alguna cosa, usaria `return`.

### Pas 4: prova-la amb un `main`

Cap classe està acabada fins que no l'has vist funcionar. Afegeix un `main` que crege un compte, ingressa, retire (fins i tot més del que hi ha, per a veure la protecció) i mostri el resultat.

### La solució completa (intenta-ho abans de mirar)

<details>
<summary>🔄 Solució del compte bancari</summary>

```java
public class CuentaBancaria {
    String titular;
    double saldo;

    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    void ingresar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
        } else {
            System.out.println("No puedes ingresar " + cantidad + " €. Eso es cosa de magos.");
        }
    }

    void retirar(double cantidad) {
        if (cantidad > saldo) {
            System.out.println("No hay saldo suficiente: solo tienes " + saldo + " €.");
        } else {
            saldo -= cantidad;
        }
    }

    void mostrar() {
        System.out.println("Titular: " + titular + " | Saldo: " + saldo + " €");
    }

    public static void main(String[] args) {
        CuentaBancaria cuenta = new CuentaBancaria("Ana", 100);
        cuenta.ingresar(50);
        cuenta.retirar(200);
        cuenta.retirar(30);
        cuenta.mostrar();
    }
}
```

Sortida:

```
No hay saldo suficiente: solo tienes 150 €.
Titular: Ana | Saldo: 120 €
```

Fixa't en els detalls: l'`if` de l'`ingresar` protegeix contra quantitats negatives, l'`if` del `retirar` protegeix el saldo, i el `main` és la prova de foc que demostra que la classe funciona.

</details>

---

## ⭐ Nivells d'assoliment

- ⭐ **Ho tens, però has hagut de mirar la solució una vegada.** Aprovat raspant.
- ⭐⭐ **T'ha sortit a la primera i funciona.** Ets una màquina.
- ⭐⭐⭐ **T'ha sortit a la primera, amb els dos `if` de protecció i, a més, li has afegit un mètode `double consultarSaldo()` que retorna el saldo.** No necessites aquest curs. Ves a donar una xerrada TED.

> [!TIP]
> Pista mental gratuïta: una classe necessita **quatre peces** — atributs, constructor, mètodes i una prova (`main`). Si memoritzes aquella escala, qualsevol classe que et demanen en l'examen se't rendeix en cinc minuts.

---

## 🧩 El lío

El departament de qualitat ha rebut aquesta classe. Alguna cosa fa mala olor. Troba els **3 errors**:

```java
public class Coche {
    String marca;
    int velocidad;

    public Coche(String marca) {
        marca = marca;
    }

    void acelerar(int inc) {
        velocidad += inc;
    }

    void mostrar() {
        System.out.println(marca + " a " + velocidad + " km/h");
    }
}
```

> 🕶️ **Don Tip:** executa-ho amb `new Coche("Seat")` i mira què imprimeix `mostrar()`. Després revisa el constructor amb lupa.

<details>
<summary>🔄 Solució del lío</summary>

1. **El constructor es queda sense inicialitzar l'atribut**: `marca = marca` assigna el paràmetre al paràmetre (sense `this`, guanya el paràmetre). L'atribut `marca` queda en `null`. Ha de ser `this.marca = marca`.
2. **La velocitat mai no s'inicialitza**: Java la deixa en 0 per defecte, però això és dependre del regal. Un constructor ben educat posaria `this.velocidad = 0` (o millor, un constructor que la rebi).
3. **El `main` no existeix**: la classe no té cap prova. La classe compila, però ningú no pot executar-la per a veure si funciona. Tota classe sense `main`... i sense un altre programa que l'usi, és una classe que viu en l'ombra.

La lliçó: **el constructor és el que "bateja" els atributs, i sense un `main` (o un programa que instancii) la teva classe és només teoria**. Els tres errors típics del novell en una sola classe.

</details>

---

## 🎯 Mini-chequeig

Posat a prova en 30 segons (les respostes estan amagades):

1. Quines són les quatre peces de l'escala per a dissenyar una classe?
2. Què passa en el constructor si escrius `marca = marca` sense `this`?
3. Per què el `retirar` necessita un `if` abans de restar?
4. Quan està "acabada" una classe?

<details>
<summary>🔄 Respostes</summary>

1. **Atributs → constructor → mètodes → prova (`main`)**.
2. Que assignes el paràmetre al paràmetre i l'atribut queda en **`null`**.
3. Per a **no deixar el saldo en negatiu** (o rebutjar l'operació si no hi ha fons).
4. Quan **funciona**, és a dir, quan un `main` (o un altre programa) la instancia i produeix el resultat esperat.

</details>

---

## ✅ Resum en 3 frases

1. Dissenyar una classe és una **escala de quatre pisos**: atributs, constructor, mètodes i prova.
2. El constructor **bateja els atributs** amb `this` quan hi ha xoc de noms; sense ell, els atributs viuen en `null` o en `0`.
3. Els mètodes **protegeixen les dades** (un `if` abans de retirar) i el `main` demostra que tot funciona.

> 🐛 **Vocabulari ràpid**
>
> | Terme | Idea general |
> |---|---|
> | Dissenyar una classe | Triar atributs, constructor, mètodes i prova |
> | Batejar | Inicialitzar els atributs en el constructor |
> | Protegir | Validar abans de modificar (no saldos negatius) |
> | `main` de prova | El programa que demostra que la classe funciona |
> | Iterar | Provar, trobar l'error, corregir i tornar a provar |

📚 [Tornar a l'índex de la unitat](/ApuntesProgramacion/ca/09-poo-clases-objetos) · **Anterior:** [07 · Sobrecàrrega i pas per valor](/ApuntesProgramacion/ca/09-poo-clases-objetos/07-sobrecarga-paso-valor) · **Següent:** [09 · Repàs interactiu](/ApuntesProgramacion/ca/09-poo-clases-objetos/09-repaso-interactivo)