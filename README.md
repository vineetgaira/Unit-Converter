<div align="center">

# 📐 Unit Converter CLI

### *Convert anything, from anywhere — right in your terminal.*

```
   ┌─────────┐        ┌─────────┐        ┌─────────┐
   │  1.00 m │  ───▶  │ 3.28 ft │  ───▶  │ 39.37 in│
   └─────────┘        └─────────┘        └─────────┘
        📏  Length · ⚖️ Weight · ⏱️ Time · 🚀 Speed · 🗺️ Area · 🧪 Volume · 🌡️ Temperature
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Colorama](https://img.shields.io/badge/Colorama-Enabled-FFD43B?style=for-the-badge)
![CLI](https://img.shields.io/badge/Interface-Terminal-000000?style=for-the-badge&logo=windowsterminal&logoColor=white)
![Status](https://img.shields.io/badge/Status-Practice%20Project-orange?style=for-the-badge)

</div>

---

## ✨ Overview

**Unit Converter CLI** is a colorful, menu-driven terminal application that converts values across **7 measurement categories** — no internet, no clutter, just fast and accurate conversions powered by pure Python.

Every prompt, menu, and result is styled with `colorama` for a clean, readable terminal experience.

## 🎨 Preview

```
...Welcome to unit converter...
Choose category:
1 : Length
2 : Weight
3 : Time
4 : Speed
5 : Area
6 : Volume
7 : Temperature
Choose your category :1

..Unit Options..
1 : Meter(m)
2 : Kilometer(km)
3 : Centimeter(cm)
4 : Millimeter(mm)
5 : Inch
6 : Foot
7 : Yard
8 : Mile
From unit :1
To unit :6
Enter a value :10

10.0 Meter: 32.80840 Foot
Convert one more value(y/n):
```

## 🧭 Supported Categories

<div align="center">

| # | Category | Units Supported |
|:-:|:---|:---|
| 📏 | **Length** | Meter · Kilometer · Centimeter · Millimeter · Inch · Foot · Yard · Mile |
| ⚖️ | **Weight** | Gram · Kilogram · Pound · Ounce · Ton |
| ⏱️ | **Time** | Second · Minute · Hour · Day · Week |
| 🚀 | **Speed** | m/s · Km/h · mph |
| 🗺️ | **Area** | Square Meter · Square Kilometer · Hectare · Acre |
| 🧪 | **Volume** | Milliliter · Liter · Cubic Meter · Gallon |
| 🌡️ | **Temperature** | Celsius (°C) · Fahrenheit (°F) · Kelvin (K) |

</div>

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- `colorama` package

### Installation

```bash
git clone https://github.com/vineetgaira/Unit-Converter.git
cd Unit-Converter
pip install colorama
```

### Run it

```bash
python main.py
```

## 🕹️ How to Use

1. **Pick a category** — Length, Weight, Time, Speed, Area, Volume, or Temperature.
2. **Choose your "from" unit** and **"to" unit** from the category's menu.
3. **Enter a value** to convert.
4. Get an instantly formatted, color-coded result.
5. Choose `y` to convert again, or `n` to exit.

## 🗂️ Project Structure

```
Unit-Converter/
├── main.py             # Entry point — handles input flow & conversion logic
├── constants.py         # Conversion factors, unit names & category mappings
├── menu_functions.py     # Menu display functions for each category
├── requirements.txt       # Project dependencies
├── src/                    # Reserved for future modularization
├── tests/                   # Reserved for future test coverage
└── docs/                     # Reserved for future documentation
```

## 🧠 How Conversions Work

Most categories convert through a **common base unit**:

```
value_in_from_unit × factor(from_unit) = value_in_base_unit
value_in_base_unit ÷ factor(to_unit)   = value_in_to_unit
```

**Temperature** is the exception — since Celsius, Fahrenheit, and Kelvin don't share a simple multiplicative relationship, each conversion pair uses its own dedicated formula (e.g. `°F = °C × 9/5 + 32`).

## 🛠️ Built With

- 🐍 **Python** — core application logic
- 🎨 **Colorama** — cross-platform colored terminal text

## 📈 Roadmap

- [ ] Move conversion logic into `src/` for cleaner structure
- [ ] Add unit tests under `tests/`
- [ ] Support additional categories (data storage, energy, pressure)
- [ ] Add a `--value --from --to` CLI argument mode for quick one-liners
- [ ] Package as an installable CLI tool (`pip install`-able)

## ⚠️ Disclaimer

This is a **practice project** built for learning Python fundamentals — input validation, dictionaries, modular code, and CLI UX. It's not intended for production or scientific-grade precision use.

## 📄 License

Open source — free to use, learn from, and build upon.

---

<div align="center">

Made with 🐍 Python — *measure twice, convert once.* 📐

</div>
