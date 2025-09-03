# 🔧 API Reference

## 📚 Theme Integration API

### Python (PyQt6)

#### Basic Theme Loading
```python
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QFile, QTextStream

def load_theme(app: QApplication, theme_path: str) -> bool:
    """
    Load a QSS theme file and apply it to the application.
    
    Args:
        app: QApplication instance
        theme_path: Path to the .qss file
        
    Returns:
        bool: True if theme loaded successfully
    """
    file = QFile(theme_path)
    if file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text):
        stream = QTextStream(file)
        stylesheet = stream.readAll()
        app.setStyleSheet(stylesheet)
        file.close()
        return True
    return False

# Usage
app = QApplication(sys.argv)
load_theme(app, "MacOS-Enhanced.qss")
```

#### Advanced Theme Manager
```python
class ThemeManager:
    """Advanced theme management with caching and validation."""
    
    def __init__(self, app: QApplication):
        self.app = app
        self.themes = {}
        self.current_theme = None
    
    def register_theme(self, name: str, path: str):
        """Register a theme for later use."""
        self.themes[name] = path
    
    def apply_theme(self, name: str) -> bool:
        """Apply a registered theme."""
        if name in self.themes:
            return load_theme(self.app, self.themes[name])
        return False
    
    def get_available_themes(self) -> list:
        """Get list of available theme names."""
        return list(self.themes.keys())

# Usage
theme_manager = ThemeManager(app)
theme_manager.register_theme("MacOS", "MacOS-Enhanced.qss")
theme_manager.register_theme("Material", "MaterialDark-Enhanced.qss")
theme_manager.apply_theme("MacOS")
```

### C++ (Qt6)

#### Basic Theme Loading
```cpp
#include <QApplication>
#include <QFile>
#include <QTextStream>

bool loadTheme(QApplication* app, const QString& themePath) {
    QFile file(themePath);
    if (file.open(QFile::ReadOnly | QFile::Text)) {
        QTextStream stream(&file);
        QString stylesheet = stream.readAll();
        app->setStyleSheet(stylesheet);
        file.close();
        return true;
    }
    return false;
}

// Usage
QApplication app(argc, argv);
loadTheme(&app, "MacOS-Enhanced.qss");
```

#### Theme Manager Class
```cpp
class ThemeManager : public QObject {
    Q_OBJECT
    
public:
    explicit ThemeManager(QApplication* app, QObject* parent = nullptr);
    
    void registerTheme(const QString& name, const QString& path);
    bool applyTheme(const QString& name);
    QStringList availableThemes() const;
    
signals:
    void themeChanged(const QString& themeName);
    
private:
    QApplication* m_app;
    QHash<QString, QString> m_themes;
    QString m_currentTheme;
};
```

## 🎨 Icon System API

### SVG Icon Loading
```python
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtGui import QPixmap, QPainter

def load_svg_icon(path: str, size: tuple = (16, 16)) -> QPixmap:
    """
    Load SVG icon and convert to QPixmap.
    
    Args:
        path: Path to SVG file
        size: Desired size (width, height)
        
    Returns:
        QPixmap: Rendered icon
    """
    renderer = QSvgRenderer(path)
    pixmap = QPixmap(*size)
    pixmap.fill(Qt.GlobalColor.transparent)
    
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()
    
    return pixmap

# Usage
icon = load_svg_icon("icons/svg/arrow-up.svg", (24, 24))
button.setIcon(QIcon(icon))
```

### Dynamic Icon Coloring
```python
def colorize_svg_icon(svg_path: str, color: str) -> str:
    """
    Replace currentColor in SVG with specified color.
    
    Args:
        svg_path: Path to SVG file
        color: Hex color code
        
    Returns:
        str: Modified SVG content
    """
    with open(svg_path, 'r') as file:
        svg_content = file.read()
    
    return svg_content.replace('currentColor', color)
```

## 🔧 Widget Customization API

### Custom Widget Styling
```python
def apply_widget_style(widget, style_dict: dict):
    """
    Apply custom styles to a widget.
    
    Args:
        widget: Qt widget instance
        style_dict: Dictionary of CSS properties
    """
    styles = []
    for property, value in style_dict.items():
        styles.append(f"{property}: {value}")
    
    stylesheet = f"{widget.__class__.__name__} {{ {'; '.join(styles)} }}"
    widget.setStyleSheet(stylesheet)

# Usage
apply_widget_style(button, {
    'background-color': '#007AFF',
    'border-radius': '6px',
    'padding': '8px 16px'
})
```

### Theme Property Access
```python
def get_theme_property(theme_path: str, selector: str, property: str) -> str:
    """
    Extract specific property value from QSS theme.
    
    Args:
        theme_path: Path to QSS file
        selector: CSS selector
        property: CSS property name
        
    Returns:
        str: Property value or empty string
    """
    import re
    
    with open(theme_path, 'r') as file:
        content = file.read()
    
    # Simple regex-based extraction
    pattern = rf"{re.escape(selector)}\s*\{{[^}}]*{re.escape(property)}\s*:\s*([^;}}]+)"
    match = re.search(pattern, content, re.IGNORECASE)
    
    return match.group(1).strip() if match else ""

# Usage
primary_color = get_theme_property("MacOS-Enhanced.qss", "QPushButton", "background-color")
```

## 📊 Theme Validation API

### Theme Validator
```python
class ThemeValidator:
    """Validate QSS theme files for completeness and correctness."""
    
    REQUIRED_SELECTORS = [
        'QPushButton', 'QLineEdit', 'QComboBox', 
        'QCheckBox', 'QRadioButton', 'QSlider'
    ]
    
    def validate_theme(self, theme_path: str) -> dict:
        """
        Validate a theme file.
        
        Returns:
            dict: Validation results with errors and warnings
        """
        results = {
            'valid': True,
            'errors': [],
            'warnings': [],
            'coverage': 0
        }
        
        try:
            with open(theme_path, 'r') as file:
                content = file.read()
            
            # Check for required selectors
            found_selectors = 0
            for selector in self.REQUIRED_SELECTORS:
                if selector in content:
                    found_selectors += 1
                else:
                    results['warnings'].append(f"Missing selector: {selector}")
            
            results['coverage'] = (found_selectors / len(self.REQUIRED_SELECTORS)) * 100
            
        except Exception as e:
            results['valid'] = False
            results['errors'].append(str(e))
        
        return results

# Usage
validator = ThemeValidator()
result = validator.validate_theme("MyTheme.qss")
print(f"Theme coverage: {result['coverage']:.1f}%")
```

## 🎯 Event Handling

### Theme Change Events
```python
from PyQt6.QtCore import QObject, pyqtSignal

class ThemeEventHandler(QObject):
    """Handle theme-related events."""
    
    theme_changed = pyqtSignal(str)  # theme name
    theme_loaded = pyqtSignal(bool)  # success status
    
    def __init__(self, theme_manager):
        super().__init__()
        self.theme_manager = theme_manager
        
    def on_theme_change(self, theme_name: str):
        """Handle theme change request."""
        success = self.theme_manager.apply_theme(theme_name)
        self.theme_loaded.emit(success)
        if success:
            self.theme_changed.emit(theme_name)

# Usage
handler = ThemeEventHandler(theme_manager)
handler.theme_changed.connect(lambda name: print(f"Theme changed to: {name}"))
```

## 📈 Performance Optimization

### Theme Caching
```python
from functools import lru_cache

@lru_cache(maxsize=10)
def load_cached_theme(theme_path: str) -> str:
    """Load and cache theme content."""
    with open(theme_path, 'r') as file:
        return file.read()

def apply_cached_theme(app: QApplication, theme_path: str):
    """Apply theme using cached content."""
    stylesheet = load_cached_theme(theme_path)
    app.setStyleSheet(stylesheet)
```

## 🔍 Debugging Utilities

### Theme Inspector
```python
def inspect_theme(theme_path: str) -> dict:
    """
    Analyze theme file and return statistics.
    
    Returns:
        dict: Theme analysis results
    """
    with open(theme_path, 'r') as file:
        content = file.read()
    
    import re
    
    selectors = re.findall(r'([A-Za-z][A-Za-z0-9]*(?:::[a-z-]+)?)\s*\{', content)
    properties = re.findall(r'([a-z-]+)\s*:', content)
    
    return {
        'file_size': len(content),
        'line_count': content.count('\n'),
        'selector_count': len(set(selectors)),
        'property_count': len(set(properties)),
        'selectors': list(set(selectors)),
        'properties': list(set(properties))
    }

# Usage
stats = inspect_theme("MacOS-Enhanced.qss")
print(f"Theme has {stats['selector_count']} unique selectors")
```
