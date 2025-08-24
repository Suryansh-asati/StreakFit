***This project is till in it's early stage of development, many features are still yet to come.***<br><br>
 
 ## StreakFit 🏋️‍♂️

**Your Personal Fitness Companion**

StreakFit is a modern, responsive web application designed to help users track their fitness journey, maintain workout streaks, and achieve their health goals. Built with clean HTML, CSS, and JavaScript, it offers an intuitive dashboard experience for fitness enthusiasts of all levels.

**Demo Link:** **https://streakfit.vercel.app/**

## 🌟 Features 

### 🎯 Core Functionality
- **Fitness Tracking**: Monitor your workouts and progress over time
- **Streak Management**: Keep track of your workout streaks and stay motivated
- **Goal Setting**: Set and achieve personalized fitness goals
- **Progress Dashboard**: Visualize your fitness journey with an intuitive interface

### 🎨 User Experience
- **Responsive Design**: Seamlessly works across desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional interface with smooth animations
- **Mobile-First Navigation**: Collapsible burger menu for mobile users
- **Smooth Scrolling**: Enhanced user experience with smooth page navigation

### 📱 Interface Elements
- **Interactive Navigation**: Fixed navbar with smooth scroll-to-section functionality
- **Contact Form**: Built-in contact form for user feedback and support
- **Hero Section**: Engaging landing area with clear call-to-action
- **About Section**: Information about the platform and its benefits

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Basic web server (optional, for local development)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/streakfit.git
   cd streakfit
   ```

2. **Open locally:**
   - Simply open `index.html` in your web browser, OR
   - Use a local development server:

   **Using Python:**
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   ```

   **Using Node.js (with http-server):**
   ```bash
   npm install -g http-server
   http-server
   ```

   **Using Live Server (VS Code extension):**
   - Install the Live Server extension
   - Right-click on `index.html` and select "Open with Live Server"

3. **Access the application:**
   - Direct file access: Open `index.html` in your browser
   - Local server: Navigate to `http://localhost:8000`

## 📁 Project Structure

```
StreakFit/
│
├── index.html              # Main HTML file
├── about.html              # About page
├── README.md               # Project documentation
├── Contribute.md           # Contribution guide
│
└── assets/
    ├── logo.png            # StreakFit logo/favicon
    ├── main.css            # Main stylesheet
    ├── loader.css          # Preloader styling
    └── script.js           # JavaScript functionality
```

## 🛠️ Technical Details

### Technologies Used
- **HTML5**: Semantic markup structure
- **CSS3**: Modern styling with CSS custom properties (variables)
- **Vanilla JavaScript**: Interactive functionality without external dependencies

### Key Features Implementation
- **CSS Custom Properties**: Consistent design system with brand colors and typography
- **Responsive Grid/Flexbox**: Mobile-first responsive design
- **Smooth Scrolling API**: Enhanced navigation experience
- **Event Delegation**: Efficient event handling for interactive elements

### Browser Compatibility
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ⚠️ Internet Explorer (limited support)

## 🎨 Design System

### Color Palette
```css
--primary-color: #2f6a87      /* Fresh Green for buttons, highlights */
--secondary-color: #9a5131    /* Vibrant Orange for accents */
--accent-color: #ea6c36       /* Bright Orange for highlights */
--background-light: #e7e7e7   /* Soft light gray backgrounds */
--success-color: #2ecc71      /* Success states and streaks */
--error-color: #e74c3c        /* Error states */
```

### Typography
- **Primary Font**: SF Pro Display (system font)
- **Fallback**: Geist, sans-serif
- **Base Size**: 16px with responsive scaling

## 🔧 Customization

### Modifying Colors
Edit the CSS custom properties in `assets/main.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    /* ... other variables */
}
```

### Adding New Sections
1. Add the section to `index.html`
2. Add corresponding styles to `assets/main.css`
3. Update navigation links in the navbar
4. Add smooth scrolling functionality in `assets/script.js`

### Contact Form Configuration
The contact form uses Formspree. To activate:
1. Sign up at [Formspree.io](https://formspree.io)
2. Replace `your-form-id` in the form action with your actual form ID
3. Update the contact email address

## 📱 Responsive Breakpoints

- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact & Support

- **Email**: [Contact Form](mailto:blahblah@gmail.com)
- **Issues**: GitHub Issues tab
- **Updates**: Follow the repository for updates

## 🚀 Future Enhancements

- [ ] User authentication and profiles
- [ ] Workout plan templates
- [ ] Progress charts and analytics
- [ ] Social sharing features
- [ ] Mobile app integration
- [ ] Wearable device connectivity

---

**Built with ❤️ for the fitness community**

*Start your fitness journey today with StreakFit!*

