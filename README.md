# Haar & Härz - Website

Eine professionelle Website für den Coiffeur-Salon "Haar & Härz".

## Setup

### 1. Virtuelle Umgebung aktivieren
```bash
source .venv/bin/activate  # Auf macOS/Linux
```

### 2. Django Server starten
```bash
python manage.py runserver
```

Die Website ist dann unter `http://127.0.0.1:8000/` erreichbar.

## Benötigte Bilder

Um die Website vollständig zu machen, müssen folgende Bilder hinzugefügt werden:

### Logo
- **Pfad:** `website/static/images/logo.png`
- **Beschreibung:** Das Logo "HAAR & HÄRZ" (idealerweise auf weißem Hintergrund)
- **Empfohlene Größe:** 400x400 Pixel (PNG mit transparentem Hintergrund)

### Hero-Hintergrundbild
- **Pfad:** `website/static/images/hero-background.png`
- **Beschreibung:** Ein professionelles Bild vom Salon oder einer Friseurin bei der Arbeit
- **Empfohlene Größe:** Mindestens 1920x1080 Pixel (Landscape Format)

### Service-Bilder

#### Schnitt
- **Pfad:** `website/static/images/service-schnitt.jpg`
- **Beschreibung:** Bild von Schere und Kamm auf Holztisch
- **Empfohlene Größe:** 800x600 Pixel (Landscape Format)

#### Farbe
- **Pfad:** `website/static/images/service-farbe.jpg`
- **Beschreibung:** Bild von Farbschale und Pinsel
- **Empfohlene Größe:** 800x600 Pixel (Landscape Format)

#### Dauerwelle
- **Pfad:** `website/static/images/service-dauerwelle.jpg`
- **Beschreibung:** Bild von Lockenwicklern und Styling-Tools
- **Empfohlene Größe:** 800x600 Pixel (Landscape Format)

### Preise-Seite Bilder

#### Kinder
- **Pfad:** `website/static/images/price-kinder.png`
- **Beschreibung:** Bild eines Jungen
- **Status:** ✅ Vorhanden

#### Frauen
- **Pfad:** `website/static/images/price-frauen.png`
- **Beschreibung:** Bild einer Frau
- **Status:** ✅ Vorhanden

#### Männer
- **Pfad:** `website/static/images/price-männer.png`
- **Beschreibung:** Bild eines Mannes
- **Status:** ✅ Vorhanden

#### Bewohner Senevita
- **Pfad:** `website/static/images/price-senevita.png`
- **Beschreibung:** Bild einer älteren Person
- **Status:** ✅ Vorhanden

## Projektstruktur

```
HaarundHaerz/
├── HaarundHaerz/          # Django Projekt-Einstellungen
│   ├── settings.py        # Einstellungen
│   ├── urls.py            # Haupt-URL-Konfiguration
│   └── ...
├── website/               # Haupt-App
│   ├── static/            # Static Files
│   │   ├── css/           # CSS-Dateien
│   │   │   └── style.css
│   │   ├── js/            # JavaScript-Dateien
│   │   │   └── main.js
│   │   └── images/        # Bilder (Logo & Hero-Hintergrund)
│   ├── templates/         # HTML Templates
│   │   └── website/
│   │       └── index.html
│   ├── views.py           # Views
│   └── urls.py            # URL-Konfiguration
└── manage.py              # Django Management Script
```

## Features

- **Responsive Design:** Die Website passt sich automatisch an verschiedene Bildschirmgrößen an
- **Moderne Navigation:** Klare und übersichtliche Navigation mit 6 Hauptbereichen
- **Hero Section:** Beeindruckende Willkommens-Sektion mit Hintergrundbild
- **Dienstleistungen:** Drei Service-Karten (Schnitt, Farbe, Dauerwelle) mit Bildern und Beschreibungen
- **Über-Mich Sektion:** Persönliche Vorstellung von Jasmin Feller
- **Preise-Seite:** Vollständige Preisliste mit 4 Kategorien (Kinder, Frauen, Männer, Bewohner Senevita)
- **Öffnungszeiten-Seite:** Übersichtliche Tabelle mit allen Öffnungszeiten (schwarze Tabelle auf türkisem Hintergrund)
- **Kontakt-Seite:** Professionelles Kontaktformular mit Name, E-Mail und Nachricht-Feldern
- **SumUp Booking-Seite:** Informationsseite mit 2 Sektionen (Mehrere Leistungen buchen + Termin-Buchung in 2 Schritten)
- **Footer:** Kontaktinformationen, Standort und Info-Bereich
- **Smooth Scrolling:** Sanftes Scrollen zu verschiedenen Bereichen der Seite
- **Professional Styling:** Modernes, professionelles Design mit Hauptfarbe RGB(59, 134, 139)

## Nächste Schritte

1. **Bilder Status:**
   - ✅ Logo: `website/static/images/logo.png`
   - ✅ Hero-Hintergrundbild: `website/static/images/hero-background.png`
   - ✅ Service-Bilder: `service-schnitt.jpg`, `service-farbe.jpg`, `service-dauerwelle.jpg`
   - ✅ Preise-Bilder: `price-kinder.png`, `price-frauen.png`, `price-männer.png`, `price-senevita.png`

2. **Weitere Features** (optional):
   - Kontaktformular Backend-Integration (E-Mail-Versand)
   - Echte SumUp Booking Integration mit API
   - Google Maps für Standort
   - WhatsApp Button
   - Cookie Banner / Datenschutz

3. **SEO & Performance:**
   - Meta-Tags hinzufügen
   - Bilder optimieren
   - SSL-Zertifikat für Produktion

## Kontakt

Bei Fragen oder Problemen:
- Telefon: 079 449 00 81
- E-Mail: jasmin@haarundhaerz.com
