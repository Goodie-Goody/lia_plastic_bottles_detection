# Plastic Detection for Recycling Support

## Purpose

This project aims to detect plastic waste on water and land beyond the reach of LAWMA (Lagos State Waste Management Authority) to aid in recycling efforts. The funds raised from recycling will support children's education and vocational training.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

Plastic pollution is a significant environmental issue, affecting both land and water ecosystems. This project utilizes the advanced YOLOv8 Large model to identify plastic waste in various environments, aiding cleanup efforts and recycling initiatives. The ultimate goal is to generate funds for supporting children's education and vocational training.

## Features

- Detects plastic waste on water and land
- Uses the YOLOv8 Large model for object detection
- Helps in recycling efforts to support educational and vocational programs
- Real-time monitoring and detection capabilities

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/plastic-detection.git
    cd plastic-detection
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the plastic detection script using a webcam, follow these steps:

1. **Run the detection script**:
    ```bash
    python load_best_pt.py
    ```

The script will automatically initialize the YOLOv8 Large model and use the webcam to detect plastic waste in real-time.

## Contributing

We welcome contributions to this project! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their invaluable contributions and support.
