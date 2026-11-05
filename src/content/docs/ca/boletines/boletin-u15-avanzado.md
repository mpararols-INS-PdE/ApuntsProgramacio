---
title: "Butlletí U15 — Avançat"
description: "Exercicis de dificultat progressiva per a exprimir el JDBC: PreparedStatement, DAO, transaccions i més"
---

# 📝 Butlletí U15 — Avançat

> Dificultat progressiva. ⭐ per a escalfar, ⭐⭐ per a pensar, ⭐⭐⭐ per a concursar. Cada exercici inclou una pista (resisteix a mirar-la).

---

## ⭐ Exercici 1: Connexió des de fitxer de propietats

Crea un fitxer `db.properties` amb les dades de connexió:

```properties
url=jdbc:sqlite:instituto.db
```

Escriu un programa que llegeixi aquest fitxer usant la classe `Properties` i estableixi la connexió. Si el fitxer no existeix o falta la propietat `url`, mostra un missatge d'error clar.

**Pista:** carrega el fitxer amb `props.load(Files.newInputStream(Path.of("db.properties")))` i usa `props.getProperty("url")`. `load` llança una `IOException` (la vas veure a la U14 amb els fitxers) a més de la `SQLException`.

---

## ⭐ Exercici 2: INSERT amb clau autogenerada

Insereix un nou alumne a la taula `alumnos` i **recupera l'ID** que la base de dades li ha assignat automàticament (és un `AUTOINCREMENT`). Usa `PreparedStatement` amb `Statement.RETURN_GENERATED_KEYS` i el mètode `getGeneratedKeys()`.

**Pista:**

```java
PreparedStatement pstmt = con.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
pstmt.executeUpdate();
ResultSet claus = pstmt.getGeneratedKeys();
if (claus.next()) {
    int id = claus.getInt(1);
}
```

El `getGeneratedKeys()` torna un `ResultSet` amb la clau que acaba de generar la base de dades. Es llegeix amb `next()` i `getInt(1)`.

---

## ⭐ Exercici 3: UPDATE condicional

Actualitza el curs de tots els alumnes que tinguin una edat superior a un valor donat. Per exemple:

```
Quina edat mínima? 25
Quin nou curs? DAM2
```

Tots els alumnes majors de 25 anys passen al curs «DAM2». Mostra quantes files s'han actualitzat.

**Pista:** `UPDATE alumnos SET curso = ? WHERE edad > ?` amb `setInt` i `setString`. `executeUpdate()` et torna el nombre de files afectades: és el teu millor amic per a confirmar que alguna cosa ha canviat.

---

## ⭐⭐ Exercici 4: INNER JOIN amb PreparedStatement

Donada una taula `matriculas` amb `id_alumno`, `asignatura`, `nota`, escriu un programa que rebi un nom d'alumne i mostri totes les seves assignatures i notes. Usa un `INNER JOIN` entre `alumnos` i `matriculas`.

Exemple de sortida:

```
Alumne: Ana García
  Matemàtiques: 8.5
  Programació: 9.0
  Bases de Dades: 7.5
```

**Pista:** el `?` va a la part del nom: `SELECT a.nombre, m.asignatura, m.nota FROM alumnos a INNER JOIN matriculas m ON m.id_alumno = a.id WHERE a.nombre = ?`. El `JOIN` relaciona les dues taules en una sola consulta: ni un bucle, ni consultes dins de bucles.

---

## ⭐⭐ Exercici 5: Cerca amb LIKE

Implementa una cerca d'alumnes per nom usant `LIKE` i `PreparedStatement`. L'usuari escriu una part del nom i es mostren tots els que coincideixin. Si no hi ha resultats, mostra «Sense resultats».

**Pista:** `SELECT * FROM alumnos WHERE nombre LIKE ?` amb `pstmt.setString(1, "%" + text + "%")`. Els `%` són comodins i van dins del **valor**, no en l'SQL. El `%text%` busca el text en qualsevol posició.

---

## ⭐⭐ Exercici 6: Dates en JDBC

Afegeix una columna `fecha_nacimiento DATE` a la taula `alumnos` (assumeix que ja existeix). Crea un programa que:

1. Demani nom, edat, curs i data de naixement (format `YYYY-MM-DD`).
2. Insereixi l'alumne usant `PreparedStatement` amb `java.sql.Date.valueOf()`.
3. Lliste tots els alumnes mostrant també la seva data de naixement.

**Pista:** `Date.valueOf("2000-03-15")` converteix el text en `java.sql.Date` (alerta: és `java.sql.Date`, no `java.util.Date`!). Per a llegir-la, `rs.getDate("fecha_nacimiento")`. Recorda comprovar el valor que torna `executeUpdate()`.

---

## ⭐⭐ Exercici 7: Batch INSERT — 100 alumnes de prova

Crea un programa que insereixi **100 alumnes de prova** a la taula `alumnos` usant lots (batch). Els noms poden ser genèrics: `Alumno1`, `Alumno2`, etc.

Usa `addBatch()` i `executeBatch()` de `PreparedStatement`. Mesura el temps que tarda amb `System.currentTimeMillis()`.

**Pista:** al bucle, fas `addBatch()` a cada vegada i un sol `executeBatch()` al final (o cada 50). Per a mesurar: `long inicio = System.currentTimeMillis();` ... `long fin = System.currentTimeMillis();` i restes. Compara mentalment amb 100 `executeUpdate()` solts.

---

## ⭐⭐⭐ Exercici 8: El patró DAO

Implementa el patró **Data Access Object (DAO)** per a la taula `alumnos`. Crea les següents classes:

1. `Alumno` — classe model amb `id`, `nombre`, `edad`, `curso`.
2. `AlumnoDAO` — interfície amb mètodes: `listar()`, `buscarPorId(int id)`, `buscarPorNombre(String nombre)`, `insertar(Alumno a)`, `actualizar(Alumno a)`, `eliminar(int id)`.
3. `AlumnoDAOImpl` — implementació concreta amb JDBC i SQLite.
4. `Main` — programa amb menú que usi el DAO.

**Pista:** la URL (`jdbc:sqlite:instituto.db`) és una constant privada de la implementació. Cada mètode obre la seva pròpia connexió amb `try-with-resources`. El `Main` només parla amb la interfície `AlumnoDAO`; l'SQL no li importa.

---

## ⭐⭐⭐ Exercici 9: Transacció bancària atòmica

Simula una transferència entre dos comptes en una taula `cuentas(id, titular, saldo)`. La transferència ha de ser **atòmica**: treu 100 € d'un compte, posa'ls en l'altre, i si falla qualsevol pas, fes `rollback()` perquè el sistema no quedi a mitges.

Exemple de sortida:

```
Saldo abans: Ana 500, Luis 300
Transferència OK
Saldo després: Ana 400, Luis 400
```

**Pista:** `con.setAutoCommit(false)`, després les dues operacions amb `PreparedStatement`, i al final `con.commit()`. El `rollback()` va al `catch (SQLException e)` intern. Prova a forçar la fallada (per exemple, un compte inexistent) i comprova que el saldo d'Ana no canvia.