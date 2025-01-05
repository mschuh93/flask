# Simple Flask App

## Beschreibung

Dies ist eine einfache Flask-Webanwendung, mit der Dateien hochgeladen und angezeigt werden können. Hochgeladene Dateien werden im Verzeichnis `uploads/` gespeichert und können über die Benutzeroberfläche abgerufen werden.

---

## Voraussetzungen

1. **Python 3.7 oder höher**
2. **Installierte Abhängigkeiten**:
   - Flask

### Installation der Abhängigkeiten

Führe folgenden Befehl aus, um Flask zu installieren:

```bash
pip install flask
```

Alternativ: Installiere alle Abhängigkeiten aus der `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Nutzung

### App starten

1. Navigiere zum Projektordner:

   ```bash
   cd /path/to/your/project
   ```

2. Starte die Flask-App:

   ```bash
   python app.py
   ```

3. Öffne einen Browser und gehe zu:

   ```
   http://127.0.0.1:5000
   ```

### Funktionen
1. **Datei hochladen**:

   - Gehe zur Startseite der App.
   - Wähle eine Datei aus und lade sie hoch.
   - Die Datei wird im Ordner `uploads/` gespeichert.

2. **Hochgeladene Datei anzeigen**:

   - Nach dem Hochladen wirst du zur Seite weitergeleitet, die den Dateinamen und weitere Informationen anzeigt.

---

## Projektstruktur

```
project/
├── flask_test.py         # Haupt-Flask-App
├── templates/            # HTML-Vorlagen
│   ├── index.html        # Startseite
│   └── uploaded.html     # Ergebnisanzeige
├── uploads/              # Verzeichnis für hochgeladene Dateien
└── requirements.txt      # Abhängigkeiten
```

---

## Nächste Schritte

1. **Styling hinzufügen**:

   - Verwende CSS, um die Benutzeroberfläche attraktiver zu gestalten.

2. **Erweiterungen**:

   - Unterstütze mehrere Dateitypen.
   - Füge eine Datenbank hinzu, um Informationen zu hochgeladenen Dateien zu speichern.

---

## Beiträge

Pull Requests und Vorschläge zur Verbesserung sind willkommen. Für Fragen oder Fehlerberichte erstelle bitte ein Issue im Repository.


