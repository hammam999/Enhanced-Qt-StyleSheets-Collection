# 🤝 Contributing to Enhanced Qt StyleSheets

Thank you for your interest in contributing to the Enhanced Qt StyleSheets project! This guide will help you get started.

## 📋 Table of Contents

- [🚀 Getting Started](#-getting-started)
- [🎨 Adding New Themes](#-adding-new-themes)
- [🎯 Creating Icons](#-creating-icons)
- [🧪 Testing](#-testing)
- [📝 Documentation](#-documentation)
- [🔧 Development Setup](#-development-setup)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PyQt6 6.4+
- Basic knowledge of CSS/QSS
- SVG editing tools (optional)

### Development Setup
```bash
# Clone the repository
git clone https://github.com/GTRONICK/QSS.git
cd QSS

# Install dependencies
pip install -r requirements.txt

# Run the theme tester
python theme_tester.py
```

## 🎨 Adding New Themes

### 1. Create Theme File
```bash
# Copy an existing enhanced theme as base
cp MacOS-Enhanced.qss YourTheme-Enhanced.qss
```

### 2. Customize Colors
```css
/* Define your color palette */
:root {
    --primary-color: #your-primary;
    --secondary-color: #your-secondary;
    --background-color: #your-background;
    --text-color: #your-text;
}
```

### 3. Test Your Theme
- Use the theme tester application
- Test all widget states (normal, hover, pressed, disabled)
- Ensure accessibility compliance

## 🎯 Creating Icons

### Icon Guidelines
- **Size**: 16x16px viewBox
- **Format**: SVG
- **Colors**: Use `currentColor` for dynamic theming
- **Style**: Consistent with existing icons

### Example Icon
```svg
<svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
  <path d="M8 2L2 8l6 6 6-6-6-6z" fill="currentColor"/>
</svg>
```

## 🧪 Testing

### Manual Testing
1. Run theme tester application
2. Switch between themes
3. Test all widget interactions
4. Check different screen sizes

### Automated Testing
```bash
# Run theme validation
python scripts/validate_themes.py

# Check icon integrity
python scripts/check_icons.py
```

## 📝 Documentation

### Theme Documentation
Each new theme should include:
- Color palette description
- Design inspiration
- Best use cases
- Known limitations

### Code Comments
```css
/* Button styling for enhanced interaction */
QPushButton {
    /* Primary button color */
    background-color: #007AFF;
    
    /* Rounded corners for modern look */
    border-radius: 6px;
}
```

## 🔧 Development Workflow

### 1. Fork & Branch
```bash
git fork https://github.com/GTRONICK/QSS.git
git checkout -b feature/your-theme-name
```

### 2. Make Changes
- Follow existing code style
- Test thoroughly
- Update documentation

### 3. Submit Pull Request
- Clear description of changes
- Screenshots of new themes
- Test results

## 📊 Code Style

### QSS Formatting
```css
/* Good */
QPushButton {
    background-color: #007AFF;
    border: 1px solid #0056CC;
    border-radius: 6px;
    padding: 8px 16px;
}

/* Avoid */
QPushButton{background-color:#007AFF;border:1px solid #0056CC;}
```

### File Organization
```
themes/
├── enhanced/
│   ├── MacOS-Enhanced.qss
│   ├── MaterialDark-Enhanced.qss
│   └── Ubuntu-Enhanced.qss
├── original/
│   └── [original themes]
└── experimental/
    └── [work in progress]
```

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in theme headers
- Mentioned in release notes

## 📞 Getting Help

- 💬 **Discussions**: GitHub Discussions
- 🐛 **Issues**: GitHub Issues
- 📧 **Email**: [maintainer email]

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.
