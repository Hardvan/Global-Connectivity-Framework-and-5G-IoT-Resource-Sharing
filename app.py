from flask import Flask, render_template, request, jsonify
import os


# Custom Modules
import NodesScript


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/visualize', methods=['POST'])
def visualize():
    region_number = request.form['region']
    print(f"Region number: {region_number}")

    folder_path = NodesScript.handler(region_number)

    # Iterate over the images in the folder and add their paths to the list
    graph_images = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            graph_images.append(filename)
    # Add prefix of folder path to the image names
    graph_images = [folder_path + "/" + image for image in graph_images]
    print(f"Graph images: {graph_images}")

    return render_template("index.html",
                           graph_images=graph_images)


if __name__ == "__main__":
    app.run(debug=True)
