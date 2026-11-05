---
title: "Butlletí U15 — Inicial"
description: "Exercicis bàsics d'APIs web: HttpServer, servir HTML, paràmetres GET i primers JSON"
---

# 📝 Butlletí U15 — Inicial

> Sense solucions. Sense presses. Obre l'IDE, crea el teu primer `HttpServer` i fes que el navegador et parli de tu a tu. Promet que cap bit sortirà ferit. Comença suaument, que la web mossega a a poc a poc.

---

## Exercici 1: Escriu aquest programa — Hola, món web

Crea un servidor HTTP al port 8080 amb una ruta `/` que torni el text `Hola, mundo web!`. Obre `http://localhost:8080` en el teu navegador i comprova que ho veus.

Pista: `HttpServer.create(new InetSocketAddress(8080), 0)`, després `createContext("/", ...)` i `sendResponseHeaders(200, ...)`. No oblidis tancar el cos de la resposta.

---

## Exercici 2: Escriu aquest programa — servidor de l'hora

Afegeix al teu servidor una ruta `/hora` que torni l'hora actual en text pla amb format `HH:mm:ss`.

Cada vegada que recarregues el navegador, l'hora canvia. Màgia negra amb `LocalTime.now()`.

```java
// Pista:
String hora = java.time.LocalTime.now().format(
    java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss")
);
```

---

## Exercici 3: Escriu aquest programa — pàgina que diu el teu nom

Afegeix una ruta `/saludo?nombre=Pepe` que torni una pàgina HTML amb `<h1>¡Hola, Pepe!</h1>`.

Si no es passa nom, que digui `¡Hola, desconocido!`.

Pista: `e.getRequestURI().getQuery()` et dona `nombre=Pepe`. Divideix per `=` i llest.

---

## Exercici 4: Escriu aquest programa — comptador de visites global

Usa una variable `static int visites = 0`. Cada vegada que algú visita `/`, incrementa el comptador i mostra:

```
Eres el visitante número 47
```

Què passa si dues persones recarreguen alhora? (spoiler: problemes — però de moment no et preocupes).

---

## Exercici 5: Escriu aquest programa — generador d'excuses per a lliuraments tardans

Crea una ruta `/excusa` que torni una excusa generada aleatòriament combinant elements de tres arrays:

```java
String[] subjectes = {"El meu gos", "GitHub", "El plugin d'IntelliJ", "La connexió"};
String[] verbs     = {"es va menjar", "va esborrar", "va corrompre", "va perdre"};
String[] objectes  = {"l'examen", "la pràctica", "els apunts", "la meua paciència"};
```

Exemple: *"GitHub va esborrar la pràctica"*. Torna-ho en HTML amb bona lletra.

---

## Exercici 6: Escriu aquest programa — taula de multiplicar personalitzada

Ruta `/tabla?num=7` que generi una taula HTML completa amb la taula de multiplicar del 7 (del 7×1 al 7×10).

Si no es passa número, usa el 5 per defecte. Formata la taula amb `border=1` i colors alterns en les files.

---

## Exercici 7: Escriu aquest programa — convertidor d'euros a pessetes (sí, pessetes)

Ruta `/conversor?euros=50` que torni HTML amb el resultat: "50 euros son 8319.3 pesetas".

1 € = 166.386 pts. Mostra dos decimals.

Pista: `String.format("%.2f", valor)` per als decimals. Sí, pessetes. Si ets jove, pregunta-li a un vell què era això.

---

## Exercici 8: Escriu aquest programa — pàgina d'estat del servidor

Ruta `/estado` que torni un JSON amb aquesta pinta:

```json
{
    "servidor": "ok",
    "hora": "14:30:01",
    "visites": 47,
    "versio": "1.0",
    "autor": "El teu nom ací"
}
```

No oblidis el `Content-Type: application/json` o el navegador es tornarà tonto.

---

## Exercici 9: Troba l'error — el Content-Type oblidat

Un company t'ensenya aquest handler i jura que torna JSON:

```java
server.createContext("/api/frase", intercambio -> {
    String json = """
        {"frase": "El código limpio es como un buen chiste"}
        """;
    intercambio.sendResponseHeaders(200, json.getBytes().length);
    intercambio.getResponseBody().write(json.getBytes());
    intercambio.getResponseBody().close();
});
```

El navegador mostra el text, però el `fetch` que el consumeix es queixa: `r.json()` peta. Què falta i per què és tan important?