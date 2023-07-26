```python
import three
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/3d_simulation')
def create_3d_simulation():
    visualization_data = get_visualization_data()  # Assuming this function fetches the required data for visualization
    return render_template('3d_simulation.html', data=visualization_data)

def get_visualization_data():
    # Fetch the data from the processed_data variable
    # This function needs to be implemented based on how the data is stored and accessed
    pass

if __name__ == '__main__':
    app.run(debug=True)
```

In the HTML file (3d_simulation.html):

```html
<!DOCTYPE html>
<html>
<head>
    <title>3D Simulation</title>
    <script src="https://threejs.org/build/three.js"></script>
</head>
<body>
    <div id="3d-simulation-container"></div>
    <script>
        var container = document.getElementById('3d-simulation-container');
        var data = {{ data|tojson|safe }};
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
        var renderer = new THREE.WebGLRenderer();

        renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(renderer.domElement);

        // Add your 3D objects, lights and controls here using the data variable

        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }
        animate();
    </script>
</body>
</html>
```

This is a basic setup for a 3D simulation using Flask and Three.js. The actual 3D objects, lights, and controls need to be added based on the `visualization_data`.