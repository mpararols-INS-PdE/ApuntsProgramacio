---
title: Butlletí U11 — Inicial
description: Exercicis bàsics d'Herència, polimorfisme i interfícies
---

# 📝 Butlletí U11 — Inicial

> Sense solucions. Sense presses. Obre l'IDE, dona-li la mà a la primera superclasse i fes que `extends` deixi de semblar màgia. L'herència en Java és com la de veritat: de vegades et portes genial amb les subclasses, de vegades vols renegar de tot. Però ningú no neix sabent usar `super`.

---

## Exercici 1: Què imprimeix? — La família musical

```java
class Instrumentista {
    void tocar() { System.out.println("L'instrumentista toca un instrument"); }
}

class Guitarrista extends Instrumentista {
    void tocar() { System.out.println("El guitarrista toca la guitarra"); }
}

class Baixista extends Guitarrista {
    void tocar() { System.out.println("El baixista toca el baix"); }
}

public class Banda {
    public static void main(String[] args) {
        Baixista b = new Baixista();
        b.tocar();
    }
}
```

Què imprimeix? Per què?

---

## Exercici 2: Troba l'error — extends mal usat

```java
public class Animal {
    private String especie;

    public Animal(String especie) {
        this.especie = especie;
    }
}

public class Gos extends Animal {
    private String raça;

    public Gos(String raça) {
        this.raça = raça;
    }
}
```

Aquest codi **no compila**. Per què? Explica l'error i corregeix-lo.

---

## Exercici 3: Completa el codi — el gat que crida el seu pare

```java
public class Animal {
    public void ferSo() {
        System.out.println("Algun so genèric...");
    }
}

public class Gat extends Animal {
    @Override
    public void ferSo() {
        ________.ferSo();   // primer el del pare
        System.out.println("¡MIAU!");
    }
}
```

Quina paraula falta al buit perquè `Gat` primer executi el so d'`Animal` i després el seu "¡MIAU!"? Escriu a més un `main` que creï un `Gat` i crida a `ferSo()`.

---

## Exercici 4: Escriu aquest programa — l'herència de vehicles

Crea una jerarquia de 3 nivells usant `extends`:

- `Vehicle` (atribut: `String marca`)
- `Cotxe` (atribut: `int numPortes`)
- `Esportiu` (atribut: `int velocitatMaxima`)

Cada classe ha de tenir un constructor que rebi els seus atributs i usi `super`. En `main()`, crea un `Esportiu` de marca "Ferrari", 2 portes i 340 km/h. Imprimeix els seus atributs.

---

## Exercici 5: Què imprimeix? — Polimorfisme amb referències

```java
class X {
    void missatge() { System.out.println("X"); }
}

class Y extends X {
    void missatge() { System.out.println("Y"); }
}

class Z extends Y { }

public class Test {
    public static void main(String[] args) {
        X ref1 = new Y();
        X ref2 = new Z();
        Y ref3 = new Z();

        ref1.missatge();
        ref2.missatge();
        ref3.missatge();
    }
}
```

Què imprimeix cada crida? Per què el tipus de la referència no decideix res?

---

## Exercici 6: Escriu aquest programa — la granja polimòrfica

Crea una classe `Animal` amb mètode `ferSo()`. Crea `Vaca`, `Ovella` i `Gallina` que el sobreescriguin. En `main()`, crea un `ArrayList<Animal>`, fica una vaca, una ovella i una gallina, recorre'l amb un for-each cridant a `ferSo()`.

```java
// Eixida esperada:
// Muuuu
// Beeee
// Cloc cloc
```

---

## Exercici 7: Troba l'error — @Override que no ho és

```java
public class Animal {
    public void ferSo() {
        System.out.println("...");
    }
}

public class Peix extends Animal {
    @Override
    public void ferSo() { }   // ¿compila?

    @Override
    public void nedar() { }   // ¿compila?
}
```

Una de les dues línies amb `@Override` impedeix compilar. Quina i per què? Què t'avisa el compilador en l'instant en què escrius aquella línia?

---

## Exercici 8: Escriu aquest programa — el gos ben heretat

Parteix d'aquesta classe base:

```java
public class Animal {
    protected String nom;
    protected int edat;

    public Animal(String nom, int edat) {
        this.nom = nom;
        this.edat = edat;
    }
}
```

Escriu una classe `Gos extends Animal` amb:

- Constructor que usi `super(nom, edat)`.
- Mètode `lladrar()` que imprimeixi `nom + " diu: ¡Guau!"`.
- Un `main` que creï un `Gos("Firulais", 3)` i crida a `lladrar()`.

Respon: per què `Gos` pot usar `nom` i `edat` encara que no les declari?

---

## Exercici 9: Què imprimeix? — la cadena de constructors

```java
class Avi {
    public Avi() { System.out.println("Avi"); }
}

class Pare extends Avi {
    public Pare() { System.out.println("Pare"); }
}

class Fill extends Pare {
    public Fill() { System.out.println("Fill"); }
}

public class Test {
    public static void main(String[] args) {
        new Fill();
    }
}
```

Què imprimeix i per què en aquell ordre?