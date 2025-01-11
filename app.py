from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Uniq Evenz</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 0; color: #333; line-height: 1.6; }
            header { background-color: #FF5733; color: white; padding: 20px; text-align: center; }
            nav { background: #C70039; padding: 10px; text-align: center; }
            nav a { color: white; text-decoration: none; margin: 0 10px; font-weight: bold; }
            nav a:hover { text-decoration: underline; }
            .hero { background: url('https://via.placeholder.com/1200x400') no-repeat center center/cover; height: 300px; text-align: center; color: white; padding: 50px; }
            section { padding: 20px; }
            footer { background: #900C3F; color: white; text-align: center; padding: 10px; }
        </style>
    </head>
    <body>
        <header>
            <h1>Uniq Evenz</h1>
        </header>
        <nav>
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#portfolio">Portfolio</a>
            <a href="#contact">Contact</a>
        </nav>
        <div class="hero">
            <h1>Welcome to Bezalel Events</h1>
        </div>
        <section id="about">
            <h2>About Us</h2>
            <p>Founded in 2021, Uniq Evenz offers exceptional event management and construction services.</p>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <p>Wedding planning, catering, photography, and more.</p>
        </section>
        <section id="portfolio">
            <h2>Portfolio</h2>
            <p>View our projects and see why clients trust us!</p>
        </section>
        <section id="contact">
            <h2>Contact</h2>
            <p>Phone: +91 78100 03105</p>
            <p>Email: uniqevenz@gmail.com</p>
        </section>
        <footer>
            <p>&copy; 2025 Uniq Evenz. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
