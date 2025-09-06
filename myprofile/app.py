from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def profile():
    # Sample profile data
    profile_data = {
        'name': 'John Doe',
        'title': 'Software Developer',
        'email': 'john.doe@example.com',
        'phone': '+1 (555) 123-4567',
        'location': 'San Francisco, CA',
        'about': 'Passionate software developer with 5+ years of experience in full-stack development. Specializes in Python, JavaScript, and modern web technologies.',
        'skills': ['Python', 'JavaScript', 'React', 'Flask', 'HTML/CSS', 'SQL', 'Git'],
        'experience': [
            {
                'company': 'Tech Corp',
                'position': 'Senior Developer',
                'duration': '2021 - Present',
                'description': 'Led development of web applications using Python and React'
            },
            {
                'company': 'StartupXYZ',
                'position': 'Full Stack Developer',
                'duration': '2019 - 2021',
                'description': 'Developed and maintained multiple client applications'
            }
        ]
    }
    return render_template('profile.html', profile=profile_data)

if __name__ == '__main__':
    app.run(debug=True, port=5002)