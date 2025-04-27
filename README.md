# Sports Video Analysis

This project analyzes sports videos to track player movements, assign team colors, estimate speed and distance, and more. The output is an annotated video with various metrics and visualizations.

## Project Structure

## Download Data dan Yolo Model

1. Download Dataset:
    ```sh
    https://universe.roboflow.com/roboflow-jvuqo/football-players-detection-3zvbc/dataset/1
    ```

2. Download Model:
    ```sh
    https://drive.google.com/drive/folders/1-bR2vpRcrYDgc7UIkTO3h005sucUB7I1?usp=sharing
    ```

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Install the Model here (https://drive.google.com/drive/folders/1ArcHQ-5IByonmNFbwudbHJiPf83TlX2z?usp=sharing) and put the model at models folder
## Usage

1. Place your input video in the [input_videos](http://_vscodecontentref_/3) directory.
2. Run the main script:
    ```sh
    python main.py
    ```
3. The output video will be saved in the [output_videos](http://_vscodecontentref_/4) directory.

## Main Components

- **Trackers**: Tracks objects in the video.
- **Team Assigner**: Assigns team colors to players.
- **Player Ball Assigner**: Assigns ball possession to players.
- **Camera Movement Estimator**: Estimates camera movement.
- **Speed and Distance Estimator**: Estimates speed and distance of players.
- **View Transformer**: Transforms player positions for better visualization.

## Example

To analyze the provided example video, run:
```sh
python main.pyumpy.org/)
- [scikit-learn](https://scikit-learn.org/)
